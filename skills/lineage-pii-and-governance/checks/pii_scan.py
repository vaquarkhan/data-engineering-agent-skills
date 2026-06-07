#!/usr/bin/env python3
"""Scan columns for PII patterns and flag unmasked sensitive data.

This check scans both column names and sample values for patterns indicating
personally identifiable information (PII): email addresses, phone numbers,
SSNs, credit card numbers, IP addresses, and names.

Unmasked PII in analytics or publish layers violates data governance policies
and may breach regulations (GDPR, CCPA, HIPAA).

Usage:
    python checks/pii_scan.py --source data.csv
    python checks/pii_scan.py --source data.parquet --sample-size 500
    python checks/pii_scan.py --source data.jsonl --allowed-columns email_hash
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


# Column name patterns that suggest PII
PII_COLUMN_PATTERNS: dict[str, list[str]] = {
    "email": ["email", "e_mail", "email_address", "user_email"],
    "phone": ["phone", "phone_number", "mobile", "cell", "telephone"],
    "ssn": ["ssn", "social_security", "social_security_number", "sin"],
    "credit_card": ["credit_card", "card_number", "cc_number", "pan"],
    "address": ["street_address", "home_address", "mailing_address"],
    "name": ["full_name", "first_name", "last_name", "surname"],
    "ip_address": ["ip_address", "ip_addr", "client_ip", "user_ip"],
    "date_of_birth": ["dob", "date_of_birth", "birth_date", "birthday"],
}

# Value patterns (regex) for detecting PII in sample data
PII_VALUE_PATTERNS: dict[str, re.Pattern[str]] = {
    "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", re.IGNORECASE),
    "phone_us": re.compile(r"\b(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "credit_card": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan columns and values for unmasked PII."
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to data file (parquet, csv, or jsonl).",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=200,
        help="Number of rows to sample for value scanning. Default: 200",
    )
    parser.add_argument(
        "--allowed-columns",
        help="Comma-separated columns where PII is expected (e.g., already masked).",
    )
    return parser.parse_args()


def load_dataframe(path: Path, sample_size: int = 200) -> "Any":
    """Load a sample of the data file."""
    import pandas as pd

    suffix = path.suffix.lower()
    if suffix == ".parquet":
        df = pd.read_parquet(path)
    elif suffix == ".csv":
        df = pd.read_csv(path)
    elif suffix in {".jsonl", ".ndjson"}:
        df = pd.read_json(path, lines=True)
    else:
        raise SystemExit(f"Unsupported format: {suffix}")

    if len(df) > sample_size:
        return df.sample(n=sample_size, random_state=42)
    return df


def scan_column_names(columns: list[str]) -> list[dict[str, Any]]:
    """Scan column names for PII indicators."""
    findings: list[dict[str, Any]] = []
    for col in columns:
        col_lower = col.lower().strip()
        for pii_type, patterns in PII_COLUMN_PATTERNS.items():
            for pattern in patterns:
                if pattern in col_lower or col_lower == pattern:
                    findings.append({
                        "column": col,
                        "pii_type": pii_type,
                        "match_reason": f"column name matches pattern '{pattern}'",
                        "confidence": "high",
                    })
                    break
    return findings


def scan_column_values(df: "Any", columns: list[str]) -> list[dict[str, Any]]:
    """Scan sample values for PII patterns."""
    findings: list[dict[str, Any]] = []

    for col in columns:
        if col not in df.columns:
            continue
        # Only scan string-like columns
        sample_values = df[col].dropna().astype(str).head(200).tolist()
        if not sample_values:
            continue

        for pii_type, pattern in PII_VALUE_PATTERNS.items():
            matches = [v for v in sample_values if pattern.search(str(v))]
            if matches:
                findings.append({
                    "column": col,
                    "pii_type": pii_type,
                    "match_reason": "value pattern match",
                    "matches_found": len(matches),
                    "sample_match": _redact(matches[0]),
                    "confidence": "high" if len(matches) > 5 else "medium",
                })

    return findings


def _redact(value: str) -> str:
    """Partially redact a PII value for evidence (show first/last chars)."""
    if len(value) <= 4:
        return "***"
    return value[:2] + "***" + value[-2:]


def check_pii_scan(
    source: Path,
    sample_size: int = 200,
    allowed_columns: list[str] | None = None,
) -> dict[str, Any]:
    """Run PII scan and return structured evidence."""
    df = load_dataframe(source, sample_size)
    allowed = set(allowed_columns or [])
    columns = [str(c) for c in df.columns]

    # Scan column names
    name_findings = scan_column_names(columns)

    # Scan values
    value_findings = scan_column_values(df, columns)

    # Combine and de-duplicate
    all_findings: list[dict[str, Any]] = []
    seen_columns: set[str] = set()

    for finding in name_findings + value_findings:
        col = finding["column"]
        if col in allowed:
            continue
        if col not in seen_columns:
            all_findings.append(finding)
            seen_columns.add(col)

    status = "fail" if all_findings else "pass"

    return {
        "check": "pii_scan",
        "status": status,
        "source": str(source),
        "sample_size": min(sample_size, len(df)),
        "total_columns": len(columns),
        "columns_scanned": len(columns),
        "allowed_columns": list(allowed),
        "findings": all_findings,
        "pii_columns_found": len(all_findings),
        "pii_types_found": list(set(f["pii_type"] for f in all_findings)),
    }


def main() -> int:
    args = parse_args()
    allowed = [c.strip() for c in args.allowed_columns.split(",")] if args.allowed_columns else []
    result = check_pii_scan(args.source, args.sample_size, allowed)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
