# Strategy Lead Lab Workbook: Shaping Strategic Intent

Welcome to the Strategy Lead Lab. In the Context Factory, your job is not to write code or even detailed user stories. Your job is **Decomposition and Bounding**. If you feed a massive, vague Epic into the factory, the downstream AI agents will hallucinate due to token limits. 

This workbook contains practical exercises to train you to set strict boundaries for the AI.

---

## Lab 1: The Epic Decomposition Test (Module 3)

**The Scenario:** 
Leadership wants a "New Customer Loyalty Program."
A traditional Strategy Lead might write an Epic like this:
> *Epic: Build a loyalty program where users earn points for purchases and can spend them on rewards.*

If this Epic hits an AI agent downstream, the AI will try to hallucinate a database schema for points, a UI for rewards, and an integration with the checkout system all at once, exceeding its context window and failing catastrophically.

### Your Task
Rewrite the Epic by decomposing it into **Token-Friendly Vertical Slices** (bounded contexts). 

**Step 1:** Open your Agile tool (e.g., Jira). 
**Step 2:** Break the monolithic idea into 3 strictly bounded Epics that share zero immediate dependencies.
**Step 3:** Use the `epic_semantic_blueprint.md` template to define the Value Boundary.

### Answer Key (Compare Your Work)
A properly decomposed set of Epics for AI consumption:
*   **Epic 1 (The Engine):** Implement point accrual logic purely in the backend API. No UI. (Strict boundary: Backend processing only).
*   **Epic 2 (The Vault):** Create the secure ledger database schema to store loyalty points. (Strict boundary: Database only).
*   **Epic 3 (The Display):** Build a Read-Only React component showing a user's current point balance. (Strict boundary: Frontend UI only).

---

## Lab 2: Defining the "No" Boundary (Module 2: Adversarial Thinking)

AI agents are inherently eager to please. If you don't tell them what *not* to do, they will build extra features you didn't ask for.

### Your Task
Take your "Epic 1 (The Engine)" from Lab 1. Write an explicit "Out of Scope" rule that prevents the AI from over-engineering.

### Answer Key (Compare Your Work)
*   **Out of Scope (Negative Prompt):** "Do NOT build any redemption logic. Do NOT build an admin dashboard to manage points. Do NOT send email notifications when points are earned."

---

## Lab 3: Handing off to the Requirements Lead (Module 4: Context Engineering)

You must explicitly map your Epic to the Requirements Lead.
Write a 3-sentence handoff that the Requirements Lead will use as the foundation for their context-enriched story.

**Example Handoff:**
*"We are building the Point Accrual Engine. It must trigger exclusively off the existing `OrderComplete` event. Provide me 5 edge cases regarding what happens if an order is refunded within 24 hours."*
