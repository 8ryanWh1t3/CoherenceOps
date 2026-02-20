# Changelog

All notable changes to CoherenceOps are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/).

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
