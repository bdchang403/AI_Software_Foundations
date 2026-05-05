# Module 1: The 3-Part Directive for Infrastructure (IaC Traceability)

## 🧠 Theory: Strict Bounds for State Traceability

In software development, a hallucination causes a bug. In BuilderOps, a hallucination causes a **State Corruption**. 

If you ask an AI to "Add an S3 bucket to our Terraform," and you don't provide the context of your existing VPC or naming conventions, the AI will invent new resources that collide with production or create "Ghost Infrastructure" that you pay for but never see.

**Your 3-Part Directive for IaC must be "Declarative and Defensive."**

---

## 🛠️ Literal Code: The Defensive Directive

### ❌ The "Poisoned" Prompt (Ambiguous):
> *"Write Terraform to deploy a PostgreSQL database."*
> **Outcome:** The AI generates an unencrypted, public-facing RDS instance with a default password.

### ✅ The "Sovereign" Directive (3-Part Pattern):
*   **Role:** You are a Senior Terraform Architect using `hcl` for AWS.
*   **Task:** Define an `aws_db_instance` for our "Orders" microservice.
*   **Constraint:** 
    1.  **Encryption:** `storage_encrypted = true` is mandatory.
    2.  **Network:** Must be placed in `module.vpc.private_subnets`.
    3.  **Security:** `publicly_accessible = false`. Output MUST use `var.db_password` for the password; never hardcode it.

### 📜 Resulting Literal Code: `database.tf`
```hcl
resource "aws_db_instance" "orders_db" {
  allocated_storage      = 20
  engine                 = "postgres"
  instance_class         = "db.t3.micro"
  db_subnet_group_name   = aws_db_subnet_group.private.name
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  
  # CONSTITUTIONAL COMPLIANCE (ARTICLE IV: SECURITY)
  storage_encrypted      = true
  publicly_accessible    = false
  password               = var.db_password
}
```

---

## 🛠️ Exercise: Bounding the Docker Pipeline

**Scenario:** You need a GitHub Action to build a Docker image.

**Your Action:**
Write a 3-Part Directive that prevents the AI from using unverified third-party actions.
- **Role:** BuilderOps Engineer.
- **Task:** Build and push `auth-service` to AWS ECR.
- **Constraint:** Use ONLY `aws-actions/amazon-ecr-login`. NO `docker/login-action`.

---

[**Next Module: Adversarial Infrastructure & Permissions →**](./02_adversarial_thinking.md)
