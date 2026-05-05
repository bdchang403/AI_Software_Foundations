# Module 1: The 3-Part Directive for Architecture

## Theory: Stop Using AI as a Magic Wand
When builders get access to an AI agent, they often provide a single line: *"Implement the checkout flow."*
The AI then hallucinates folder structures, ignores existing design patterns, and injects foreign libraries.

You must structure your prompt to the AI agent using a strict **3-Part Directive**:
1. **Context Boundary:** Defining the exact files and registries the AI is allowed to look at.
2. **Task Instruction:** The explicitly scoped requirement.
3. **Format/Constraint:** The rigid standard the code must follow (e.g., your company's linter or `skills.md` template).

## Verbose Example
### Bad (For AI):
"Refactor the authentication middleware."

### Good (Context-Rich 3-Part Directive):
* **Context:** "We are working in the `src/middleware/auth` boundary. The Requirements Lead's semantic blueprint has mapped this feature exclusively to the `verifyToken.ts` and `errorHandler.ts` files."
* **Task:** "Refactor `verifyToken.ts` to utilize the new Redis caching layer defined in ADR-042."
* **Constraint:** "Do not modify the public API schema of `verifyToken.ts`. Provide your output as a unified diff. Wrap all errors in the standard `DomainError` class."

## Exercise: Re-writing the Vague Request
**Scenario:** You have a Semantic Blueprint from the Requirements Lead that states the system needs to "Emit a new event when a user is successfully invoiced."

**Your Action:**
Write the 3-Part Directive below. 

* **Context:** [Define what files the AI should look at, and what it should ignore]
* **Task:** [Explicitly define the trigger and event name]
* **Constraint:** [Rule out hallucination: e.g., "Use the existing EventBus class, do not install a new library."]

---
[**Next Module: Adversarial Thinking →**](./02_adversarial_thinking.md)
