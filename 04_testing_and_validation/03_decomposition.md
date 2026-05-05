# Module 3: Test Suite Decomposition

## Theory: Chunking the Test Context
Just like Builders cannot feed a 500k LOC repo to an AI, you cannot feed an entire E2E test suite (which could be hundreds of files and page objects) to an AI.

You must decompose the automated testing instructions by **Contextual Sandbox**. 

## Verbose Example
If you want the AI to write Cypress E2E tests for the "Shopping Cart":
* **Test PR 1:** "Generate the Page Object Model (POM) for the Shopping Cart ONLY. Do not write test logic. Context allowed: `cart.html`."
* **Test PR 2:** "Generate the positive Add-to-Cart tests using the POM created in PR 1." 
* **Test PR 3:** "Generate the adversarial network interception tests (e.g., Mock a 500 API response) for the Cart."

By decomposing, the AI holds a small, perfectly accurate mental model of your testing framework.

## Exercise: Slice the Automation

**Scenario:** You need to automate testing for a new "User Profile Setup" wizard (3 screens: Info, Avatar, Preferences).

**Your Action:**
Slice the test suite generation into 3 prompts that an AI can handle within a tight token budget.
1. **Prompt 1 Context:** [...]
2. **Prompt 2 Context:** [...]
3. **Prompt 3 Context:** [...]

---
[**Next Module: Context Engineering (Traceability) →**](./04_context_engineering.md)
