# Module 2: Intervening in the Factory

## Theory: Targeted Coaching
When you identify a metric failure, you don't "Retrain the team on AI." You target the specific role in the Context Factory that failed their hand-off.

### Scenario A: High Defect Rate
* **Metric:** Change Failure Rate (CFR) is up 30%.
* **Investigation:** You check the BuilderOps trace. The PR had an `EPIC-ID`. So what happened?
* **Intervention:** Go to the Validation Leads. Check their prompts. Are they using the 3-Part Directive? Are they explicitly importing the Requirements Lead's Semantic Blueprint into the Agent's context? If not, the Validation Lead's AI is writing tests against the Builder's hallucinated code, rather than the true business rules.

### Scenario B: Massive PR Size (Token Bloat)
* **Metric:** Average PR size is now 3,000 LOC. Reviewers are abandoning PRs.
* **Investigation:** You check the Builder's prompts.
* **Intervention:** The Requirements Lead failed at **Decomposition**. They handed the Builder a Semantic Blueprint asking for a monolithic feature. The Builder passed that to the AI, and the AI tried to write the whole monolith. Intervene at the Requirements Lead level: "Slice this into 3 token-isolated stories."

## The Final Responsibility: Auditing the Constitutional Logs

AI does not make engineering easier—it makes it faster. Fast, incorrectly constrained engineering will destroy a codebase in weeks. 

As the Agile Leader, it is your absolute responsibility to ensure the Context Factory is adhered to relentlessly. You must build dashboards that monitor the Builder AI's `<CRITIQUE>` logs.

### Scenario C: High Re-Generation Throttling
* **Metric:** Builders report the AI takes 5 minutes to generate code.
* **Investigation:** You pull the `<CRITIQUE>` logs from the orchestration layer. You notice the AI is writing code, critiquing itself: *"Violation of Article I: This route leaks PII,"* deleting the code, and regenerating it 10 times in a loop before succeeding.
* **Intervention:** The Requirements Lead's Semantic Blueprint is inherently violating the Constitution by demanding PII in the Acceptance Criteria. Intervene at the Requirements Lead level: "Redesign this payload to use an anonymized ID so the AI stops triggering Constitutional rollbacks."
