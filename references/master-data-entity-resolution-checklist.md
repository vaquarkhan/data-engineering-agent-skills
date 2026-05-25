# Master Data Entity Resolution Checklist

Use this checklist when building canonical entities or golden records.

## Entity Design

- [ ] Canonical entity type is defined
- [ ] Contributing systems are identified
- [ ] Match rules are explicit

## Survivorship

- [ ] Attribute-level survivorship is documented
- [ ] Ambiguous cases are handled explicitly
- [ ] Confidence or resolution state is preserved where needed

## Publishing

- [ ] Downstream consumers understand match assumptions
- [ ] Lineage and ownership are explicit for the published master dataset
