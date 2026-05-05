# Context Data Template: Semantic Blueprint

*This file serves as the input data for the Requirements Lead's reasoning engine.*

## Epic Meta
- **Epic ID:** `[EPIC-001]`
- **Title:** `[Title]`

## 1. Business Intent (3-Part Directive)
- **Context:** `[Current local state]`
- **Task:** `[What needs to be achieved]`
- **Constraint:** `[How the output must be delivered]`

## 2. Domain Boundaries (Token-Budgeted)
*Prevent token bloat downstream. List specific domains.*
- **Included Domains (In Context):** `[e.g., Authentication Service]`
- **Excluded Systems (Out of Bounds):** `[e.g., User Profile Database]`

## 3. Explicit Constraints (Red-Team Patches)
*Close loopholes the AI might exploit.*
- `[e.g., Do not touch legacy login forms under any circumstances.]`
