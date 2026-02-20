# CI Installation Contract

> Single-page reference for installing CoherenceOps as a CI tool in your repository.

## Required Permissions

Your workflows need these permissions in their `permissions:` block:

| Permission | Used By | Why |
|---|---|---|
| `contents: read` | coherence-gates | Read files, assumptions, drift |
| `contents: write` | coherence-score, weekly-rollup | Commit telemetry JSON to repo |
| `pull-requests: write` | coherence-gates | Post summary comment on PRs |
| `checks: write` | coherence-gates | Report gate pass/fail status |
| `issues: write` | coherence-score, drift-auto-detect | Create/update dashboard issue, open drift issues |

If your org uses a restricted `GITHUB_TOKEN`, ensure these permissions are allowed at the org or repo level under **Settings > Actions > General > Workflow permissions**.

### Token Requirements

All workflows use the default `GITHUB_TOKEN`. No personal access token (PAT) is required unless:

- You have branch protection rules that block pushes from `github-actions[bot]` — in this case, set `commit_results: 'false'` (see [Scheduled Commits](#scheduled-commits)) or create a PAT with `contents: write` and pass it as a secret.

## Required Labels

CoherenceOps gates and workflows check for these labels:

| Label | Used By | Purpose |
|---|---|---|
| `major` | Gate 1 (DLR Required) | Marks a PR as major (DLR required) |
| `assumption-waiver` | Gate 2 (Assumption Expiry) | Waives expired-assumption gate failure |
| `coherence:waiver` | Gate 5 (Waiver Validation) | General coherence waiver (requires reason + expiry in PR body) |
| `coherence-dashboard` | coherence-score | Identifies the pinned dashboard issue |
| `drift` | drift-auto-detect | Tags auto-opened drift issues |
| `auto-detected` | drift-auto-detect | Tags auto-opened drift issues |

### Creating Labels

Run the label bootstrap workflow:

```bash
gh workflow run label-bootstrap.yml
```

Or create labels manually:

```bash
gh label create "major" --color "D93F0B" --description "Major PR — DLR required"
gh label create "assumption-waiver" --color "FBCA04" --description "Waive expired assumption gate"
gh label create "coherence:waiver" --color "FBCA04" --description "General coherence waiver"
gh label create "coherence-dashboard" --color "0E8A16" --description "Coherence dashboard issue"
gh label create "drift" --color "E4E669" --description "Drift signal"
gh label create "auto-detected" --color "C5DEF5" --description "Auto-detected by CI"
```

## Branch Protection

### Recommended Settings

Under **Settings > Branches > Branch protection rules** for your default branch:

| Setting | Recommended | Notes |
|---|---|---|
| Require pull request reviews | Yes | Ensures DLR gate runs before merge |
| Require status checks to pass | Yes | Add `Coherence Gates` as required |
| Require branches to be up to date | Optional | Useful but slows merge queue |
| Restrict who can push | Optional | If enabled, allow `github-actions[bot]` for telemetry commits |

### CODEOWNERS

CoherenceOps ships a `CODEOWNERS` file requiring maintainer review for:

- `coherence/canon/**` — canon changes need sign-off
- `coherence/intel/**` — assumption/claim changes need sign-off
- `.github/workflows/**` — workflow changes need sign-off
- `bin/**` — tool changes need sign-off

## Scheduled Commits

The `coherence-score` and `coherence-weekly-rollup` workflows commit telemetry JSON directly to the default branch on their schedule (Monday 9:00 UTC by default).

### Implications

- Commits come from `github-actions[bot]` — they bypass PR requirements
- Commits include `[skip ci]` in the message — they don't trigger other workflows
- If branch protection blocks pushes from bots, the commit step will fail silently

### Opting Out

Set `commit_results: 'false'` when triggering manually:

```bash
gh workflow run coherence-score.yml -f commit_results=false
```

For scheduled runs, fork the workflow and change the default:

```yaml
inputs:
  commit_results:
    default: 'false'
```

When commits are disabled, telemetry is still calculated and output to workflow logs. The dashboard issue is still updated (it uses the GitHub API, not a commit).

## Verify Your Setup

Run this checklist after installation:

- [ ] `coherence/intel/assumptions.yaml` exists (run `bin/coherence-init` if not)
- [ ] `coherence/drift/` directory exists
- [ ] `coherence/decisions/` directory exists
- [ ] `coherence/canon/` directory exists
- [ ] Labels created (run `gh workflow run label-bootstrap.yml`)
- [ ] `bin/coherence-check` passes locally: `./bin/coherence-check`
- [ ] Open a test PR touching >10 files — verify `Coherence Gates` check appears
- [ ] Run `gh workflow run coherence-score.yml` — verify dashboard issue created
- [ ] If using branch protection: verify `Coherence Gates` is listed as a required check
