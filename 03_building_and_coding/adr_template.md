# Architecture Decision Record (ADR)

*Authoring prompt for LLM: "Generate an ADR following this exact template, storing context explicitly so future LLM context queries can easily parse it without noise."*

---

**ADR-ID:** `[e.g., ADR-0042]`
**Title:** `[Short noun phrase]`
**Date:** `[YYYY-MM-DD]`
**Status:** `[Proposed | Accepted | Deprecated | Superseded]`
**Context Link (Epic):** `[Epic ID / Semantic Blueprint link]`

## 1. Context and Problem Statement
*Describe the context driving this decision. Why are we making this change now? Keep it token-efficient (concise).*

## 2. Decision Drivers
*What constraints influenced this? (e.g., Scaled Agile deadline, 200k token processing limit on AI, database horizontal scaling).*
- [Driver 1]
- [Driver 2]

## 3. Considered Options
*What other patterns did we consider? Let the AI know what was rejected so it doesn't suggest them again.*
1. [Option 1]
2. [Option 2]

## 4. Decision Outcome
*What did we choose and why?*
Chosen option: "[Option 1]", because [justification].

## 5. Consequences & Agentic Constraints
*What explicit rules does this impose on future AI operations?*
- **Positive:** [e.g., Reduced latency]
- **Negative:** [e.g., Increased dependency on cache]
- **AI Constraint:** **Agents must now validate data against `Schema Registry V2` before executing DB mutations.** (Add this to `skills.md`).
