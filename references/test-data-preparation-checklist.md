# Test Data Preparation Checklist

Use this checklist when building synthetic data, masked fixtures, or lower-environment validation datasets.

## Purpose

- [ ] The test-data use case is explicit
- [ ] The required realism level is understood
- [ ] Performance, correctness, and demo goals are not conflated

## Safety

- [ ] Sensitive fields are masked, tokenized, or replaced
- [ ] Production secrets or live reads are not required to regenerate the data
- [ ] Lower-environment access boundaries are defined

## Representativeness

- [ ] Edge cases are included
- [ ] Null, duplicate, and late-arrival behaviors are represented
- [ ] Cardinality and skew are realistic enough for the test goal

## Maintainability

- [ ] The generation or sampling method is documented
- [ ] Refresh cadence is defined
- [ ] Dataset limitations versus production are known
