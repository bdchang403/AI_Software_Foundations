# Module 4: Context Engineering (The Builder's Guardrails)

## 🧠 Theory: Translating Blueprints to Architecture

As a Builder in the **Context Factory**, your job is not just to write code. It is to take the *Semantic Blueprint* created by the Requirements Lead and translate it into physical, structural guardrails for the AI.

If the Requirements Lead says, "The AI MUST NOT touch the database schema," you are the one who builds the physical sandbox that enforces that rule.

---

## 🛠️ 1. The Function Registry (The "Hands" of the Agent)

To prevent the AI from randomly guessing logic or reading thousands of files to understand your architecture, you must construct a **Function Registry**. 

The registry acts as a knowledge graph of upstream and downstream dependencies, and strictly defines what tools the AI can execute. 

> **Deep Dive:** [Read the full guide on building the Function Registry schemas here.](./function_registry.md)

---

## 🏗️ 2. The ADR (Architectural Decision Record)

### 📜 Literal Code: `0003-use-hexagonal-architecture.md`
```markdown
# ADR 0003: Use Hexagonal Architecture

## Context
Our AI Agents frequently struggle with "Spaghetti Code" where database logic is mixed with UI logic. This causes the AI to hallucinate database changes in frontend PRs.

## Decision
We will use **Hexagonal Architecture** (Ports and Adapters). All business logic must live in `src/domain/`. All infrastructure (DB, API) must live in `src/infrastructure/`.

## Consequence for AI
When the AI reads this ADR, it is FORCED to separate concerns. It will generate a 'Port' interface before implementing a 'Database Adapter.'
```

---

## 🛠️ Exercise: Building the Physical Guardrails

**Your Action:**
1. **Review the Blueprint:** Assume the Requirements Lead handed you a Semantic Blueprint that states: `[BOOLEAN: FALSE] Modifying database schema files`.
2. **Write the ADR:** Create a new ADR (e.g., `0004-database-schema-locks.md`) that explicitly states: "All database schema changes must be manually executed by a human DBA. The AI agent must only generate migration scripts in `src/db/migrations` and MUST NOT execute them."
3. **Register the Function:** Go to the [Function Registry Template](./function_registry.md) and define a tool called `generate_migration_script` that only writes to that specific directory.

---

### 🚀 Continue the Journey
Now that you know how to build physical architectural guardrails, proceed to the next module to learn how to actively route the AI into those sandboxes.

[**Next Module: Context Chaining & Codebase Routing →**](./05_context_chaining_and_routing.md)
