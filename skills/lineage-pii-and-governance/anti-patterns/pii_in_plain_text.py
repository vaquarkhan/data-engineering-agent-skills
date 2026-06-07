#!/usr/bin/env python3
"""
ANTI-PATTERN: Unmasked PII Reaching the Publish Layer
======================================================

Problem:
    This pipeline ingests customer data containing PII (emails, phone numbers,
    SSNs) and writes it directly to a publish/analytics layer without any
    masking, hashing, or tokenization.  Downstream consumers (analysts, ML
    models, dashboards, partner feeds) gain unrestricted access to raw PII.

    This violates data minimization principles (GDPR Art. 5), creates
    unauthorized disclosure risk, and makes regulatory responses (deletion
    requests, breach notifications) extremely costly because PII has
    proliferated across the data estate.

Symptoms:
    - Governance audits find raw emails/SSNs in analytics tables
    - Deletion requests require scanning dozens of downstream tables
    - Data breach notification scope expands to include analytics consumers
    - Compliance team discovers PII in exported reports or partner feeds
    - Data classification tools flag publish-layer tables as sensitive

Expected Diagnosis:
    The agent should identify:
    1. No masking/hashing transform between raw and publish layers
    2. PII columns (email, phone, ssn) exposed with original values
    3. No column-level access control or dynamic masking in place

Expected Fix:
    - Hash or tokenize PII columns before publish (SHA-256, format-preserving)
    - Apply column-level masking policies (dynamic masking for authorized users)
    - Classify columns at ingestion and enforce masking by classification
    - Implement data minimization: only publish the fields consumers need
    - Add PII scan as a quality gate before publish promotion

Root Cause:
    Treating the publish layer as a copy of the raw layer instead of a
    purpose-built consumer interface.  The pipeline developer focused on
    data completeness without considering data governance boundaries.
    Masking should be part of the transformation layer, not an afterthought.
"""
from __future__ import annotations

import hashlib
import json
import random
import sys
from typing import Any


def generate_customer_data(num_customers: int = 100) -> list[dict[str, Any]]:
    """Generate realistic customer records with PII."""
    random.seed(42)
    first_names = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Henry"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis"]
    domains = ["gmail.com", "yahoo.com", "outlook.com", "company.org"]

    customers: list[dict[str, Any]] = []
    for i in range(num_customers):
        first = random.choice(first_names)
        last = random.choice(last_names)
        customers.append({
            "customer_id": f"CUST-{i + 1:05d}",
            "full_name": f"{first} {last}",
            "email": f"{first.lower()}.{last.lower()}{i}@{random.choice(domains)}",
            "phone": f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
            "ssn": f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}",
            "date_of_birth": f"19{random.randint(50,99)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "address": f"{random.randint(100,9999)} {random.choice(['Main','Oak','Elm','Pine'])} St",
            "total_orders": random.randint(1, 50),
            "lifetime_value": round(random.uniform(100, 10000), 2),
        })
    return customers


def raw_to_publish_no_masking(raw_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Transform raw data to publish layer WITHOUT masking PII.

    BUG: Copies all fields including PII directly to the publish layer.
    No hashing, no tokenization, no column removal, no access control.
    """
    publish_data: list[dict[str, Any]] = []
    for record in raw_data:
        # BUG: blind copy — PII passes through unmasked
        publish_record = {
            "customer_id": record["customer_id"],
            "full_name": record["full_name"],        # PII — should be masked
            "email": record["email"],                # PII — should be hashed
            "phone": record["phone"],                # PII — should be masked
            "ssn": record["ssn"],                    # PII — CRITICAL, must never reach publish
            "date_of_birth": record["date_of_birth"],  # PII — should be removed or generalized
            "address": record["address"],            # PII — should be removed
            "total_orders": record["total_orders"],
            "lifetime_value": record["lifetime_value"],
            "layer": "publish",
        }
        publish_data.append(publish_record)
    return publish_data


def demonstrate_correct_masking(record: dict[str, Any]) -> dict[str, Any]:
    """Show what a properly masked publish record looks like."""
    return {
        "customer_id": record["customer_id"],
        "full_name": "***MASKED***",
        "email_hash": hashlib.sha256(record["email"].encode()).hexdigest()[:16],
        "phone_last4": record["phone"][-4:],
        "ssn": "***REMOVED***",
        "age_band": "30-40",  # generalized from DOB
        "address": "***REMOVED***",
        "total_orders": record["total_orders"],
        "lifetime_value": record["lifetime_value"],
        "layer": "publish",
    }


def main() -> int:
    """Demonstrate PII reaching publish layer unmasked."""
    print("=" * 70)
    print("ANTI-PATTERN DEMONSTRATION: Unmasked PII in Publish Layer")
    print("=" * 70)
    print()

    # Generate customer data with PII
    raw_data = generate_customer_data(num_customers=100)
    print(f"Raw customer records: {len(raw_data)}")

    # Transform to publish WITHOUT masking (the anti-pattern)
    publish_data = raw_to_publish_no_masking(raw_data)
    print(f"Published records: {len(publish_data)}")
    print()

    # Analyze the damage
    pii_columns = ["full_name", "email", "phone", "ssn", "date_of_birth", "address"]
    exposed_pii: dict[str, int] = {}
    for col in pii_columns:
        non_null = sum(1 for r in publish_data if r.get(col))
        exposed_pii[col] = non_null

    # Show a sample exposed record vs. correct masked record
    sample_exposed = publish_data[0]
    sample_correct = demonstrate_correct_masking(raw_data[0])

    result = {
        "anti_pattern": "pii_in_plain_text",
        "records_published": len(publish_data),
        "pii_columns_exposed": pii_columns,
        "pii_exposure_counts": exposed_pii,
        "total_pii_field_exposures": sum(exposed_pii.values()),
        "sample_exposed_record": sample_exposed,
        "sample_correct_record": sample_correct,
        "regulatory_risk": {
            "gdpr_violation": "Art. 5 data minimization, Art. 25 data protection by design",
            "ccpa_risk": "Unnecessary collection exposure in analytics layer",
            "breach_scope": f"{len(publish_data)} customer records with SSN, email, phone exposed",
            "deletion_complexity": "PII now in publish layer — must track all downstream copies",
        },
        "diagnosis": (
            f"Pipeline published {len(publish_data)} records with {len(pii_columns)} "
            f"PII columns unmasked. SSNs, emails, and phone numbers are directly "
            f"accessible in the publish layer. Any consumer, report, or export "
            f"now has access to raw PII without authorization controls."
        ),
    }

    print(json.dumps(result, indent=2))
    print()
    print("FIX: Apply masking before publish:")
    print("  1. Hash emails: SHA-256 -> email_hash (for joins without exposing value)")
    print("  2. Remove SSN entirely from publish layer")
    print("  3. Mask names: first initial + last initial only")
    print("  4. Generalize DOB -> age_band (e.g., '30-40')")
    print("  5. Remove address or generalize to zip/region")
    print("  6. Add PII scan as quality gate before layer promotion")

    return 1  # Always exits non-zero: this is an anti-pattern demonstration


if __name__ == "__main__":
    sys.exit(main())
