# Branch Protection Recommendations

Configure these settings on your `main` branch for full governance enforcement.

## Required Status Checks

Enable **Require status checks to pass before merging** with:

- `Coherence Gates` (from `coherence-gates.yml`)

Optional but recommended:
- `Calculate Coherence Score` (from `coherence-score.yml`)
- `Weekly Rollup` (from `coherence-weekly-rollup.yml`)

## Required Reviews

- Require at least **1 approving review**
- Enable **Require review from Code Owners** (enforces CODEOWNERS rules)
- Restrict who can dismiss reviews to maintainers only

## Push Restrictions

- **Do not allow direct pushes** to `main`
- All changes must go through pull requests
- Consider enabling **Require linear history** for clean audit trails

## Waiver Policy

CoherenceOps supports a `coherence:waiver` label for exceptional cases:

1. Add the `coherence:waiver` label to the PR
2. Include in the PR body:
   ```
   WAIVER: [reason for bypassing governance]
   WAIVER-EXPIRY: YYYY-MM-DD
   ```
3. Gate 5 validates that both lines are present and expiry is in the future
4. Expired waivers are rejected automatically

## Setup Commands

```bash
# Via GitHub CLI (requires admin access)
gh api repos/{owner}/{repo}/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["Coherence Gates"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"require_code_owner_reviews":true}'
```

Or configure via **Settings > Branches > Branch protection rules** in the GitHub UI.
