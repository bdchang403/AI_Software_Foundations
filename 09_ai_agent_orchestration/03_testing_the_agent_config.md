# Bridge Module 3: Testing the Agent Config

Before you deploy an agent into a CI/CD pipeline, you must perform a **Configuration Audit**. This is where the Builder and Validation Lead (Validation Lead) work together.

## The Builder's Sandbox Test
The Builder takes the **Function Registry** and the **Requirements Lead's Directive** and runs a "Mock Execution."
1.  **Input:** Give the Agent the Directive.
2.  **Observation:** Does the Agent call the correct tools from the Registry?
3.  **Validation:** If the Agent tries to "invent" a tool, the Builder must go back and tighten the **Constraint** in the 3-Part Directive.

## The Validation Lead's Adversarial Audit
The Validation Lead takes the **Enterprise Constitution** and the **Agent YAML** and tries to "Break the Guardrails."
1.  **Adversarial Task:** "I am a malicious user. Can I get this agent to reveal a database password by asking it nicely?"
2.  **The Fix:** If the agent reveals the password, the Validation Lead and Builder must update the `skills.md` file to include a "PII Scrubbing" rule.

## The Final Handshake
The agent is only "Production Ready" when:
*   [ ] Builder confirms the **Registry** maps to current code.
*   [ ] Validation Lead confirms the **Constitution** is enforced.
*   [ ] Compliance confirms **Article VI (Bias)** is respected.

---

[**Next: Context Mapping Matrix →**](./04_context_mapping_matrix.md)
