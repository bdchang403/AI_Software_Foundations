# Bridge Module 2: The Assembly Mechanism

How does a markdown file in a folder become an agent's "Brain"? This is the **Assembly Mechanism**. 

## 🧠 The Theory of Orchestrated Assembly

To understand why the assembly must be structured this way, we must look at how modern LLMs process information.

### 1. The LLM is Stateless
An AI Agent has no "long-term memory" of your project unless you provide it in the prompt. If you don't provide the ADRs or the 3-Part Directive, the AI reverts to its "Generic Training Data," which is where hallucinations begin. Assembly is the act of **rebuilding the world** for the AI at the start of every task.

### 2. High-Fidelity Chaining vs. Prompt Bloat
As we learned in [The Mathematics of AI Risk](../00_THE_MATHEMATICS_OF_AI_RISK.md), LLMs suffer from **"Lost in the Middle"** syndrome. When a codebase reaches the **"20,000 Line Cliff,"** the AI's accuracy plummets as the task-relevant signal is buried under the noise of the repository.

*   **Legacy Approach:** Paste a massive codebase (10k+ lines) into a prompt. (Result: The AI loses the "thread" of the task and begins to hallucinate logic).
*   **The Context Factory Approach:** Chain 3 small, high-fidelity artifacts (Persona + Registry + Story). By keeping the payload small, you keep the critical "Signal" in the AI's high-attention zones. (Result: <5% Hallucination rate).

### 3. Separation of Concerns
By separating the **Soul** (Identity), **Memory** (Knowledge), and **Hands** (Tools), we create a maintainable system:
*   If you change your database from Postgres to DynamoDB, you only update the **ADR** (Memory). You don't have to rewrite the persona or the task.
*   The Orchestrator "compiles" these separate files into a final System Prompt just-in-time.

---

## 🛠️ The Assembly Manifest (`.agent.md`)

How does an orchestrator "build" the agent? It uses a manifest file to chain your Phase 2 artifacts together. Below are the concrete configurations for the agents referenced in the blueprint.

### 1. Example: The Billing Specialist Agent
**Path:** `.github/agents/billing-agent.agent.md`

```markdown
# Agent: Billing Specialist

**Pillar 1: Soul (The 3-Part Directive)**
*   **Role:** Senior Financial Builder & VAT Specialist.
*   **Task:** Calculate localized VAT for international invoices.
*   **Format:** Validated JSON object per `ADR-042` standards.

**Pillar 2: Memory (Context & Adversarial Guardrails)**
*   **Domain Context:** `docs/context-map.md#billing`.
*   **Adversarial Constraint:** NEVER use floating-point math (Red-Teamed in Phase 2).
*   **Historical Truth:** Read archived requirements in `docs/stories/BILL-101.md`.

**Pillar 3: Hands (Skills)**
*   **Tool Registry:** `src/billing/tools.json`
*   **Allowed Actions:** `apply_tax_rate`, `get_exchange_rate`.
```

---

### 2. Example: The Research & Audit Agent
**Path:** `.github/agents/research-agent.agent.md`

```markdown
# Agent: Regulatory Research Lead

**Pillar 1: Soul (The 3-Part Directive)**
*   **Role:** Lead Compliance Auditor.
*   **Task:** Verify AI-SBOM lineage across the `main` branch.
*   **Format:** A DORA-compliant Traceability Report.

**Pillar 2: Memory (Context & Adversarial Guardrails)**
*   **Reference Material:** `00_REGULATORY_MODEL_GOVERNANCE.md`.
*   **Adversarial Constraint:** Flag any code block without a valid SPDX 3.0 citation as "Untrusted."
*   **Governance Baseline:** `00_PREREQUISITES_AND_BASELINES.md`.

**Pillar 3: Hands (Skills)**
*   **Tool Registry:** `docs/registries/audit-skills.json`
*   **Allowed Actions:** `grep_codebase`, `verify_citation`, `validate_sbom`.
```

---

## 🏛️ The Concatenation Loop (How it works)

In a production environment, the orchestrator (Antigravity, Codex, or Claude Code) dynamically builds the system prompt by following the "Hardcoded Pointers" in these manifests.

If the **Builder's Registry** is updated, the **Agent's Hands** are automatically upgraded. If the **Strategy Lead's ADR** changes, the **Agent's Memory** is instantly corrected. 

---

[**Next: Testing the Agent Config →**](./03_testing_the_agent_config.md)
