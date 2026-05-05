# Lab Workbook: Registries, Chaining, & Routing

## 🎯 Lab Objectives
1.  **Build a Function Registry:** Define a tool that bounds the AI's actions.
2.  **Chain Context:** Programmatically assemble a persona, a rule, and a task.
3.  **Implement a 2-Tier Route:** Create a 1-hop link from a Global Router to a Domain Context.

---

## Lab 1: The Function Registry (Module 4)

**The Scenario:**
You are building a "Currency Validation" service. You want to give the AI a tool that checks if a currency code is valid, but you DO NOT want it to write its own validation logic.

### Your Task
Create a JSON tool definition (following the `function_registry.md` template) for a function called `verify_iso_currency`. It should take a `currency_code` (string) as a parameter.

*Check your work:* Does your JSON schema include a `description` that explicitly tells the AI to use this tool instead of writing a regex?

---

## Lab 2: The 2-Tier Route Test (Module 5)

**The Scenario:**
You are about to ask the AI to write the point accrual logic. You must use the 1-Hop pattern to provide the domain context and the task requirements simultaneously.

### Your Task
Execute a prompt in your IDE (using `@workspace` or your Agent CLI) that explicitly directs the AI to the specific Tier 2 domain context.

### Answer Key (Compare Your Work)
Run this exact prompt in your AI Chat:
> *"@workspace Load the domain context from `docs/context/billing.md`. This file contains the ADRs and the active story for FEAT-101. Using ONLY the Function Registry tools, implement the point accrual logic defined in the story."*

**The Result:** You will witness the AI skip the "hunting" phase. It goes directly to the truth, reads the ADR for integer precision, and applies the logic from the story on the first try.

---

## Lab 3: Breaking the Chain (Troubleshooting)

**The Scenario:**
Your AI agent is ignoring the `ADR-042` (Integer-only math) and is using floats anyway. 

### Your Task
1.  Look at your **Context Chain**. Is the ADR buried at the top of a 20,000-token file?
2.  **Fix:** Move the "HARD CONSTRAINT" into a **System Skill** (see `skills.md`) and inject it at the *bottom* of the prompt, right before the user command.

---

## ✅ Lab Completion Check
- [ ] I have a valid JSON schema for my registry.
- [ ] My AI agent successfully read a file path I provided in a prompt.
- [ ] I successfully forced the AI to follow an ADR it was previously ignoring.

1. [**Proceed to Module 5: Context Chaining & Codebase Routing →**](./05_context_chaining_and_routing.md)
2. [**Proceed to Module 6: 2-Tier Precision Routing Architecture →**](./06_information_routing_structure.md)
