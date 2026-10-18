# Master Skills Template Hub

This directory contains the "Cognitive Scaffolding" for your AI Agents. These templates ensure that regardless of the IDE or LLM used (Copilot, Cursor, Claude Code), the agent adheres to the **Context Factory** standards.

## 📂 Included Templates

### 1. 2-Tier Precision Routing (The Brain)
- [**Master Router**](./master_router.md): The primary entry point.
- [**Domain Contexts**](./context/): Sub-files for domain-specific rules (e.g., Billing, Auth).
- [**Story Templates**](./stories/): Context-enriched story templates and the **Semantic Blueprint Gallery**.
- [**Functions Registry**](./functions_registry.md): Defines available agentic tools.

### 2. Platform Scaffolding
- [**Platforms Hub**](./platforms/): Includes tailored rules for Copilot, Cursor, and Claude Code.
- [**Agent Examples**](./agents/): Real-world configurations for GitHub Agents, Antigravity, Codex (OpenAI), and Claude Code.
- [**Skills Hub**](./skills/): Defines specific personas (Coder, Reviewer, Auditor).

### 3. Auditability (The AI Trailer)
Every template now includes mandatory **AI Trailers** for commit messages and PR reviews. This ensures that AI-assisted changes are distinguishable from human-only changes in the audit log.

### 4. Empirical Telemetry & Governance Benchmark (Canonical Standard)
- [**Empirical AI Telemetry, Repository Economics & Governance Benchmark**](./EMPIRICAL_AI_TELEMETRY_AND_GOVERNANCE_BENCHMARK.md): The canonical empirical reference manual for enterprise autonomous software engineering. Codifies longitudinal developer telemetry, the GitClear 211M LOC code churn and duplicate logic inversion (+39% churn, 10x duplicate blocks), Google Cloud DORA 2024–2026 delivery stability telemetry and the 2026 DORA Verification Trap, Faros AI PR review bloat (+91% cycle duration, +9% defects), the Stack Overflow 63.3% Context Wall, repository noise analysis (83% non-source clutter), the 5-Level Comparative Context Maturity Model, quantitative multi-model pipeline economics (83.8% OpEx reduction, \$25.50 vs \$157.50), and statutory mappings across NIST AI RMF 1.0, ISO/IEC 42001:2023, and EU AI Act (Regulation (EU) 2024/1689).

---

## 🛠️ Usage
1. Copy the relevant template to your repository's configuration directory.
2. Replace the `[BRACKETED]` placeholders with your specific project details.
3. Update the **Master Router** whenever new microservices or architectural domains are added.
