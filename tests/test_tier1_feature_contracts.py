"""Tier 1: Feature Contract Verification Suite.

Tests feature coverage across all 5 major feature areas:
1. Markdown AST syntax, header hierarchy, and table formatting parity
2. LaTeX mathematical completeness and validity across core equations
3. All 22 Canonical Invariants (I01–I22) registry and attribute completeness
4. 10 Inviolable Commandments presence and non-negotiable clauses
5. Static AST Zero-Mock scanner rules (ZM001–ZM007) node visitor enforcement
"""

import glob
import math
import os
import re
import numpy as np
import pytest

from tests.e2e_curriculum_validator import (
    INVARIANTS_REGISTRY,
    TEN_COMMANDMENTS,
    ASTZeroMockScanner,
    attention_entropy,
    lost_in_the_middle_fidelity,
    continuous_half_life_decay,
    conjunctive_joint_probability,
    compensatory_confluence,
    logit,
    sigmoid,
    scan_python_code_for_mock_violations,
    validate_markdown_syntax,
    extract_and_validate_latex,
)


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# ============================================================================
# MAJOR FEATURE AREA 1: MARKDOWN SYNTAX CONTRACTS (>=5 TESTS)
# ============================================================================

def test_markdown_all_curriculum_files_have_closed_code_fences():
    """Verify that all markdown files in curriculum directories have properly closed code fences."""
    md_files = glob.glob(os.path.join(REPO_ROOT, "0[0-9]_*/**/*.md"), recursive=True)
    md_files.extend(glob.glob(os.path.join(REPO_ROOT, "00_*.md")))
    md_files.append(os.path.join(REPO_ROOT, "README.md"))
    
    assert len(md_files) >= 10, f"Expected at least 10 curriculum files, found {len(md_files)}"
    
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        issues = validate_markdown_syntax(content)
        unclosed = [issue for issue in issues if "Unclosed code fence" in issue]
        assert len(unclosed) == 0, f"Unclosed code fence in {filepath}: {unclosed}"


def test_markdown_table_separator_column_integrity():
    """Verify table column integrity in curriculum files."""
    test_md = """
| Feature | Class | Status |
| :--- | :--- | :--- |
| Invariant I01 | Hard-Safety | Active |
| Invariant I02 | Hard-Safety | Active |
"""
    issues = validate_markdown_syntax(test_md)
    assert len(issues) == 0, f"Expected zero table issues in valid markdown, got: {issues}"


def test_markdown_parser_catches_unclosed_fence():
    """Verify markdown validator catches unclosed code fences."""
    broken_md = "# Title\n\n```python\ndef test():\n    pass\n"
    issues = validate_markdown_syntax(broken_md)
    assert any("Unclosed code fence" in issue for issue in issues), "Expected unclosed fence warning"


def test_markdown_parser_catches_skipped_header_levels():
    """Verify markdown validator catches skipped header levels (e.g. H1 to H3)."""
    broken_md = "# Root Header\n\n### Skipped Header Level 3\n\nContent here."
    issues = validate_markdown_syntax(broken_md)
    assert any("Header level skipped" in issue for issue in issues), "Expected skipped header level warning"


def test_markdown_core_documents_syntax_validity():
    """Verify syntax integrity of core architectural documentation (TEST_INFRA.md, README.md)."""
    core_docs = ["TEST_INFRA.md", "README.md"]
    for doc in core_docs:
        doc_path = os.path.join(REPO_ROOT, doc)
        if os.path.exists(doc_path):
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            issues = validate_markdown_syntax(content)
            # Code fence closure must be 100% clean
            unclosed = [i for i in issues if "Unclosed code fence" in i]
            assert len(unclosed) == 0, f"Unclosed code fence in {doc}: {unclosed}"


# ============================================================================
# MAJOR FEATURE AREA 2: LATEX FORMULA PRESENCE AND VALIDITY (>=5 TESTS)
# ============================================================================

def test_latex_formula_delimiter_and_brace_balance_in_specs():
    """Verify that LaTeX formulas in authoritative guide have balanced delimiters and braces."""
    guide_path = os.path.join(
        REPO_ROOT,
        "templates_and_resources",
        "stories",
        "autonomous_agentic_quant_engineering_master_guide.md"
    )
    assert os.path.exists(guide_path), f"Authoritative guide missing at {guide_path}"
    with open(guide_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    extracted = extract_and_validate_latex(content)
    assert len(extracted) >= 10, f"Expected at least 10 LaTeX formulas in guide, found {len(extracted)}"
    
    unbalanced = [e for e in extracted if not e["balanced"]]
    assert len(unbalanced) == 0, f"Found unbalanced LaTeX formulas: {unbalanced}"


def test_latex_attention_entropy_mathematical_formulation():
    """Verify attention entropy formula mechanics: H(A_i) = -sum(A_ij * ln(A_ij))."""
    # Uniform attention over N=10 tokens gives maximum entropy ln(10)
    uniform_weights = np.ones(10) / 10.0
    h_uniform = attention_entropy(uniform_weights)
    assert math.isclose(h_uniform, math.log(10), rel_tol=1e-5), f"Entropy {h_uniform} != ln(10)"
    
    # Concentrated attention over single token gives minimum entropy 0.0
    peaked_weights = np.zeros(10)
    peaked_weights[0] = 1.0
    h_peaked = attention_entropy(peaked_weights)
    assert math.isclose(h_peaked, 0.0, abs_tol=1e-5), f"Entropy {h_peaked} != 0.0 for delta"


def test_latex_lost_in_the_middle_formulation():
    """Verify U-shaped positional attention curve F(x) fidelity drop in [0.15, 0.85]."""
    f_start = lost_in_the_middle_fidelity(0.0)
    f_end = lost_in_the_middle_fidelity(1.0)
    f_middle = lost_in_the_middle_fidelity(0.50)
    
    assert f_start > 0.90, f"Start fidelity {f_start} should exhibit primacy bias (>0.90)"
    assert f_end > 0.90, f"End fidelity {f_end} should exhibit recency bias (>0.90)"
    assert f_middle <= 0.40, f"Middle fidelity {f_middle} should drop into degradation valley (<=0.40)"
    assert f_middle < f_start and f_middle < f_end


def test_latex_continuous_half_life_decay_formulation():
    """Verify exponential half-life telemetry decay w(Delta t) = w0 * (1/2)^(Delta t / t_1/2)."""
    w0 = 100.0
    t_half = 7.0  # Tactical horizon
    
    # At t = 0, weight is w0
    assert math.isclose(continuous_half_life_decay(w0, 0.0, t_half), 100.0)
    # At t = t_half, weight is w0 / 2
    assert math.isclose(continuous_half_life_decay(w0, 7.0, t_half), 50.0)
    # At t = 2 * t_half, weight is w0 / 4
    assert math.isclose(continuous_half_life_decay(w0, 14.0, t_half), 25.0)


def test_latex_joint_probability_vs_confluence_formulation():
    """Verify joint failure probability collapse prod(p_k) vs compensatory confluence."""
    # 5 independent gates with p=0.30
    p_gates = [0.30] * 5
    p_joint = conjunctive_joint_probability(p_gates)
    assert math.isclose(p_joint, 0.00243, rel_tol=1e-4), f"Joint probability {p_joint} != 0.00243 (0.243%)"
    
    # Compensatory confluence: 2 of 4 pillars >= 0.35 passes
    pillars = [0.70, 0.40, 0.10, 0.20]  # Pillars 1 and 2 pass
    result = compensatory_confluence(pillars, threshold=0.35, min_pillars=2)
    assert result["approved"] is True
    assert result["confluent_pillars"] == 2


def test_latex_log_odds_convex_evidence_fusion_mechanics():
    """Verify closed-form logit transformation logit(P) = ln(P / (1 - P)) and sigmoid."""
    p = 0.75
    logit_val = logit(p)
    expected_logit = math.log(0.75 / 0.25)
    assert math.isclose(logit_val, expected_logit, rel_tol=1e-5)
    
    p_reconstructed = sigmoid(logit_val)
    assert math.isclose(p_reconstructed, p, rel_tol=1e-5)


# ============================================================================
# MAJOR FEATURE AREA 3: ALL 22 CANONICAL INVARIANTS PRESENT (>=5 TESTS)
# ============================================================================

def test_invariants_count_and_keys():
    """Verify that exactly 22 canonical invariants (I01 to I22) are formally defined."""
    assert len(INVARIANTS_REGISTRY) == 22, f"Expected 22 invariants, found {len(INVARIANTS_REGISTRY)}"
    for i in range(1, 23):
        key = f"I{i:02d}"
        assert key in INVARIANTS_REGISTRY, f"Missing invariant key: {key}"


def test_invariants_hard_safety_class():
    """Verify all Hard-Safety invariants (I01 to I05) have formal predicates and target modules."""
    hard_safety_ids = ["I01", "I02", "I03", "I04", "I05"]
    for inv_id in hard_safety_ids:
        inv = INVARIANTS_REGISTRY[inv_id]
        assert inv.invariant_class == "HARD-SAFETY", f"{inv_id} class is {inv.invariant_class}"
        assert len(inv.predicate) > 20, f"{inv_id} has insufficient predicate: {inv.predicate}"
        assert len(inv.target_modules) >= 1, f"{inv_id} has no target modules"
        assert len(inv.enforcement_tests) >= 1, f"{inv_id} has no enforcement tests"


def test_invariants_math_bound_class():
    """Verify all Math-Bound invariants (I06 to I12) have formal mathematical specifications."""
    math_bound_ids = ["I06", "I07", "I08", "I09", "I10", "I11", "I12"]
    for inv_id in math_bound_ids:
        inv = INVARIANTS_REGISTRY[inv_id]
        assert inv.invariant_class == "MATH-BOUND", f"{inv_id} class is {inv.invariant_class}"
        assert len(inv.adrs) >= 1, f"{inv_id} has no governing ADRs"
        assert len(inv.predicate) > 15, f"{inv_id} predicate empty"


def test_invariants_schema_parity_and_decay_classes():
    """Verify Schema-Parity (I13-I16) and Decay-Timing (I17-I19) specifications."""
    schema_ids = ["I13", "I14", "I15", "I16"]
    for inv_id in schema_ids:
        inv = INVARIANTS_REGISTRY[inv_id]
        assert inv.invariant_class == "SCHEMA-PARITY", f"{inv_id} class is {inv.invariant_class}"
        
    decay_ids = ["I17", "I18", "I19"]
    for inv_id in decay_ids:
        inv = INVARIANTS_REGISTRY[inv_id]
        assert inv.invariant_class == "DECAY-TIMING", f"{inv_id} class is {inv.invariant_class}"


def test_invariants_context_isolation_and_code_hygiene_classes():
    """Verify Context-Isolation (I20-I21) and Code-Hygiene (I22) specifications."""
    assert INVARIANTS_REGISTRY["I20"].invariant_class == "CONTEXT-ISOLATION"
    assert INVARIANTS_REGISTRY["I21"].invariant_class == "CONTEXT-ISOLATION"
    assert INVARIANTS_REGISTRY["I22"].invariant_class == "CODE-HYGIENE"
    assert "400" in INVARIANTS_REGISTRY["I22"].predicate


# ============================================================================
# MAJOR FEATURE AREA 4: 10 COMMANDMENTS PRESENT (>=5 TESTS)
# ============================================================================

def test_commandments_count_and_ordering():
    """Verify that all 10 Inviolable Commandments are defined in sequence 1 to 10."""
    assert len(TEN_COMMANDMENTS) == 10, f"Expected 10 commandments, found {len(TEN_COMMANDMENTS)}"
    for i in range(1, 11):
        assert i in TEN_COMMANDMENTS, f"Missing commandment #{i}"


def test_commandments_have_required_attributes():
    """Verify every commandment has title, text, and linked invariant."""
    for i, cmd in TEN_COMMANDMENTS.items():
        assert "title" in cmd and len(cmd["title"]) > 5, f"Commandment #{i} missing title"
        assert "commandment" in cmd and len(cmd["commandment"]) > 20, f"Commandment #{i} missing text"
        assert "invariant" in cmd, f"Commandment #{i} missing invariant link"


def test_commandments_invariant_linkage_validity():
    """Verify all linked invariants in commandments exist in INVARIANTS_REGISTRY."""
    for i, cmd in TEN_COMMANDMENTS.items():
        inv_id = cmd["invariant"]
        assert inv_id in INVARIANTS_REGISTRY, f"Commandment #{i} links invalid invariant: {inv_id}"


def test_commandments_uniqueness():
    """Verify all commandment titles and texts are unique."""
    titles = [cmd["title"] for cmd in TEN_COMMANDMENTS.values()]
    texts = [cmd["commandment"] for cmd in TEN_COMMANDMENTS.values()]
    assert len(set(titles)) == 10, "Duplicate commandment title found"
    assert len(set(texts)) == 10, "Duplicate commandment text found"


def test_commandments_core_doctrines_covered():
    """Verify core enterprise doctrines: Zero-Mock, Plausibility, Fatal Contagion, Quarantine."""
    all_text = " ".join([cmd["commandment"] for cmd in TEN_COMMANDMENTS.values()])
    assert "synthetic" in all_text.lower(), "Zero-synthetic doctrine missing from commandments"
    assert "quarantine" in all_text.lower(), "Quarantine doctrine missing from commandments"
    assert "domain" in all_text.lower(), "Domain safety doctrine missing from commandments"
    assert "400" in all_text or "lines of code" in all_text.lower(), "LOC boundary doctrine missing"


# ============================================================================
# MAJOR FEATURE AREA 5: ZM001-ZM007 STATIC AST RULES (>=5 TESTS)
# ============================================================================

def test_ast_rule_zm001_detects_numeric_return_in_except():
    """ZM001: detects positive numeric returns in except blocks."""
    bad_code = """
def fetch_dark_pool_ratio():
    try:
        return query_api()
    except Exception:
        return 0.50
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM001_EXCEPT_NUMERIC_RETURN" in rule_ids, f"Expected ZM001 violation, got {rule_ids}"


def test_ast_rule_zm002_detects_dict_return_in_except():
    """ZM002: detects synthetic dictionary returns in except blocks."""
    bad_code = """
def fetch_telemetry():
    try:
        return stream.get()
    except Exception:
        return {"dark_pool_ratio": 0.45, "status": "OK"}
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM002_EXCEPT_DICT_RETURN" in rule_ids, f"Expected ZM002 violation, got {rule_ids}"


def test_ast_rule_zm003_detects_banned_variable_prefixes():
    """ZM003: detects variables with MOCK_, SYNTHETIC_, DUMMY_ prefixes."""
    bad_code = """
MOCK_FEED_PRICE = 150.0
SYNTHETIC_DATA_FLAG = True
DUMMY_ACCOUNT_ID = 9999
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert rule_ids.count("ZM003_BANNED_VARIABLE_PREFIX") == 3


def test_ast_rule_zm004_detects_static_profile_registry():
    """ZM004: detects STATIC_PROFILE_REGISTRY definition."""
    bad_code = """
STATIC_PROFILE_REGISTRY = {
    'AAPL': {'pe': 28.5, 'beta': 1.1}
}
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM004_STATIC_PROFILE_REGISTRY" in rule_ids


def test_ast_rule_zm005_detects_numeric_arg_defaults():
    """ZM005: detects positive numeric argument defaults for domain parameters."""
    bad_code = """
def calculate_dcf(price: float = 200.0, rate: float = 0.05):
    return price * rate
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM005_NUMERIC_ARG_DEFAULT" in rule_ids


def test_ast_rule_zm006_detects_dict_get_fallback():
    """ZM006: detects .get('price', 100.0) positive numeric fallback."""
    bad_code = """
def process_quote(payload):
    price = payload.get("price", 100.0)
    return price
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM006_GET_NUMERIC_FALLBACK" in rule_ids


def test_ast_rule_zm007_detects_boolean_or_fallback():
    """ZM007: detects boolean OR positive numeric fallback x or 150.0."""
    bad_code = """
def extract_spot(quote):
    spot = quote.price or 150.0
    return spot
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM007_OR_NUMERIC_FALLBACK" in rule_ids


def test_ast_rule_zm008_detects_empty_except_pass():
    """ZM008: detects empty pass statement in except blocks (silent error swallowing)."""
    bad_code = """
def fetch_telemetry():
    try:
        stream.get()
    except Exception:
        pass
"""
    violations = scan_python_code_for_mock_violations(bad_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM008_EMPTY_EXCEPT_PASS" in rule_ids, f"Expected ZM008 violation, got {rule_ids}"


def test_ast_rule_zm009_detects_mock_import_and_instantiation():
    """ZM009: detects unittest.mock imports and Mock/MagicMock object instantiation."""
    bad_import_code = """
import unittest.mock
from unittest.mock import Mock, patch, MagicMock
from unittest import mock
import mock
"""
    violations = scan_python_code_for_mock_violations(bad_import_code)
    rule_ids = [v.rule_id for v in violations]
    assert "ZM009_BANNED_MOCK_IMPORT_AND_USAGE" in rule_ids, f"Expected ZM009 import violation, got {rule_ids}"
    assert rule_ids.count("ZM009_BANNED_MOCK_IMPORT_AND_USAGE") >= 3

    bad_call_code = """
def setup_test():
    m = Mock()
    fake_feed = MagicMock()
    return m, fake_feed
"""
    violations_call = scan_python_code_for_mock_violations(bad_call_code)
    rule_ids_call = [v.rule_id for v in violations_call]
    assert "ZM009_BANNED_MOCK_IMPORT_AND_USAGE" in rule_ids_call
    assert rule_ids_call.count("ZM009_BANNED_MOCK_IMPORT_AND_USAGE") == 2


def test_ast_scanner_passes_compliant_code():
    """Verify that clean, fail-closed code produces 0 violations."""
    clean_code = """
def fetch_spot_price(ticker: str, price: Optional[float] = None) -> Optional[float]:
    try:
        val = query_live_api(ticker)
        if val is None or not math.isfinite(val):
            return None
        return float(val)
    except UpstreamTimeoutError:
        log_telemetry_failure(ticker)
        return None
    except Exception as e:
        raise DomainExecutionError(f"Fatal error fetching spot for {ticker}: {e}") from e
"""
    violations = scan_python_code_for_mock_violations(clean_code)
    assert len(violations) == 0, f"Expected 0 violations for clean code, got: {violations}"
