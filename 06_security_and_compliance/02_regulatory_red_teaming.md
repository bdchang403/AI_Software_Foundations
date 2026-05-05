# Module 2: Regulatory Red-Teaming

## Theory: Looking for the "Hidden Bias"
AI Agents don't just follow instructions; they interpolate between them. **Regulatory Red-Teaming** means testing the agent's output specifically for violations of laws like GDPR, HIPAA, or the AI Act.

## 1. PII Leakage Test (GDPR/HIPAA)
Even if the Builder says "I used anonymized IDs," the AI might have hallucinated a `console.log(userData)` during debugging that remains in the code.
*   **The Audit Action:** Use a Grep-based search tool (or an AI Auditor) to scan the codebase for keywords like `email`, `ssn`, `address` inside `log` or `print` functions.

## 2. Fairness Red-Teaming
If the AI wrote a "Credit Approval" class, you must ask an adversarial AI to try and "Cheat the System."
*   **Adversarial Prompt:** "Try to get the Credit Approval class to reject a user solely because they have a 'First Generation Immigrant' status flag."
*   **The Pass Condition:** The system should explicitly throw an error or default to a neutral merit-based logic, proving the guardrails work.

## Exercise: The PII Leak
**Scenario:** An AI agent refactored the `LoginService.ts`. You suspect it might be logging the user's password on failure.

**Your Action:**
Write the adversarial test prompt you would give to the Validation Lead team to verify that passwords are never captured in the telemetry traces.

---
### 🎓 Final Step: Practical Application
Congratulations! You have completed the theory modules. Now it's time to put these concepts into practice.

[**Go to Lab Workbook: The AI Audit & Fairness Check →**](./LAB_WORKBOOK.md)
