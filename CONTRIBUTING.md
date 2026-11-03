# Contributing

This repository follows the team's Jira workflow and review agreement. The `main` branch is the shared integration branch.

## Branches

Create a short-lived branch for each Jira work item. Use one of these prefixes:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
chore/<short-description>
```

Examples: `feature/student-profile`, `fix/excel-validation`, `docs/ai-rules`.

Do not commit directly to `main`. Keep each branch focused and sync it with the latest `main` before merging.

## Commits

Use a short, action-oriented commit message. A conventional prefix is recommended:

```text
feat: add student health profile
fix: reject duplicate Excel rows
docs: document AI use rules
chore: configure CI workflow
```

## Pull requests

1. Open a pull request from your branch to `main` and include the related Jira key, such as `SCRUM-15`.
2. Explain what changed and how you checked it. Link screenshots for visible UI changes when useful.
3. Wait for CI to pass and at least one teammate to approve the pull request.
4. Resolve review comments and conversations before merging.
5. Merge only work that meets the team's Definition of Done.

Use the pull request template and check the data safety and AI-use items where relevant. See [`AI_RULES.md`](AI_RULES.md) for project-specific AI guidance.

## Checks

The GitHub Actions workflow runs the available backend and frontend checks on pushes and pull requests. Run the relevant checks locally before requesting review. Current commands are documented in the [README](README.md); they become runnable as the application code and dependencies are added.

## Data and secrets

- Use synthetic student records only in development and demos.
- Never commit real health data, passwords, API keys, tokens, or local environment files.
- Do not include sensitive information in commit messages, issue references, logs, or screenshots.
