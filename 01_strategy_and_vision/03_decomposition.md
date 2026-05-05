# Module 3: Decomposition Mathematics (Token Constraints)

## Theory: The Mathematical Proof for Bounded Context
Why is the "Context Factory" required? Why can't we just use a 2 Million Token Context Window to analyze the whole 500k LOC repository at once?

Let's do the math.

* **1 Line of Code (LOC)** $\approx$ 8 Tokens (including whitespace, syntax, variable names).
* **500,000 LOC Enterprise Monolith** $\approx$ 4,000,000 Tokens. 

If you as the Strategy Lead give an open-ended Epic like *"Rebuild the E-Commerce flow"*, the AI Builder Agent mathematically cannot ingest your codebase. It will hit a hard limit.

Even if you use a 2M token model (like Gemini 1.5 Pro) and "stuff" half the codebase into it:
1. **The "Lost in the Middle" Phenomenon:** LLMs degrade in accuracy when the context window exceeds 100k tokens. They forget variables declared at token #40,000 when they are writing code at token #1,200,000. 
2. **Cost:** Sending 2 Million tokens per prompt (for hundreds of iterations) is financially catastrophic.

## The Scaled Agile Solution: Mathematical Boundry

You must structurally decompose your Epic so that the combined Context Boundary (The files required) is `< 50,000 tokens`.

- `Epic 1: The UI Layout (10 React components)` = ~4,000 tokens. **(SAFE)**
- `Epic 2: The Logic (5 Controllers)` = ~3,000 tokens. **(SAFE)**

 As the Strategy Lead, your primary job in the AI era is to look at the business request and mathematically guarantee it can be executed in a small, isolated sandbox without bleeding into the 4 Million token monolith.

---
[**Next Module: Context Engineering →**](./04_context_engineering.md)
