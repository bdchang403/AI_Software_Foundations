# Module 3: Pipeline Decomposition, Modular Action Ceilings & Canary Wave Deployment

## 🧠 Theory: Pipeline Modularity & Blast Radius Containment

In continuous integration and delivery engineering, monolithic pipeline definitions create severe operational fragility. A single CI/CD workflow file exceeding 1,000 lines introduces three catastrophic failure modes:

1. **Context Window Attention Dilution**: When an autonomous agent attempts to modify a deployment step at line 850 in a 1,500-line YAML file, the model suffers from attention dilution. It frequently corrupts indentation, misconfigures environment variables, or accidentally deletes security verification steps in line 120.
2. **Blast Radius Cascades**: A minor change to a test dependency forces the entire monolithic workflow to re-execute, risking accidental triggers of downstream production deployment jobs.
3. **Impenetrable Debugging**: When an automated release fails in a monolithic script, diagnosing whether the failure originated in environment setup, compilation, security scanning, or cloud credential exchange requires extensive manual triage.

To eliminate these failure modes, BuilderOps engineers enforce the **Architectural Modularity Ceiling**:
* **Maximum 400 Lines of Code per Workflow or Composite Action**.
* **Refactoring Trigger at 350 Lines**.
* **Strict Separation of Concerns**: Isolate pipeline logic into atomic, reusable workflow blocks.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MONOLITHIC PIPELINE VS. MODULAR REUSABLE ARCHITECTURE                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ❌ MONOLITHIC DEPLOYMENT PIPELINE (HIGH BLAST RADIUS)                                          │
│   ┌────────────────────────────────────────────────────────────────────────────────────────┐     │
│   │ .github/workflows/deploy.yml (1,850 lines)                                            │     │
│   │ [Lint] ──► [Test] ──► [Security] ──► [Docker Build] ──► [K8s Deploy] ──► [Smoke Test] │     │
│   │ • Attention dilution in LLM edits                                                      │     │
│   │ • A typo in smoke testing triggers unwanted redeployments                              │     │
│   └────────────────────────────────────────────────────────────────────────────────────────┘     │
│                                                                                                  │
│   ✅ MODULAR REUSABLE PIPELINE ARCHITECTURE (CEILING <= 400 LOC)                                │
│   ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐                │
│   │ verify_integrity.yml  │  │ build_container.yml   │  │ deploy_canary.yml     │                │
│   │ (AST Zero-Drift & CI) │  │ (Trivy Scan & ECR)    │  │ (Wave Rollouts)       │                │
│   │ • Length: 120 LOC     │  │ • Length: 160 LOC     │  │ • Length: 210 LOC     │                │
│   └───────────────────────┘  └───────────────────────┘  └───────────────────────┘                │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🌊 Progressive Canary Wave Deployment Topology

When autonomous systems deploy software into production, releases must never transition from 0% to 100% traffic instantaneously. Instead, BuilderOps pipelines execute **Progressive Canary Wave Deployments**:

1. **Wave 0 (Internal Synthetic Shadow)**: Deploys the release to an isolated shadow environment and mirrors 5% of production read traffic without committing external writes.
2. **Wave 1 (Canary 10%)**: Routes 10% of live user traffic to the canary instance for 30 minutes while evaluating automated health and divergence metrics.
3. **Wave 2 (Broad Canary 50%)**: If Wave 1 exhibits zero metric anomalies, traffic scales to 50% for 60 minutes.
4. **Wave 3 (Full Promotion 100%)**: Release is promoted to 100% production traffic; older container tasks are gracefully drained and decommissioned.

```mermaid
flowchart TD
    subgraph Wave_0 ["Wave 0: Internal Verification & Shadowing"]
        A["Merge to main Branch"] --> B["Build Cryptographically Tagged Container"]
        B --> C["Deploy Shadow Instance (0% Live User Traffic)"]
        C --> D["Execute Hermetic Smoke Tests & Invariant Verification"]
        D --> E{"Smoke Tests Pass & Zero Drift?"}
        E -- "Failure Detected" --> F["ABORT: Immediate Rollback to Previous Stable"]
    end

    subgraph Wave_1 ["Wave 1: Canary 10% Live Traffic"]
        E -- "Verified Clean" --> G["Route 10% Production Traffic to Canary"]
        G --> H["Monitor Runtime Error Rates & Latency for 30 Minutes"]
        H --> I{"Error Rate Spike > 0.05% or Drift > USD 250.00?"}
        I -- "Anomaly Tripped" --> J["CIRCUIT BREAKER: Automated Instant Traffic Drain to 0%"]
        J --> F
    end

    subgraph Wave_2 ["Wave 2: Broad Canary 50% Traffic"]
        I -- "Healthy Baseline" --> K["Expand Traffic Route to 50%"]
        K --> L["Monitor State Reconciliation & PnL Invariants for 60 Minutes"]
        L --> M{"State Divergence Detected?"}
        M -- "Divergence Detected" --> J
    end

    subgraph Wave_3 ["Wave 3: Full Production Promotion 100%"]
        M -- "Zero Invariant Violations" --> N["Promote Release to 100% Production Traffic"]
        N --> O["Drain & Terminate Previous Generation Containers"]
        O --> P["Emit Cryptographic Release Attestation & Update AI-SBOM"]
    end

    style Wave_0 fill:#f8f9fa,stroke:#343a40,stroke-width:2px;
    style Wave_1 fill:#e8f4f8,stroke:#17a2b8,stroke-width:2px;
    style Wave_2 fill:#fef9e7,stroke:#ffc107,stroke-width:2px;
    style Wave_3 fill:#eafaf1,stroke:#28a745,stroke-width:2px;
    style F fill:#ffcdd2,stroke:#c62828,stroke-width:2px;
    style J fill:#ffcdd2,stroke:#c62828,stroke-width:2px;
```

---

## 📜 Reusable GitHub Composite Actions Pattern

Instead of embedding raw shell commands into top-level deployment workflows, encapsulate deployment primitives inside dedicated **Composite Actions** located in `.github/actions/`:

### Example: `.github/actions/verify-ast-drift/action.yml` (< 80 LOC)

```yaml
name: "Verify AST Registry Zero-Drift"
description: "Executes AST generators and asserts byte parity across context registries"

runs:
  using: "composite"
  steps:
    - name: Run AST Registry Synchronizers
      shell: bash
      run: |
        python3 scripts/update_state_registry.py
        python3 scripts/update_math_registry.py
        python3 scripts/generate_living_context.py

    - name: Assert Zero Git Diff
      shell: bash
      run: |
        if ! git diff --exit-code; then
          echo "❌ ERROR: Uncommitted changes detected in context registries!"
          exit 1
        fi
        echo "✅ AST Registries are in 100% byte parity with source code."
```

---

## 🌐 Dual-Use Regulated Comparison: Progressive Deployment Across Sectors

| Progressive Rollout Phase | Healthcare / Medical Device Cloud Platform | Core Banking Wire Settlement Gateway |
| :--- | :--- | :--- |
| **Canary Traffic Routing** | Routes 5% of non-critical telemetry streams to the canary cluster; patient telemetry processing remains on the certified baseline. | Routes 5% of low-value consumer transfers to the new settlement container; high-value wholesale transactions remain on the legacy engine. |
| **Automated Rollback Metric** | An algorithmic divergence exceeding 2.0% in calculated vital scores triggers an immediate, zero-downtime rollback. | Any ledger balance mismatch exceeding \$0.01 between parallel engines trips an immediate execution halt and traffic rollback. |
| **Regulatory Validation** | Generates an automated Design Verification audit record showing 0 regression errors across 10,000 de-identified historical clinical test traces. | Generates a Federal Reserve SR 11-7 model outcome analysis record demonstrating mathematical equivalence to historical ledger entries. |

---

## 🛠️ Hands-On Pipeline Decomposition Exercise

**Scenario**: You inherit a legacy 900-line `.github/workflows/main_ci_cd.yml` workflow that handles linting, testing, Docker building, Helm charting, and database migrations.

**Your Refactoring Plan**:
1. Decompose the monolithic file into four discrete workflows, each under 300 LOC:
   - `.github/workflows/01_verify_quality.yml`: AST zero-drift, linting, and hermetic socket testing.
   - `.github/workflows/02_build_artifacts.yml`: Container compilation, Trivy scanning, and AI-SBOM signing.
   - `.github/workflows/03_migrate_database.yml`: Idempotent schema migration and immutable quarantine verification.
   - `.github/workflows/04_canary_deploy.yml`: Progressive traffic shifting (10% $\to$ 50% $\to$ 100%) with automated rollback triggers.
2. Author the workflow dependency chaining using GitHub Actions `workflow_run` or `needs` triggers.

---

[**Next: Module 4 — Infrastructure Context Engineering & The Resource Map →**](./04_context_engineering.md) | [**Return to Deployment Lead Hub →**](./README.md)
