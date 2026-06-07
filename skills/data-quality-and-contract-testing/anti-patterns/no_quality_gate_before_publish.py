#!/usr/bin/env python3
"""
ANTI-PATTERN: Publishing Data Without Quality Gates
====================================================

Problem:
    This pipeline ingests raw data, transforms it, and publishes directly to
    a consumer-facing table without any quality validation step.  There is no
    null check, no row-count assertion, no schema validation, and no freshness
    gate between the transform and publish stages.

    When upstream sources deliver corrupt, partial, or malformed data, the
    pipeline blindly propagates it to consumers.  Dashboards break, ML models
    train on garbage, and downstream aggregates silently become wrong.

Symptoms:
    - Consumer complaints about unexpected NULLs or missing rows
    - Dashboard metrics dropping to zero after a pipeline run
    - ML model accuracy degrading after retraining on fresh data
    - Periodic "bad data" incidents with no automated detection
    - Data issues discovered hours or days after publish

Expected Diagnosis:
    The agent should identify:
    1. No quality assertion between transform and publish stages
    2. Null-heavy or schema-violated data reaching the publish layer
    3. Missing freshness/completeness checks before consumer exposure

Expected Fix:
    - Add a quality gate stage between transform and publish
    - Validate null rates, row counts, schema, and freshness before publish
    - On gate failure: halt publish, alert, write to quarantine table
    - Use contract-driven thresholds (not hardcoded magic numbers)
    - Implement circuit-breaker: consecutive failures block publish

Root Cause:
    Treating the pipeline as a simple source→transform→sink flow without
    acknowledging that upstream data quality is not guaranteed.  Every
    boundary between systems is a trust boundary that requires validation.
"""
from __future__ import annotations

import json
import sys
import random
from datetime import datetime, timedelta, timezone
from typing import Any


def generate_raw_data(num_rows: int = 500) -> list[dict[str, Any]]:
    """Simulate raw ingested data with realistic quality issues."""
    random.seed(42)
    rows: list[dict[str, Any]] = []
    base_time = datetime(2024, 3, 15, 10, 0, 0, tzinfo=timezone.utc)

    for i in range(num_rows):
        row: dict[str, Any] = {
            "order_id": f"ORD-{i + 1:05d}",
            "customer_id": f"CUST-{random.randint(1, 200):04d}",
            "amount": round(random.uniform(10.0, 500.0), 2),
            "currency": random.choice(["USD", "EUR", "GBP"]),
            "status": random.choice(["completed", "pending", "cancelled"]),
            "created_at": (base_time + timedelta(minutes=i)).isoformat(),
        }

        # Inject quality issues (simulating upstream corruption)
        if random.random() < 0.15:  # 15% null amounts
            row["amount"] = None
        if random.random() < 0.08:  # 8% null customer_ids
            row["customer_id"] = None
        if random.random() < 0.05:  # 5% invalid currency codes
            row["currency"] = "INVALID"
        if random.random() < 0.03:  # 3% null timestamps
            row["created_at"] = None

        rows.append(row)

    return rows


def transform(raw_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Simple transform: filter completed orders, add derived field.

    BUG: Does NOT validate data quality. Nulls and invalid values pass through.
    """
    transformed = []
    for row in raw_data:
        # No null check, no validation — just pass through
        enriched = {
            **row,
            "amount_usd": row["amount"] if row.get("currency") == "USD" else None,
            "published_at": datetime.now(timezone.utc).isoformat(),
        }
        transformed.append(enriched)
    return transformed


def publish(transformed_data: list[dict[str, Any]]) -> dict[str, Any]:
    """Publish to consumer-facing table WITHOUT quality gate.

    BUG: No validation between transform and publish. Bad data reaches consumers.
    """
    # Simulate writing to a publish table
    published_count = len(transformed_data)

    # Measure the damage
    null_amounts = sum(1 for r in transformed_data if r.get("amount") is None)
    null_customers = sum(1 for r in transformed_data if r.get("customer_id") is None)
    invalid_currencies = sum(
        1 for r in transformed_data
        if r.get("currency") not in {"USD", "EUR", "GBP", None}
    )
    null_timestamps = sum(1 for r in transformed_data if r.get("created_at") is None)

    return {
        "published_rows": published_count,
        "null_amounts": null_amounts,
        "null_customers": null_customers,
        "invalid_currencies": invalid_currencies,
        "null_timestamps": null_timestamps,
    }


def main() -> int:
    """Demonstrate the no-quality-gate anti-pattern."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: No Quality Gate Before Publish")
    print("=" * 70)
    print()

    # Stage 1: Ingest raw data (with quality issues from source)
    raw_data = generate_raw_data(num_rows=500)
    print(f"Raw data ingested: {len(raw_data)} rows")

    # Stage 2: Transform (no quality checks)
    transformed = transform(raw_data)
    print(f"Transformed: {len(transformed)} rows")

    # Stage 3: Publish directly (no gate!)
    publish_result = publish(transformed)
    print(f"Published: {publish_result['published_rows']} rows")
    print()

    # Calculate impact
    total = publish_result["published_rows"]
    bad_rows = (
        publish_result["null_amounts"]
        + publish_result["null_customers"]
        + publish_result["invalid_currencies"]
        + publish_result["null_timestamps"]
    )

    result = {
        "anti_pattern": "no_quality_gate_before_publish",
        "pipeline_stages": ["ingest", "transform", "publish"],
        "missing_stage": "quality_gate (between transform and publish)",
        "raw_rows": len(raw_data),
        "published_rows": total,
        "quality_issues_published": {
            "null_amounts": publish_result["null_amounts"],
            "null_customers": publish_result["null_customers"],
            "invalid_currencies": publish_result["invalid_currencies"],
            "null_timestamps": publish_result["null_timestamps"],
            "total_bad_fields": bad_rows,
        },
        "consumer_impact": {
            "null_amount_rate": round(publish_result["null_amounts"] / total, 4),
            "null_customer_rate": round(publish_result["null_customers"] / total, 4),
            "invalid_currency_rate": round(publish_result["invalid_currencies"] / total, 4),
        },
        "diagnosis": (
            f"Pipeline published {total} rows with {bad_rows} quality issues. "
            f"No validation occurred between transform and publish. "
            f"Consumers now have {publish_result['null_amounts']} orders with null amounts "
            f"and {publish_result['invalid_currencies']} orders with invalid currencies."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Add a quality gate between transform and publish:")
    print("  1. Assert null_rate(amount) < 0.01")
    print("  2. Assert null_rate(customer_id) == 0.0")
    print("  3. Assert currency IN ('USD','EUR','GBP')")
    print("  4. Assert freshness(created_at) < 60 minutes")
    print("  5. On failure: halt publish, write to quarantine, alert")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
