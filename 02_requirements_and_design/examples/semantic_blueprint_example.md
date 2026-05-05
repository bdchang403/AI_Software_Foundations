# Example: The Semantic Blueprint

Requirements Leads must translate soft English requirements into boolean, structural contracts that AI Agents (and Validation Leads) can map to the Function Registry.

## ❌ The BAD Example: Soft Requirements
**Story:** The User Login Flow
- **Description:** "The user should be able to log in with their email and password. Sometimes they use Google. If they type the wrong password, give them an error nicely. Also, make sure it is secure."

### Why this fails:
"Make sure it is secure" means nothing to an LLM. It will likely hallucinate a generic `bcrypt` implementation locally instead of using your enterprise authentication provider (like Okta/Auth0), violating your entire security architecture.

---

## ✅ The GOOD Example: Semantic Function Mapping
**Story:** The User Login Flow

### 1. Bounded Sub-System Execution Map
| Business Domain | Required Code Pattern (Must Exist) | Restricted Search Path (Sandbox) |
| --- | --- | --- |
| `[Auth Core]` | `[Auth0 JWT Validator]` | `[/src/auth/auth0_service.ts]` |
| `[Database]` | `[Prisma User Repository]` | `[/src/database/repos/user.ts]` |

*(The Agent Router will lock the AI completely out of any files except these two).*

### 2. Boolean Acceptance Criteria
- `[BOOLEAN: TRUE]` User provides `email` and `password`.
- `[BOOLEAN: TRUE]` Request is routed to `FunctionRegistry::Auth0ProviderTool`.
- `[BOOLEAN: FALSE]` Local `bcrypt` comparison. (DO NOT compute passwords locally).
- **Expected Return Contract:** `HTTP 200` with JWT scoped to `role: user`.
- **Expected Failure Contract:** `HTTP 401` with strict payload `{"error": "INVALID_CREDENTIALS"}`.

### Why this succeeds:
The builder's AI agent now has a strict API contract to fulfill. It cannot hallucinate security; it must find the `Auth0ProviderTool` in the registry and execute it or the compilation will intentionally fail.

---

## ✅ Another GOOD Example: E-Commerce Checkout

**Story:** Processing an Order Payment

### 1. Bounded Sub-System Execution Map
| Business Domain | Required Code Pattern (Must Exist) | Restricted Search Path (Sandbox) |
| --- | --- | --- |
| `[Payment Processing]` | `[Stripe Billing Service]` | `[/src/payments/stripe/]` |
| `[Order Management]` | `[Order State Machine]` | `[/src/orders/state_machine.ts]` |
| `[Inventory]` | `[Inventory Reservation]` | `[/src/inventory/reserve.ts]` |

> **AGENT ROUTING DIRECTIVE:** If `Stripe Billing Service` is unavailable, you MUST fall back to `[/src/payments/paypal/]`. DO NOT write a custom credit card processor.

### 2. Boolean Acceptance Criteria
- `[BOOLEAN: TRUE]` Inventory is reserved via `Inventory Reservation` *before* attempting payment.
- `[BOOLEAN: TRUE]` Payment request is routed to `Stripe Billing Service`.
- `[BOOLEAN: FALSE]` Storing credit card numbers in the local database.
- **Expected Return Contract:** `HTTP 201` with `order_id` and status `PAYMENT_SUCCESS`.
- **Expected Failure Contract:** If payment fails, `[BOOLEAN: TRUE]` release the inventory lock immediately. `HTTP 402` with `{"error": "PAYMENT_DECLINED"}`.

### Why this succeeds:
This blueprint forces the AI to consider the *sequence* of operations (inventory before payment) and explicitly outlaws dangerous behaviors (storing credit cards). It maps business logic directly to physical folders, ensuring the AI only operates within the bounds of the existing architecture.
