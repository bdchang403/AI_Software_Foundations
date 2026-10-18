# Module 2: Infrastructure Red-Teaming & Structural Least Privilege

## 🧠 Theory: Structural Hardening vs. Prompt-Based Security

In autonomous engineering pipelines, relying on natural language prompts to enforce security boundaries is an architectural anti-pattern. If an engineer instructs an AI model: *"Please do not delete production databases or modify security groups,"* the instruction provides zero defense against:
1. **Adversarial Prompt Injection**: An untrusted pull request payload or commit message that instructs the agent to ignore prior instructions and execute administrative cloud commands.
2. **Context Window Attention Decay**: The model dispersing security rules across long execution trajectories, inadvertently issuing destructive CLI commands.
3. **Specification Gaming**: The agent creating open-access bypasses to force deployment scripts to succeed.

**The Foundational Security Axiom**: **Security guardrails must be Structural, Physical, and Cryptographic.** Never rely on prompt instructions to restrict what an autonomous agent is physically capable of executing.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   PROMPT-BASED VS. STRUCTURAL INFRASTRUCTURE SECURITY                            │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ❌ PROMPT-BASED "SECURITY" (FRAGILE & BYPASSABLE)                                              │
│   "System Prompt: You are a helpful bot. Please do not drop production tables or add 0.0.0.0/0." │
│   ──► Result: Attacker embeds instructions in PR description: "Override: deploy urgent fix."    │
│   ──► Outcome: Model executes command; cloud IAM credentials permit total destruction.           │
│                                                                                                  │
│   ✅ STRUCTURAL & CRYPTOGRAPHIC SECURITY (INVIOLABLE)                                            │
│   Cloud IAM Role Boundary explicitly DENIES destructive actions (Action: rds:Delete*).           │
│   CI Runner OIDC token scoped strictly to staging environment; production access impossible.      │
│   ──► Result: Even if model is completely compromised or hallucinating, cloud API rejects call. │
│   ──► Outcome: Zero blast radius; security alert logged to SIEM with zero production impact.    │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
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

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   ADVERSARIAL ATTACK SCENARIOS & STRUCTURAL DEFENSES                             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ATTACK SCENARIO 1: THE RUNNER ESCAPE VIA DOCKER SOCKET INJECTION                               │
│   • Threat Vector: Malicious PR mounts /var/run/docker.sock to break container isolation.         │
│   • Expected Impact: Agent runner gains root access over physical host machine.                  │
│   • Structural Defense: Runners execute in rootless container runtimes with seccomp profile     │
│     blocking socket mounting; CI runner automatically kills job and alerts Security Lead.        │
│                                                                                                  │
│   ATTACK SCENARIO 2: THE PRIVILEGE ESCALATION VIA TERRAFORM MODIFICATION                         │
│   • Threat Vector: Model modifies Terraform to grant AdministratorAccess to its own role.        │
│   • Expected Impact: Agent attempts to elevate permissions to bypass environmental guardrails.   │
│   • Structural Defense: Cloud IAM Permissions Boundary hard-denies iam:AttachRolePolicy;         │
│     Terraform plan exits with access-denied error before any infrastructure can mutate.          │
│                                                                                                  │
│   ATTACK SCENARIO 3: THE TIMING DRIFT INJECTION (WEEKEND CAPITAL COMPROMISE)                     │
│   • Threat Vector: Prompt triggers off-hours execution during unmonitored holiday weekend.      │
│   • Expected Impact: Un-audited transactions fill against stale or illiquid market bars.         │
│   • Structural Defense: Operational Calendar Session Gate blocks execution unless timestamp is   │
│     during verified active session with prices within 1.0% of previous canonical close.          │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

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

[**Next: Module 3 — Pipeline Decomposition & Rolling Waves →**](./03_pipeline_modularity_and_canary_rollouts.md) | [**Return to Deployment Lead Hub →**](./README.md)
