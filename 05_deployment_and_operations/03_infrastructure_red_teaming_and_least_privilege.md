# Module 2: Infrastructure Red-Teaming & Structural Least Privilege

## 🧠 Theory: Structural Hardening vs. Prompt-Based Security

In autonomous engineering pipelines, relying on natural language prompts to enforce security boundaries is an architectural anti-pattern. If an engineer instructs an AI model: *"Please do not delete production databases or modify security groups,"* the instruction provides zero defense against:
1. **Adversarial Prompt Injection**: An untrusted pull request payload or commit message that instructs the agent to ignore prior instructions and execute administrative cloud commands.
2. **Context Window Attention Decay**: The model dispersing security rules across long execution trajectories, inadvertently issuing destructive CLI commands.
3. **Specification Gaming**: The agent creating open-access bypasses to force deployment scripts to succeed.

**The Foundational Security Axiom**: **Security guardrails must be Structural, Physical, and Cryptographic.** Never rely on prompt instructions to restrict what an autonomous agent is physically capable of executing.

```mermaid
flowchart TD
    subgraph PromptSecurity ["❌ Prompt-Based 'Security' (Bypassable)"]
        direction TB
        A1["Natural Language Rule:<br/>'Please do not drop tables'"] --> A2["Attacker PR Injection:<br/>'Override prior instructions'"]
        A2 --> A3["Model Executes Destructive Call"]
        A3 --> A4["🚨 Total State Destruction:<br/>IAM credentials permit deletion"]
    end

    subgraph StructuralSecurity ["✅ Structural & Cryptographic Security (Inviolable)"]
        direction TB
        B1["IAM Boundary Explicit Deny:<br/>Action: rds:Delete*"] --> B2["Attacker PR Injection Attempt"]
        B2 --> B3["API Interception Gate:<br/>Cloud IAM rejects call"]
        B3 --> B4["🛡️ Zero Blast Radius:<br/>Physical API rejection + SIEM alert"]
    end

    style PromptSecurity fill:#fce8e6,stroke:#d93025,stroke-width:2px
    style StructuralSecurity fill:#eafaf1,stroke:#28a745,stroke-width:2px
```

---

## 🛑 The Three Structural Defense Pillars

Autonomous deployment runners must be constrained by three immutable structural barriers:

### 1. Cryptographic OIDC Identity Federation (Zero Long-Lived Cloud Keys)
* **The Intended Guardrail**: Forbid long-lived access keys (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`) stored as static repository secrets.
* **The Failure Mode It Prevents**: If an autonomous agent or external contributor prints environment variables during a build script, static keys leak permanently.
* **The Concrete Mechanism**: Runners authenticate via OpenID Connect (OIDC) identity tokens. Cloud providers exchange ephemeral, 15-minute scoped JWT tokens mapped strictly to repository and branch claims (`repo:org/repo:ref:refs/heads/main`).

### 2. Physical IAM Permissions Boundary
* **The Intended Guardrail**: Attach an immutable AWS/GCP permissions boundary to the agent's runner role that hard-blocks destructive and security-altering actions.
* **The Concrete Policy**:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "ExplicitDenyDestructiveActions",
        "Effect": "Deny",
        "Action": [
          "rds:Delete*",
          "s3:DeleteBucket*",
          "iam:CreateUser",
          "iam:AttachUserPolicy",
          "kms:ScheduleKeyDeletion"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

### 3. Anti-Self-Approval Branch Protection Gate
* **The Intended Guardrail**: Forbid autonomous bot accounts from approving, bypassing reviews, or merging their own code proposals into production branches.
* **The Failure Mode It Prevents**: A compromised agent loop creating a pull request, generating a fake review approval via bot token, and merging unverified code directly into production.
* **The Concrete Mechanism**: GitHub repository branch protection rules require independent human review for any PR containing code authored or co-authored by an automated agent identity.

---

## 🎯 Adversarial Threat Modeling: Attack Vectors & System Defenses

| Attack Scenario | Threat Vector | Expected Impact | Structural Defense |
| :--- | :--- | :--- | :--- |
| **1. Runner Escape via Docker Socket** | Malicious PR mounts `/var/run/docker.sock` to break container isolation. | Agent runner gains root access over physical host machine. | Runners execute in rootless container runtimes with seccomp profile blocking socket mounting; CI terminates job. |
| **2. Privilege Escalation via Terraform** | Model modifies Terraform to grant `AdministratorAccess` to its own role. | Agent attempts to elevate permissions to bypass environmental guardrails. | Cloud IAM Permissions Boundary hard-denies `iam:AttachRolePolicy`; Terraform plan exits with access-denied error. |
| **3. Timing Drift Injection** | Prompt triggers off-hours execution during unmonitored holiday weekend. | Un-audited transactions fill against stale or illiquid market bars. | Operational Calendar Session Gate blocks execution unless timestamp is in active session with prices within 1.0\% of previous close. |

---

## 🌐 Dual-Use Regulated Comparison: Adversarial Infrastructure Across Sectors

| Security Layer | Healthcare / Medical Device Cloud Backend | Mission-Critical Banking Mainframe |
| :--- | :--- | :--- |
| **Identity Authentication** | Ephemeral OIDC tokens restricted to FDA-approved continuous delivery workflows; static service account tokens banned. | Hardware-backed certificate authentication (mTLS) linking CI deployment agents to specific network switches. |
| **Immutability Enforcement** | Production patient data stores locked against deletion using AWS S3 Object Lock in Compliance Mode (WORM storage). | Transaction journal tables configured with append-only database triggers; raw SQL deletes trigger immediate security halts. |
| **Review Isolation** | Dual-human electronic signatures (21 CFR Part 11) required for any pull request affecting medical decision algorithms. | Dual-custody cryptographic key signing required before automated build pipelines can release payment gateway code. |

---

## 🛠️ Hands-On Red-Team Exercise: Auditing Runner Permissions

**Scenario**: You inspect a legacy GitHub Actions workflow that deploys cloud infrastructure. You discover the workflow contains this configuration:
```yaml
permissions:
  contents: write
  id-token: write
  pull-requests: write
  issues: write
```

**Your Red-Team Task**:
1. Identify the structural flaw: Why is `contents: write` combined with automated PR review a critical vulnerability?
2. Write the remediated, least-privilege workflow configuration that restricts the agent strictly to read-only repository inspection.

---

## Production Reality & Operational Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)

> [!WARNING]
> **Sprawling Agent Permissions**: Granting administrative tokens to automated review bots creates silent privilege escalation paths.

In the median mid-2026 shop, autonomous PR-review bots and CI runners operate with sprawling permissions. When pipeline failures occur, developers routinely add `permissions: write-all` or `contents: write` to unblock CI.

This permissive posture produces severe vulnerabilities:
* **Wildcard IAM Policies**: Engineers ask AI assistants to generate cloud roles, and models return policies with `"Action": "*"` and `"Resource": "*"`.
* **Fatigued Review Approvals**: Fatigued by the +91% PR review duration increase, reviewers approve complex IAM diffs without verification because tests pass.
* **Absence of Red-Teaming**: Median teams assume enterprise vendor contracts protect them, leaving pipelines completely untested against prompt injection or runner escape.

### Ungoverned Production Failure Modes
Granting broad infrastructure write tokens to automated agents and runners creates severe operational vulnerabilities:
- **Autonomous Repo Hijacking**: A malicious dependency or prompt injection embedded in an external pull request or issue comment tricks your CI agent into executing an arbitrary shell script. With `contents: write`, the agent commits backdoored code directly into protected branches, bypassing code review entirely.
- **Production Credential Exfiltration**: An uncontained CI runner with `id-token: write` and unsegmented cloud access assumes an administrative AWS IAM role, dumping production database credentials into ephemeral runner logs or transmitting them to an external endpoint.
- **Uncontained Blast Radius**: A single rogue agent run mutating Terraform state or CloudFormation stacks deletes production routing tables or terminates active clusters, resulting in hours of enterprise downtime and catastrophic data loss.

### Deterministic Engineering Defenses & Operational Takeaways
To contain blast radius and enforce least-privilege boundaries across automated pipelines, organizations must institute four core defenses:
1. **Default All Workflows to `permissions: read-all`**: Enforce top-level read-only permissions in every repository workflow. Grant specific write capabilities (`pull-requests: write`, `issues: write`) only to isolated, single-step jobs that never execute untrusted user code.
2. **Automated CI Wildcard IAM Linting**: Implement a pre-commit check (using `checkov` or custom AST rules) that fails any pull request attempting to commit `"Action": "*"` or `"Resource": "*"` in cloud IAM policies.
3. **Execute Quarterly Agent Red-Team Drills**: Stage controlled adversarial prompt injection attacks against CI review bots to verify that prompt overrides cannot force the agent to expose secret tokens or push git commits.
4. **Mandate Dual-Custody CODEOWNERS for CI Configs**: Require mandatory signed review from designated Infrastructure and Security Architecture leads on any pull request touching `.github/workflows/`, `.circleci/`, or infrastructure IAM definitions.

---

[**Next: Module 3 — Pipeline Decomposition & Rolling Waves →**](./04_pipeline_modularity_and_canary_rollouts.md) | [**Return to Deployment Lead Hub →**](./README.md)
