# Master Context Router

You are an AI agent operating within the **Context Factory**. You MUST use this router to find the source of truth for your current task.

## 1. Core Directives (Always Load)
1.  [**Enterprise Constitution**](../00_ENTERPRISE_CONSTITUTION.md)
    *   *Rules that apply to every single line of code written in the company.*
2.  [**Regulatory & Governance Baselines**](../00_REGULATORY_MODEL_GOVERNANCE.md)

## 2. Dynamic Domain Routing
Depending on the file path you are modifying, you MUST load the corresponding context file from `./context/`:

| Path Pattern | Context File |
| :--- | :--- |
| `src/domain_a/**` | [Domain A Context](./context/example_domain_context.md) |
| `src/domain_b/**` | [Domain B Context](./context/example_domain_context.md) |

## 3. Active Story Context
Before starting any work, you MUST locate the active story:
- Path: `docs/stories/[STORY-ID].md`

## 4. AI Trailer Rule (Auditability)
For every commit message you suggest or code review you perform, you MUST append a trailer:
- **Generated Code:** `AI-Generated-By: [LLM Name]`
- **AI Review:** `AI-Reviewed-By: [LLM Name]`
- **Reasoning:** This is required for Article VII Reproducibility.
