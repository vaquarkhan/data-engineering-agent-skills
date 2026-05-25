# Notebook Production Hardening Checklist

Use this checklist when converting notebooks into production jobs.

## Structure

- [ ] Reusable logic is extracted from notebook cells
- [ ] Inputs and configuration are explicit
- [ ] Manual cell-order dependencies are removed

## Reliability

- [ ] Validation and logging exist
- [ ] Output writes are idempotent or recoverable
- [ ] Error handling and retry expectations are defined

## Delivery

- [ ] Deployment path is defined
- [ ] Monitoring path is defined
- [ ] The notebook no longer relies on hidden interactive state
