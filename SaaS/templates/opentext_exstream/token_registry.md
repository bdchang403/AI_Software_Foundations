# Opentext Exstream Token Registry

Use this registry to map environment-specific variables. GitHub Copilot will use this to ensure `dev` strings never reach `prod`.

| Key | Dev Value | Prod Value | Description |
|-----|-----------|------------|-------------|
| `BASE_URL` | `https://dev.opentext.com` | `https://api.opentext.com` | API Gateway |
| `DB_SCHEMA` | `DEV_SCHEMA` | `PROD_SCHEMA` | Database owner |
| `LOG_LEVEL` | `DEBUG` | `WARN` | Logging verbosity |
