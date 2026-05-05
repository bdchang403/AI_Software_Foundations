# Module 3: Pipeline Decomposition

## Theory: Standardizing the Agent Workflows
A single `deploy.yml` file that is 2000 lines long is impenetrable to both humans and bounded AI agents. If you ask an AI to fix a regex deployment issue in line 1800, it will likely mess up spacing or variables in line 200.

You must decompose pipeline logic into discrete, reusable Action files.

## Verbose Example
Instead of one massive YAML file, decompose your workflows:
1. `.github/workflows/lint.yml`
2. `.github/workflows/test.yml`
3. `.github/workflows/build.yml`
4. `.github/workflows/deploy.yml`

If an AI needs to fix a testing issue, you explicitly prompt it with: *"Context: Only read the `test.yml` file. Constraint: Do not touch `build.yml`."*

## Exercise: Slice the Tooling

**Your Action:**
Look at your current deployment pipeline. Write down how you would split your massive deployment steps into at least 3 discrete, reusable YAML components so an AI could manage them individually.

1. **Component 1:** [e.g., `setup-aws-credentials-action`]
2. **Component 2:** [e.g., `docker-build-push-action`]
3. **Component 3:** [e.g., `helm-deploy-action`]

---
[**Next Module: Infrastructure Context Engineering (The Resource Map) →**](./04_context_engineering.md)
