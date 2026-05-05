# Module 2: Adversarial Thinking & Red-Teaming for Builders

## Theory: The Lazy AI Agent
AI Agents are lazy and overly confident. If you tell an AI to "Update the user's password," and you don't explicitly explicitly tell it to hash the password, it might store it in plain text because the token context didn't include the hashing utility.

**Red-Teaming** means asking yourself: *"If I give this task to a competent but incredibly literal intern who has no common sense, how will they break my production database?"*

## Verbose Example
**The Requirements Lead's Story:** "Allow users to upload an avatar image."

**Adversarial Thought:** "If I tell the AI to write the upload route, it's going to accept any file type. It might allow a `.sh` file upload. It might save the file directly to the local disk instead of our S3 bucket because it doesn't know about our S3 infrastructure."

**The Red-Team Patch (Added to the builder prompt):**
"Constraint: Use the existing `S3UploadHelper` found in `/lib/aws/`. Reject any MIME type that is not `image/png` or `image/jpeg`. Do not write to the local filesystem."

## Exercise: Finding the Security Threat

**Scenario:** The Requirements Lead handed you a blueprint to "Update the `deleteAccount` API to also delete the user's connected Stripe records."

**Your Action:** 
Identify two ways an AI agent could catastrophically misinterpret the implementation, and write the patch constraint.

1. **Adversarial Loopholes:** [e.g., Does it delete the Stripe Customer completely, or just the card? Does it handle API ratelimiting?]
2. **Your Explicit Patch:** [Write the explicit constraint closing the loophole]

---
[**Next Module: Code Decomposition (PR Slicing) →**](./03_decomposition.md)
