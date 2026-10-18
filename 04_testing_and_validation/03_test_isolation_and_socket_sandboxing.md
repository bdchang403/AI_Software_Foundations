# Module 3: Test Suite Decomposition & Hermetic Socket Sandboxing

## 🧠 Theory: Bounded Context Slicing & The Danger of Monolithic Test Suites

In large-scale enterprise systems, automated test suites frequently suffer from the same architectural degradation as production code. When quality engineers allow test files to grow into 1,000+ line monoliths containing hundreds of assertions, page objects, and fixtures, autonomous AI refactoring agents suffer severe attention degradation.

Under the transformer's $O(N^2)$ attention mechanism and the U-shaped positional attention curve, an AI modifying a monolithic test file loses track of earlier mock setups, accidentally deletes shared fixtures, and introduces unasserted side effects.

### The Architectural Modularity Test Heuristic (~400 LOC)
To maintain deterministic test quality, the **Architectural Modularity Heuristic (~400 LOC)** guides test code sizing:
1. **Target ~400-LOC Heuristic**: Test suites should target ~400 LOC for test clarity, cognitive focus, and Single Responsibility Principle (SRP). Comprehensive integration test suites, meta-harnesses, or AST validators (such as `e2e_curriculum_validator.py`) that evaluate cross-system properties may span multiple cohesive functional visitors without violating modularity invariants.
2. **350-LOC Refactoring Trigger**: When a unit test file reaches 350 lines, teams should proactively consider decomposing it into cohesive, isolated sub-suites before adding large new test matrices.
3. **Semantic AST Test Scoping**: Test authoring directives must operate within cohesive AST node scopes (<1,000 tokens) rather than arbitrary physical line windows.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                     DECOMPOSITION OF TEST SUITES BY BOUNDED CONTEXT                              │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ❌ MONOLITHIC TEST SUITE (COLLAPSE RISK)                                                       │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ test_orders_all.py (1,250 LOC)                                                           │   │
│   │ • Unit logic + DB queries + Network HTTP + UI E2E + Auth fixtures                         │   │
│   │ • Attention decay leads to silent fixture deletion & test flakiness                      │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ✅ DECOMPOSED HERMETIC TEST PYRAMID (400-LOC MODULAR HEURISTIC COMPLIANT)                      │
│   ┌────────────────────────┐  ┌────────────────────────┐  ┌────────────────────────┐             │
│   │ test_order_math.py     │  │ test_guardrails.py     │  │ test_conformal_fuzz.py │             │
│   │ (Pure math, <250 LOC)  │  │ (Fail-closed, <300 LOC)│  │ (Fault inject, <350 LOC)│            │
│   └────────────────────────┘  └────────────────────────┘  └────────────────────────┘             │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔒 Hermetic Socket Isolation: OS-Level Network Interception

One of the most insidious testing failure modes in autonomous engineering is **Network Egress Leakage**. If a unit test suite makes outbound HTTP requests to live production or staging APIs:
1. Tests become non-deterministic and flaky due to transient network latency or rate limits (HTTP 429).
2. Live API keys risk credential leakage into logs.
3. AI coding agents can silently bypass zero-mock rules by calling external endpoints during test execution.

To guarantee 100% hermetic isolation, network egress is blocked at the operating system system call boundary using `pytest-socket`.

### The Hermetic Socket Architecture
In `tests/conftest.py`, the Python `socket.socket.connect` system call is intercepted at fixture initialization:

```python
# tests/conftest.py: Hermetic OS-Level Socket Interception
import os
import socket
import pytest

class SocketBlockedError(RuntimeError):
    """Raised when an unauthorized outbound network socket connection is attempted."""
    pass

def guard_socket_connect(*args, **kwargs):
    raise SocketBlockedError(
        "NETWORK EGRESS BLOCKED: Unit tests must execute under 100% hermetic isolation. "
        "Outbound network socket calls are strictly forbidden."
    )

@pytest.fixture(autouse=True)
def block_outbound_sockets(monkeypatch):
    """Intercept socket system calls unless explicitly overridden by ALLOW_NET=true."""
    if os.getenv("ALLOW_NET", "").lower() != "true":
        monkeypatch.setattr(socket.socket, "connect", guard_socket_connect)
```

### Why SocketBlockedError Is Superior to Synthetic Mocks
Traditional unit testing advises developers to use `unittest.mock.patch` to mock HTTP clients. However, when an AI agent generates code, it often mocks the wrong interface or invents synthetic responses that do not reflect live API schemas.

Under Hermetic Socket Isolation:
* Code under test cannot reach the external network.
* If the code attempts an unauthorized outbound socket call, the test framework halts instantly in $<2\text{ms}$ with `SocketBlockedError`.
* Developers are forced to design decoupled architectures where functions accept pure data inputs rather than instantiating external network clients within business logic.

---

## 📦 Golden Recorded Telemetry vs. Synthetic Mocks

The Zero-Mock Mandate ($I_{01}$) does not mean systems cannot be tested against offline data. Instead, it creates a vital distinction between **Synthetic Mocks** and **Golden Recorded Telemetry**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                 SYNTHETIC MOCKS vs. GOLDEN RECORDED TELEMETRY                                    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   SYNTHETIC MOCK (BANNED UNDER ZM001–ZM007)                                                      │
│   • Authored by an LLM or developer using arbitrary constants.                                   │
│   • Example: `{"dark_pool_ratio": 0.50, "spot_price": 200.0, "fed_funds": 5.25}`                 │
│   • Disconnected from physical market distributions, cross-table integrity, and schema timestamps.│
│                                                                                                  │
│   GOLDEN RECORDED TELEMETRY (PERMITTED UNDER INVARIANT I01)                                      │
│   • Exact, byte-for-byte capture of live market/sensor telemetry recorded from verified source. │
│   • Immutably signed with SHA256 checksum and provenance metadata.                               │
│   • Example: `SEC_EDGAR_RAW` Form 10-K Item 8 JSON payload captured on 2026-09-15.               │
│   • Preserves all real-world quirks: irregular timestamps, decimal fractions, and missing fields.│
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Dual-Use Regulated Callout Box

### 🛡️ Dual-Use Callout Box: Hermetic Test Isolation
> **Algorithmic Asset Management**: Outbound network interception via `pytest-socket` guarantees that backtests and unit test suites do not query live exchanges, preventing lookahead data leakage, rate-limiting IP bans, and unrepeatable execution results.  
> **Aerospace Hardware-in-the-Loop (HIL) Avionics (DO-178C Level A)**: In avionics flight control software verification, RTCA DO-178C Section 6.4 mandates software testing in target or closed-loop simulation environments without unverified external network dependencies. RTCA DO-178C software verification does NOT require "Air-Gapped Faraday Chambers" (Faraday cages and anechoic chambers are used for DO-160 radio frequency/electromagnetic interference environmental testing). Instead, DO-178C Level A requires deterministic closed-loop simulation environments with certified recorded sensor streams (e.g., ARINC 424 navigation telemetry) and hermetic execution without ambient network dependencies, ensuring 100% Modified Condition/Decision Coverage (MC/DC) repeatability free from external network jitter or packet interference.
