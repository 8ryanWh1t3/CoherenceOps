# Adoption Checklist

Complete these steps after copying or templating CoherenceOps into your repo.

## Setup

- [ ] Run `bin/coherence-adopt` to replace `ORG/REPO` placeholders
- [ ] Run the label-bootstrap workflow: `gh workflow run label-bootstrap.yml`
- [ ] Verify GitHub Actions are enabled in repo settings
- [ ] Update `CODEOWNERS` with your team's GitHub handles

## Branch Protection (Recommended)

- [ ] Require status checks: `Coherence Gates`
- [ ] Require pull request reviews (1+ reviewer)
- [ ] Restrict direct pushes to `main`

See [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md) for detailed recommendations.

## Personalize

- [ ] Edit `coherence/canon/mission.md` with your project's mission
- [ ] Edit `coherence/canon/architecture.md` with your architecture
- [ ] Edit `coherence/canon/public-commitments.md` with your API/SLA commitments
- [ ] Add your initial assumptions to `coherence/intel/assumptions.yaml`
- [ ] Update README.md badge URL to point to your repo

## Verify

- [ ] Open a test PR touching `coherence/canon/` — Gate 3 should fire
- [ ] Add `major` label — Gate 1 should require a DLR
- [ ] Run `bin/coherence-check` locally — all gates report
- [ ] Trigger coherence-score workflow: `gh workflow run coherence-score.yml`

## Optional

- [ ] Run the 10-minute demo with your team ([DEMO_DRIFT_TO_PATCH.md](DEMO_DRIFT_TO_PATCH.md))
- [ ] Schedule a 30-minute training session ([TRAINING_30MIN_OUTLINE.md](TRAINING_30MIN_OUTLINE.md))
