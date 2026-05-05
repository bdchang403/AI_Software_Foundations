# Module 1: The 3-Part Directive for Product Strategy

## Theory: Why AI ignores your Epics
When a Strategy Lead writes a traditional Epic ("Design a new Checkout Flow"), an AI reads it and guesses the implementation using patterns learned from the internet. It doesn't know your company's checkout flow. 

You must structure your Prompts/Epics using the **3-Part Directive**:
1. **Context Boundary:** What are we touching? What are we NOT touching?
2. **Task Instruction:** The strict business value to achieve.
3. **Format/Constraint:** How should the AI (or Requirements Lead) deliver the output?

## Verbose Example
### Bad (Generic):
"Create an epic for updating our analytics dashboard to include real-time metrics."

### Good (3-Part Directive):
* **Context:** "We operate a Large, complex existing software system. This feature only touches the `Telemetry` subsystem and the `Reporting` UI. It does NOT touch `Billing`."
* **Task:** "Define the business capability for Real-Time Streaming Analytics. The focus is exclusively on sub-second latency for admin users."
* **Constraint:** "Output this as a markdown bulleted list. Do not propose technical stack solutions (e.g. Kafka vs. Redis); leave that to the Builders."

## Exercise: Re-writing the Vague Request
**Scenario:** You need an AI to help you draft the scope for expanding your enterprise SaaS to support European languages (Localization).

**Your Prompt:** "Draft an epic for SaaS Localization."

**Action Required:**
Right below this line, rewrite the above prompt using the 3-Part Directive structure.
* **Context:** [Fill in constraints about what existing systems Localization will touch]
* **Task:** [Explicitly define what the AI is helping you define]
* **Constraint:** [Tell the AI exactly what format to output, and what *not* to do]

*(Once complete, proceed to the next module)*

---
[**Next Module: Adversarial Thinking →**](./02_adversarial_thinking.md)
