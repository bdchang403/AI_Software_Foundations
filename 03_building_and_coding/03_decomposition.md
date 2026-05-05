# Module 3: Code Decomposition (PR Slicing)

## Theory: The Token Limit vs. The Pull Request
A massive 500k LOC repository is essentially a black box to an AI with a 200k token limit. 
If a Requirements Lead gives you an Epic Blueprint, you cannot say to the AI: *"Implement this whole blueprint."* 

You must decompose the implementation into **Sequential Pull Requests (PRs)**. Each PR must fit comfortably within the token logic limit (usually ~20k-50k tokens of context).

### The Decomposition Pipeline
1. **PR 1: Database & Schemas:** (AI Context: Only SQL migration files).
2. **PR 2: Core Domain Logic:** (AI Context: Only the schema output from PR 1, and the domain model files).
3. **PR 3: API / Interface:** (AI Context: Only the domain models from PR 2, and the router files).

If you feed the AI one slice at a time, it will generate flawless code.

## Exercise: Slice the Implementation

**Scenario:** Implement a new "Subscription Upgrade" workflow. It involves a new DB table `subscription_history`, a new `BillingManager` class, and a new `PUT /api/upgrade` route.

**Your Action:**
Write the sequential prompts you would feed an AI to build this feature across three isolated steps. For each step, define what files the AI is *allowed* to read.

1. **Slice 1 Prompt & Context Files:** [e.g., Read `schema.prisma`. Task: Add the table.]
2. **Slice 2 Prompt & Context Files:** [...]
3. **Slice 3 Prompt & Context Files:** [...]

---
[**Next Module: Context Engineering (Registries & Skills) →**](./04_context_engineering.md)
