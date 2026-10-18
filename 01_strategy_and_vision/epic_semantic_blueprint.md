# Context Data Template: Epic Semantic Blueprint

*This template serves as the authoritative input contract for the Requirements Lead's reasoning engine, emitted by the Strategy Lead / Product Owner.*

## 1. Epic Execution Metadata
- **Epic ID**: `[EPIC-SYS-001]`
- **Title**: `[Strategic Initiative Title]`
- **Strategic Owner**: `[Product Owner / Strategy Lead Role]`
- **Target Subsystem**: `[Bounded Subsystem Domain Path]`
- **Max Token Budget**: `[<= 15,000 tokens for entire Epic]`
- **Max Story Blast Radius**: `[<= 4,000 tokens per child story]`
- **Target File LOC**: `[<= 400 lines per module per Architectural Modularity Ceiling (<= 400 LOC)]`
- **Governing Invariants**: `[e.g., I01, I02, I04, I07, I15, I20]`

---

## 2. Business Intent (3-Part Directive)
- **Role**: `[Explicit persona, bounded permissions, and isolated toolset]`
- **Task**: `[Deterministic functional transformation, input schemas, and expected output DTOs]`
- **Constraint**: `[Constitutional locks, invariant bindings, and negative boundary assertions]`

---

## 3. Epistemic Sandbox & Domain Boundaries (Role-Based Epistemic Slicing Guardrail)
*Enforce strict context bounding to prevent token bloat and cognitive attention dilution.*
- **Included Code Paths (In Sandbox)**: `[e.g., src/telemetry/*, schemas/events.py]`
- **Air-Gapped Context (Unidirectional Epistemic Air-Gap Guardrail Prohibited)**: `[e.g., portfolio/live_positions.db, clinical/patient_records.db]`
- **Out-of-Bounds Systems**: `[e.g., legacy/billing/*, admin/console/*]`

---

## 4. Mathematical Contracts & De-Biasing Filters
- **Primary Formulation**:
  $$[LaTeX Mathematical Formulation]$$
- **Unstructured Intelligence Discount (Unidirectional Epistemic Air-Gap Guardrail)**:
  All external media or vendor marketing with commercial conflicts (`commercial_conflict: true`) must apply the 80% discount:
  $$W_{\text{eff}} = W_{\text{Brier}} \times 0.20, \quad \text{Polarity}_{\text{stored}} = \text{round}(\text{Polarity}_{\text{raw}} \times 0.20, \; 2)$$
- **Telemetry Decay ($I_{17}$)**:
  $$w(\Delta t) = w_0 \cdot 2^{-\Delta t / t_{1/2}}$$

---

## 5. Explicit Negative Constraints (Constitutional Red-Team Patches)
*Explicitly close loopholes that autonomous agents might exploit during implementation.*
- **Zero-Mock Enforcement ($I_{01}$)**: The agent MUST NOT generate synthetic constants in exception handlers (`return 0.50` or `return 200.0` is strictly forbidden). If live dependencies fail, fail closed: return `None` or raise a domain exception.
- **Immutable Quarantine Mandate ($I_{04}$)**: Raw SQL `DELETE` calls are permanently prohibited. Invalidate records via append-only archival to designated quarantine ledgers.
- **Fail-Closed Fallback ($I_{05}$)**: Upstream service timeouts must return typed closed-world schemas with missing attributes explicitly marked as `UNAVAILABLE`.
