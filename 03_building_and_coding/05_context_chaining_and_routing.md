# Module 5: Context Chaining & Codebase Routing (The Orchestrator)

## 🧠 Theory: The Physics of Token Compression & Risk Mitigation

In a 500,000 LOC codebase, an AI cannot "read" your repository. If you attempt to feed it the whole repo, you will exceed the token window and suffer from massive latency. More importantly, as discussed in [The Mathematics of AI Risk](../00_THE_MATHEMATICS_OF_AI_RISK.md), feeding an AI too much context exponentially increases the mathematical probability of a **Compound Hallucination**.

**Context Chaining** is the process of programmatically assembling a "Surgical Payload" that only contains the 1% of code necessary for the task, mathematically minimizing the hallucination surface area.

The industry has converged on a **2-Tier Precision Routing** model: 
1.  **Tier 1 (Traffic Controller):** Points the AI to the domain.
2.  **Tier 2 (Surgical Payload):** Directly injects all domain knowledge and task requirements in a single ingestion event.

---

## 🛠️ 1. Literal Code: The Context Assembler

In the Context Factory, you don't talk to the AI directly. You use an **Orchestrator Script** (Python/Node) to build the prompt by concatenating your Markdown artifacts.

### 📜 `orchestrator.py` (The Pattern)
```python
import os

def assemble_context(story_id, domain):
    # 1. Load the Persona & Corporate Constitution (Global Identity)
    persona = "You are an Expert Enterprise TypeScript Builder."
    constitution = open("00_ENTERPRISE_CONSTITUTION.md").read()
    
    # 2. Load the Tier 2 Domain Context (The 'Rules' + 'The Why')
    domain_context = open(f"docs/context/{domain}.md").read()
    
    # 3. Load the Active Task (The 'What')
    story = open(f"docs/stories/{story_id}.md").read()
    
    # 4. Chain the Payload for 1-Hop Execution
    final_prompt = f"{persona}\n\n### CONSTITUTION ###\n{constitution}\n\n### DOMAIN CONTEXT ###\n{domain_context}\n\n### THE TASK ###\n{story}"
    
    return final_prompt
```

---

## 🏗️ 2. Injecting the "Hands" (Tool Definitions)

The AI needs to know it has tools to "walk" the repo. You must convert your `function_registry.md` into a JSON structure the API understands (OpenAI Tool format).

---

## 🔄 3. 2-Tier Precision Routing in Action

Instead of forcing the AI to "hunt" or "hop" through the repository, the Context Factory uses **1-Hop Ingestion**:

1.  **Identification:** The Orchestrator identifies the target domain (`src/billing`).
2.  **Assembly:** It automatically pulls the **Tier 2 Domain Context** (ADRs/Standards) and the **Active Story** into a single system prompt.
3.  **Execution:** The AI receives a bounded, high-fidelity environment and generates code on the first try.

**ROI:** Total tokens used: **~4,000**. Total time: **< 5 seconds**. 

---

## 🛠️ Exercise: Build your first "Chain Logic"

**Scenario:** You need to fix a massive memory leak in the `InvoiceProcessor.ts` file.

**Your Action:**
1.  **Select the Files:** Which 2 files would you chain together to ensure the AI knows the memory standards for this domain?
2.  **Order the Chain:** Place them in the order that prevents the AI from forgetting the "Global Performance Constraints."

---

[**Next Module: 2-Tier Precision Routing Architecture →**](./06_information_routing_structure.md)
