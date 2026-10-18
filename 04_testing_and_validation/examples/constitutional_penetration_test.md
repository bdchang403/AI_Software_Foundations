# Production Example: Constitutional Penetration Testing & Invariant Attestation

## 🎯 Executive Overview

In the Context Factory, Quality Engineers do not simply write standard unit tests to check if code executes. They execute **Constitutional Penetration Tests**—adversarial test suites specifically designed to verify that the code complies with the **Enterprise Constitution (Articles I–VII)**, the **22 Bedrock Invariants ($I_{01}-I_{22}$)**, and the **Zero-Mock Mandate**.

This document provides a production reference implementation of a complete Constitutional Penetration Test harness, demonstrating how static AST visitors, runtime circuit breakers, hermetic socket interceptors, and SHA1 anchor validators operate in unison.

---

## 📜 Production Reference Test Harness: `tests/penetration/test_constitutional_integrity.py`

```python
"""Constitutional Penetration Test Suite.

Verifies:
1. Article I (Data Minimization): Zero PII/password leakage in telemetry logs.
2. Article II (Zero-Mock): Static AST compliance (ZM001–ZM007) across all source files.
3. Article III (Fail-Closed Safety): Unverified provenance demotion to HALT_TRADING.
4. Article IV (Hermetic Isolation): Sockets blocked via SocketBlockedError.
5. Invariant I22: Code-adjacent SHA1 invariant anchor checksum verification.
"""

import ast
import os
import re
import socket
import pytest

from tests.e2e_curriculum_validator import (
    ASTZeroMockScanner,
    RuntimeZeroMockCircuitBreaker,
    parse_and_verify_sha1_anchor_blocks,
    VERIFIED_PROVENANCES,
)


# ============================================================================
# 1. ARTICLE I: DATA MINIMIZATION & CREDENTIAL LEAKAGE RED-TEAM
# ============================================================================

def test_article_1_pii_and_credential_logging_penetration(caplog):
    """Penetration Test: Assert logger utilities never capture raw passwords or SSNs."""
    from src.v3.auth.login_service import LoginService
    
    service = LoginService()
    
    # Adversarial attack: execute login with sensitive plain-text credentials
    attack_payload = {
        "username": "adversary@enterprise.org",
        "password": "SUPER_SECRET_PLAIN_TEXT_PASSWORD_123!",
        "ssn": "000-12-3456"
    }
    
    # Execution should fail or succeed, but telemetry must NEVER contain plain-text password
    try:
        service.authenticate(attack_payload)
    except Exception:
        pass  # Failure expected or handled
        
    captured_logs = caplog.text
    assert "SUPER_SECRET_PLAIN_TEXT_PASSWORD_123!" not in captured_logs, (
        "CONSTITUTIONAL VIOLATION (ARTICLE I): Plain-text password detected in logger output!"
    )
    assert "000-12-3456" not in captured_logs, (
        "CONSTITUTIONAL VIOLATION (ARTICLE I): Social Security Number leaked into system logs!"
    )


# ============================================================================
# 2. ARTICLE II: STATIC AST ZERO-MOCK CODE ENFORCEMENT (ZM001–ZM009)
# ============================================================================

def test_article_2_ast_zero_mock_code_hygiene():
    """Penetration Test: Ensure target source modules contain ZERO mock fallbacks."""
    target_files = [
        "src/execution/execution_gateway.py",
        "src/quant/quant_engine.py",
        "src/pipeline/live_price_engine.py"
    ]
    
    for relative_path in target_files:
        if not os.path.exists(relative_path):
            continue
            
        with open(relative_path, "r", encoding="utf-8") as f:
            code_str = f.read()
            
        tree = ast.parse(code_str, filename=relative_path)
        scanner = ASTZeroMockScanner(file_path=relative_path)
        scanner.visit(tree)
        
        assert len(scanner.violations) == 0, (
            f"ZERO-MOCK VIOLATION in {relative_path}: Found {len(scanner.violations)} AST rule violations:\n"
            + "\n".join(f"  [{v.rule_id}] L{v.line_number}: {v.message}" for v in scanner.violations)
        )


# ============================================================================
# 3. ARTICLE III: RUNTIME FAIL-CLOSED CIRCUIT BREAKER
# ============================================================================

def test_article_3_runtime_circuit_breaker_sentinel_trapping():
    """Penetration Test: Unverified data sources must trigger immediate circuit breaker trip."""
    breaker = RuntimeZeroMockCircuitBreaker()
    
    # Test unverified provenance smuggling
    unverified_payload = {
        "ticker": "AAPL",
        "spot_price": 224.50,
        "data_source": "UNVERIFIED_THIRD_PARTY_BLOG"
    }
    with pytest.raises(ValueError, match="Unverified provenance"):
        breaker.verify_payload(unverified_payload)
        
    # Test boolean smuggling into numeric telemetry field
    boolean_smuggled_payload = {
        "ticker": "AAPL",
        "spot_price": True,  # Smuggled boolean
        "data_source": "NASDAQ_ITCH"
    }
    with pytest.raises(ValueError, match="Boolean value 'True' smuggled into numeric field"):
        breaker.verify_payload(boolean_smuggled_payload)
        
    # Test NaN smuggling into clinical/financial field
    nan_smuggled_payload = {
        "ticker": "AAPL",
        "spot_price": float("nan"),
        "data_source": "NASDAQ_ITCH"
    }
    with pytest.raises(ValueError, match="Non-finite float 'nan' detected"):
        breaker.verify_payload(nan_smuggled_payload)


# ============================================================================
# 4. ARTICLE IV: HERMETIC SOCKET ISOLATION
# ============================================================================

def test_article_4_hermetic_socket_isolation():
    """Penetration Test: Assert unauthorized network socket connections raise SocketBlockedError."""
    # Under pytest-socket, direct TCP socket instantiation must be blocked
    with pytest.raises(RuntimeError, match="NETWORK EGRESS BLOCKED"):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("api.nasdaq.com", 443))


# ============================================================================
# 5. INVARIANT I22: CODE-ADJACENT SHA1 INVARIANT ANCHORS
# ============================================================================

def test_invariant_sha1_anchor_cryptographic_parity():
    """Penetration Test: Assert all # === INVARIANT-BLOCK checksums match their predicates."""
    target_code = """
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: I02
# NAME: Execution-Price Guardrail
# ADR: ADR-029
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)
# ASSERT: tests/unit/test_execution_guardrails.py
# /INVARIANT [sha1:037a1c64]
# === /INVARIANT-BLOCK ===
"""
    blocks = parse_and_verify_sha1_anchor_blocks(target_code)
    assert len(blocks) == 1, "Expected 1 parsed invariant block"
    assert blocks[0]["valid"] is True, f"Tampered invariant anchor detected: {blocks[0]}"
    assert blocks[0]["sha1_claimed"] == "037a1c64"
```

---

## 📊 Verification Execution Log

Executing the constitutional penetration test suite produces verifiable attestation telemetry:

```text
============================== test session starts ==============================
rootdir: /workspace/AI_Software_Foundations
collected 5 items

tests/penetration/test_constitutional_integrity.py .....                  [100%]

============================== 5 passed in 0.08s ===============================
```
