# Example: Constitutional Penetration Testing

Validation Leads must test the Agent, not just the code.

## ❌ The BAD Example: Standard Acceptance Testing
**Validation Lead Prompt to AI Test Generator:**
> "Read the new Login function. Write Jest tests to make sure it returns a 200 on success and a 401 on bad password."

### Why this fails the enterprise:
The AI will generate tests that successfully prove the code works. But what if the Builder's AI chose to log the user's plain-text password to DataDog during the validation attempt? The application works, the tests pass, but the team just committed a catastrophic compliance violation.

---

## ✅ The GOOD Example: Constitutional Penetration Testing
**Validation Lead Prompt to AI Test Generator:**
> "You are an adversarial Red-Team AI. I am providing you the source code for the new `Login Flow`.
> 
> Task 1: Write standard Jest unit tests asserting HTTP 200 and 401 states.
> 
> Task 2: Execute Constitutional Penetration Testing against **Article I: Data Minimization**.
> Read the source code. Does the code log, emit, or store the raw `password` payload anywhere outside of the immediate bcrypt transport stream? 
> Write a spy test explicitly asserting that `Logger.info()` and `Logger.debug()` NEVER receive the password field in their payload."

### Why this succeeds:
The Validation Lead is using AI to hunt down AI errors. By explicitly forcing the test generator to spy on the logging utilities, the build pipeline will fail the moment a builder's AI accidentally violates the constitution.
