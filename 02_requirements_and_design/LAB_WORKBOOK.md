# Requirements Lead Lab Workbook: Context-Enriched Semantics

Welcome to the Requirements Lead Lab. You are the critical bridge in the Context Factory. The Strategy Lead gave you a bounded idea. Now, you must translate that idea into a **context-enriched story** that is mathematically strict enough for a Builder's AI Agent to ingest without hallucinating.

---

## Lab 1: The 3-Part Directive (Module 1)

**The Scenario:**
The Strategy Lead handed you Epic 1: "Implement point accrual logic."
A traditional Requirements Lead might write: *As a user, I want to earn 1 point for every dollar I spend, so I get rewarded.*
If a Builder feeds this to an AI Agent, the AI will invent its own mathematical rounding rules and database structure.

### Your Task
Rewrite this requirement using the **3-Part Directive** (Role, Task, Format) so it acts as a programmatic constraint.

### Answer Key (Compare Your Work)
*   **Role:** You are the Point Accrual Service.
*   **Task:** Listen to the `OrderComplete` event. Multiply the `order_total` by 1.
*   **Format:** Output the result to the `LoyaltyLedger` database table using the exact schema defined in `LedgerSchema.ts`.

---

## Lab 2: Adversarial Edge Case Generation (Module 2)

AI Agents struggle with "unhappy paths" unless explicitly told to look for them.

### Your Task
Before you hand the story to the Builder, you must generate 3 adversarial edge cases that the AI must account for.
Open an AI Chat tool (like ChatGPT or Copilot Chat) and prompt it to attack your logic.

**Execute this prompt in your AI Tool:**
> *"I am building a rule where users earn 1 point per $1 spent. Attack this logic. Give me 3 edge cases where this math breaks down or causes a business vulnerability."*

### Answer Key (Compare Your Work)
Your AI should have generated edge cases like:
1.  **Fractional Dollars:** What happens if the user spends $1.99? Does it round up to 2 points, round down to 1, or use floating-point points?
2.  **Refunds/Chargebacks:** If an order is refunded, are the points automatically clawed back? What if the user already spent them?
3.  **Discounts/Taxes:** Are points calculated on the subtotal, or the total after tax and shipping?

*You must now add the explicit answers to these edge cases into your [Context-Enriched Story Template](../templates_and_resources/stories/context_enriched_story_template.md).*

---

## Lab 3: Repository Injection (Module 4)

Context is useless if the Builder's AI cannot see it.

### Your Task
Take your finished 3-Part Directive and the Edge Cases from Lab 1 and 2. 
Format them using the [Context-Enriched Story Template](../templates_and_resources/stories/context_enriched_story_template.md). 
**Crucial Step:** You must physically export this markdown file from Jira/Confluence and commit it to the repository (e.g., `/docs/stories/LOYALTY-101.md`). 

If you do not do this, the Builder's AI Agent will be blind.

---

## 🏁 The Finish Line

Congratulations! You have successfully translated a high-level strategic vision into a machine-readable context payload. 

Now that your story is committed to the repository, proceed to the final phase to see how an AI Agent orchestrates your context into working software.

[**Proceed to Phase 4: Agent Orchestration & Assembly →**](../09_ai_agent_orchestration/01_anatomy_of_an_agent.md)
