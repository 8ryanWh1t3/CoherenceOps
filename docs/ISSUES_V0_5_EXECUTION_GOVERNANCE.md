# v0.5 Issue Specs - Execution Governance

This document defines issue-ready implementation items for moving from workflow-level checks to execution-bound governance infrastructure.

## ISSUE 1 - Fail-Closed Structural Refusal Gate in CI

### Problem
Current checks validate governance signals, but refusal behavior is not uniformly fail-closed across all binding paths.

### Deliverable
Add a mandatory gate that blocks merge/deploy when authority, refusal path, or required evidence is missing.

### Acceptance Criteria
- A shared gate step returns hard fail for missing authority/evidence/refusal wiring.
- Workflow cannot proceed on warning-only mode for binding actions.
- Branch protection requires the fail-closed check.

### Target Files
- `.github/workflows/coherence-gates.yml`
- `.github/workflows/release.yml`
- `docs/CI_INSTALLATION.md`

## ISSUE 2 - Execution-Time Evidence Contract

### Problem
Evidence is partially present but not formally required as a precondition to action.

### Deliverable
Define required execution-time evidence fields and enforce presence at decision binding.

### Acceptance Criteria
- New schema document for evidence contract.
- Gate validates contract fields before merge/deploy.
- Missing fields produce deterministic block with actionable error message.

### Target Files
- `docs/GOVERNANCE_EVIDENCE_SCHEMA.md` (new)
- `.github/workflows/coherence-gates.yml`
- `scripts/coherence_pr_comment.py`

## ISSUE 3 - Refusal Authority Matrix Template

### Problem
Refusal authority exists socially but is not consistently encoded as a machine-checkable artifact.

### Deliverable
Add an authority matrix template that maps decision class -> who can refuse -> legal/policy basis.

### Acceptance Criteria
- Template exists with required fields and examples.
- Gate checks that major decision paths reference a valid authority entry.
- Documentation describes ownership and update cadence.

### Target Files
- `coherence/canon/REFUSAL_AUTHORITY_MATRIX.md` (new)
- `docs/PRINCIPLES.md`
- `.github/workflows/coherence-gates.yml`

## ISSUE 4 - Structural Pause Before Irreversible Actions

### Problem
Irreversible actions may proceed without explicit pause/hold semantics.

### Deliverable
Implement mandatory pause checkpoint for protected merge/deploy paths.

### Acceptance Criteria
- Protected actions require explicit pause approval step.
- Pause approvers are tied to authority matrix.
- Bypass path is disallowed or logged as policy violation.

### Target Files
- `.github/workflows/coherence-gates.yml`
- `.github/workflows/release.yml`
- `docs/BRANCH_PROTECTION.md`

## ISSUE 5 - Binding-Time Control Plane Spec

### Problem
CoherenceOps defines governance patterns but lacks a formal control-plane architecture spec above model/runtime components.

### Deliverable
Write a control-plane specification that defines execution routing, authority checks, refusal semantics, and evidence emission interfaces.

### Acceptance Criteria
- Architecture doc with components, interfaces, and decision sequence.
- Clear boundary between telemetry, supervision, and governance enforcement.
- MVP implementation path mapped to existing CI and repo artifacts.

### Target Files
- `docs/EXECUTION_CONTROL_PLANE_SPEC.md` (new)
- `docs/RUNTIME_GOVERNANCE_ENGINEERING.md`
- `docs/RUNTIME_GOVERNANCE_ENGINEERING_PART_II.md`
