# Module 4: Infrastructure Context Engineering (The Resource Map)

## 🧠 Theory: Bounding the "Resource Graph"

When a Builder writes code, the AI looks at files. When a BuilderOps Engineer writes code, the AI looks at a **Cloud Resource Graph**. 

If you don't provide a "Map" of your existing infrastructure, the AI will assume a "Greenfield" environment and attempt to create new VPCs, Gateways, and IAM Users for every small change. This leads to "State Bloat" and catastrophic billing surprises.

**Context Engineering for BuilderOps is the process of defining your "Approved Cloud Surface."**

---

## 🛠️ 1. The Infrastructure Registry (`infra_registry.json`)

Just like builders use a Function Registry, BuilderOps must use an **Infrastructure Registry**. This is a machine-readable JSON file that lists the **Existing Resource IDs** the AI is allowed to reference.

### 📜 Example: `infra_registry.json`
```json
{
  "approved_vpc_id": "vpc-0a1b2c3d4e5f6g7h8",
  "private_subnets": ["subnet-111", "subnet-222"],
  "allowed_regions": ["us-east-1"],
  "naming_convention": "env-app-resource-id",
  "approved_instance_types": ["t3.micro", "t3.small"]
}
```

By injecting this JSON into the AI's system prompt, you are mathematically preventing it from "guessing" your subnet IDs or choosing expensive `p4d.24xlarge` instances.

---

## 🏗️ 2. ADR Enforcement (Architectural Decision Records)

You must provide the AI with your **Infrastructure ADRs**. These are the "Immutable Laws" of your cloud.

**Example ADR-09 (Database Traceability):**
> "All RDS instances must be Multi-AZ. No single-node databases are allowed in production."

### The Effect:
If the AI generates a single-node database, you don't catch it at the PR stage; the AI **never writes it in the first place** because the constraint was part of its initial context chain.

---

## 🛠️ Exercise: Bounding a "Serverless" Change

**Scenario:** You are asking the AI to add a new Lambda function.

**Your Action:**
1.  **Define the Registry:** What piece of metadata (e.g., `IAM_Role_ARN`) must you provide to ensure the AI doesn't create a new, unmanaged IAM Role?
2.  **Define the Constraint:** Write a 1-sentence ADR that prevents the AI from setting the Lambda timeout to more than 30 seconds.

---

[**Next Module: Automated Traceability & AI-SBOM →**](./05_automated_traceability.md)
