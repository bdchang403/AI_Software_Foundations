"""Tier 2: Boundary and Invariant Corner Case Verification Suite.

Tests boundary conditions and extreme corner cases across:
1. Zero-mock exception returns & runtime sentinel interception (>=5 tests)
2. Division-by-zero domain safety & mathematical boundary handling (>=5 tests)
3. Condition number limits cond(Sigma) <= 10^12 & regularized floor (>=5 tests)
4. ADR-016 400 LOC ceiling check, 350 LOC refactor warnings, anchor exclusions (>=5 tests)
5. SHA1 anchor block hash validation & anti-tamper detection (>=5 tests)
"""

import math
import numpy as np
import pytest

from tests.e2e_curriculum_validator import (
    RuntimeZeroMockCircuitBreaker,
    attention_entropy,
    continuous_half_life_decay,
    ledoit_wolf_covariance_shrinkage,
    logit,
    sigmoid,
    calculate_physical_loc,
    compute_anchor_hash,
    extract_anchor_blocks,
    scan_python_code_for_mock_violations,
)


# ============================================================================
# 1. ZERO-MOCK EXCEPTION RETURNS & SENTINEL INTERCEPTION (>=5 TESTS)
# ============================================================================

def test_zero_mock_ast_allows_return_none():
    """Verify AST scanner permits return None in except blocks (fail-closed)."""
    code = """
def fetch_quote(ticker):
    try:
        return api.get_quote(ticker)
    except Exception:
        return None
"""
    violations = scan_python_code_for_mock_violations(code)
    assert len(violations) == 0, f"return None was falsely flagged: {violations}"


def test_zero_mock_ast_allows_raise_in_except():
    """Verify AST scanner permits re-raising custom domain exceptions in except blocks."""
    code = """
def fetch_quote(ticker):
    try:
        return api.get_quote(ticker)
    except TimeoutError as e:
        raise DomainFeedError(f"Feed unavailable: {e}") from e
"""
    violations = scan_python_code_for_mock_violations(code)
    assert len(violations) == 0, f"raise was falsely flagged: {violations}"


def test_zero_mock_runtime_breaker_catches_boolean_smuggling():
    """Verify circuit breaker catches boolean smuggled into numeric fields (True/False)."""
    breaker = RuntimeZeroMockCircuitBreaker()
    bad_payload = {
        "ticker": "NVDA",
        "spot_price": True,  # Smuggled boolean
        "data_source": "NYSE_DIRECT_FEED"
    }
    with pytest.raises(ValueError, match="Boolean value 'True' smuggled into numeric field"):
        breaker.verify_payload(bad_payload)


def test_zero_mock_runtime_breaker_catches_nan_and_inf_smuggling():
    """Verify circuit breaker catches non-finite floats (NaN, Inf) in telemetry payloads."""
    breaker = RuntimeZeroMockCircuitBreaker()
    nan_payload = {
        "ticker": "TSLA",
        "price": float("nan"),
        "data_source": "NASDAQ_ITCH"
    }
    with pytest.raises(ValueError, match="Non-finite float"):
        breaker.verify_payload(nan_payload)
        
    inf_payload = {
        "ticker": "TSLA",
        "price": float("inf"),
        "data_source": "NASDAQ_ITCH"
    }
    with pytest.raises(ValueError, match="Non-finite float"):
        breaker.verify_payload(inf_payload)


def test_zero_mock_runtime_breaker_validates_provenances():
    """Verify circuit breaker accepts verified provenances and blocks unverified sources."""
    breaker = RuntimeZeroMockCircuitBreaker()
    
    # Valid provenance
    valid_payload = {
        "ticker": "SPY",
        "price": 510.50,
        "data_source": "NYSE_DIRECT_FEED"
    }
    result = breaker.verify_payload(valid_payload)
    assert result["status"] == "VERIFIED"
    
    # Unverified provenance
    unverified_payload = {
        "ticker": "SPY",
        "price": 510.50,
        "data_source": "REDDIT_RUMOR_SCRAPER"
    }
    with pytest.raises(ValueError, match="Unverified provenance 'REDDIT_RUMOR_SCRAPER'"):
        breaker.verify_payload(unverified_payload)


def test_zero_mock_runtime_breaker_fails_closed_on_missing_data_source():
    """Verify circuit breaker fails closed when 'data_source' key is omitted from telemetry payload."""
    breaker = RuntimeZeroMockCircuitBreaker()
    payload_missing_source = {
        "ticker": "AAPL",
        "price": 175.50
    }
    with pytest.raises(ValueError, match="Missing or unverified provenance"):
        breaker.verify_payload(payload_missing_source)


def test_zero_mock_runtime_breaker_sanitize_or_block_verdict_demotes_unverified():
    """Verify sanitize_or_block_verdict demotes unverified or missing provenance to safe halt verdict."""
    breaker = RuntimeZeroMockCircuitBreaker()
    
    # Case 1: Missing provenance
    payload_missing = {"ticker": "AAPL", "price": 175.50}
    sanitized_missing = breaker.sanitize_or_block_verdict(payload_missing)
    assert sanitized_missing["signal"] == "BLOCKED_DATA_INTEGRITY_VIOLATION"
    assert sanitized_missing["confidence"] == 0
    assert sanitized_missing["recommendation"] == "HALT_TRADING_DUE_TO_UNVERIFIED_DATA"
    assert sanitized_missing["action"] == "HALT"
    assert sanitized_missing["is_data_integrity_blocked"] is True
    assert "Missing or unverified provenance" in sanitized_missing["circuit_breaker_error"]

    # Case 2: Unverified source
    payload_unverified = {"ticker": "SPY", "price": 510.50, "data_source": "REDDIT_RUMORS"}
    sanitized_unverified = breaker.sanitize_or_block_verdict(payload_unverified)
    assert sanitized_unverified["signal"] == "BLOCKED_DATA_INTEGRITY_VIOLATION"
    assert sanitized_unverified["confidence"] == 0
    assert sanitized_unverified["recommendation"] == "HALT_TRADING_DUE_TO_UNVERIFIED_DATA"
    assert sanitized_unverified["is_data_integrity_blocked"] is True

    # Case 3: Valid verified provenance passes through unaltered
    payload_valid = {"ticker": "SPY", "price": 510.50, "data_source": "NYSE_DIRECT_FEED"}
    verdict_valid = breaker.sanitize_or_block_verdict(payload_valid)
    assert verdict_valid.get("status") == "VERIFIED" or verdict_valid.get("price") == 510.50
    assert "signal" not in verdict_valid or verdict_valid.get("signal") != "BLOCKED_DATA_INTEGRITY_VIOLATION"
    assert verdict_valid.get("is_data_integrity_blocked", False) is False


# ============================================================================
# 2. DIVISION-BY-ZERO DOMAIN SAFETY (>=5 TESTS)
# ============================================================================

def test_div_by_zero_logit_boundary_clamping():
    """Verify logit(P) handles exact P=0.0 and P=1.0 without ZeroDivisionError."""
    # P = 0.0 clamps to eps
    l_zero = logit(0.0, eps=1e-7)
    assert math.isclose(l_zero, math.log(1e-7 / (1.0 - 1e-7)), rel_tol=1e-5)
    assert not math.isinf(l_zero)
    
    # P = 1.0 clamps to 1 - eps
    l_one = logit(1.0, eps=1e-7)
    assert math.isclose(l_one, math.log((1.0 - 1e-7) / 1e-7), rel_tol=1e-5)
    assert not math.isinf(l_one)


def test_div_by_zero_attention_entropy_with_zeros():
    """Verify attention entropy safely handles 0.0 attention weights (0 ln 0 = 0)."""
    weights_with_zeros = np.array([0.5, 0.5, 0.0, 0.0])
    h = attention_entropy(weights_with_zeros)
    expected = - (0.5 * math.log(0.5) + 0.5 * math.log(0.5))
    assert math.isclose(h, expected, rel_tol=1e-5)
    assert math.isfinite(h)


def test_div_by_zero_attention_entropy_empty_or_zero_sum():
    """Verify attention entropy handles empty or zero-sum arrays safely."""
    assert attention_entropy(np.array([])) == 0.0
    assert attention_entropy(np.zeros(5)) == 0.0


def test_div_by_zero_half_life_negative_or_zero():
    """Verify continuous half-life decay raises ValueError on half_life <= 0."""
    with pytest.raises(ValueError, match="half_life must be strictly positive"):
        continuous_half_life_decay(w0=100.0, delta_t=5.0, half_life=0.0)
        
    with pytest.raises(ValueError, match="half_life must be strictly positive"):
        continuous_half_life_decay(w0=100.0, delta_t=5.0, half_life=-5.0)


def test_div_by_zero_domain_safety_sigmoid_saturation():
    """Verify sigmoid handles extreme positive/negative values without overflow."""
    assert sigmoid(1000.0) == 1.0
    assert sigmoid(-1000.0) < 1e-15
    assert 0.0 <= sigmoid(0.0) <= 1.0


# ============================================================================
# 3. CONDITION NUMBER LIMITS COND(SIGMA) <= 10^12 (>=5 TESTS)
# ============================================================================

def test_condition_number_well_conditioned_matrix():
    """Verify well-conditioned random covariance matrix satisfies cond(Sigma) <= 10^12."""
    np.random.seed(42)
    X = np.random.randn(100, 4)
    sigma, cond_num = ledoit_wolf_covariance_shrinkage(X)
    assert cond_num <= 1e12, f"Condition number {cond_num} exceeds 10^12 limit"
    assert cond_num >= 1.0


def test_condition_number_collinear_matrix_shrinkage_stabilization():
    """Verify collinear / rank-deficient matrix is regularized to cond(Sigma) <= 10^12."""
    np.random.seed(42)
    # Column 2 and 3 are exact linear combinations of Column 1
    col1 = np.random.randn(100, 1)
    col2 = col1 * 2.5
    col3 = col1 * -1.2
    col4 = np.random.randn(100, 1)
    X = np.hstack([col1, col2, col3, col4])
    
    sigma, cond_num = ledoit_wolf_covariance_shrinkage(X)
    assert cond_num <= 1e12, f"Collinear matrix condition number {cond_num} not stabilized <= 10^12"
    assert np.all(np.isfinite(sigma)), "Shrunk covariance contains non-finite entries"


def test_condition_number_identical_rows_handling():
    """Verify identical data vectors trigger regularized floor clamping."""
    X = np.ones((50, 4)) * 3.5  # Constant zero-variance data
    sigma, cond_num = ledoit_wolf_covariance_shrinkage(X)
    assert cond_num <= 1e12
    assert sigma.shape == (4, 4)


def test_condition_number_dimension_scaling():
    """Verify condition number stability holds across varying feature dimensions p=2, 4, 8."""
    for p in [2, 4, 8]:
        np.random.seed(p)
        X = np.random.randn(60, p)
        sigma, cond_num = ledoit_wolf_covariance_shrinkage(X)
        assert cond_num <= 1e12, f"Failed condition bound for p={p}: {cond_num}"


def test_condition_number_rejects_insufficient_samples():
    """Verify covariance estimator rejects matrices with n < 2."""
    with pytest.raises(ValueError, match="dimensions too small"):
        ledoit_wolf_covariance_shrinkage(np.array([[1.0, 2.0]]))


# ============================================================================
# 4. ADR-016 400 LOC CEILING CHECK (>=5 TESTS)
# ============================================================================

def test_adr016_loc_counter_excludes_anchor_blocks():
    """Verify calculate_physical_loc excludes # === INVARIANT-BLOCK lines."""
    code = """# Normal line 1
# Normal line 2
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: I02
# NAME: Execution-Price Guardrail
# ADR: ADR-029
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: Execution guardrail
# /INVARIANT [sha1:037a1c64]
# === /INVARIANT-BLOCK ===
# Normal line 3
"""
    total, non_anchor = calculate_physical_loc(code)
    assert total == 12
    assert non_anchor == 3, f"Expected 3 non-anchor lines, got {non_anchor}"


def test_adr016_loc_pass_at_exact_400_ceiling():
    """Verify file with exactly 400 non-anchor lines passes ADR-016 ceiling."""
    lines = ["x = 1\n"] * 400
    code = "".join(lines)
    _, non_anchor = calculate_physical_loc(code)
    assert non_anchor == 400
    assert non_anchor <= 400, "Exact 400 LOC should pass"


def test_adr016_loc_fail_at_401_lines():
    """Verify file with 401 non-anchor lines exceeds ADR-016 ceiling."""
    lines = ["x = 1\n"] * 401
    code = "".join(lines)
    _, non_anchor = calculate_physical_loc(code)
    assert non_anchor == 401
    assert non_anchor > 400, "401 LOC must trigger ceiling violation"


def test_adr016_refactor_warning_threshold_at_350():
    """Verify 350-LOC refactor trigger boundary detection."""
    lines_349 = ["x = 1\n"] * 349
    lines_350 = ["x = 1\n"] * 350
    _, non_anchor_349 = calculate_physical_loc("".join(lines_349))
    _, non_anchor_350 = calculate_physical_loc("".join(lines_350))
    
    assert non_anchor_349 < 350
    assert non_anchor_350 >= 350, "350 LOC should trigger refactor warning threshold"


def test_adr016_empty_and_single_line_files():
    """Verify LOC counter handles empty and single-line files gracefully."""
    total_empty, non_empty = calculate_physical_loc("")
    assert total_empty == 0
    assert non_empty == 0
    
    total_one, non_one = calculate_physical_loc("# Single line\n")
    assert total_one == 1
    assert non_one == 1


# ============================================================================
# 5. SHA1 ANCHOR BLOCK HASH VALIDATION (>=5 TESTS)
# ============================================================================

def test_sha1_anchor_hash_calculation():
    """Verify SHA1 checksum formula sha1(inv_id || adr || predicate)[:8]."""
    inv_id = "I02"
    adr = "ADR-029"
    predicate = "Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)"
    
    expected_hash = compute_anchor_hash(inv_id, adr, predicate)
    assert len(expected_hash) == 8, f"Hash length {len(expected_hash)} != 8"
    assert all(c in "0123456789abcdef" for c in expected_hash), "Hash contains invalid hex chars"


def test_sha1_anchor_hash_detects_tampered_predicate():
    """Verify hash mismatch when predicate text is modified."""
    inv_id = "I01"
    adr = "ADR-029"
    pred_orig = "forall p in Pipeline: p.src in ALLOWLIST and not p.synthetic"
    pred_tampered = "forall p in Pipeline: p.src in ALLOWLIST and True"
    
    hash_orig = compute_anchor_hash(inv_id, adr, pred_orig)
    hash_tampered = compute_anchor_hash(inv_id, adr, pred_tampered)
    assert hash_orig != hash_tampered, "Hash failed to detect tampered predicate"


def test_sha1_anchor_hash_detects_tampered_ids():
    """Verify hash mismatch when inv_id or adr is altered."""
    pred = "Consistent predicate"
    hash1 = compute_anchor_hash("I01", "ADR-029", pred)
    hash2 = compute_anchor_hash("I02", "ADR-029", pred)
    hash3 = compute_anchor_hash("I01", "ADR-045", pred)
    
    assert hash1 != hash2, "Failed to detect changed inv_id"
    assert hash1 != hash3, "Failed to detect changed adr"


def test_sha1_anchor_block_parser_extracts_and_validates():
    """Verify parser extracts code-adjacent anchor block and verifies valid checksum."""
    inv_id = "I02"
    adr = "ADR-029"
    predicate = "Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)"
    valid_hash = compute_anchor_hash(inv_id, adr, predicate)
    
    block_text = f"""
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: {inv_id}
# NAME: Execution-Price Guardrail
# ADR: {adr}
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: {predicate}
# /INVARIANT [sha1:{valid_hash}]
# === /INVARIANT-BLOCK ===
def execute_order():
    pass
"""
    blocks = extract_anchor_blocks(block_text)
    assert len(blocks) == 1
    assert blocks[0]["inv_id"] == "I02"
    assert blocks[0]["valid"] is True
    assert blocks[0]["sha1_claimed"] == valid_hash


def test_sha1_anchor_block_parser_flags_corrupted_hash():
    """Verify parser flags invalid checksum when claimed hash doesn't match recomputed hash."""
    inv_id = "I03"
    adr = "ADR-024"
    predicate = "SCSI <= -0.35 => verdict != BUY"
    
    corrupted_block = f"""
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: {inv_id}
# NAME: Fatal-Contagion Veto
# ADR: {adr}
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: {predicate}
# /INVARIANT [sha1:deadbeef]
# === /INVARIANT-BLOCK ===
"""
    blocks = extract_anchor_blocks(corrupted_block)
    assert len(blocks) == 1
    assert blocks[0]["valid"] is False, "Corrupted anchor was falsely marked valid"
    assert blocks[0]["sha1_claimed"] == "deadbeef"
    assert blocks[0]["sha1_expected"] != "deadbeef"
