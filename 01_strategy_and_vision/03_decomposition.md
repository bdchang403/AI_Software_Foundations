# Module 3: Strategic Decomposition Mathematics & Blast Radius Management

## 🔢 The Mathematical Proof for Bounded Context

A common misconception among enterprise leadership is that massive Large Language Model context windows (e.g., 1 Million to 2 Million tokens) eliminate the need for software modularity and task decomposition. Strategy Leads often ask:
> *"Why can't we simply feed our entire 500,000 LOC enterprise codebase into a single prompt and ask the AI to refactor our system?"*

The answer is dictated by the fundamental mathematical laws of Transformer attention mechanics, attention entropy, and token economics.

---

### 1. Quadratic Computational Scaling and Attention Entropy

In the standard Transformer architecture, computing self-attention across a sequence of $N$ tokens requires calculating the pairwise dot product between Query ($Q$) and Key ($K$) representations in $\mathbb{R}^{N \times d_k}$:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

The computational workload scales quadratically with sequence length $N$:
$$\text{FLOPs}_{\text{attention}} \sim 2 \cdot L \cdot H \cdot N^2 \cdot d_k$$
where $L$ is the layer count and $H$ is the attention head count.

As the context window expands, the softmax probability mass disperses across thousands of irrelevant tokens. The information-theoretic attention entropy across sequence length $N$ is defined as:
$$\mathcal{H}(A_i) = -\sum_{j=1}^N A_{ij} \ln A_{ij}$$

As $N \to \infty$, the maximum entropy approaches $\ln N$. When attention entropy is high, the model's focus becomes diffuse, causing it to overlook critical conditional predicates, negative constraints, and type signatures.

---

### 2. The U-Shaped Attention Curve ("Lost in the Middle")

Empirical evaluations of large context models demonstrate a pronounced U-shaped retention fidelity curve. Retrieval accuracy $F(x)$ across relative context coordinate $x \in [0.0, 1.0]$ exhibits severe degradation:

$$F(x) = \begin{cases} 
1.0 - k_1 x & x \in [0.0, 0.15] \quad \text{(Primacy Bias: High Recall)} \\
0.35 + \epsilon(x) & x \in (0.15, 0.85) \quad \text{(Degradation Valley: 40%–75% Loss)} \\
1.0 - k_2 (1.0 - x) & x \in [0.85, 1.0] \quad \text{(Recency Bias: High Recall)}
\end{cases}$$

When an enterprise codebase of 500,000 LOC ($\approx 4,000,000$ tokens) is stuffed into an unconstrained prompt:
1. **The Middle Zone Collapse**: System constraints and business logic placed in the middle 70% of the prompt suffer a 40% to 75% probability of being ignored during generation.
2. **Diff Corruption & Feature Erasure**: The model experiences token amnesia, frequently hallucinating missing helper functions, dropping error handlers, or truncating existing code with comments like `# ... existing logic remains unchanged ...`.

---

### 3. Token Economics & The Daily Spend Ceiling (ADR-011)

Unconstrained prompts are financially unsustainable in enterprise production. Executing a 500,000-token context sweep across 50 iterations costs hundreds of dollars per feature. 

Under Invariant $I_{21}$ and ADR-011, autonomous systems operate under a **Rolling 24-Hour Micro-USD Spend Quota**:
$$Q_{\text{rem}} = Q_{\text{limit}} - \sum_{t \in 24\text{h}} \text{Spend}_t, \quad Q_{\text{limit}} = \$0.40/\text{day} = 400,000\,\mu\text{USD}$$
with an individual subsystem/ticker spend ceiling:
$$Q_{\text{subsystem}} \le \$0.08/\text{day} = 80,000\,\mu\text{USD}$$

To remain within these mathematical constraints, the Strategy Lead must enforce **Strict Task Decomposition**.

---

## ✂️ The Strategic Decomposition Hierarchy

The Strategy Lead establishes an invariant-bounded slicing hierarchy that governs downstream engineering:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE DECOMPOSITION HIERARCHY                     │
├────────────────────────────────────────────────────────────────────────┤
│ Level 1: Enterprise Vision & Regulatory Mandates                       │
│          (Unbounded Natural Language Stakeholder Goals)                │
│                                  │                                     │
│                                  ▼                                     │
│ Level 2: Epistemic Epic Sandbox (< 50,000 Tokens)                      │
│          Bounded Sub-System: Single Domain Service (e.g. Ingestion)    │
│          Governing Invariants: I_01, I_04, I_20                        │
│                                  │                                     │
│                                  ▼                                     │
│ Level 3: Context-Enriched User Story (< 4,000 Tokens Blast Radius)     │
│          Single Functional Unit (ADR-016 <= 400 LOC)                   │
│          Machine-Executable 3-Part Directive & Semantic Blueprint     │
└────────────────────────────────────────────────────────────────────────┘
```

### Invariant Slicing Rules

1. **The 50k-Token Epic Ceiling**: An Epic must never encompass more than one bounded subsystem. Total context required to reason about the Epic must remain strictly below 50,000 tokens.
2. **The 4k-Token Story Blast Radius**: Each user story must be sized so that an autonomous agent can complete the implementation, unit tests, and verification in a single turn without exceeding a 4,000-token input/output budget.
3. **Multi-Subsystem Isolation ($I_{16}$)**:
   $$\forall s_1 \neq s_2: \text{State}(s_1) \cap \text{State}(s_2) = \emptyset$$
   State, memory, and telemetry from Subsystem 1 must never bleed into Subsystem 2. Loop-carried scalar contamination across batch loops is structurally banned.

---

## 🔬 Dual-Use Regulated Callout Boxes

### Callout 1: Algorithmic Asset Management (Multi-Ticker Isolation)
In multi-asset portfolio rebalancing, processing a universe of 500 equities within a single unconstrained loop leads to loop-carried contamination ($I_{16}$).
- **The Failure**: In a batch iteration, the spot price of an illiquid small-cap ticker ($t_{14}$) leaked into the evaluation context of a mega-cap tech compounder ($t_{15}$). The model calculated a 90% discount relative to historical DCF, triggering an erroneous allocation.
- **Strategic Decomposition**: The Strategy Lead partitions the universe into discrete single-ticker evaluation sandboxes ($Q_{\text{ticker}} \le \$0.08/\text{day}$). Each ticker evaluation runs in an isolated sub-process with independent memory allocation, satisfying Invariant $I_{16}$.

### Callout 2: FDA Class III ICU Multi-Bed Patient Monitoring
In a hospital intensive care telemetry platform monitoring 32 beds:
- **The Failure**: An unconstrained AI summarizer ingests telemetry streams from Bed 1 through Bed 32 in a single rolling context window. In the middle degradation valley (Beds 10–22), the attention weights blur. The elevated intracranial pressure (ICP) of Bed 12 is mistakenly attributed to Bed 14, causing the agent to issue an inappropriate mannitol diuretic order.
- **Strategic Decomposition**: The Strategy Lead establishes an unbreachable patient sandbox boundary. Each bed constitutes an independent Epic domain with a dedicated 4k-token blast radius. Multi-patient cross-contamination is blocked at the schema level ($I_{16}$), guaranteeing that telemetry packets carry cryptographic patient UUIDs that fail closed if mismatched.

---

## 🛠️ Worked Decomposition Example

### Monolithic Initiative (Flawed):
> *"Rebuild the hospital emergency department clinical triage and billing integration system to support real-time sepsis detection and automated insurance pre-authorization."*

### Strategy Lead Decomposition (Compliant):

| Slice ID | Slice Title | Bounded Context Scope | Token Budget | Governing Invariants |
| :--- | :--- | :--- | :--- | :--- |
| **EPIC-SEP-01** | **Arterial Lactate & Vitals Sepsis Scout** | Ingestion of blood gas analyzer telemetry & bedside pulse oximetry. | $< 12,000$ tokens | $I_{01}$ (Zero Mock), $I_{03}$ (Fatal Veto) |
| **EPIC-SEP-02** | **qSOFA Clinical Decision Alert Dispatcher** | Deterministic score calculation & pager alert bus emission. | $< 8,000$ tokens | $I_{02}$ (Plausibility Band), $I_{07}$ (Div-by-Zero) |
| **EPIC-SEP-03** | **Sepsis Episode Quarantine & Audit Ledger** | Archival of invalidated lab results and false positives. | $< 6,000$ tokens | $I_{04}$ (Immutable Quarantine), $I_{15}$ (UUID Trace) |
| **EPIC-SEP-04** | **Insurance Pre-Authorization Gateway** | Air-gapped insurance claim submission (decoupled from acute ICU loop).| $< 15,000$ tokens | $I_{20}$ (Epistemic Air-Gap) |
