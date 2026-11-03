# AI Use Rules

These rules apply to AI-assisted development and to AI features in SchoolHealth. They follow the project team's agreement to review AI-generated work, protect project data, and keep clinical decisions with healthcare professionals.

## 1. Protect student and project data

- Use synthetic student records in development, tests, screenshots, and demos.
- Never paste real student names, contact details, health records, checkup results, or other identifying information into an AI prompt.
- Do not send confidential project data, credentials, API keys, access tokens, or private repository content to an AI service.
- Treat local models and AI tools as untrusted unless the team has explicitly reviewed their data handling. Running a model locally does not make real student data safe to use.
- Keep secrets in local environment files or an approved secret store. Commit only placeholder examples such as `.env.example`.

## 2. Review AI-generated code and content

- Understand generated code before adding it to the project. Check correctness, security, licensing, dependencies, and consistency with the existing design.
- Run the relevant tests and checks before proposing a merge. Add tests for new behavior where practical.
- Verify facts, calculations, references, and health-related wording against reliable sources. AI output can be incomplete, biased, or incorrect.
- Do not present generated content as verified unless a team member has checked it.

## 3. Keep clinical decisions with healthcare professionals

- AI may explain health information in plain language and offer general nutrition suggestions. It must not diagnose, prescribe medication, or replace a healthcare professional's judgment.
- Make the limits of AI assistance clear to users. Route clinical questions or concerning results to qualified school health staff or another appropriate healthcare professional.
- Do not use AI output alone to make decisions about a student's care, access, eligibility, or priority for follow-up.
- Have a qualified healthcare professional review health prompts, response templates, and user-facing health guidance before release.

## 4. Build AI features with safeguards

- Enforce authentication, authorization, and data validation in application code. Never rely on an AI response to grant access or authorize an action.
- Treat model output as untrusted input: validate its format, escape it before display, and do not execute code, SQL, or tool instructions returned by a model.
- Test normal, ambiguous, out-of-scope, and adversarial prompts. Include checks that the feature does not expose another student's information or make unsupported clinical claims.
- If a feature uses approved reference material, keep its source and version identifiable so the team can review the basis for its answers.

## 5. Be transparent and accountable

- Tell users when content is generated or materially assisted by AI.
- A team member remains responsible for code or content submitted for review, even when AI helped create it.
- Mention significant AI assistance in the pull request when it affects implementation or user-facing behavior, so reviewers know what to examine.
- Report unsafe or misleading output to the team and fix or disable the affected behavior before release.
