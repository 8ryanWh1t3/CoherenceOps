# Changelog

All notable changes to CoherenceOps are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.4.0] - 2026-02-20

### Added
- Drift-to-Patch money demo (`docs/DEMO_DRIFT_TO_PATCH.md`) + 10-min script + demo fixtures
- Template adoption guide (`TEMPLATE_ADOPTION.md`) + checklist + `bin/coherence-adopt`
- Date-based ID tools: `bin/coherence-new-dlr`, `bin/coherence-new-drift`
- Decision and drift INDEX files (`coherence/decisions/INDEX.md`, `coherence/drift/INDEX.md`)
- Weekly rollup workflow (`coherence-weekly-rollup.yml`) + `top_risks.md`
- Executive health guide (`docs/EXECUTIVE_README.md`)
- Branch protection guide (`docs/BRANCH_PROTECTION.md`)
- PR template with DLR checklist and waiver fields
- Gate 5: Waiver validation — enforces `WAIVER:` reason + `WAIVER-EXPIRY:` date

### Changed
- CODEOWNERS expanded to cover `bin/` directory
- DLR regex in score workflow widened to accept plain IDs and date-based formats
- README quick links expanded with demo, playbook, executive guide, adoption checklist

## [0.3.0] - 2026-02-20

### Added
- Drift auto-detection workflow — auto-opens GitHub issues for expired assumptions
- CODEOWNERS file — canon, intel, and workflow files require maintainer review
- Coherence score badge in README (shields.io endpoint)
- Label bootstrap workflow — one-click creation of all required labels
- `bin/coherence-init` — bootstrap CoherenceOps into any repo (bash, zero deps)
- `bin/coherence-check` — run coherence gates locally before pushing (bash, zero deps)
- Release automation workflow — GitHub Releases from version tags

### Changed
- `coherence-score.yml` now also generates `coherence_badge.json` for the README badge

## [0.2.0] - 2026-02-20

### Added
- GitHub Actions: `coherence-gates.yml` — 4 PR validation gates
  - Gate 1: DLR required for major PRs
  - Gate 2: Assumption expiry check (warn 14d, block expired)
  - Gate 3: Canon changelog enforcement
  - Gate 4: Drift format validation (non-blocking)
  - Consolidated summary comment on PRs
- GitHub Actions: `coherence-score.yml` — automated weekly score calculation
  - Reads assumptions, drift, PR data to compute 4-component score
  - Commits updated `coherence_score.json` on schedule
  - Creates/updates pinned "Coherence Dashboard" issue

## [0.1.0] - 2026-02-20

### Added
- Initial repo structure: intel, decisions, canon, drift, telemetry
- DLR template and DLR-0001 seed record
- Drift template and DRIFT-0001 seed signal
- Canon seed files: mission, architecture, public-commitments
- Claims and assumptions YAML with half-life tracking
- PR template with DLR/assumption/canon/drift checkpoints
- GitHub Issue templates for decisions and drift (YAML forms)
- Coherence Score specification (0-100)
- Policy logic documentation for CI gates
- One-page Quick Start, 30-min training outline, swim lane diagram
- Principles and glossary documentation
- One-click "Create New" links in folder READMEs
