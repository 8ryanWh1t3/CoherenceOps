# Roadmap

## v0.4.3 (current)
- [x] Feature + Category Catalog source of truth (`coherence/telemetry/feature_catalog.json`)
- [x] Feature Catalog renderer (`docs/FEATURE_CATALOG.md` via `scripts/render_feature_catalog.py`)
- [x] PR comment artifact generator (`release_kpis/COHERENCE_PR_COMMENT.md`)
- [x] Outer-edge boundaries doc (`docs/OUTER_EDGE_BOUNDARIES.md`)
- [x] Single-source version sync helper (`VERSION` + `scripts/version_sync.py`)
- [x] Make targets for `version-sync`, `feature-catalog`, `coherence-pr-comment`
- [x] Workflow wiring for catalog + PR-comment artifact generation
- [x] Automation boundaries language (coding vs engineering distinction)
- [x] Runtime Governance Engineering (Part I): Pre-Execution Authority Gate
- [x] Runtime Governance Engineering (Part II): moment-of-binding, structural refusal, fail-closed
- [x] Five Preconditions for Production Governance (intent, literacy, traceability, criteria, stop authority)

## Issue Roadmap Alignment (v0.4.3)

Completed and ready to reference in issue tracker:
- [x] `ISSUE: Feature Catalog as authoritative governance inventory`
- [x] `ISSUE: Coherence Gate Summary artifact for PR automation`
- [x] `ISSUE: Outer-edge boundaries and explicit non-claims`
- [x] `ISSUE: Version single-source-of-truth + sync utility`
- [x] `ISSUE: Runtime Governance Engineering Part I (pre-execution authority)`
- [x] `ISSUE: Runtime Governance Engineering Part II (moment-of-binding + fail-closed)`
- [x] `ISSUE: Automation boundaries (coding outlier vs organizational decision work)`
- [x] `ISSUE: Five preconditions for production behavior control added to runtime governance guidance`

Next issues to open (v0.5.0 execution track):
- [ ] `ISSUE: Enforce fail-closed structural refusal gate in CI policy checks`
- [ ] `ISSUE: Require execution-time evidence fields for binding decisions`
- [ ] `ISSUE: Add explicit refusal authority matrix template (who can block, under what authority)`
- [ ] `ISSUE: Add structural pause checkpoint before irreversible merge/deploy actions`
- [ ] `ISSUE: Publish governance evidence schema for non-reconstructive incident review`

Issue specs: `docs/ISSUES_V0_5_EXECUTION_GOVERNANCE.md`

## v0.4.0
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
- Execution governance implementation track (fail-closed refusal, authority matrix, structural pause, evidence contract, control-plane spec)
- Agnostic Executive Control Plane (ECP) definition:
  - authority routing model
  - execution gating model
  - reasoning validation contract
  - cross-domain oversight boundaries
- ECP MVP integration across existing CI/workflow binding points

## v0.6.0
- Cross-repo coherence federation (shared canon references, upstream discovery, auth model)
- ECP expansion beyond CI:
  - multi-agent orchestration policy hooks
  - human-in-the-loop authority checkpoints
  - vendor/model-agnostic governance adapters

## Release Checklist

- [ ] All templates render correctly on GitHub
- [ ] One-click "Create New" links work (replace ORG/REPO)
- [ ] Issue templates appear in GitHub issue picker
- [ ] PR template auto-loads on new PRs
- [ ] CHANGELOG updated
- [ ] Version bumped in README
- [ ] Tag created: `git tag v0.x.0 && git push --tags`
