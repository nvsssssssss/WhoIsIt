# Environment Variables & Secrets Policy

## Purpose

WhoIsIt uses environment variables to store configuration that may vary between development, testing, and production environments.

Sensitive values such as API keys, passwords, database credentials, and secret keys must not be stored directly in source code or committed to the Git repository.

## Environment Files

### `.env`

The `.env` file contains local environment-specific values.

It may contain sensitive information and must never be committed to Git.

Example:

~~~text
DATABASE_URL=actual_database_url
SECRET_KEY=actual_secret_key
~~~

### `.env.example`

The `.env.example` file documents the environment variables required by the project.

It must not contain real secrets.

Example:

~~~text
DATABASE_URL=
SECRET_KEY=
~~~

The `.env.example` file is safe to commit and should be kept updated whenever new required environment variables are introduced.

## Secrets Policy

The following values must never be committed to the repository:

- API keys
- Database passwords
- Authentication secrets
- Private tokens
- Encryption keys
- Production credentials
- Other confidential configuration values

Secrets must be provided through environment variables or an appropriate secret-management system.

## Git Policy

The `.env` file is excluded through `.gitignore`.

Developers must verify that sensitive files are not staged before committing.

If a secret is accidentally committed, it must be considered compromised and rotated/revoked immediately.

## Environment Separation

Development, testing, and production environments should use separate configuration values.

Production secrets must never be copied into development configuration files or committed to the repository.

## Current Environment Variables

No application-specific environment variables are currently required.

This section will be updated as the WhoIsIt backend, database, authentication, and deployment infrastructure are implemented.