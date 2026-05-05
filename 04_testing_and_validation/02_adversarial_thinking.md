# Module 2: Constitutional Penetration Testing (Red-Teaming)

## Theory: Hallucination Edge Cases & Constitutional Violations
The AI agent that wrote the code might have hallucinated a feature that wasn't in the blueprint, or worse, violated the **Enterprise AI Constitution**. For example, if asked to parse an Excel file, it might have logged the entire payload including PII to stdout, violating Article I: Data Minimization.

As a Validation Lead, you must use Adversarial Prompts to generate **Constitutional Penetration Tests**. You are Red-Teaming not just the business logic, but the AI's adherence to the global constitution.

## Verbose Example
**The Blueprint:** "Calculate sales tax based on state."

**Adversarial Thought:** "The AI probably used a generic standard library for tax or hallucinated default rates. Furthermore, did it log the customer's full address during the calculation, violating Article I?"

**The Test Generation Prompt:**
"Generate API tests explicitly designed to break the `calculate_tax` function. Assert that providing empty state strings throws a `StrictValidationException`. Additionally, write a test asserting that the system logs do NOT contain the `street_address` payload upon successful execution, proving adherence to Article I of the Constitution."

## Exercise: Red-Teaming the Prompt

**Scenario:** The builder's AI wrote an `update_password` function.

**Your Action:**
Write an adversarial test-generation prompt targeting the weakest implicit logic the AI might have used.
1. **Adversarial Loopholes:** [e.g., Does the AI check past passwords? Does it enforce entropy?]
2. **Your Test Prompt:** [Write the prompt for your AI assistant to generate the adversarial Jest tests].

---
[**Next Module: Test Suite Decomposition →**](./03_decomposition.md)
