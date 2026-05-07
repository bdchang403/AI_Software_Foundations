# ADR-001: [SaaS Name] Security Boundaries

## Context
To prevent misconfiguration, all AI-generated logic must adhere to organizational RBAC policies.

## Decision
1. **Admin Access:** Never generate scripts or configurations that grant the `System Administrator` role to non-service accounts.
2. **Naming Conventions:** All new configuration objects (queues, workflows, templates) must be prefixed with `PRD_` or `DEV_` depending on the environment payload.
