# Warehouse Performance Cost Checklist

Use this checklist when optimizing warehouse workloads.

## Measurement

- [ ] A baseline runtime or cost measurement exists
- [ ] The bottleneck is identified
- [ ] Expensive joins, scans, or concurrency patterns are known

## Optimization

- [ ] Physical design choices such as partitioning or clustering are reviewed
- [ ] Materialization choices are justified
- [ ] Workload isolation or right-sizing is considered

## Safety

- [ ] Optimizations preserve business correctness
- [ ] Resulting cost and performance trade-offs are documented
- [ ] The same anti-pattern is not repeated elsewhere without review
