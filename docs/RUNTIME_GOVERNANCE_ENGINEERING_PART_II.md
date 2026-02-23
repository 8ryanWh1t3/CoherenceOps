# Runtime Governance Engineering (Part II)

## Authority Transfer at the Moment of Binding

Most organizations do not lose control because they lack AI policy documents. They lose control when authority transfers quietly at the moment an output is accepted and acted on.

If a system can influence a decision and all of the following are absent, authority has already moved:

- Explicitly assigned refusal authority
- A required structural pause before commitment
- Execution-time evidence showing who could intervene and on what grounds

Undeclared authority becomes assumed authority. Assumed authority becomes permanent authority.

## Governance Is an Execution Condition

Governance is not a policy category. It is an execution condition.

Retrospective accountability is a sign that governance was reconstructed after the fact. Effective governance is inspectable during execution, before commitment.

## Five Preconditions for Production AI Governance

Within CoherenceOps scope (repo and workflow execution governance), production control requires all five:

1. Human-defined intent: decision intent is explicit in governing artifacts before execution.
2. Operational literacy: operators, reviewers, and approvers understand gate semantics and failure handling.
3. Tested, traceable workflows: binding paths are testable and leave auditable traces.
4. Transparent judgment criteria: pass/fail criteria are explicit, deterministic, and reviewable.
5. One named owner with stop authority: refusal authority is assigned and enforceable.

Missing any one of these turns governance into theater.

## Structural Refusal Requirements

For governance to exist at decision time, all three must be true:

1. Authority boundaries are technically bound to real decisions.
2. Refusal is a valid, enforceable, non-bypassable outcome.
3. Evidence is generated because action required it, not because someone later requested it.

Anything else is supervision.

- Supervision observes.
- Governance constrains.

## Fail-Closed Rule

At the moment of binding, inability to prove authority and refusal conditions must block progression by default.

- Unknown authority -> block
- Missing required evidence -> block
- Unmet refusal path -> block

This is fail-closed governance.

## Operating Test

At binding time, the system must answer without reconstruction:

- Who could refuse?
- Under what authority?
- What would have stopped this from proceeding?

If these cannot be shown in execution-time evidence, governance was never present.
