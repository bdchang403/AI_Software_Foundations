# ADR-001: SideDrawer Permission Matrix

## Context
Strict RBAC must be enforced on all newly provisioned drawers to prevent data leakage.

## Decision
1. **Sponsors:** Always grant `Sponsor` role to internal relationship managers.
2. **Third-Parties:** The AI must ALWAYS assign the `Viewer` role (read-only) to third-party consultants in the API payload. Never grant `Collaborator` role to an external email domain.
