# Module 1: The 3-Part Directive for User Stories

## Theory: Given/When/Then is Output Formatting
A standard user story contains Acceptance Criteria written in Given/When/Then syntax (BDD). For an AI Agent, this syntax is highly advantageous—but only if you explicitly frame it as a **3-Part Directive**.

1. **Context Boundary:** Defining the exact state preconditions (The "Given").
2. **Task Instruction:** The explicit action (The "When").
3. **Format/Constraint:** The strict definition of expected output (The "Then").

## Verbose Example
### Bad (For AI):
"User can log in with Google."
*AI will write a generic Google OAuth flow and inject it wherever it thinks is best, likely ignoring your custom middleware.*

### Good (Context-Rich 3-Part Directive):
* **Context (Given):** "Given the user is on the frontend React App and the backend Auth Service is utilizing Passport.js."
* **Task (When):** "When the user clicks 'Login with Google', initiate the OAuth 2.0 handshake through the existing `api/auth/google` route."
* **Constraint (Then):** "Then extract the JWT, store it in the HTTP-Only cookie, and route the user to `/dashboard`. Do not expose the JWT to local storage."

## Exercise: Re-writing BDD for AI
**Scenario:** A user wants to retrieve their past invoices.

**Your Action:**
Write the 3-Part Directive (Given/When/Then) below, ensuring you add constraints that an AI won't know by default (like where invoices are stored).

* **Context (Given):** [Your explicitly bounded context]
* **Task (When):** [The exact trigger]
* **Constraint (Then):** [The explicit outcome and any negative constraints]

---
[**Next Module: Adversarial Thinking →**](./02_adversarial_thinking.md)
