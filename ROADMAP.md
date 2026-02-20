# Roadmap

## v0.1.0 (current)
- Folder structure and templates
- Seed DLR, drift, canon, intel files
- Documentation and training assets
- PR and issue templates
- Coherence Score specification

## v0.2.0
- GitHub Actions: DLR enforcement on major PRs
- GitHub Actions: assumption expiry warnings
- Automated coherence score calculation
- Dashboard issue (auto-generated summary)

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
