# Data Validation And Testcase Patterns

Use this reference when validation needs to move beyond a generic "add tests" instruction. It helps teams choose concrete testcase types and checks for pipelines, models, streaming systems, and regulated data products.

## Core Testcase Categories

### Shape And Contract Cases

Use when the first risk is structural compatibility.

Include:

- missing required fields
- type mismatches
- breaking schema changes
- unexpected new columns
- key or uniqueness violations

### Null And Boundary Cases

Use when correctness depends on edge handling, not only common values.

Include:

- nulls in required fields
- zero, negative, and extreme numeric values
- empty strings and placeholder values
- date boundaries, DST changes, and timezone edges

### Duplicate And Replay Cases

Use when reruns, retries, or upstream duplication can happen.

Include:

- duplicate business keys
- replay of previously processed windows
- exactly-once claims that still need sink validation
- idempotent rerun behavior

### Change-Data And Mutation Cases

Use when updates and deletes matter.

Include:

- late arriving updates
- hard deletes and tombstones
- slowly changing dimensions
- merge conflicts and conflicting source versions

### Freshness And Completeness Cases

Use when publish timing and arrival behavior are part of the contract.

Include:

- late partitions
- empty batch windows
- partial extract delivery
- completeness thresholds by source or partition

### Distribution And Skew Cases

Use when data shape affects performance or correctness.

Include:

- hot keys
- outlier tenants or entities
- unusually large payloads
- highly imbalanced partitions

### Security And Compliance Cases

Use when a dataset has access, masking, or deletion obligations.

Include:

- masked-field validation
- unauthorized-access checks
- sensitive values not appearing in logs or exports
- deletion and retention propagation behavior

## Recommended Checks By System Type

### Batch Pipeline

- schema and contract checks
- row-count and completeness checks
- null and duplicate checks
- reconciliation against trusted totals

### Streaming Pipeline

- schema compatibility
- out-of-order and late-event cases
- duplicate and replay cases
- checkpoint and dead-letter-path validation

### CDC Pipeline

- insert, update, and delete propagation
- ordering and deduplication checks
- tombstone and retraction behavior
- target-side merge correctness

### Published Dataset Or Mart

- grain stability
- key uniqueness
- metric parity
- freshness and publish gating

### Regulated Or Sensitive Dataset

- masking and access validation
- audit-log sanity
- retention and deletion behavior
- lower-environment safety checks

## Review Questions

- [ ] Are there testcase inputs for edge cases, not just happy paths?
- [ ] Is there a replay or rerun case if the system can ever be rerun?
- [ ] Are mutation cases covered where updates or deletes matter?
- [ ] Are security or masking checks present where sensitive data exists?
- [ ] Is evidence captured in a form that reviewers can inspect?
