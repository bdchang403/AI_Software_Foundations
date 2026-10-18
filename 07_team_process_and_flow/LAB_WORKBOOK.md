# Agile Leader Lab Workbook: The Autonomous Engineering Metrics Audit

---

## 🎯 Executive Overview & Lab Objectives

In this lab, you act as the **Principal Agile Coach and Delivery Lead**. You will analyze live telemetry streams from an AI-assisted engineering team, detect structural context failures, calculate key mathematical indices (CDR, PRI, TCER), and execute targeted coaching interventions across the Context Factory roles.

By completing this lab, you will:
1. Calculate the **Context Debt Ratio (CDR)** and **Prompt Regression Interval (PRI)** from commit logs.
2. Detect **Ghost Productivity** and enforce the **Architectural Modularity Ceiling (maximum 400 LOC)**.
3. Execute the automated **Pull Request Review Comment Classifier** to diagnose upstream breakdowns.
4. Quantify the mathematical **Token Cost Efficiency Ratio (TCER)** and present an executive ROI proof.

---

## 🛠️ Lab Setup & Telemetry Environment

Verify your Python environment before starting the exercises:

```bash
python3 --version
pytest --version
```

---

## 🧪 Exercise 1: Auditing the "Hallucination Loop" & Calculating CDR

### The Scenario:
Team Epsilon is building an automated compliance microservice. Over a two-week sprint, the team expended $4,200,000$ model tokens. The lead developer reports feeling exhausted by prompt iterations.

### Telemetry Data:
*   Total tokens expended on successful merged PRs: $1,250,000$ tokens.
*   Tokens expended on discarded prompt loops, broken builds, and reverted branches: $2,950,000$ tokens.

### Step 1: Calculate Context Debt Ratio (CDR)
$$\text{CDR} = \frac{\text{Rework Tokens}}{\text{Total Tokens}} = \frac{2,950,000}{4,200,000} = 0.702 \; (70.2\%)$$

### Step 2: Diagnostic Evaluation
*   **Threshold Rule**: $\text{CDR} \le 0.18$ is Healthy. $\text{CDR} > 0.25$ demands an immediate generation freeze.
*   **Diagnostic Finding**: CDR of $0.702$ indicates severe prompt looping. The model is guessing context rather than executing deterministic instructions.
*   **Root Cause**: The Requirements Lead supplied user stories with narrative prose rather than the 3-Part Directive and 20-edge-case matrix.
*   **Agile Leader Intervention**: Freeze AI code generation on this epic. Convene a 45-minute working session with the Requirements Lead to author formal Semantic Blueprints with strict input/output schemas.

---

## 🧪 Exercise 2: Detecting "Ghost Productivity" & Enforcing Modularity

### The Scenario:
A builder submits pull request `PR-412` titled *"Implement multi-currency wire fees"*. The PR diff reveals:
*   Total Files Changed: 14 files.
*   Lines of Code Added: 1,850 LOC.
*   Commit Message: *"AI generated complete wire fee calculations with helpers."*

### Step 1: Invariant Check
*   **Governing Rule**: Architectural Modularity Ceiling (maximum 400 lines of code per pull request; refactoring triggered at 350 LOC).
*   **Status**: **VIOLATION (1,850 LOC > 400 LOC ceiling)**.

### Step 2: Diagnostic Script Execution
Run this verification script to detect oversized pull requests and flag violations:

```python
def verify_pull_request_modularity(files_changed: list[tuple[str, int]], max_loc_ceiling: int = 400) -> dict:
    total_loc = sum(loc for _, loc in files_changed)
    is_compliant = total_loc <= max_loc_ceiling
    
    return {
        "total_loc": total_loc,
        "max_ceiling": max_loc_ceiling,
        "is_compliant": is_compliant,
        "action": "APPROVE_PIPELINE" if is_compliant else "REJECT_EXCEEDS_MODULARITY_CEILING"
    }

if __name__ == "__main__":
    pr_diff = [
        ("services/fee_calculator.py", 650),
        ("models/currency.py", 420),
        ("utils/math_helpers.py", 780)
    ]
    result = verify_pull_request_modularity(pr_diff)
    print("Modularity Audit Result:", result)
```

### Step 3: Coaching Intervention:
Reject the PR in GitHub with the following coaching message:
> *"This pull request adds 1,850 lines of code, exceeding our Architectural Modularity Ceiling of 400 LOC. Monolithic PRs overwhelm human reviewers and prevent automated invariant isolation. Please decompose this feature into three Bounded Task Units (BTUs): (1) Currency data models, (2) Core fee calculation engine, and (3) Integration tests."*

---

## 🧪 Exercise 3: Automated Review Comment Triaging

### The Scenario:
You are reviewing the last 10 pull requests for a high-value payments module. Peer review comments are unusually high. Run the automated classifier to identify the upstream breakdown:

```python
import re

def classify_pr_comments(comments: list[str]) -> dict:
    tally = {
        "requirements_gap": 0,
        "modularity_breach": 0,
        "mock_smuggling": 0
    }
    
    for c in comments:
        c_low = c.lower()
        if re.search(r"(edge case|unclear|null handling|schema|specification)", c_low):
            tally["requirements_gap"] += 1
        elif re.search(r"(too long|split|refactor|modularity|ceiling|400)", c_low):
            tally["modularity_breach"] += 1
        elif re.search(r"(magicmock|fake data|mock|synthetic|stub|zm001)", c_low):
            tally["mock_smuggling"] += 1

    return tally

if __name__ == "__main__":
    comments = [
        "What happens when the currency pair is not found in the cache? Requirement is silent.",
        "This function is 520 lines long; violates our 400 LOC modularity ceiling.",
        "Why is this unit test mocking the ledger database with MagicMock? Use SQLite in-memory.",
        "Edge case missing for negative settlement amounts."
    ]
    tally = classify_pr_comments(comments)
    print("Comment Classification:", tally)
```

### Analysis:
*   `requirements_gap: 2` $	o$ Requirements Lead intervention needed.
*   `modularity_breach: 1` $	o$ Builder coaching on PR slicing.
*   `mock_smuggling: 1` $	o$ Validation Lead coaching on AST Zero-Mock rules.

---

## 🧪 Exercise 4: Executive ROI & Determinism Quantification

Calculate the Token Cost Efficiency Ratio (TCER) comparing unconstrained prompting vs. the Context Factory:

```python
def compute_token_roi(zero_context_tokens: int, factory_tokens: int, token_price_per_million: float = 10.0) -> dict:
    tcer = zero_context_tokens / factory_tokens
    cost_zero_context = (zero_context_tokens / 1_000_000) * token_price_per_million
    cost_factory = (factory_tokens / 1_000_000) * token_price_per_million
    savings_pct = ((cost_zero_context - cost_factory) / cost_zero_context) * 100.0

    return {
        "zero_context_cost_usd": round(cost_zero_context, 4),
        "factory_cost_usd": round(cost_factory, 4),
        "tcer_multiplier": round(tcer, 1),
        "savings_percentage": round(savings_pct, 2)
    }

if __name__ == "__main__":
    # Baseline: 120,000 tokens (repo dump) vs 1,500 tokens (Living Context)
    roi = compute_token_roi(zero_context_tokens=120_000, factory_tokens=1_500)
    print("ROI Analysis:", roi)
```

### Expected Output:
```json
{
  "zero_context_cost_usd": 1.2,
  "factory_cost_usd": 0.015,
  "tcer_multiplier": 80.0,
  "savings_percentage": 98.75
}
```

---

## 🏁 Lab Completion Checklist
- [ ] Context Debt Ratio (CDR) calculated and evaluated against the $0.18$ threshold.
- [ ] Architectural Modularity Ceiling enforced on pull requests ($> 400$ LOC rejected).
- [ ] Pull request review comments triaged to specific upstream roles.
- [ ] Token Cost Efficiency Ratio (TCER $\ge 80	imes$) quantified for executive reporting.

---

## Staff Engineer Reality Check: Does This Actually Help the Mid-2026 Team?

### 1. The Mid-2026 Median Reality (The 75%-84% Baseline Trap)
In the median mid-2026 team, agile ceremonies and workbook exercises are run as rote rituals disconnected from engineering mechanics. Scrum Masters track Jira burndown charts and sprint velocity points while ignoring that half the committed code is AI boilerplate that requires 90 minutes per PR to review. When presented with lab calculations for Context Debt Ratio (CDR) and Token Cost Efficiency Ratio (TCER), agile leaders dismiss them as "niche DevOps metrics." Meanwhile, the pod suffers from chronic sprint rollover—stories remain blocked in review on the last day of the sprint because PR sizes exceed 500 lines and developers are caught in multi-turn hallucination loops.

### 2. What Happens Tomorrow Morning If You Ignore This?
If your team continues to treat process metrics as optional theory:
- **Chronic Sprint Rollover and False Predictability**: Sprints will fail to deliver committed scope. Because CDR is unmonitored ($> 0.18$), developers spend more time fighting context debt and reworking AI mistakes than delivering new features.
- **Uncontrolled Token Budget Hemorrhage**: Developers will continue dumping 120,000-token repository context blobs into brute-force prompts, running up thousand-dollar monthly bills while achieving poor code quality that fails compilation.
- **Review Gridlock and Friction**: Without the lab's PR comment triaging, code reviews will remain acrimonious battlegrounds where senior developers complain about style and missing requirements without any systemic feedback loop to the Business Analyst or Architect.

### 3. Tactical Playbook: Hand This to Your Tech Lead / Pod Tomorrow
1. **Enforce the Automated 400-LOC PR Ceiling**: Configure branch protection to reject any pull request exceeding 400 LOC (ADR-016), forcing developers to submit small, reviewable slices.
2. **Calculate CDR in Every Sprint Retrospective**: Run the lab's `calculate_cdr()` script over the sprint's git commits; if CDR exceeds $0.18$, dedicate the next sprint's technical debt budget to repairing AST context registries.
3. **Audit PR Comments to Upstream Roles**: Categorize review comments into the 4 factory stations (BA, Architect, Builder, QE) during retrospectives, using the data to retrain prompt directives and clarify requirements.
4. **Enforce Living Context Compression in Tooling**: Replace raw repository dumps with compiled Living Context slices ($< 1,500$ tokens) to maintain $\text{TCER} \ge 80\times$ across all agentic workloads.

---

[**Proceed to Phase 4: Agent Orchestration & Assembly →**](../09_ai_agent_orchestration/README.md)

