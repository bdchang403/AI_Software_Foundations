# Module 1: The 3-Part Directive for Validation

## Theory: Test the Contract, Not the AI's Code
If you ask an AI to "write unit tests for this file," it will look at the code the Builder's AI just wrote and write tests that pass, even if the code contradicts the Requirements Lead's Semantic Blueprint.

You must write a **3-Part Directive** that forces the AI to look at the *Blueprint* first, and the *Code* second.

## Verbose Example
### Bad (For AI Test Generation):
"Write Playwright tests for the checkout page component."
*(The AI will write tests that check if buttons exist, ignoring the actual business rules).*

### Good (Context-Rich 3-Part Directive):
* **Context:** "The business rules are strictly defined in `blueprint_checkout.md`. The target code is `CheckoutComponent.tsx`. Do not look at any other UI components."
* **Task:** "Generate e2e Playwright tests asserting that the Red-Team Negative Constraints defined in the blueprint (e.g., 'Cannot checkout with empty cart') are actively enforced."
* **Constraint:** "Output only the `.spec.ts` file. Do not invent mock data; use the `mockDataRegistry.json` exactly as defined."

## Exercise: Re-writing the Test Prompt
**Scenario:** You need to test a new "Delete Photo" API endpoint.

**Your Action:**
Write the 3-Part Directive instructing an AI to generate the `jest` tests.

* **Context:** [Define the Blueprint and the specific code file]
* **Task:** [Focus the test on the boundaries]
* **Constraint:** [Limit the scope or enforce mocking]

---
[**Next Module: Adversarial Thinking →**](./02_adversarial_thinking.md)
