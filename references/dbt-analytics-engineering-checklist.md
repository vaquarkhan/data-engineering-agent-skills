# dbt Analytics Engineering Checklist

Use this checklist when reviewing or implementing `dbt` models and project structure.

## Model Design

- [ ] The model belongs to a clear layer: staging, intermediate, or mart
- [ ] Grain and keys are explicit
- [ ] Business logic is not duplicated unnecessarily
- [ ] Raw cleanup and publish semantics are not mixed carelessly

## Quality

- [ ] YAML tests exist for important columns and relationships
- [ ] Documentation exists for models and key fields
- [ ] Source freshness is defined where relevant
- [ ] Snapshots or historical logic are explicit where needed

## Usability

- [ ] Output naming is understandable for analysts
- [ ] Downstream metric and dashboard use cases are considered
- [ ] The model can be maintained without reading the whole project
