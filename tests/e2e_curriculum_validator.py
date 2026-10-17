"""Enterprise E2E Curriculum Validator & Algorithmic Engine.

Provides authoritative implementations for:
- 22 Canonical Invariants ($I_{01}-I_{22}$) Registry & Checksum Verification
- The 10 Inviolable Commandments
- The 6 Forensic Failure-Mode Crises
- Dual-Use Regulated Domain Mappings (FDA Class III vs Quantitative Trading)
- Static AST Zero-Mock Visitor Scanner (ZM001–ZM007)
- Runtime Zero-Mock Circuit Breaker with 15 verified provenances
- Complete Mathematical Formulation Suite (Entropy, U-Curve, Half-Life Decay,
  Confluence, Convex Fusion, JSD Bypass, DSR, Ledoit-Wolf & ZCA Whitening,
  Pre-Action Plausibility Bands)
- Markdown Syntax & LaTeX Bracket Balancing Parsers
"""

import ast
import hashlib
import math
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from scipy import stats


# ============================================================================
# 1. HERMETIC SOCKET ERROR
# ============================================================================

class SocketBlockedError(RuntimeError):
    """Raised when an outbound network call is attempted under hermetic isolation."""
    pass


# ============================================================================
# 2. THE 22 CANONICAL SYSTEM INVARIANTS (I01 - I22)
# ============================================================================

@dataclass(frozen=True)
class InvariantSpec:
    id: str
    name: str
    adrs: Tuple[str, ...]
    invariant_class: str
    predicate: str
    target_modules: Tuple[str, ...]
    enforcement_tests: Tuple[str, ...]


INVARIANTS_REGISTRY: Dict[str, InvariantSpec] = {
    "I01": InvariantSpec(
        id="I01",
        name="Zero-Simulated-Data",
        adrs=("ADR-029", "ADR-045"),
        invariant_class="HARD-SAFETY",
        predicate="forall p in Pipeline: p.src in ALLOWLIST and not p.synthetic. ATR requires >= 15 live bars; else fail-closed.",
        target_modules=("api_client.py", "quant_engine.py", "data_ingest.py"),
        enforcement_tests=("test_zero_taint_fail_closed.py", "test_spot_price_enforcement.py"),
    ),
    "I02": InvariantSpec(
        id="I02",
        name="Execution-Price Guardrail",
        adrs=("ADR-029",),
        invariant_class="HARD-SAFETY",
        predicate="|P_exec - EMA_5| <= max(3*ATR_14, 0.08*EMA_5). Weekend marks reject unless matching Friday close <= 1.0%.",
        target_modules=("execution_guardrails.py", "paper_portfolio_tracker.py"),
        enforcement_tests=("test_execution_guardrails.py", "test_math_stress_invariants.py"),
    ),
    "I03": InvariantSpec(
        id="I03",
        name="Fatal-Contagion Veto",
        adrs=("ADR-024", "ADR-026"),
        invariant_class="HARD-SAFETY",
        predicate="SCSI <= -0.35 or D_toxic > 1.50 or Altman_Z < 1.1 => verdict != BUY regardless of positive confluence.",
        target_modules=("consensus_service.py", "debate/matrix.py"),
        enforcement_tests=("test_compensatory_confluence.py", "test_hype_divergence_veto.py"),
    ),
    "I04": InvariantSpec(
        id="I04",
        name="Immutable-Ledger Quarantine",
        adrs=("ADR-027",),
        invariant_class="HARD-SAFETY",
        predicate="forall r in Ledger: DELETE(r) = emptyset. Invalidated/buggy records archive to consensus_quarantine with non-null reason.",
        target_modules=("consensus_service.py", "api_client.py"),
        enforcement_tests=("test_quarantine_governance.py",),
    ),
    "I05": InvariantSpec(
        id="I05",
        name="Closed-World Fallback",
        adrs=("ADR-029", "ADR-045"),
        invariant_class="HARD-SAFETY",
        predicate="On bundle/D1 failure with verified spot: prompt receives closed-world schema with 4-Pillars UNAVAILABLE, stops UNAVAILABLE, baseline WATCH.",
        target_modules=("query_orchestrator.py", "data_ingest.py"),
        enforcement_tests=("test_cross_channel_conformal_fuzz.py",),
    ),
    "I06": InvariantSpec(
        id="I06",
        name="MOS Bounded Multipliers",
        adrs=("ADR-043", "ADR-034"),
        invariant_class="MATH-BOUND",
        predicate="Risk sizing multiplier M in [0.20, 1.25]. Margin of Safety MOS in [-1.0, 1.0]. Values outside are clamped with telemetry event.",
        target_modules=("quant_engine.py", "composite_mos.py"),
        enforcement_tests=("test_math_stress_invariants.py",),
    ),
    "I07": InvariantSpec(
        id="I07",
        name="Div-by-Zero Domain Safety",
        adrs=("ADR-043",),
        invariant_class="MATH-BOUND",
        predicate="forall a/b: b = 0 => defined fallback (never NaN/Inf propagation). Log/sqrt inputs must assert domain non-negativity.",
        target_modules=("quant_engine.py", "predictive_breakout_scout.py"),
        enforcement_tests=("test_math_stress_invariants.py",),
    ),
    "I08": InvariantSpec(
        id="I08",
        name="Growth-Adjusted Hurdle",
        adrs=("ADR-031",),
        invariant_class="MATH-BOUND",
        predicate="EGR = FCF_Yield + min(g, 0.25). For compounders (g >= 10%), BUY requires EGR >= r_fed_funds. Growth cap is 0.25.",
        target_modules=("quant_engine.py",),
        enforcement_tests=("test_growth_adjusted_hurdle.py",),
    ),
    "I09": InvariantSpec(
        id="I09",
        name="Compensatory Confluence",
        adrs=("ADR-024",),
        invariant_class="MATH-BOUND",
        predicate="BUY <=> sum(I(P_k >= 0.35)) >= 2 and not FatalContagion. Single metrics cannot act as isolated vetoes.",
        target_modules=("consensus_service.py", "debate/matrix.py"),
        enforcement_tests=("test_compensatory_confluence.py",),
    ),
    "I10": InvariantSpec(
        id="I10",
        name="Bandit Prior Integrity",
        adrs=("ADR-034",),
        invariant_class="MATH-BOUND",
        predicate="Thompson Sampling over exactly 6 discrete action arms. Beta priors alpha, beta >= 0.5. Updates evaluate beta-stripped residual return r_resid.",
        target_modules=("contextual_bandit_rl.py",),
        enforcement_tests=("test_contextual_bandit_rl.py",),
    ),
    "I11": InvariantSpec(
        id="I11",
        name="Whitening Stability",
        adrs=("ADR-039",),
        invariant_class="MATH-BOUND",
        predicate="Ledoit-Wolf shrinkage -> symmetrical ZCA whitening on 4-pillar vector. If condition number cond(Sigma) > 10^12, apply regularized floor.",
        target_modules=("quant_engine.py", "debate/matrix.py"),
        enforcement_tests=("test_zca_whitening.py",),
    ),
    "I12": InvariantSpec(
        id="I12",
        name="Conformal Coverage",
        adrs=("ADR-040",),
        invariant_class="MATH-BOUND",
        predicate="Split conformal prediction coverage sets calibrated on rolling 120-day window. Band width monotonically non-decreasing in VIX bucket.",
        target_modules=("quant_engine.py",),
        enforcement_tests=("test_conformal_calibration.py",),
    ),
    "I13": InvariantSpec(
        id="I13",
        name="Remote-First D1 Freshness",
        adrs=("ADR-000", "ADR-038"),
        invariant_class="SCHEMA-PARITY",
        predicate="Canonical truth lives in Cloudflare D1. Mandatory pull-before-push (sync_data.py --pull). Local SQLite reads > 3 days stale fail-closed.",
        target_modules=("api_client.py", "live_price_engine.py"),
        enforcement_tests=("test_spot_price_enforcement.py",),
    ),
    "I14": InvariantSpec(
        id="I14",
        name="Cross-Channel Sync",
        adrs=("ADR-038",),
        invariant_class="SCHEMA-PARITY",
        predicate="Immutable server-composed verdict lock in prompts. Table channel_verdict_audit logs all outputs; daily sentinel alerts on divergence.",
        target_modules=("consensus_service.py", "query_orchestrator.py"),
        enforcement_tests=("test_cross_channel_verdict_parity.py",),
    ),
    "I15": InvariantSpec(
        id="I15",
        name="UUID Traceability",
        adrs=("ADR-018",),
        invariant_class="SCHEMA-PARITY",
        predicate="Every LLM call, consensus verdict, and paper trade execution carries a UUIDv4 trace ID persisted into Cloudflare D1 telemetry ledgers.",
        target_modules=("decision_trace.py", "debate/matrix.py"),
        enforcement_tests=("test_traceability.py",),
    ),
    "I16": InvariantSpec(
        id="I16",
        name="Multi-Ticker Isolation",
        adrs=("ADR-045",),
        invariant_class="SCHEMA-PARITY",
        predicate="forall t1 != t2: State(t1) cap State(t2) = emptyset. Loop-carried scalar contamination banned; inject discrete ticker_spots.",
        target_modules=("query_orchestrator.py", "debate/matrix.py"),
        enforcement_tests=("test_cross_channel_conformal_fuzz.py",),
    ),
    "I17": InvariantSpec(
        id="I17",
        name="Horizon-Matched Decay",
        adrs=("ADR-027", "ADR-033"),
        invariant_class="DECAY-TIMING",
        predicate="w(t) = w0 * 2^(-Delta t / t_half(h)) with t_half(h) in [5d, 90d]. Signals > 2 * t_half demote to NEUTRAL (EXPIRED).",
        target_modules=("consensus_service.py", "quant_engine.py"),
        enforcement_tests=("test_consensus_decay.py",),
    ),
    "I18": InvariantSpec(
        id="I18",
        name="Compounder Hold Lock",
        adrs=("ADR-033", "ADR-044"),
        invariant_class="DECAY-TIMING",
        predicate="20-trading-day Time-in-State Compounder Guard: no liquidation while r_stock >= r_SPY absent fatal veto. 14-day post-exit cooldown.",
        target_modules=("paper_portfolio_tracker.py", "consensus_service.py"),
        enforcement_tests=("test_paper_portfolio_tracker.py",),
    ),
    "I19": InvariantSpec(
        id="I19",
        name="Session Momentum Lock",
        adrs=("ADR-031",),
        invariant_class="DECAY-TIMING",
        predicate="Never liquidate or downgrade an equity closing in upper quartile (close - low)/(high - low) >= 0.75 on >= 1.25x volume into cash.",
        target_modules=("execution_guardrails.py", "paper_portfolio_tracker.py"),
        enforcement_tests=("test_momentum_lock.py",),
    ),
    "I20": InvariantSpec(
        id="I20",
        name="Epistemic News Isolation",
        adrs=("ADR-030", "ADR-044"),
        invariant_class="CONTEXT-ISOLATION",
        predicate="Media ingested as objective external crowd sentiment; air-gapped from internal portfolio weights or macro bias. Marketing discounted (W_commercial = 0.20).",
        target_modules=("debate/context_slicer.py", "data_ingest.py"),
        enforcement_tests=("test_epistemic_firewall.py",),
    ),
    "I21": InvariantSpec(
        id="I21",
        name="Macro Transmission Gate",
        adrs=("ADR-044", "ADR-042"),
        invariant_class="CONTEXT-ISOLATION",
        predicate="Fast acute (10d) vs Slow structural (3y) partition. G_trans = 0 => slow structural macro drag decoupled (0.0). Whisper Shield active.",
        target_modules=("macro_regime_aggregator.py", "debate/context_slicer.py"),
        enforcement_tests=("test_macro_transmission_gate.py",),
    ),
    "I22": InvariantSpec(
        id="I22",
        name="400 LOC & Test Hygiene",
        adrs=("ADR-016", "ADR-045"),
        invariant_class="CODE-HYGIENE",
        predicate="File LOC <= 400 across src/, workers/, tests/, config/. Parseable checksummed anchors. Adversarial QA auditor score >= 90%.",
        target_modules=("All Python files",),
        enforcement_tests=("verify_code_invariants.py", "audit_test_quality.py"),
    ),
}


# ============================================================================
# 3. THE 10 INVIOLABLE COMMANDMENTS
# ============================================================================

TEN_COMMANDMENTS: Dict[int, Dict[str, str]] = {
    1: {
        "title": "Never Impose Synthetic Assumptions",
        "commandment": "Thou shalt not invent synthetic constants, default floats, or mock fallbacks in place of live empirical telemetry.",
        "invariant": "I01",
    },
    2: {
        "title": "Guard Every Execution Gate",
        "commandment": "Thou shalt bound runtime execution prices and actions within strict plausibility envelopes; reject anomalous mutations unconditionally.",
        "invariant": "I02",
    },
    3: {
        "title": "Isolate Fatal Contagion",
        "commandment": "Thou shalt never allow multi-pillar confluence to override catastrophic structural breakdown, toxic solvency, or fatal contraindication.",
        "invariant": "I03",
    },
    4: {
        "title": "Preserve Forensic Immutability",
        "commandment": "Thou shalt never execute a hard DELETE on state ledgers; errant data must migrate atomically to an immutable quarantine table with non-null audit reasons.",
        "invariant": "I04",
    },
    5: {
        "title": "Fail Closed into Safe Simplicity",
        "commandment": "When telemetry drops or upstream schemas collapse, thou shalt fail closed to a minimal safe state rather than hallucinate continuity.",
        "invariant": "I05",
    },
    6: {
        "title": "Bound All Risk & Valuation Multipliers",
        "commandment": "Thou shalt clamp all sizing multipliers and margins of safety strictly within mathematically safe envelopes [0.20, 1.25].",
        "invariant": "I06",
    },
    7: {
        "title": "Enforce Mathematical Domain Safety",
        "commandment": "Thou shalt defend every mathematical quotient against zero denominators and clamp every logarithmic or root argument to positive domains.",
        "invariant": "I07",
    },
    8: {
        "title": "Air-Gap Internal State from External Narrative",
        "commandment": "Thou shalt isolate internal portfolio weights and clinical states behind a unidirectional epistemic firewall, discounting external marketing noise by 80%.",
        "invariant": "I20",
    },
    9: {
        "title": "Synchronize All Output Channels",
        "commandment": "Thou shalt route all verdicts through a single authoritative source lock; conflicting presentations across channels shall trip an immediate circuit breaker.",
        "invariant": "I14",
    },
    10: {
        "title": "Respect Cognitive & Code Boundaries",
        "commandment": "Thou shalt bound source modules to 400 lines of code and living context to 1,500 tokens, banishing attention dilution and feature erasure.",
        "invariant": "I22",
    },
}


# ============================================================================
# 4. THE 6 FORENSIC FAILURE-MODE CRISES
# ============================================================================

FORENSIC_CRISES: Dict[str, Dict[str, Any]] = {
    "CRISIS_1": {
        "id": "CRISIS_1",
        "name": "The V1 Monolithic Cron Poller Crisis",
        "date": "May 2026",
        "naive_architecture": "Nightly batch cron job sweeps 35 equities in monolithic 1,200 LOC procedural loops triggering unconstrained 8,000-token LLM debates per ticker.",
        "silent_failure": "Runaway token burn ($750/mo on flat stocks), 16-hour crash reaction latency, upstream API rate-limit bans (HTTP 429), and monolithic code diff corruption.",
        "false_solutions": "Prompt instructions for token restraint; increasing cron to 15m; splitting into 3 unconstrained files without LOC ceilings.",
        "permanent_mechanisms": [
            "Event-Driven Webhook Ingress (ADR-001) at $0 compute baseline",
            "3-Tier Severity Triage Funnel (ADR-002: Breadcrumb, Accumulation, Eruption)",
            "Continuous Polarity Accumulation with Exponential Half-Life Decay (ADR-003)",
            "Rolling 24-Hour Micro-USD Spend Ceiling (ADR-011: $0.40/day)",
            "ADR-016 400-LOC Hard Modular Ceiling (I22)",
        ],
        "governing_invariants": ("I17", "I21", "I22"),
        "dual_use_pair": {
            "fintech": "Event-driven volatility webhooks replacing 8:00 PM cron sweeps",
            "medical_device": "Event-driven edge interrupts for closed-loop insulin infusion replacing 30-min polling",
        },
    },
    "CRISIS_2": {
        "id": "CRISIS_2",
        "name": "The V2 Architectural & Context Drift Crisis",
        "date": "July 2026",
        "naive_architecture": "40+ prose Markdown blueprints guiding multi-agent refactoring across asynchronous edge infrastructure (Cloudflare Workers, D1 SQL).",
        "silent_failure": "Code-documentation divergence within 3 weeks; schema hallucinations querying non-existent columns; sqlite3 busy locks under 50 concurrent webhooks.",
        "false_solutions": "Authoring more Markdown blueprints; prompt directives to 'read docs first'; naive vector RAG over code.",
        "permanent_mechanisms": [
            "Deterministic AST State Registry (STATE_REGISTRY.md < 5,000 tokens)",
            "Canonical Mathematical Registry (MATHEMATICAL_REGISTRY.md cataloging exact line ranges)",
            "Living Context Compiler (data/openrouter_context.json < 1,500 tokens)",
            "In-Memory Zero-Drift CI Quality Gate (git diff --exit-code)",
            "SQLite WAL Mode with 5,000ms Busy Timeout",
        ],
        "governing_invariants": ("I13", "I15", "I22"),
        "dual_use_pair": {
            "fintech": "AST State/Math Registries keeping edge worker schemas in sync with D1",
            "medical_device": "AST-verified hardware register maps and MISRA-C invariant checks in firmware",
        },
    },
    "CRISIS_3": {
        "id": "CRISIS_3",
        "name": "The 900,000-Row Synthetic Poison Catastrophe",
        "date": "August-October 2026",
        "naive_architecture": "Silenced except blocks returning fallback constants (0.50 dark pool ratio, 5.25% interest rate stub) to prevent pipeline crashes.",
        "silent_failure": "900,000 database rows poisoned by synthetic defaults; DCF, Kelly, and Omega models compounded errors silently; liquidated $150k TSLA into SGOV.",
        "false_solutions": "Prompting models to be careful; adding try/except wrappers; heuristic data sanity checks.",
        "permanent_mechanisms": [
            "Absolute Zero-Mock Mandate (I01 / ADR-029)",
            "Programmatic AST Zero-Mock Code Scanner (Rules ZM001–ZM007)",
            "Runtime Zero-Mock Circuit Breaker verifying 15 immutable data provenances",
            "Fail-Closed Telemetry Doctrine (return None, domain exception, or UNAVAILABLE)",
            "4-Tier Live Price Discovery Waterfall with fail-closed sink",
        ],
        "governing_invariants": ("I01", "I02", "I04", "I05"),
        "dual_use_pair": {
            "fintech": "Catch-block fallback returning 0.50 ratio halts trading; fails closed",
            "medical_device": "Pulse oximeter sensor disconnect fails closed to safe basal rate rather than defaulting SpO2 to 98%",
        },
    },
    "CRISIS_4": {
        "id": "CRISIS_4",
        "name": "The 99% Gate Paralysis Crisis",
        "date": "September 2026",
        "naive_architecture": "100 sequential conjunctive boolean AND-gates requiring agreement across quality, momentum, DCF valuation, and macro screens.",
        "silent_failure": "Joint probability collapse (P_joint = prod(p_k) = 0.243%); rejected NVDA, PLTR, CRM, NOW during rallies due to high-reinvestment DCF paradox.",
        "false_solutions": "Lowering all hurdles uniformly (admitted junk stocks); removing valuation gates entirely.",
        "permanent_mechanisms": [
            "Compensatory 4-Pillar Confluence Engine (ADR-024: >= 2 of 4 pillars >= 0.35)",
            "Isolated Fatal Defensive Veto (I03: Altman Z < 1.1, SCSI <= -0.35)",
            "Growth-Adjusted Capitalized ROIC Margin of Safety (GAC-ROIC-MOS, ADR-034)",
            "Ledoit-Wolf Covariance Shrinkage & Anchor-Preserving Symmetrical ZCA Whitening",
            "6-Arm Bayesian Contextual Bandit Thompson Sampling",
        ],
        "governing_invariants": ("I03", "I08", "I09", "I10", "I11"),
        "dual_use_pair": {
            "fintech": "Compensatory 2-of-4 pillars unblocking compounders while vetoing bankruptcy risk",
            "medical_device": "Multi-biomarker diagnostic oncology triage triggering on 2-of-4 positive modalities rather than 10-of-10",
        },
    },
    "CRISIS_5": {
        "id": "CRISIS_5",
        "name": "The Epistemic Priming & Liquidation Incident",
        "date": "October 2026",
        "naive_architecture": "Omniscient context injection passing portfolio loss data and unstructured YouTube/media transcripts into sentiment agents.",
        "silent_failure": "Sentiment scraper primed by portfolio drawdown; interpreted a retail trading course promotional funnel as empirical crash proof; panic liquidated $150k at market bottom.",
        "false_solutions": "Prompting AI to 'be objective'; adding more LLM debate rounds; blacklisting single channels.",
        "permanent_mechanisms": [
            "ADR-030 Unidirectional Epistemic Air-Gap (zero internal portfolio state in ingestion)",
            "80% Commercial Marketing Funnel Discount (W_commercial = 0.20)",
            "ADR-044 Role-Based Epistemic Slicing (FORENSIC, CATALYST, ADVERSARIAL allowlists)",
            "ADR-039 3-Stage Dialectical Adversarial Triad arbitrated by convex solver",
            "Level-2 $0-Compute JSD Consensus Bypass (JSD <= 0.12)",
        ],
        "governing_invariants": ("I09", "I14", "I20"),
        "dual_use_pair": {
            "fintech": "Air-gapping media sentiment from portfolio state; 80% discount on marketing funnels",
            "medical_device": "Air-gapping clinical efficacy literature reviews from hospital budget deficits; 80% discount on vendor brochures",
        },
    },
    "CRISIS_6": {
        "id": "CRISIS_6",
        "name": "Cross-Channel Verdict Desynchronization",
        "date": "October 2026",
        "naive_architecture": "Separate presentation agents for Email, Slack, and IDE generating qualitative summaries directly from decentralized local SQLite replicas.",
        "silent_failure": "Same equity emitted contradictory verdicts on the same morning (Email: BUY, Slack: SUPPRESS, IDE: EXPIRED SELL) due to cache staleness and budget caps.",
        "false_solutions": "Instructing LLMs to check prior channel outputs; synchronizing cron schedules; manual verification.",
        "permanent_mechanisms": [
            "Single-Source Routing via ConsensusService (ADR-038)",
            "Remote-First D1 Telemetry Freshness Gate (I13: local SQLite > 3d stale fails closed)",
            "Immutable Server-Composed Verdict Lock in prompts (I14)",
            "Daily Parity Sentinel auditing channel_verdict_audit for discrepancies",
            "StaleDataCircuitBreaker halting execution when canonical D1 is unreachable",
        ],
        "governing_invariants": ("I13", "I14", "I15", "I16"),
        "dual_use_pair": {
            "fintech": "Single-source ConsensusService lock preventing Email vs Slack verdict clash",
            "medical_device": "Single-source broker lock preventing ICU bedside monitor vs central nursing telemetry desync",
        },
    },
}


# ============================================================================
# 5. DUAL-USE DOMAIN MAPPING MATRIX
# ============================================================================

DUAL_USE_MAPPINGS = [
    {
        "subsystem": "Pre-Action Execution Plausibility Band",
        "fintech": "|P_exec - EMA_5| <= max(3*ATR_14, 0.08*EMA_5)",
        "medical_device": "|Rate_exec - Rate_baseline| <= max(3*sigma_pt, 0.10*Rate_baseline)",
        "aerospace": "|Theta_surface - Theta_trim| <= MaxDeflection(Airspeed)",
        "mainframe": "|Amount - Mu_history| <= 3*Sigma_account",
    },
    {
        "subsystem": "Zero-Mock Telemetry Interception (Fail-Closed)",
        "fintech": "Missing quote feed fails closed to spot_price=None, status='UNAVAILABLE'",
        "medical_device": "Probe disconnect fails closed to safe basal titration, triggers audible alarm",
        "aerospace": "Iced pitot tube disengages autopilot, alerts crew with Direct Law dynamics",
        "mainframe": "Ledger timeout declines transaction, logs to immutable quarantine ledger",
    },
    {
        "subsystem": "Compensatory Orthogonal Confluence vs Conjunctive Gates",
        "fintech": ">= 2 of 4 pillars >= 0.35 unblocks high-reinvestment compounders",
        "medical_device": ">= 2 of 4 biomarker modalities trigger oncology biopsy triage",
        "aerospace": "Triple Modular Redundancy (TMR) voting with fault-isolated channel veto",
        "mainframe": "Multi-pillar fraud scoring (geo, velocity, device, biometrics) vs 15 boolean blocks",
    },
    {
        "subsystem": "Ledoit-Wolf Shrinkage & Symmetrical ZCA Whitening",
        "fintech": "Decorrelates collinear momentum/valuation pillars while cond(Sigma) <= 10^12",
        "medical_device": "Stabilizes ill-conditioned collinear vital signs (HR, SpO2, ECG R-peaks)",
        "aerospace": "Decorrelates coupled IMU gyroscope/accelerometer drift during turbulence",
        "mainframe": "Decorrelates multicollinear forensic transaction graph features across shell entities",
    },
]


# ============================================================================
# 6. STATIC AST ZERO-MOCK CODE SCANNER (ZM001 - ZM007)
# ============================================================================

@dataclass
class MockViolation:
    rule_id: str
    file_path: str
    line_number: int
    message: str


class ASTZeroMockScanner(ast.NodeVisitor):
    """Static AST visitor detecting synthetic fallbacks and mock data patterns."""

    BANNED_PREFIXES = ("MOCK_", "SYNTHETIC_", "DUMMY_", "TEST_STUB_")
    FINANCIAL_OR_CLINICAL_FIELDS = {
        "price", "spot_price", "quote", "rate", "fed_funds_rate", "spread",
        "dark_pool_ratio", "infusion_rate", "dosage", "spo2", "heart_rate"
    }

    def __init__(self, file_path: str = "<unknown>"):
        self.file_path = file_path
        self.violations: List[MockViolation] = []

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        """ZM001: numeric return; ZM002: dict return; ZM008: empty pass in except."""
        for stmt in node.body:
            if isinstance(stmt, ast.Return) and stmt.value is not None:
                # ZM001: numeric return in except block
                if isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, (int, float)):
                    if stmt.value.value > 0:
                        self.violations.append(MockViolation(
                            rule_id="ZM001_EXCEPT_NUMERIC_RETURN",
                            file_path=self.file_path,
                            line_number=stmt.lineno,
                            message=f"Banned positive numeric fallback in except handler: return {stmt.value.value}. Must fail closed.",
                        ))
                # ZM002: dict return in except block
                elif isinstance(stmt.value, ast.Dict):
                    self.violations.append(MockViolation(
                        rule_id="ZM002_EXCEPT_DICT_RETURN",
                        file_path=self.file_path,
                        line_number=stmt.lineno,
                        message="Banned synthetic dictionary fallback in except handler. Must fail closed.",
                    ))
            elif isinstance(stmt, ast.Pass):
                # ZM008: empty pass statement in except handler (silent error swallowing)
                self.violations.append(MockViolation(
                    rule_id="ZM008_EMPTY_EXCEPT_PASS",
                    file_path=self.file_path,
                    line_number=stmt.lineno,
                    message="Banned empty pass statement in except handler. Must fail closed (return None or raise).",
                ))
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """ZM003: banned variable prefixes; ZM004: static profile registry."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                for prefix in self.BANNED_PREFIXES:
                    if target.id.startswith(prefix):
                        self.violations.append(MockViolation(
                            rule_id="ZM003_BANNED_VARIABLE_PREFIX",
                            file_path=self.file_path,
                            line_number=node.lineno,
                            message=f"Banned variable prefix '{prefix}' in '{target.id}'. Zero-mock mandate violated.",
                        ))
                if target.id in ("STATIC_PROFILE_REGISTRY", "MOCK_CATALOG"):
                    self.violations.append(MockViolation(
                        rule_id="ZM004_STATIC_PROFILE_REGISTRY",
                        file_path=self.file_path,
                        line_number=node.lineno,
                        message=f"Banned static profile registry '{target.id}'. Must query live provenance.",
                    ))
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """ZM005: numeric argument defaults > 0 in domain functions."""
        for default, arg in zip(reversed(node.args.defaults), reversed(node.args.args)):
            if isinstance(default, ast.Constant) and isinstance(default.value, (int, float)):
                if default.value > 0 and arg.arg.lower() in self.FINANCIAL_OR_CLINICAL_FIELDS:
                    self.violations.append(MockViolation(
                        rule_id="ZM005_NUMERIC_ARG_DEFAULT",
                        file_path=self.file_path,
                        line_number=node.lineno,
                        message=f"Banned positive numeric default {default.value} for domain argument '{arg.arg}'. Must default to None.",
                    ))
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import):
        """ZM009: Banned mock library imports (import unittest.mock, import mock)."""
        for alias in node.names:
            name_lower = alias.name.lower()
            if "mock" in name_lower:
                self.violations.append(MockViolation(
                    rule_id="ZM009_BANNED_MOCK_IMPORT_AND_USAGE",
                    file_path=self.file_path,
                    line_number=node.lineno,
                    message=f"Banned mock import '{alias.name}'. Use hermetic socket isolation instead of synthetic mocks.",
                ))
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """ZM009: Banned mock imports from unittest.mock, mock, or importing Mock/MagicMock."""
        module_lower = (node.module or "").lower()
        if "mock" in module_lower:
            self.violations.append(MockViolation(
                rule_id="ZM009_BANNED_MOCK_IMPORT_AND_USAGE",
                file_path=self.file_path,
                line_number=node.lineno,
                message=f"Banned mock import from '{node.module}'. Use hermetic socket isolation instead of synthetic mocks.",
            ))
        else:
            for alias in node.names:
                if "mock" in alias.name.lower() or alias.name in ("Mock", "MagicMock", "patch", "AsyncMock", "PropertyMock"):
                    self.violations.append(MockViolation(
                        rule_id="ZM009_BANNED_MOCK_IMPORT_AND_USAGE",
                        file_path=self.file_path,
                        line_number=node.lineno,
                        message=f"Banned mock object import '{alias.name}'. Synthetic test stubs violate zero-mock doctrine.",
                    ))
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """ZM006: .get fallback; ZM009: Mock/MagicMock instantiation or call."""
        if isinstance(node.func, ast.Attribute) and node.func.attr == "get":
            if len(node.args) >= 2:
                key_arg = node.args[0]
                fallback_arg = node.args[1]
                if isinstance(fallback_arg, ast.Constant) and isinstance(fallback_arg.value, (int, float)):
                    if fallback_arg.value > 0:
                        key_name = getattr(key_arg, "value", str(key_arg))
                        self.violations.append(MockViolation(
                            rule_id="ZM006_GET_NUMERIC_FALLBACK",
                            file_path=self.file_path,
                            line_number=node.lineno,
                            message=f"Banned positive fallback {fallback_arg.value} in .get('{key_name}'). Must default to None.",
                        ))

        # ZM009: Detect Mock() / MagicMock() / patch() / AsyncMock() instantiation/call
        call_name = ""
        if isinstance(node.func, ast.Name):
            call_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            call_name = node.func.attr
        if call_name in ("Mock", "MagicMock", "patch", "AsyncMock", "PropertyMock"):
            self.violations.append(MockViolation(
                rule_id="ZM009_BANNED_MOCK_IMPORT_AND_USAGE",
                file_path=self.file_path,
                line_number=node.lineno,
                message=f"Banned mock object instantiation/call '{call_name}()'. Mocks masquerading as live feeds violate zero-mock doctrine.",
            ))
        self.generic_visit(node)

    def visit_BinOp(self, node: ast.BinOp):
        """ZM007: boolean or positive numeric fallback (or / |)."""
        self.generic_visit(node)

    def visit_BoolOp(self, node: ast.BoolOp):
        """ZM007: x or <positive_constant>."""
        if isinstance(node.op, ast.Or):
            for val in node.values[1:]:
                if isinstance(val, ast.Constant) and isinstance(val.value, (int, float)):
                    if val.value > 0:
                        self.violations.append(MockViolation(
                            rule_id="ZM007_OR_NUMERIC_FALLBACK",
                            file_path=self.file_path,
                            line_number=node.lineno,
                            message=f"Banned positive numeric fallback in boolean OR: {val.value}. Must fail closed.",
                        ))
        self.generic_visit(node)


def scan_python_code_for_mock_violations(code_str: str, file_path: str = "<memory>") -> List[MockViolation]:
    """Parse python code string and execute ASTZeroMockScanner."""
    try:
        tree = ast.parse(code_str, filename=file_path)
    except SyntaxError as e:
        return [MockViolation(rule_id="SYNTAX_ERROR", file_path=file_path, line_number=e.lineno or 1, message=str(e))]
    scanner = ASTZeroMockScanner(file_path=file_path)
    scanner.visit(tree)
    return scanner.violations


# ============================================================================
# 7. RUNTIME ZERO-MOCK CIRCUIT BREAKER
# ============================================================================

VERIFIED_PROVENANCES = frozenset({
    "FRED_ST_LOUIS_LIVE", "SEC_EDGAR_RAW", "NYSE_DIRECT_FEED", "NASDAQ_ITCH",
    "FDA_MAUDE_DATABASE", "ISO_13485_AUDIT_LOG", "ARINC_424_NAV_DATABASE",
    "DO178C_TELEMETRY", "SWIFT_FIN_GATEWAY", "FEDWIRE_SETTLEMENT",
    "BLOOMBERG_BPIPE", "REFINITIV_ELEKTRON", "FMP_REST_API", "YAHOO_FINANCE_RAPID",
    "FINNHUB_STREAM",
})


class RuntimeZeroMockCircuitBreaker:
    """Deep recursive payload walker intercepting synthetic sentinels, boolean smuggling, unverified data, and missing provenance."""

    def __init__(self, allowed_provenances: Optional[frozenset] = None):
        self.allowed_provenances = allowed_provenances or VERIFIED_PROVENANCES

    def verify_payload(self, payload: Any, current_path: str = "root") -> Dict[str, Any]:
        """Verify telemetry payload; raises ValueError if synthetic contamination or missing provenance detected."""
        if isinstance(payload, dict):
            # Check provenance: fail-closed if missing at root telemetry payload
            src = payload.get("data_source")
            if current_path == "root":
                if not src:
                    raise ValueError(f"Circuit Breaker tripped at {current_path}: Missing or unverified provenance '{src}'.")
                if src != "NONE" and src not in self.allowed_provenances:
                    raise ValueError(f"Circuit Breaker tripped at {current_path}: Unverified provenance '{src}'.")
            elif "data_source" in payload:
                if not src or (src != "NONE" and src not in self.allowed_provenances):
                    raise ValueError(f"Circuit Breaker tripped at {current_path}: Unverified provenance '{src}'.")

            # Check for synthetic sentinels
            for key, val in payload.items():
                field_path = f"{current_path}.{key}"
                # Boolean smuggling check for numeric fields (isinstance(True, int) == True)
                if key in ASTZeroMockScanner.FINANCIAL_OR_CLINICAL_FIELDS:
                    if isinstance(val, bool):
                        raise ValueError(f"Circuit Breaker tripped at {field_path}: Boolean value '{val}' smuggled into numeric field.")
                    if isinstance(val, (int, float)):
                        if not math.isfinite(val):
                            raise ValueError(f"Circuit Breaker tripped at {field_path}: Non-finite float '{val}' detected.")
                # Recurse
                self.verify_payload(val, field_path)

        elif isinstance(payload, list):
            for i, item in enumerate(payload):
                self.verify_payload(item, f"{current_path}[{i}]")

        return {"status": "VERIFIED", "payload": payload}

    def sanitize_or_block_verdict(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Fail-closed demotion method: verifies payload and returns sanitized verdict on violation."""
        try:
            self.verify_payload(payload)
            return payload
        except ValueError as err:
            sanitized = dict(payload) if isinstance(payload, dict) else {"original_payload": payload}
            sanitized["signal"] = "BLOCKED_DATA_INTEGRITY_VIOLATION"
            sanitized["confidence"] = 0
            sanitized["recommendation"] = "HALT_TRADING_DUE_TO_UNVERIFIED_DATA"
            sanitized["action"] = "HALT"
            sanitized["is_data_integrity_blocked"] = True
            sanitized["circuit_breaker_error"] = str(err)
            return sanitized


# ============================================================================
# 8. MATHEMATICAL FORMULATION SUITE
# ============================================================================

def attention_entropy(weights: np.ndarray, eps: float = 1e-12) -> float:
    """Compute information-theoretic attention entropy H(A_i) = -sum(A_ij * ln(A_ij))."""
    weights = np.asarray(weights, dtype=float)
    if weights.size == 0:
        return 0.0
    # Normalize to probability distribution
    total = np.sum(weights)
    if total <= 0:
        return 0.0
    p = weights / total
    # Safely compute p * ln(p) with 0 ln 0 -> 0
    p_safe = np.where(p > eps, p, 1.0)
    log_p = np.where(p > eps, np.log(p_safe), 0.0)
    return float(-np.sum(p * log_p))


def lost_in_the_middle_fidelity(position: float) -> float:
    """U-shaped positional attention curve F(x) with 40-75% loss in [0.15, 0.85]."""
    x = max(0.0, min(1.0, float(position)))
    if x <= 0.15:
        # Primacy bias
        return float(1.0 - (0.50 / 0.15) * x)
    elif x >= 0.85:
        # Recency bias
        return float(0.50 + (0.50 / 0.15) * (x - 0.85))
    else:
        # Degradation valley: 15% to 85%
        # Minimum at midpoint x=0.50 around 0.35
        mid = 0.50
        dist = abs(x - mid) / 0.35
        return float(0.35 + 0.15 * (dist ** 2))


def continuous_half_life_decay(w0: float, delta_t: float, half_life: float) -> float:
    """w(Delta t) = w0 * (1/2)^(Delta t / t_half) with t_half > 0."""
    if half_life <= 0:
        raise ValueError("half_life must be strictly positive.")
    if delta_t < 0:
        return float(w0)
    return float(w0 * (0.5 ** (delta_t / half_life)))


def conjunctive_joint_probability(gate_probabilities: List[float]) -> float:
    """Exponential joint failure probability P_joint = prod(p_k)."""
    if not gate_probabilities:
        return 1.0
    prod = 1.0
    for p in gate_probabilities:
        prod *= max(0.0, min(1.0, float(p)))
    return float(prod)


def compensatory_confluence(
    pillar_scores: List[float],
    threshold: float = 0.35,
    min_pillars: int = 2,
    fatal_contagion: bool = False
) -> Dict[str, Any]:
    """Compensatory M-of-N orthogonal confluence (ADR-024) with isolated fatal contagion veto."""
    if fatal_contagion:
        return {
            "approved": False,
            "verdict": "AVOID_FATAL_CONTAGION",
            "confluent_pillars": 0,
            "fatal_veto": True,
        }
    passed_count = sum(1 for s in pillar_scores if s >= threshold)
    approved = passed_count >= min_pillars
    return {
        "approved": approved,
        "verdict": "BUY_CONFLUENT" if approved else "WATCH_INSUFFICIENT_CONFLUENCE",
        "confluent_pillars": passed_count,
        "fatal_veto": False,
    }


def logit(p: float, eps: float = 1e-7) -> float:
    """Log-odds transformation logit(P) = ln(P / (1 - P)) with epsilon clamping."""
    p_clamped = max(eps, min(1.0 - eps, float(p)))
    return float(math.log(p_clamped / (1.0 - p_clamped)))


def sigmoid(z: float) -> float:
    """Sigmoid activation sigma(z) = 1 / (1 + exp(-z))."""
    z_clamped = max(-50.0, min(50.0, float(z)))
    return float(1.0 / (1.0 + math.exp(-z_clamped)))


def jensen_shannon_divergence(p: np.ndarray, q: np.ndarray, eps: float = 1e-12) -> float:
    """Compute Jensen-Shannon Divergence JSD(P || Q) = 0.5 * KL(P || M) + 0.5 * KL(Q || M)."""
    p = np.asarray(p, dtype=float) + eps
    q = np.asarray(q, dtype=float) + eps
    p = p / np.sum(p)
    q = q / np.sum(q)
    m = 0.5 * (p + q)
    kl_pm = np.sum(p * np.log(p / m))
    kl_qm = np.sum(q * np.log(q / m))
    return float(max(0.0, 0.5 * kl_pm + 0.5 * kl_qm))


def compute_pillar_js_divergence(pillar_scores: List[float], eps: float = 1e-12) -> float:
    """Compute Jensen-Shannon Divergence across multiple Bernoulli pillar distributions.
    
    Each pillar score s_i represents distribution P_i = [s_i, 1 - s_i].
    JSD = (1/K) * sum(KL(P_i || M)) where M = (1/K) * sum(P_i).
    """
    if not pillar_scores:
        return 0.0
    scores = np.clip(np.asarray(pillar_scores, dtype=float), eps, 1.0 - eps)
    k = len(scores)
    # Form K x 2 probability matrix
    P = np.column_stack([scores, 1.0 - scores])
    # Mixture distribution M
    M = np.mean(P, axis=0)
    
    # Average KL divergence
    kl_sum = 0.0
    for i in range(k):
        kl_sum += np.sum(P[i] * np.log(P[i] / M))
    return float(max(0.0, kl_sum / k))


def should_bypass_dialectical_debate(
    pillar_scores: List[float],
    jsd_threshold: float = 0.12,
    extreme_high: float = 0.70,
    extreme_low: float = 0.30
) -> Tuple[bool, float, float]:
    """Level-2 $0-compute JSD bypass evaluator (Master Guide §2.6.1).
    
    Returns (bypass_flag, jsd_value, mean_score).
    Bypass activates if JSD <= 0.12 and (mean >= 0.70 or mean <= 0.30).
    """
    if not pillar_scores:
        return False, 0.50, 0.50
    scores = np.asarray(pillar_scores, dtype=float)
    mean_val = float(np.mean(scores))
    jsd_val = compute_pillar_js_divergence(pillar_scores)
    
    is_consensus = (mean_val >= extreme_high) or (mean_val <= extreme_low)
    bypass = bool((jsd_val <= jsd_threshold) and is_consensus)
    return bypass, jsd_val, mean_val


def convex_evidence_fusion(
    p_quant: float,
    p_valuation: float,
    p_forensic: float,
    p_catalyst: float,
    p_adversarial: float,
    jsd_bull_bear: float,
    lambda_jsd: float = 1.5,
    w_rag: float = 0.0,
    l_rag: float = 0.0,
    social_skew: float = 0.0,
) -> Dict[str, Any]:
    """Closed-form Log-Odds Convex Evidence Fusion with JSD Discounting (ADR-039)."""
    l_quant = 0.55 * logit(p_quant) + 0.45 * logit(p_valuation)
    l_triad = 0.35 * logit(p_forensic) + 0.35 * logit(p_catalyst) + 0.30 * logit(p_adversarial)
    entropy_discount = max(0.15, 1.0 - lambda_jsd * max(0.0, jsd_bull_bear))
    delta_l_social = 0.15 * math.tanh(social_skew / 5.0)
    
    l_posterior = l_quant + (entropy_discount * l_triad) + (w_rag * l_rag) + delta_l_social
    p_posterior = sigmoid(l_posterior)
    
    # Bounded sizing multiplier M in [0.20, 1.25]
    sizing_multiplier = max(0.20, min(1.25, 0.20 + 1.05 * p_posterior))
    
    return {
        "l_quant": l_quant,
        "l_triad": l_triad,
        "entropy_discount": entropy_discount,
        "l_posterior": l_posterior,
        "p_posterior": p_posterior,
        "sizing_multiplier": sizing_multiplier,
    }


def deflated_sharpe_ratio(
    estimated_sr: float,
    trials: int,
    sigma_trials: float,
    skew: float,
    kurtosis: float,
    sample_length: int,
) -> float:
    """Bailey & López de Prado (2014) Deflated Sharpe Ratio (DSR)."""
    if trials <= 1 or sample_length <= 1:
        return 0.0
    gamma_em = 0.57721566490153286  # Euler-Mascheroni
    z1 = float(stats.norm.ppf(1.0 - 1.0 / trials))
    z2 = float(stats.norm.ppf(1.0 - 1.0 / (trials * math.e)))
    expected_max_sr = sigma_trials * ((1.0 - gamma_em) * z1 + gamma_em * z2)
    
    # Higher moment Sharpe variance
    var_sr = (1.0 - skew * estimated_sr + ((kurtosis - 1.0) / 4.0) * (estimated_sr ** 2)) / (sample_length - 1)
    if var_sr <= 0:
        return 0.0
    se_sr = math.sqrt(var_sr)
    t_stat = (estimated_sr - expected_max_sr) / se_sr
    return float(stats.norm.cdf(t_stat))


def ledoit_wolf_covariance_shrinkage(X: np.ndarray) -> Tuple[np.ndarray, float]:
    """Analytical Ledoit-Wolf Covariance Shrinkage toward (Tr(S)/p)*I with condition number check."""
    X = np.asarray(X, dtype=float)
    n, p = X.shape
    if n < 2 or p < 1:
        raise ValueError("Matrix dimensions too small for covariance computation.")
    X_centered = X - np.mean(X, axis=0)
    S = (X_centered.T @ X_centered) / (n - 1)
    mu = np.trace(S) / p
    target = mu * np.eye(p)
    
    # Analytical shrinkage intensity estimation
    d2 = np.linalg.norm(S - target, "fro") ** 2
    if d2 <= 1e-12:
        sigma_lw = S.copy()
    else:
        # Asymptotic variance estimator
        y = X_centered ** 2
        phi_mat = (y.T @ y) / n - 2 * (X_centered.T @ X_centered) * S / n + S ** 2
        phi = np.sum(phi_mat)
        shrinkage = max(0.0, min(1.0, phi / (n * d2)))
        sigma_lw = (1.0 - shrinkage) * S + shrinkage * target
    
    cond_num = float(np.linalg.cond(sigma_lw))
    if cond_num > 1e12 or not np.isfinite(cond_num):
        # Apply regularized floor
        sigma_lw = sigma_lw + 1e-6 * np.eye(p)
        cond_num = float(np.linalg.cond(sigma_lw))
        
    return sigma_lw, cond_num


def anchor_preserving_zca_whitening(X: np.ndarray, anchor_col: int = 0) -> np.ndarray:
    """Alg #89: Anchor-Preserving Symmetrical ZCA Whitening on multi-pillar matrix."""
    X = np.asarray(X, dtype=float).copy()
    n, p = X.shape
    if p < 2:
        return X
    
    # Stage 1: Gram-Schmidt residualization of secondary columns against anchor
    anchor = X[:, anchor_col]
    anchor_norm_sq = np.dot(anchor, anchor)
    if anchor_norm_sq > 1e-12:
        for j in range(p):
            if j != anchor_col:
                proj = np.dot(X[:, j], anchor) / anchor_norm_sq
                X[:, j] = X[:, j] - 0.65 * proj * anchor
                
    # Stage 2: Ledoit-Wolf Covariance Shrinkage
    sigma_lw, _ = ledoit_wolf_covariance_shrinkage(X)
    
    # Stage 3: Eigenvalue-Clamped Symmetrical ZCA Whitening
    eigenvalues, eigenvectors = np.linalg.eigh(sigma_lw)
    mu = np.trace(sigma_lw) / p
    lambda_max = np.max(eigenvalues)
    lambda_floor = max(1e-6 * lambda_max, 1e-8)
    lambda_safe = np.clip(eigenvalues, lambda_floor, max(1.0, mu))
    
    inv_sqrt_lambda = np.diag(1.0 / np.sqrt(lambda_safe))
    w_zca = eigenvectors @ inv_sqrt_lambda @ eigenvectors.T
    
    X_centered = X - np.mean(X, axis=0)
    X_whitened = (X_centered @ w_zca.T) + np.mean(X, axis=0)
    return X_whitened


def pre_action_plausibility_band(
    proposed_value: float,
    baseline_value: float,
    atr: float,
    atr_mult: float = 3.0,
    max_pct: float = 0.08,
) -> bool:
    """Mathematical gate: |V_exec - Baseline| <= max(atr_mult * ATR, max_pct * Baseline)."""
    allowed_band = max(atr_mult * abs(atr), max_pct * abs(baseline_value))
    deviation = abs(proposed_value - baseline_value)
    return bool(deviation <= allowed_band + 1e-9)


# ============================================================================
# 9. MARKDOWN & INVARIANT ANCHOR PARSER
# ============================================================================

def compute_anchor_hash(inv_id: str, adr: str, predicate: str) -> str:
    """SHA1 checksum formula: sha1(inv_id.strip() || adr.strip() || predicate.strip())[:8]."""
    raw_str = f"{inv_id.strip()}|{adr.strip()}|{predicate.strip()}"
    return hashlib.sha1(raw_str.encode("utf-8")).hexdigest()[:8]


def calculate_physical_loc(file_content: str) -> Tuple[int, int]:
    """Calculate (total_lines, non_anchor_lines) respecting ADR-016."""
    lines = file_content.splitlines()
    total = len(lines)
    non_anchor = 0
    in_anchor = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# === INVARIANT-BLOCK"):
            in_anchor = True
            continue
        if stripped.startswith("# === /INVARIANT-BLOCK"):
            in_anchor = False
            continue
        if not in_anchor:
            non_anchor += 1
    return total, non_anchor


def extract_anchor_blocks(file_content: str) -> List[Dict[str, Any]]:
    """Parse # === INVARIANT-BLOCK v1 ... # === /INVARIANT-BLOCK blocks from code comments."""
    pattern = re.compile(
        r"# === INVARIANT-BLOCK v1[^\n]*\n"
        r"(?:#[^\n]*\n)*?"
        r"# INVARIANT:\s*(?P<inv_id>\S+)[^\n]*\n"
        r"(?:#[^\n]*\n)*?"
        r"# ADR:\s*(?P<adr>\S+)[^\n]*\n"
        r"(?:#[^\n]*\n)*?"
        r"# PREDICATE:\s*(?P<predicate>[^\n]+)\n"
        r"(?:#[^\n]*\n)*?"
        r"# /INVARIANT \[sha1:(?P<sha1>[0-9a-fA-F]{8})\]\n"
        r"# === /INVARIANT-BLOCK ===",
        re.MULTILINE
    )
    blocks = []
    for match in pattern.finditer(file_content):
        inv_id = match.group("inv_id")
        adr = match.group("adr")
        predicate = match.group("predicate")
        sha1_claimed = match.group("sha1").lower()
        sha1_expected = compute_anchor_hash(inv_id, adr, predicate).lower()
        blocks.append({
            "inv_id": inv_id,
            "adr": adr,
            "predicate": predicate,
            "sha1_claimed": sha1_claimed,
            "sha1_expected": sha1_expected,
            "valid": (sha1_claimed == sha1_expected),
        })
    return blocks


def validate_markdown_syntax(markdown_text: str) -> List[str]:
    """Validates basic markdown syntax: header hierarchy, code fences, and table column counts."""
    issues = []
    lines = markdown_text.splitlines()
    in_fence = False
    fence_char = ""
    last_header_level = 0
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Code fence tracking
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_char = stripped[:3]
            else:
                in_fence = False
            continue
            
        if in_fence:
            continue
            
        # Header hierarchy tracking
        if stripped.startswith("#"):
            match = re.match(r"^(#+)\s+", stripped)
            if match:
                level = len(match.group(1))
                if last_header_level > 0 and level > last_header_level + 1:
                    issues.append(f"Line {i}: Header level skipped from H{last_header_level} to H{level}.")
                last_header_level = level
                
        # Markdown table column count validation
        if stripped.startswith("|") and stripped.endswith("|") and "---" in stripped:
            # Separator line
            cols = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cols) < 2:
                issues.append(f"Line {i}: Table separator has fewer than 2 columns.")
                
    if in_fence:
        issues.append("Unclosed code fence (```) at end of file.")
        
    return issues


def extract_and_validate_latex(markdown_text: str) -> List[Dict[str, Any]]:
    """Extract all inline and block LaTeX formulas; validates delimiter and brace balance."""
    results = []
    
    # Block math $$...$$
    block_matches = re.finditer(r"\$\$(.*?)\$\$", markdown_text, re.DOTALL)
    for m in block_matches:
        formula = m.group(1).strip()
        open_braces = formula.count("{")
        close_braces = formula.count("}")
        balanced = (open_braces == close_braces)
        results.append({
            "type": "block",
            "formula": formula,
            "balanced": balanced,
            "open_braces": open_braces,
            "close_braces": close_braces,
        })
        
    # Inline math $...$
    inline_matches = re.finditer(r"(?<!\$)\$([^\$\n]+)\$(?!\$)", markdown_text)
    for m in inline_matches:
        formula = m.group(1).strip()
        open_braces = formula.count("{")
        close_braces = formula.count("}")
        balanced = (open_braces == close_braces)
        results.append({
            "type": "inline",
            "formula": formula,
            "balanced": balanced,
            "open_braces": open_braces,
            "close_braces": close_braces,
        })
        
    return results
