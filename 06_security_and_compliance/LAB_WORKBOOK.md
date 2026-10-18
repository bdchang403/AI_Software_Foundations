# Security & Compliance Lab Workbook: Auditing Lineage, Plausibility Envelopes & Immutable Quarantine

## 🎯 Welcome to the Compliance & Model Risk Laboratory

In this laboratory workbook, you will perform hands-on audits and implement engineering verification controls that provide the objective evidence required under regulatory compliance frameworks (such as Federal Reserve SR 11-7, FDA 21 CFR Part 820/11) and the Enterprise AI Constitution.

---

## 🧪 Lab 1: Auditing Requirements for Demographic Proxy Variables

### Objective
Audit an incoming Requirements Lead directive to identify implicit demographic proxies, unconstrained optimization risks, and constitutional violations under Article VI.

### Step 1: The Submitted Directive
```markdown
### TASK: Create a high-yield retail consumer loan underwriting algorithm.
### CONSTRAINTS:
1. Maximize annual percentage rate (APR) revenue while keeping default rates below 4.0%.
2. Incorporate the applicant's residential postal zip code to evaluate neighborhood economic health.
3. Factor in the applicant's primary language setting on their mobile operating system.
```

### Step 2: Your Audit Task
Review the directive against the **Enterprise AI Constitution (Article VI: Fairness)** and federal lending regulations (Equal Credit Opportunity Act / Regulation B):
1. Identify the proxy variables and explain why they constitute regulatory violations.
2. Draft the formal **Auditor's Rejection Memo**.
3. Rewrite the directive into a constitutionally compliant version.

### Step 3: Verified Answer Key
```markdown
### AUDITOR'S REJECTION MEMO
STATUS: REJECTED - REGULATORY & CONSTITUTIONAL VIOLATION (ARTICLE VI)
VIOLATIONS DETECTED:
1. "Residential postal zip code": Acts as a well-documented statistical proxy for race and ethnic origin. Using geographic proxies in credit underwriting violates Regulation B (12 CFR § 1002) and creates severe disparate impact liabilities.
2. "Primary language setting": Acts as a direct proxy for national origin and immigrant status, violating federal anti-discrimination statutes.
3. "Maximize APR revenue without constraints": Encourages predatory pricing structures targeted at vulnerable demographics.

REMEDIATED COMPLIANT DIRECTIVE:
### 1. CONTEXT BOUNDARY: Use strictly verified financial capability metrics: debt-to-income (DTI) ratio, verified liquid assets, seasoned credit trade-lines. Strictly exclude zip codes, language settings, and device telemetry.
### 2. TASK INSTRUCTION: Implement an additive credit scorecard with transparent mathematical weights. Generate adverse action reason codes conforming to FCRA § 615(a) for every score reduction.
### 3. FORMAT CONSTRAINTS: Assert zero disparate impact across simulated demographic cohorts; persist audit traces with UUIDv4.
```

---

## 🧪 Lab 2: Implementing & Verifying the Pre-Action Plausibility Band ($I_{02}$)

### Objective
Implement the mathematical execution guardrail function that evaluates proposed orders, dosages, or actions against historical baseline kinematics, halting out-of-band execution.

### Step 1: Your Implementation Task
Write a function `validate_execution_plausibility(proposed_price: float, ema_5: float, atr_14: float) -> bool`:
1. Asserts non-negativity and domain safety: if any input $\le 0$ or non-finite (`NaN`/`Inf`), raise `ValueError`.
2. Evaluates the Invariant $I_{02}$ execution guardrail:
   $$|P_{\text{exec}} - \text{EMA}_5| \le \max(3.0 \cdot \text{ATR}_{14}, \; 0.08 \cdot \text{EMA}_5)$$
3. If deviation is within band, return `True`. If outside band, raise `RuntimeError("REJECTED_EXECUTION_GUARDRAIL")`.

### Step 2: Verified Answer Key
```python
import math

def validate_execution_plausibility(proposed_price: float, ema_5: float, atr_14: float) -> bool:
    # 1. Domain Safety & Non-negativity check
    for name, val in [("proposed_price", proposed_price), ("ema_5", ema_5), ("atr_14", atr_14)]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise ValueError(f"Invalid telemetry type for {name}: {type(val)}")
        if not math.isfinite(val) or val <= 0:
            raise ValueError(f"Domain safety violation: {name} must be finite positive number, got {val}")

    # 2. Invariant I02 Mathematical Envelope
    band = max(3.0 * atr_14, 0.08 * ema_5)
    deviation = abs(proposed_price - ema_5)

    if deviation > band:
        raise RuntimeError(
            f"REJECTED_EXECUTION_GUARDRAIL: Price deviation {deviation:.2f} exceeds dynamic band {band:.2f}"
        )
    return True
```

---

## 🧪 Lab 3: Immutable Quarantine Ledger Migration (Invariant $I_{04}$)

### Objective
Implement an atomic migration script that archives corrupted or tainted data records into the immutable `consensus_quarantine` ledger without executing raw database deletes.

### Step 1: Your Implementation Task
In SQLite / SQL, author a transaction that:
1. Inserts the corrupted record into `consensus_quarantine` along with `quarantine_reason`, `bug_reference`, and `invalidated_by`.
2. Updates the active record in `consensus_verdicts` to `status = 'QUARANTINED'` and `active = 0`.
3. Asserts that zero rows are deleted from the database.

### Step 2: Verified Answer Key
```python
import sqlite3

def quarantine_tainted_record(db_conn: sqlite3.Connection, record_id: int, reason: str, bug_ref: str, auditor_id: str):
    cursor = db_conn.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    try:
        # 1. Archive to immutable quarantine table
        cursor.execute("""
            INSERT INTO consensus_quarantine (
                record_id, source_table, ticker, verdict, conviction, 
                quarantine_reason, bug_reference, invalidated_by, timestamp_utc
            )
            SELECT 
                id, 'consensus_verdicts', ticker, verdict, conviction,
                ?, ?, ?, CURRENT_TIMESTAMP
            FROM consensus_verdicts
            WHERE id = ?;
        """, (reason, bug_ref, auditor_id, record_id))

        # 2. Deactivate record in production table (NO DELETE!)
        cursor.execute("""
            UPDATE consensus_verdicts
            SET status = 'QUARANTINED', active = 0
            WHERE id = ?;
        """, (record_id,))

        db_conn.commit()
    except Exception as e:
        db_conn.rollback()
        raise RuntimeError(f"Quarantine migration failed: {e}")
```

---

## 🧪 Lab 4: Nightly Mark-to-Market State Reconciliation

### Objective
Implement the automated nightly reconciliation loop that independently computes portfolio PnL and NAV from raw immutable trades and asserts tolerance $\le \text{USD } 250.00$.

### Step 1: Verified Answer Key
```python
def reconcile_portfolio_nav(cash_balance: float, open_positions: list, cached_nav: float) -> dict:
    """
    Recomputes total NAV from raw position holdings and compares against cached balance.
    open_positions: list of dicts with keys {"ticker", "shares", "entry_price", "close_price"}
    """
    recomputed_holdings_value = 0.0
    for pos in open_positions:
        shares = pos["shares"]
        close_price = pos["close_price"]
        recomputed_holdings_value += shares * close_price

    recomputed_nav = cash_balance + recomputed_holdings_value
    delta = abs(recomputed_nav - cached_nav)
    
    # Invariant tolerance: $250.00 fixed floor
    tolerance = 250.00
    is_reconciled = delta <= tolerance

    if not is_reconciled:
        raise RuntimeError(
            f"RECONCILIATION DRIFT DETECTED: Discrepancy ${delta:.2f} exceeds tolerance ${tolerance:.2f}. "
            "Halting operations and notifying compliance officer."
        )

    return {
        "status": "RECONCILED",
        "recomputed_nav": round(recomputed_nav, 2),
        "cached_nav": round(cached_nav, 2),
        "delta": round(delta, 2),
        "tolerance": tolerance
    }
```

---

## Production Reality & Operational Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)
In the median mid-2026 team, security and compliance workbook exercises are often viewed as academic busywork. Developers skim code snippets, assume external security operations handle runtime circuit breakers, and continue writing production code where `.get()` defaults and empty `except: pass` handlers mask data corruption. When external APIs fail or return partial payloads, model-generated code falls back to synthetic dummy data (`mock_price = 100.0` or `patient_heart_rate = 72`) to keep pipelines from crashing. Over 80% of teams maintain zero automated nightly reconciliation scripts, zero append-only quarantine ledgers, and zero automated checks for boolean or float smuggling in production.

### Ungoverned Production Failure Modes
Treating runtime circuit breakers and state reconciliation as optional features produces severe production vulnerabilities:
- **Silent Accounting Inversion**: State drift between cached portfolio values and ledger databases compounds over weekends. Without automated reconciliation loops, uncontained discrepancies trigger erroneous margin liquidations or massive financial misstatements.
- **Poisoned Clinical Decision Pipeline**: A broken biosensor feed returns null. Permissive default fallbacks instead of an active `ZeroMockRuntimeBreaker` cause the system to infer normal vitals, failing to trigger emergency clinical intervention.
- **Evidence Deletion and Spoliation Penalties**: Following a system failure, automated database cleanup scripts delete corrupted event rows. Without immutable quarantine ledgers (banning hard deletes), regulators treat missing records as spoliation of evidence under Sarbanes-Oxley or FDA 21 CFR Part 11.

### Deterministic Engineering Defenses & Operational Takeaways
To operationalize these workbook safeguards in production repositories, engineering teams must mandate four concrete practices:
1. **Drop `ZeroMockRuntimeBreaker` into Middleware**: Install the lab's runtime breaker into every data ingestion pipeline to enforce explicit fail-closed exceptions on unverified sources or non-finite values (`NaN`/`Inf`).
2. **Institute the Constitutional Ban on Hard Deletes**: Refactor database models so that invalid or quarantined records are moved to an append-only quarantine table with an immutable error code and timestamp; permanently revoke `DELETE` grants from application database roles.
3. **Run Nightly Automated Reconciliation Sentinels**: Schedule an automated batch job that recalculates ledger state from raw immutable events and halts deployments if state drift exceeds a strict tolerance (e.g., \$250.00 or 0.01%).
4. **Require Passing the Lab Circuit Breaker Tests for CI Clearance**: Mandate that all PRs touching stateful transactions or safety-critical logic include unit tests demonstrating that the circuit breaker trips and halts on malformed payloads.

