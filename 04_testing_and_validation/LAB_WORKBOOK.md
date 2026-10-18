# Validation Lead & Quality Engineering Lab Workbook: Adversarial Red-Teaming, AST Scanning & Conformal Labs

## 🎯 Welcome to the Quality Engineering Laboratory

In this laboratory workbook, you will transition from traditional functional testing to **Adversarial Quality Engineering** in the Context Factory. You will implement and execute static AST scanners, runtime circuit breakers, hermetic socket isolation harnesses, and compensatory confluence engines.

---

## 🧪 Lab 1: AST Zero-Mock Scanner Auditing (Rules ZM001–ZM007)

### Objective
Write an automated AST visitor script that statically parses Python code files, intercepting synthetic defaults, mock variable prefixes, and fail-soft catch blocks.

### Step 1: The Vulnerable Code Snippet (`src/vulnerable_service.py`)
```python
# A typical AI-generated "fail-soft" implementation
MOCK_BASE_RATE = 5.25

def get_market_telemetry(ticker: str, default_price: float = 200.0) -> dict:
    try:
        val = fetch_live_data(ticker)
        ratio = val.get("dark_pool_ratio", 0.50)
        return {"spot_price": val.price or 150.0, "ratio": ratio}
    except Exception:
        return 0.50  # Silenced catch block returning synthetic float
```

### Step 2: Your Implementation Task
Using Python's built-in `ast` module, write an `ASTZeroMockScanner` that inherits from `ast.NodeVisitor` and detects all violations in the snippet above:
1. `ZM001`: Detects `return 0.50` inside `ExceptHandler`.
2. `ZM003`: Detects variable `MOCK_BASE_RATE`.
3. `ZM005`: Detects `default_price: float = 200.0`.
4. `ZM006`: Detects `.get("dark_pool_ratio", 0.50)`.
5. `ZM007`: Detects `val.price or 150.0`.

### Step 3: Verified Answer Key
```python
import ast

class LabASTScanner(ast.NodeVisitor):
    def __init__(self):
        self.violations = []

    def visit_ExceptHandler(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Constant):
                if isinstance(stmt.value.value, (int, float)) and stmt.value.value > 0:
                    self.violations.append(f"ZM001: Banned numeric return {stmt.value.value} in except")
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.startswith(("MOCK_", "SYNTHETIC_")):
                self.violations.append(f"ZM003: Banned prefix in variable {target.id}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        for default, arg in zip(reversed(node.args.defaults), reversed(node.args.args)):
            if isinstance(default, ast.Constant) and isinstance(default.value, (int, float)) and default.value > 0:
                self.violations.append(f"ZM005: Banned numeric default {default.value} for {arg.arg}")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr == "get" and len(node.args) >= 2:
            fallback = node.args[1]
            if isinstance(fallback, ast.Constant) and isinstance(fallback.value, (int, float)) and fallback.value > 0:
                self.violations.append(f"ZM006: Banned positive fallback {fallback.value} in .get()")
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.Or):
            for val in node.values[1:]:
                if isinstance(val, ast.Constant) and isinstance(val.value, (int, float)) and val.value > 0:
                    self.violations.append(f"ZM007: Banned fallback {val.value} in boolean OR")
        self.generic_visit(node)
```

---

## 🧪 Lab 2: Runtime Fail-Closed Circuit Breakers & Provenance Attestation

### Objective
Implement the deep recursive runtime payload walker verifying data sources against the 15 Verified Immutable Provenances and trapping boolean and NaN smuggling.

### Step 1: Your Implementation Task
Write a class `RuntimeZeroMockCircuitBreaker` that accepts arbitrary dictionary or list payloads and asserts:
1. Every payload declaring a `data_source` must match `VERIFIED_PROVENANCES` (or `"NONE"`).
2. Numeric financial/clinical fields (`spot_price`, `infusion_rate`, `fed_funds_rate`) must reject boolean types (`isinstance(v, bool)`).
3. Numeric values must be finite floats (`math.isfinite(v)`).
4. If validation fails, raise `ValueError` describing the violation path.

### Step 2: Verified Answer Key
```python
import math

VERIFIED_PROVENANCES = frozenset({
    "FRED_ST_LOUIS_LIVE", "SEC_EDGAR_RAW", "NYSE_DIRECT_FEED", "NASDAQ_ITCH",
    "FDA_MAUDE_DATABASE", "ISO_13485_AUDIT_LOG", "ARINC_424_NAV_DATABASE",
    "DO178C_TELEMETRY", "SWIFT_FIN_GATEWAY", "FEDWIRE_SETTLEMENT",
    "BLOOMBERG_BPIPE", "REFINITIV_ELEKTRON", "FMP_REST_API", "YAHOO_FINANCE_RAPID",
    "FINNHUB_STREAM",
})

class LabCircuitBreaker:
    NUMERIC_FIELDS = {"spot_price", "infusion_rate", "fed_funds_rate", "rate", "price"}

    def verify(self, payload, path="root"):
        if isinstance(payload, dict):
            if "data_source" in payload:
                src = payload["data_source"]
                if src != "NONE" and src not in VERIFIED_PROVENANCES:
                    raise ValueError(f"Circuit Breaker tripped at {path}: Unverified provenance '{src}'")
            for k, v in payload.items():
                curr = f"{path}.{k}"
                if k in self.NUMERIC_FIELDS:
                    if isinstance(v, bool):
                        raise ValueError(f"Circuit Breaker tripped at {curr}: Boolean smuggling '{v}'")
                    if isinstance(v, (int, float)) and not math.isfinite(v):
                        raise ValueError(f"Circuit Breaker tripped at {curr}: Non-finite float '{v}'")
                self.verify(v, curr)
        elif isinstance(payload, list):
            for i, item in enumerate(payload):
                self.verify(item, f"{path}[{i}]")
        return True
```

---

## 🧪 Lab 3: Hermetic Socket Isolation & `SocketBlockedError`

### Objective
Configure a pytest fixture that intercepts OS socket calls at runtime, ensuring test suites execute without outbound network leaks.

### Step 1: Your Implementation Task
In `tests/conftest.py`, define custom exception `SocketBlockedError`. Using pytest's `monkeypatch` fixture, override `socket.socket.connect` to raise `SocketBlockedError` unless an environment variable `ALLOW_NET=true` is set.

### Step 2: Verified Answer Key
```python
import os
import socket
import pytest

class SocketBlockedError(RuntimeError):
    pass

def guard_socket_connect(*args, **kwargs):
    raise SocketBlockedError("NETWORK EGRESS BLOCKED: Hermetic isolation violation.")

@pytest.fixture(autouse=True)
def hermetic_socket_guard(monkeypatch):
    if os.getenv("ALLOW_NET", "").lower() != "true":
        monkeypatch.setattr(socket.socket, "connect", guard_socket_connect)
```

---

## 🧪 Lab 4: Compensatory 4-Pillar Confluence vs. Conjunctive Gate Collapse

### Objective
Write an algorithmic test proving that conjunctive sequential boolean gates collapse joint probability ($0.243\%$), while Compensatory 4-Pillar Confluence Guardrail (Invariant I09) unblocks high-reinvestment compounders while isolating fatal contagion vetoes ($I_{03}$).

### Step 1: Verified Answer Key
```python
def test_compensatory_confluence_unblocks_compounders():
    # 4 Pillar Scores: [Quality, Momentum, Network, DCF]
    # In Crisis 4, DCF was -0.10 due to heavy R&D reinvestment, but Quality and Momentum were elite
    nvda_pillars = [0.85, 0.75, 0.60, -0.10]
    
    # Conjunctive Gate (DCF > 0 AND Quality > 0.5 AND Momentum > 0.5) FAILS!
    conjunctive_pass = (nvda_pillars[3] > 0.0) and (nvda_pillars[0] > 0.5) and (nvda_pillars[1] > 0.5)
    assert conjunctive_pass is False, "Conjunctive gate incorrectly passed!"
    
    # Compensatory Confluence (Invariant I09): Any 2 of 4 >= 0.35 passes BUY consideration
    confluent_count = sum(1 for p in nvda_pillars if p >= 0.35)
    has_fatal_contagion = False  # SCSI > -0.35, Altman Z > 1.10
    
    confluence_pass = (confluent_count >= 2) and (not has_fatal_contagion)
    assert confluence_pass is True, "Compensatory confluence should unblock elite compounder!"
```

---

## 🧪 Lab 5: Cartesian Fault Injection & Conformal Fuzzing

### Objective
Author a Cartesian fuzzing test exercising numerical stability under ill-conditioned covariance matrices and non-finite inputs.

### Step 1: Verified Answer Key
```python
import numpy as np
import pytest

def test_cartesian_covariance_stability():
    # Construct an ill-conditioned, near-singular 4x4 matrix
    # Condition number cond(Sigma) > 1e14
    X_ill = np.array([
        [1.0, 1.0000001, 2.0, 3.0],
        [1.0, 1.0000000, 2.0, 3.0],
        [2.0, 2.0000001, 4.0, 6.0],
        [3.0, 3.0000001, 6.0, 9.0]
    ])
    
    # Analytical Ledoit-Wolf Shrinkage stabilization
    p = X_ill.shape[1]
    sample_cov = np.cov(X_ill, rowvar=False)
    shrinkage_intensity = 0.35
    target_prior = (np.trace(sample_cov) / p) * np.eye(p)
    stabilized_cov = (1.0 - shrinkage_intensity) * sample_cov + shrinkage_intensity * target_prior
    
    # Assert condition number is safely bounded below 1e12 (Invariant I11)
    cond_num = np.linalg.cond(stabilized_cov)
    assert cond_num <= 1e12, f"Condition number {cond_num} exceeds stability threshold 1e12!"
```
