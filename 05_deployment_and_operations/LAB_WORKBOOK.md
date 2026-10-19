# BuilderOps & Deployment Lead Lab Workbook: CI Zero-Drift, Hermetic Testing & AI-SBOM Audits

## 🎯 Welcome to the BuilderOps Continuous Verification Laboratory

In this laboratory workbook, you will implement, execute, and verify the automated deployment guardrails of the Context Factory. You will author executable continuous integration checks, build deterministic infrastructure registries, and validate AI Software Bills of Materials (AI-SBOMs).

---

## 🧪 Lab 1: Generating & Bounding the Infrastructure Registry (`infra_registry.json`)

### Objective
Create a machine-readable JSON infrastructure registry that prevents autonomous agents from generating duplicate Virtual Private Clouds (VPCs) or public internet gateways.

### Step 1: The Scenario
A software team requests an autonomous agent to deploy a new microservice worker on AWS Fargate. If the agent does not receive an approved infrastructure registry, it will attempt to synthesize new VPC CIDRs, colliding with the corporate network.

### Step 2: Your Implementation Task
Author a validated `docs/infra/infra_registry.json` file specifying:
1. Approved VPC ID: `vpc-0123456789abcdef0`.
2. Three private application subnets: `subnet-0a1b2c3d`, `subnet-0e1f2a3b`, `subnet-0c4d5e6f`.
3. Customer-managed KMS Key ARN: `arn:aws:kms:us-east-1:123456789012:key/mrk-healthcare-key-01`.
4. Permitted compute runtimes: strictly `AWS Fargate (ARM64)` and `AWS Fargate (x86_64)`.

### Step 3: Verified Answer Key
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "registry_version": "1.0.0",
  "environment": "production-us-east-1",
  "approved_network": {
    "vpc_id": "vpc-0123456789abcdef0",
    "private_app_subnets": [
      "subnet-0a1b2c3d",
      "subnet-0e1f2a3b",
      "subnet-0c4d5e6f"
    ],
    "isolated_data_subnets": [
      "subnet-09876543",
      "subnet-05432109"
    ],
    "public_subnets": []
  },
  "approved_security": {
    "kms_master_key_arn": "arn:aws:kms:us-east-1:123456789012:key/mrk-healthcare-key-01",
    "iam_task_execution_role": "arn:aws:iam::123456789012:role/FargateTaskExecutionRole",
    "enforce_read_only_root_filesystem": true
  },
  "compute_governance": {
    "allowed_runtimes": ["fargate-arm64", "fargate-x86_64"],
    "banned_compute": ["ec2-standalone", "gpu-instances"]
  }
}
```

---

## 🧪 Lab 2: Implementing the Pre-Commit Zero-Drift Synchronization Gate

### Objective
Author an automated pre-commit shell script that executes AST generators and blocks git commits if any registry divergence is detected.

### Step 1: Your Implementation Task
Write a bash script `scripts/verify_precommit_zero_drift.sh`:
1. Executes `python3 scripts/update_state_registry.py`.
2. Executes `python3 scripts/update_math_registry.py`.
3. Executes `python3 scripts/generate_living_context.py`.
4. Evaluates `git diff --exit-code`.
5. If uncommitted differences exist, prints an explicit error message and exits with code 1.
6. If clean, prints success and exits with code 0.

### Step 2: Verified Answer Key
```bash
#!/usr/bin/env bash
# scripts/verify_precommit_zero_drift.sh
set -euo pipefail

echo "🔍 Executing Deterministic AST Registry Synchronizers..."
python3 scripts/update_state_registry.py
python3 scripts/update_math_registry.py
python3 scripts/generate_living_context.py

echo "📊 Verifying Git Working Tree Cleanliness..."
if ! git diff --quiet STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json; then
  echo "❌ CRITICAL ZERO-DRIFT ERROR: Context registries diverge from source code!"
  echo "The following registry files have uncommitted changes:"
  git diff --name-only STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json
  echo "Run 'git add' on the updated registries before committing."
  exit 1
fi

echo "✅ ZERO-DRIFT VERIFIED: Registries are in 100% byte parity with source code."
exit 0
```

---

## 🧪 Lab 3: Validating Machine-Readable AI-SBOM Metadata

### Objective
Write an automated python validator that parses commit metadata and rejects any AI contributions using non-deterministic inference settings or unapproved models.

### Step 1: Your Implementation Task
Author a python function `validate_ai_sbom_commit_message(commit_message: str) -> bool`:
1. Asserts that the commit message contains `# === AI-SBOM-HEADER ===`.
2. Parses the YAML block enclosed within the markers.
3. Asserts `inference_parameters.temperature == 0.0`.
4. Asserts that `foundation_model.model_slug` begins with an approved prefix (`anthropic/`, `google/`, `meta-llama/`, `moonshotai/`, `deepseek/`).
5. If valid, returns `True`. If invalid, raises `ValueError` with an explicit diagnostic reason.

### Step 2: Verified Answer Key
```python
import yaml
import re

APPROVED_MODEL_PREFIXES = (
    "anthropic/",
    "google/",
    "meta-llama/",
    "moonshotai/",
    "deepseek/",
    "openai/"
)

def validate_ai_sbom_commit_message(commit_message: str) -> bool:
    # 1. Check for AI-SBOM Header Markers
    header_pattern = r"# === AI-SBOM-HEADER ===(.*?)# === /AI-SBOM-HEADER ==="
    match = re.search(header_pattern, commit_message, re.DOTALL)
    if not match:
        raise ValueError("REJECTED: Commit metadata lacks mandatory '# === AI-SBOM-HEADER ===' block.")

    raw_yaml = match.group(1).strip()
    try:
        sbom_data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        raise ValueError(f"REJECTED: Corrupted YAML syntax in AI-SBOM header: {exc}")

    # 2. Assert Deterministic Temperature == 0.0
    inference_params = sbom_data.get("foundation_model", {}).get("inference_parameters", {})
    temperature = inference_params.get("temperature")
    if temperature is None or float(temperature) != 0.0:
        raise ValueError(f"REJECTED: Non-deterministic temperature detected ({temperature}). Regulated code requires 0.0.")

    # 3. Assert Approved Model Slug
    model_slug = sbom_data.get("foundation_model", {}).get("model_slug", "")
    if not any(model_slug.startswith(prefix) for prefix in APPROVED_MODEL_PREFIXES):
        raise ValueError(f"REJECTED: Unapproved foundation model slug '{model_slug}'. Must match approved enterprise registry.")

    # 4. Assert Trace UUID Presence
    trace_uuid = sbom_data.get("trace_uuid")
    if not trace_uuid or len(str(trace_uuid)) < 16:
        raise ValueError("REJECTED: Missing or malformed 'trace_uuid' in AI-SBOM header.")

    return True
```

---

## 🧪 Lab 4: Exchange & Operational Calendar Session Gating

### Objective
Implement the execution gate that prevents autonomous trading agents or payment routers from committing state mutations on weekends or outside operational hours without Friday baseline reconciliation.

### Step 1: Verified Answer Key
```python
from datetime import datetime, timezone
import math

def validate_operational_session(execution_utc: datetime, proposed_price: float, friday_close_price: float) -> bool:
    """
    Asserts that executions occur during valid market sessions.
    If executed on a weekend (Saturday=5, Sunday=6), drift from Friday close must be <= 1.0%.
    """
    weekday = execution_utc.weekday()
    is_weekend = weekday in (5, 6)

    if is_weekend:
        if friday_close_price <= 0:
            raise RuntimeError("REJECTED_WEEKEND_SESSION: Friday closing price unavailable for reconciliation.")
        
        drift = abs(proposed_price - friday_close_price) / friday_close_price
        if drift > 0.01:
            raise RuntimeError(
                f"REJECTED_WEEKEND_DRIFT: Proposed weekend price ${proposed_price:.2f} "
                f"diverges by {drift*100:.2f}% (>1.0% limit) from Friday close ${friday_close_price:.2f}."
            )

    return True
```

---

## 🏁 The Finish Line

Congratulations! You have completed the BuilderOps & Deployment Lead Laboratory. You have constructed:
1. A machine-readable Infrastructure Registry preventing cloud resource collisions.
2. A pre-commit zero-drift gate enforcing byte-for-byte parity across context registries.
3. An automated AI-SBOM parser validating cognitive provenance and deterministic inference.
4. An operational session gate protecting production state from weekend drift.

---

## Production Reality & Operational Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)

> [!WARNING]
> **Academic Skimming vs. Automated Sentinels**: Skimming verification exercises without embedding them into CI pipelines leaves production environments vulnerable to untracked drift.

In the median mid-2026 engineering pod, lab exercises are treated as academic theory. Developers skim concepts on Friday afternoon and forget them by Monday morning.

They return to ad-hoc prompting habits:
* **Direct Production Prompting**: Engineers prompt assistants to generate raw Terraform and GitHub Actions YAML directly into production branches.
* **Missing Pre-Commit Sentinels**: Over 80% of teams have zero automated hooks validating context registry parity (`git diff --exit-code`).
* **Unprotected State**: Pods operate with zero session gates protecting state from weekend drift and zero cognitive provenance checks, mistaking Level 1 maturity for "modern AI DevOps."

### Ungoverned Production Failure Modes
Failing to convert workbook validation exercises into continuous production CI/CD sentinels results in critical operational breakdowns:
- **Production Collision Outage**: Two developers prompting separate AI agents to deploy independent services deploy overlapping security group names or conflicting CIDR blocks, triggering routing loops and dropping internal service mesh connectivity.
- **Silent Context Drift in Production**: Without pre-commit zero-drift enforcement, documentation and AST registries desynchronize from running code, causing AI models to generate code against deprecated database schemas and obsolete API contracts.
- **Unregulated Cognitive Deployments**: Without an automated AI-SBOM parser, teams deploy non-deterministic, high-temperature model outputs to production without any audit trail, resulting in catastrophic compliance failures when regulators inspect deployment records.

### Deterministic Engineering Defenses & Operational Takeaways
To operationalize these workbook mechanisms within production repositories, teams must enforce four mechanical practices:
1. **Promote the Lab Sentinels to Repo Root**: Copy the lab's `validate_infrastructure_drift()` and `verify_ai_sbom()` functions directly into your repository's CI pre-commit pipeline as non-negotiable status checks.
2. **Block Commits on Context Registry Drift**: Enforce `git diff --exit-code` in pre-commit git hooks: if code is modified without regenerating the corresponding AST or context registry, reject the commit instantly.
3. **Automate the Operational Session Gate**: Implement an automated CI gate that blocks deployment of high-risk algorithmic changes during closed market hours, weekend maintenance windows, or unmonitored operational shifts.
4. **Require Passing Lab Validation Before Onboarding**: Mandate that every engineer or DevOps contributor successfully run and pass the 4 workbook validation scripts before receiving production deployment tokens.

---

[**Proceed to 07_team_process_and_flow: Monitoring the Factory →**](../07_team_process_and_flow/README.md)

