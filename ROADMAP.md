# Roadmap

## v0.2.0 (current)
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

## v0.3.0
- Drift auto-detection from assumption expiry (scheduled workflow → auto-open DRIFT issues)
- CODEOWNERS integration for canon files
- Coherence score badge for README
- Label bootstrap (auto-create `major`, `assumption-waiver`, `coherence-dashboard`)

## v0.4.0
- Cross-repo coherence federation (shared canon references)
- Historical score trending via commit metadata
- Reusable composite actions for adoption by other repos

## Release Checklist

- [ ] All templates render correctly on GitHub
- [ ] One-click "Create New" links work (replace ORG/REPO)
- [ ] Issue templates appear in GitHub issue picker
- [ ] PR template auto-loads on new PRs
- [ ] CHANGELOG updated
- [ ] Version bumped in README
- [ ] Tag created: `git tag v0.x.0 && git push --tags`
