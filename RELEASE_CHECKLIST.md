# Release Candidate Checklist

All items must pass before tagging a new release.

## CI Gates

- [ ] Major PR without DLR — gate **fails** (Gate 1)
- [ ] Canon change without changelog entry — gate **fails** (Gate 3)
- [ ] Expired assumption — gate **fails** (Gate 2)
- [ ] Waiver label without `WAIVER:` reason + `WAIVER-EXPIRY:` date — gate **fails** (Gate 5)
- [ ] Drift format validation catches malformed drift files (Gate 4, non-blocking warn)

## Sample Mode

- [ ] `COHERENCE_ROOT=sample_data/game_studio_aaa bin/coherence-check` runs clean
- [ ] `COHERENCE_ROOT=sample_data/game_studio_aaa bin/coherence-root` validates root
- [ ] Workflow dispatch with `coherence_root=sample_data/game_studio_aaa` completes (score + rollup)
- [ ] Outputs written to `telemetry_out/sample_data_game_studio_aaa/` — **no writes into `sample_data/`**
- [ ] `bin/coherence-new-dlr` and `bin/coherence-new-drift` refuse to run when `COHERENCE_ROOT != coherence`

## Telemetry & Dashboard

- [ ] Coherence Score workflow runs and commits `coherence_score.json` + `coherence_badge.json`
- [ ] Dashboard issue created/updated with score breakdown
- [ ] Weekly rollup workflow commits `weekly_rollup.json` + `top_risks.md`
- [ ] README badge resolves (shields.io endpoint)

## Documentation

- [ ] `docs/SAMPLE_MODE.md` matches current COHERENCE_ROOT / TELEMETRY_OUT_DIR behavior
- [ ] `docs/DEMO_DRIFT_TO_PATCH.md` walkthrough still works end-to-end
- [ ] `docs/GATE_TEST_PLAYBOOK.md` gate triggers match workflow logic
- [ ] `CHANGELOG.md` has entry for this version
- [ ] `README.md` version string matches tag

## Version Consistency

- [ ] `bin/coherence-init` version string matches
- [ ] `bin/coherence-check` version string matches
- [ ] `bin/coherence-adopt` version string matches
- [ ] `coherence/telemetry/coherence_score.json` version field matches
- [ ] `coherence-score.yml` writes correct version in score JSON
