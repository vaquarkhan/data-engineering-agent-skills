# Data Platform CI CD Release Checklist

Use this checklist when promoting data changes across environments.

## Release Surface

- [ ] Code, SQL, infra, and contracts affected by the change are identified
- [ ] Environment boundaries are explicit
- [ ] Publish timing is separated from deployment when needed

## Validation

- [ ] Stage-appropriate validation gates exist
- [ ] High-risk changes have staged or shadow validation
- [ ] Rollback or forward-fix behavior is defined

## Ownership

- [ ] Release approvals are clear for risky changes
- [ ] Release evidence is captured for post-deploy review
