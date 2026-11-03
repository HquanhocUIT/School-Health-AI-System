# Contributing

This team uses Scrum with Jira as the source of truth for the product backlog, sprint goal, acceptance criteria, and work status. GitHub supports the team's short feedback loop: small changes, continuous integration, teammate review, and frequent integration into `main`.

## Start from Jira

1. Pick up a Jira story or task selected for the current Sprint.
2. Confirm its goal and acceptance criteria with the Product Owner or team when anything is unclear.
3. Keep implementation within the agreed scope. Record scope changes in Jira and re-plan with the team instead of quietly expanding the pull request.
4. Break work into reviewable increments. Keep Jira status and blockers visible as work progresses.

## Branches

Create one short-lived branch from the latest `main` for a Jira story or focused task. Include its Jira key in the branch name:

```text
feature/SCRUM-123-student-profile
fix/SCRUM-124-excel-validation
docs/SCRUM-125-ai-rules
chore/SCRUM-126-ci-maintenance
```

Do not commit directly to `main` or keep long-lived sprint branches. Merge completed increments promptly; if a story is unfinished, keep it open in Jira and do not mark it Done.

## Commits

Use short, action-oriented messages with a conventional prefix and Jira key:

```text
feat(SCRUM-123): add student health profile
fix(SCRUM-124): reject duplicate Excel rows
docs(SCRUM-125): clarify AI use rules
chore(SCRUM-126): configure CI workflow
```

## Pull requests

Open a pull request from the short-lived branch to `main`. Keep it focused on the Jira item and small enough for a teammate to review in one sitting.

Before merging:

1. Link the Jira item and explain how the change meets its acceptance criteria.
2. Confirm the Definition of Done is met: implementation is complete, relevant checks pass, documentation is updated where needed, and no secrets or real student health data are included.
3. Wait for CI to pass and at least one teammate to approve the pull request.
4. Resolve review conversations and incorporate feedback before merging.
5. Prefer squash merging so each Jira item lands as a clear, traceable change; delete the short-lived branch after merge.

See the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) and [`AI_RULES.md`](AI_RULES.md). After merge, update Jira to reflect the actual state of the work. Only move an item to Done when its acceptance criteria and the team's Definition of Done are met.

## CI and local checks

GitHub Actions runs the available backend and frontend checks on pushes and pull requests. Run the relevant checks locally before requesting review. The current commands are documented in the [README](README.md); they become runnable as application code and dependencies are added.

## Data and secrets

- Use synthetic student records only in development, tests, screenshots, and demos.
- Never commit real health data, passwords, API keys, tokens, or local environment files.
- Do not include sensitive information in Jira comments, commit messages, logs, or screenshots.
