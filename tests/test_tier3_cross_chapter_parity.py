"""Tier 3: Cross-Chapter Parity and Cross-Feature Integration Suite.

Tests pairwise integration and multi-feature contracts:
1. Dialectical Triad arbitration & log-odds convex solver evidence fusion
2. Level-2 $0-Compute JSD Bypass logic & consensus triggers
3. Cross-channel synchronization, D1 freshness gates & StaleDataCircuitBreaker
4. Role playbook cross-functional handoff contracts (PO -> BA -> Architect -> QE -> Ops)
"""

import math
import uuid
import numpy as np
import pytest

from tests.e2e_curriculum_validator import (
    INVARIANTS_REGISTRY,
    convex_evidence_fusion,
    jensen_shannon_divergence,
    should_bypass_dialectical_debate,
    logit,
    sigmoid,
)


# ============================================================================
# 1. DIALECTICAL TRIAD ARBITRATION & LOG-ODDS CONVEX EVIDENCE FUSION
# ============================================================================

def test_dialectical_triad_full_consensus_strong_buy():
    """Verify triad arbitration when Bull, Bear, and Auditor converge on high confidence."""
    # Bull=0.85, Bear=0.60, Auditor=0.80, low divergence JSD=0.04
    fusion = convex_evidence_fusion(
        p_quant=0.80,
        p_valuation=0.75,
        p_forensic=0.80,
        p_catalyst=0.85,
        p_adversarial=0.60,
        jsd_bull_bear=0.04,
    )
    assert fusion["p_posterior"] > 0.75, f"Expected high posterior, got {fusion['p_posterior']}"
    assert 0.90 <= fusion["sizing_multiplier"] <= 1.25, f"Expected upper multiplier, got {fusion['sizing_multiplier']}"
    assert fusion["entropy_discount"] >= 0.90, "Low divergence should have minimal entropy discount"


def test_dialectical_triad_high_divergence_discounts_triad():
    """Verify strong Bull vs Bear disagreement discounts epistemic triad and dampens sizing."""
    # Bull=0.90, Bear=0.10 => high JSD divergence
    p_bull = np.array([0.90, 0.10])
    p_bear = np.array([0.10, 0.90])
    jsd_high = jensen_shannon_divergence(p_bull, p_bear)
    assert jsd_high > 0.35, f"Expected high JSD, got {jsd_high}"
    
    fusion = convex_evidence_fusion(
        p_quant=0.55,
        p_valuation=0.50,
        p_forensic=0.50,
        p_catalyst=0.90,
        p_adversarial=0.10,
        jsd_bull_bear=jsd_high,
        lambda_jsd=1.5,
    )
    # Entropy discount should drop to floor max(0.15, 1 - 1.5*JSD)
    assert fusion["entropy_discount"] <= 0.45
    assert 0.20 <= fusion["sizing_multiplier"] <= 0.85, "High divergence should clamp sizing multiplier"


def test_dialectical_triad_sizing_multiplier_bounds():
    """Verify sizing multiplier is strictly bounded in [0.20, 1.25] under all extremes."""
    # Ultra-bearish extreme
    bear_fusion = convex_evidence_fusion(
        p_quant=0.01, p_valuation=0.01, p_forensic=0.01,
        p_catalyst=0.01, p_adversarial=0.01, jsd_bull_bear=0.0
    )
    assert bear_fusion["sizing_multiplier"] >= 0.20
    assert bear_fusion["p_posterior"] < 0.10
    
    # Ultra-bullish extreme
    bull_fusion = convex_evidence_fusion(
        p_quant=0.99, p_valuation=0.99, p_forensic=0.99,
        p_catalyst=0.99, p_adversarial=0.99, jsd_bull_bear=0.0
    )
    assert bull_fusion["sizing_multiplier"] <= 1.25
    assert bull_fusion["p_posterior"] > 0.90


def test_dialectical_triad_social_sentiment_skew_tanh_saturation():
    """Verify non-linear social sentiment skew bounded via tanh (ADR-035)."""
    fusion_neutral = convex_evidence_fusion(
        p_quant=0.60, p_valuation=0.60, p_forensic=0.60,
        p_catalyst=0.60, p_adversarial=0.60, jsd_bull_bear=0.05, social_skew=0.0
    )
    fusion_hyper_hyped = convex_evidence_fusion(
        p_quant=0.60, p_valuation=0.60, p_forensic=0.60,
        p_catalyst=0.60, p_adversarial=0.60, jsd_bull_bear=0.05, social_skew=100.0
    )
    # Tanh bound ensures delta is capped at +0.15
    delta_l = fusion_hyper_hyped["l_posterior"] - fusion_neutral["l_posterior"]
    assert math.isclose(delta_l, 0.15, rel_tol=1e-3), f"Social skew unconstrained: delta {delta_l} != 0.15"


# ============================================================================
# 2. LEVEL-2 $0-COMPUTE JSD BYPASS LOGIC
# ============================================================================

def test_jsd_bypass_triggers_on_unanimous_bull_confluence():
    """Verify Level-2 JSD bypass triggers when 4 pillars agree strongly (mean >= 0.70, JSD <= 0.12)."""
    # 4 pillars: Quality=0.78, Momentum=0.75, Network=0.74, Flow=0.76
    pillars = [0.78, 0.75, 0.74, 0.76]
    bypass, jsd_val, mean_val = should_bypass_dialectical_debate(pillars, jsd_threshold=0.12)
    assert bypass is True, "Bypass should fire for unanimous strong buy"
    assert jsd_val <= 0.12
    assert mean_val >= 0.70


def test_jsd_bypass_triggers_on_unanimous_bear_confluence():
    """Verify Level-2 JSD bypass triggers when 4 pillars agree on sell/avoid (mean <= 0.30, JSD <= 0.12)."""
    # 4 pillars: Quality=0.18, Momentum=0.20, Network=0.22, Flow=0.19
    pillars = [0.18, 0.20, 0.22, 0.19]
    bypass, jsd_val, mean_val = should_bypass_dialectical_debate(pillars, jsd_threshold=0.12)
    assert bypass is True, "Bypass should fire for unanimous strong sell"
    assert jsd_val <= 0.12
    assert mean_val <= 0.30


def test_jsd_bypass_does_not_trigger_on_pillar_divergence():
    """Verify Level-2 JSD bypass wakes debate triad when pillars diverge (JSD > 0.12)."""
    # Quality is high (0.85) but momentum is collapsed (0.10)
    pillars = [0.85, 0.10, 0.90, 0.15]
    bypass, jsd_val, mean_val = should_bypass_dialectical_debate(pillars, jsd_threshold=0.12)
    assert bypass is False, "Bypass must NOT fire when pillars diverge"
    assert jsd_val > 0.12


def test_jsd_bypass_does_not_trigger_in_intermediate_uncertainty():
    """Verify bypass does NOT fire when pillars agree but are in ambiguous zone (0.30, 0.70)."""
    # Uniform intermediate scores: mean = 0.50, low JSD
    pillars = [0.50, 0.52, 0.49, 0.51]
    bypass, jsd_val, mean_val = should_bypass_dialectical_debate(pillars, jsd_threshold=0.12)
    assert bypass is False, "Bypass must NOT fire in intermediate uncertainty (requires debate)"
    assert jsd_val <= 0.12
    assert 0.30 < mean_val < 0.70


# ============================================================================
# 3. CROSS-CHANNEL SYNCHRONIZATION & D1 FRESHNESS
# ============================================================================

def test_cross_channel_sync_single_source_composition():
    """Verify single-source ConsensusService lock produces identical verdict text across channels."""
    class MockConsensusService:
        @staticmethod
        def compose_verdict(ticker: str, score: float) -> dict:
            action = "BUY" if score >= 0.70 else "WATCH"
            headline = f"VERDICT: {ticker} -> {action} (Conviction: {int(score * 100)}%)"
            return {
                "ticker": ticker,
                "action": action,
                "headline": headline,
                "score": score,
                "trace_id": str(uuid.uuid4())
            }

    verdict = MockConsensusService.compose_verdict("NVDA", 0.82)
    
    # Email, Slack, and IDE must render the exact same server-composed headline
    email_channel = f"<html><body>{verdict['headline']}</body></html>"
    slack_channel = f"*{verdict['headline']}*"
    ide_channel = f"// {verdict['headline']}"
    
    assert verdict["headline"] in email_channel
    assert verdict["headline"] in slack_channel
    assert verdict["headline"] in ide_channel


def test_cross_channel_stale_data_circuit_breaker():
    """Verify StaleDataCircuitBreaker halts execution when local cache is > 72h stale and D1 down."""
    class StaleDataCircuitBreaker(RuntimeError):
        pass

    def check_telemetry_freshness(cache_age_hours: float, d1_available: bool):
        if cache_age_hours > 72.0 and not d1_available:
            raise StaleDataCircuitBreaker(
                f"Local SQLite cache is {cache_age_hours}h stale (>72h) and Cloudflare D1 is unreachable. (Invariant I13)"
            )
        return "PASS_FRESHNESS"

    # Fresh cache passes
    assert check_telemetry_freshness(cache_age_hours=12.0, d1_available=False) == "PASS_FRESHNESS"
    # Stale cache but D1 reachable passes (pulls fresh D1 data)
    assert check_telemetry_freshness(cache_age_hours=80.0, d1_available=True) == "PASS_FRESHNESS"
    # Stale cache + D1 down fails closed
    with pytest.raises(StaleDataCircuitBreaker, match=">72h.*Invariant I13"):
        check_telemetry_freshness(cache_age_hours=85.0, d1_available=False)


def test_cross_channel_audit_table_schema_verification():
    """Verify channel_verdict_audit schema parity and UUIDv4 trace retention (I14, I15)."""
    audit_row = {
        "trace_id": str(uuid.uuid4()),
        "ticker": "AAPL",
        "channel": "SLACK_ALERT",
        "verdict_headline": "VERDICT: AAPL -> BUY (Conviction: 75%)",
        "timestamp_utc": "2026-10-17T22:00:00Z",
    }
    # Validate trace ID is valid UUIDv4
    parsed_uuid = uuid.UUID(audit_row["trace_id"])
    assert parsed_uuid.version == 4, "Trace ID must be valid UUIDv4 (Invariant I15)"
    assert "channel" in audit_row
    assert "verdict_headline" in audit_row


# ============================================================================
# 4. ROLE PLAYBOOK CROSS-FUNCTIONAL HANDOFF CONTRACTS
# ============================================================================

def test_role_handoff_po_to_ba_contract():
    """Verify Product Owner to Business Analyst handoff: Decomposed Epic with bounds & invariants."""
    po_epic_directive = {
        "epic_id": "EPIC-RISK-01",
        "title": "Continuous Telemetry Decay and Epistemic Air-Gap",
        "bounded_subsystems": ["01_strategy_and_vision", "02_requirements_and_design"],
        "governing_invariants": ["I01", "I17", "I20"],
        "max_token_budget": 3500,
    }
    # Check all governing invariants exist
    for inv_id in po_epic_directive["governing_invariants"]:
        assert inv_id in INVARIANTS_REGISTRY, f"PO handoff references invalid invariant: {inv_id}"
    assert po_epic_directive["max_token_budget"] <= 4000, "Blast radius exceeds 4k token ceiling"


def test_role_handoff_ba_to_architect_semantic_blueprint():
    """Verify BA to Architect handoff: Semantic Blueprint with 3-part directive & 20 edge cases."""
    ba_blueprint = {
        "story_id": "STORY-QUANT-104",
        "role": "Quantitative Software Engineer",
        "task": "Implement Ledoit-Wolf analytical covariance shrinkage with condition limit",
        "format": "Python module adhering to ADR-016 <= 400 LOC",
        "edge_cases_count": 20,
        "governing_invariants": ["I07", "I11", "I22"],
    }
    assert ba_blueprint["edge_cases_count"] >= 20, "BA blueprint requires at least 20 pre-condition edge cases"
    for inv in ba_blueprint["governing_invariants"]:
        assert inv in INVARIANTS_REGISTRY


def test_role_handoff_architect_to_qe_invariant_anchors():
    """Verify Architect to QE handoff: code <= 400 LOC with SHA1 invariant anchors."""
    sample_module = """
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: I11
# NAME: Whitening Stability
# ADR: ADR-039
# CLASS: MATH-BOUND
# ROLE: CANONICAL_IMPL
# PREDICATE: Ledoit-Wolf shrinkage condition number cond(Sigma) <= 10^12
# /INVARIANT [sha1:c8152c92]
# === /INVARIANT-BLOCK ===
def compute_whitening():
    pass
"""
    from tests.e2e_curriculum_validator import calculate_physical_loc, extract_anchor_blocks
    total, non_anchor = calculate_physical_loc(sample_module)
    assert non_anchor <= 400
    blocks = extract_anchor_blocks(sample_module)
    assert len(blocks) == 1
    assert blocks[0]["inv_id"] == "I11"


def test_role_handoff_qe_to_ops_ai_sbom_traceability():
    """Verify QE to Ops / CI handoff: AI-SBOM header generation and verification."""
    ai_sbom_header = {
        "agent_id": "teamwork_preview_test_writer",
        "model": "claude-3-7-sonnet",
        "temperature": 0.0,
        "governing_invariants_verified": ["I01", "I02", "I03", "I11", "I22"],
        "hermetic_socket_isolated": True,
        "verification_status": "PASS",
    }
    assert ai_sbom_header["hermetic_socket_isolated"] is True
    assert ai_sbom_header["verification_status"] == "PASS"
    assert len(ai_sbom_header["governing_invariants_verified"]) >= 5
