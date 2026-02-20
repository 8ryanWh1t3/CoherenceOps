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
- Canon diff detection (alert when canon files change without changelog entry)
- Drift auto-detection from assumption expiry
- Cross-repo coherence federation (shared canon references)

## v0.4.0
- CODEOWNERS integration for canon files
- Coherence score badge for README
- Historical score trending via commit metadata

## Release Checklist

- [ ] All templates render correctly on GitHub
- [ ] One-click "Create New" links work (replace ORG/REPO)
- [ ] Issue templates appear in GitHub issue picker
- [ ] PR template auto-loads on new PRs
- [ ] CHANGELOG updated
- [ ] Version bumped in README
- [ ] Tag created: `git tag v0.x.0 && git push --tags`
