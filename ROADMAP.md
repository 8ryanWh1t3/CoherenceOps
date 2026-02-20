# Roadmap

## v0.4.0 (current)
- [x] Drift-to-Patch money demo + fixtures + 10-min script
- [x] Template adoption guide + `bin/coherence-adopt` placeholder replacement
- [x] Date-based auto IDs: `bin/coherence-new-dlr`, `bin/coherence-new-drift`
- [x] Decision and drift INDEX files
- [x] Weekly rollup workflow + `top_risks.md`
- [x] Executive health guide (`docs/EXECUTIVE_README.md`)
- [x] Enterprise hardening: expanded CODEOWNERS, branch protection guide
- [x] Waiver gate (Gate 5) with expiry enforcement
- [x] PR template with waiver fields

## v0.3.0
- [x] Drift auto-detection from assumption expiry (scheduled workflow → auto-open DRIFT issues)
- [x] CODEOWNERS integration for canon files
- [x] Coherence score badge for README
- [x] Label bootstrap (auto-create `major`, `assumption-waiver`, `coherence-dashboard`)
- [x] `coherence init` setup script (bootstrap folder structure + templates into any repo)
- [x] `coherence check` local validator (run gates locally before pushing)
- [x] Release automation (tag + GitHub Release from CI)

## v0.2.0
- [x] GitHub Actions: DLR enforcement on major PRs
- [x] GitHub Actions: assumption expiry warnings
- [x] GitHub Actions: canon changelog enforcement
- [x] GitHub Actions: drift format validation
- [x] Automated coherence score calculation
- [x] Dashboard issue (auto-generated summary)

## v0.1.0
- [x] Folder structure and templates
- [x] Seed DLR, drift, canon, intel files
- [x] Documentation and training assets
- [x] PR and issue templates
- [x] Coherence Score specification

## v0.5.0
- Reusable composite actions (`uses: 8ryanWh1t3/CoherenceOps/.github/actions/...`)
- Historical score trending via commit metadata

## v0.6.0
- Cross-repo coherence federation (shared canon references, upstream discovery, auth model)

## Release Checklist

- [ ] All templates render correctly on GitHub
- [ ] One-click "Create New" links work (replace ORG/REPO)
- [ ] Issue templates appear in GitHub issue picker
- [ ] PR template auto-loads on new PRs
- [ ] CHANGELOG updated
- [ ] Version bumped in README
- [ ] Tag created: `git tag v0.x.0 && git push --tags`
