# Schema Migration Checklist

Use this checklist when changing source or published schemas.

## Impact

- [ ] The change is classified as additive or breaking
- [ ] Consumers are identified
- [ ] Downstream dashboards, extracts, and APIs are considered

## Transition

- [ ] A compatibility or migration path exists
- [ ] Rollback behavior is defined
- [ ] Type and nullability changes are validated with real data

## Release

- [ ] Consumer communication expectations are defined
- [ ] Deprecation timing is explicit
- [ ] Old paths are removed only after confirmation
