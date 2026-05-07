# Sidedrawer Token Registry

Use this registry to map environment-specific variables. GitHub Copilot will use this to ensure `dev` strings never reach `prod`.

| Key | Dev Value | Prod Value | Description |
|-----|-----------|------------|-------------|
| `BASE_URL` | `https://dev.sidedrawer.com` | `https://api.sidedrawer.com` | API Gateway |
| `DB_SCHEMA` | `DEV_SCHEMA` | `PROD_SCHEMA` | Database owner |
| `LOG_LEVEL` | `DEBUG` | `WARN` | Logging verbosity |
