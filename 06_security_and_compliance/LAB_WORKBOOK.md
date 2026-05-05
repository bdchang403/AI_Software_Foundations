# Compliance Lab: The AI Audit & Fairness Check

In this lab, you will audit a "Credit Approval" system that was built using AI. You will verify the **Traceability**, check for **Bias**, and validate the **PII boundary**.

## Part 1: Verify the Trace (Lineage)
Check the [Audit Trace Example](../05_deployment_and_operations/github_action_trace_example.yml).
*   **Action:** Ensure the `AI-SBOM` contains the Model Version (e.g., `gemini-1.5-pro`). 
*   **Why:** If this model is found to be biased later, we need this record to trigger a recall.

## Part 2: Bias Detection
Review the logic in a simulated `CreditManager.ts`. 
*   **Action:** Does the code use "Length of Residence" or "Number of Dependents" to calculate credit? 
*   **Audit Question:** Are these variables violating Article VI of our Constitution in your specific jurisdiction?

## Part 3: PII Validation
Run a search across the generated PR for the term `log`.
*   **Action:** Identify if any `logger.info()` calls include the `raw_payload`.
*   **Correction:** If found, mark the PR as **REJECTED - CONSTITUTIONAL VIOLATION (ARTICLE I)**.

---

## 🏁 Final Submission
Provide a "Compliance Seal" (a markdown comment) on the Pull Request.
Example:
> ✅ **Compliance Validated**: [EPIC-101] Adheres to Articles I, VI, and VII. AI-SBOM verified (Model: Gemini 1.5 Pro).

---

## 🏁 The Finish Line

Congratulations! You have successfully audited an AI-assisted development workflow. Proceed to the final phase to see how your audits are orchestrated into a live agent.

[**Proceed to Phase 4: Agent Orchestration & Assembly →**](../09_ai_agent_orchestration/01_anatomy_of_an_agent.md)
