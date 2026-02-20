# Architecture Commitments

## Core Principles

1. **GitHub-native** — Everything runs on GitHub: Markdown, YAML, Issues, PRs, Actions. No external dependencies required.

2. **Folder-first** — Governance state lives in `coherence/` as plain files. Any tool that reads a filesystem can process it.

3. **Template-driven** — Humans create records via pre-filled templates. One-click links reduce friction to near zero.

4. **Version-controlled** — Every decision, claim, assumption, and drift signal is a git commit. Immutable by default.

5. **Score-observable** — Coherence health is measurable via a simple 0-100 score derived from coverage, currency, and retrieval metrics.

## Structural Decisions

| Decision | Rationale |
|----------|-----------|
| YAML for intel, Markdown for everything else | YAML is machine-parseable for automation; Markdown is human-readable for review |
| Flat numbering (DLR-0001, DRIFT-0001) | Simple, sequential, grep-friendly |
| Changelog in canon, not git log | Git log is noisy; a curated changelog shows intent, not just diffs |
| No database | Files in a repo are the database. Git is the audit log. |

## Boundaries

- CoherenceOps does NOT execute code or run agents
- CoherenceOps does NOT require a server or SaaS account
- CoherenceOps CAN be extended with GitHub Actions for enforcement
