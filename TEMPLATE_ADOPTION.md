# Template Adoption Guide

Three ways to bring CoherenceOps into your repo.

---

## Option 1: Use This Template (Recommended)

1. Click **Use this template** on the [CoherenceOps repo](https://github.com/8ryanWh1t3/CoherenceOps)
2. Name your new repo
3. Run `bin/coherence-adopt` to replace placeholders:
   ```bash
   bin/coherence-adopt
   ```
4. Enable GitHub Actions in your repo settings
5. Run the label-bootstrap workflow:
   ```bash
   gh workflow run label-bootstrap.yml
   ```

## Option 2: Copy Into Existing Repo

```bash
git clone https://github.com/8ryanWh1t3/CoherenceOps.git /tmp/coherence-ops
cp -r /tmp/coherence-ops/coherence/ your-repo/coherence/
cp -r /tmp/coherence-ops/.github/ your-repo/.github/
cp -r /tmp/coherence-ops/bin/ your-repo/bin/
cp /tmp/coherence-ops/CODEOWNERS your-repo/CODEOWNERS
cd your-repo && bin/coherence-adopt
```

## Option 3: Git Submodule

```bash
git submodule add https://github.com/8ryanWh1t3/CoherenceOps.git coherence-ops
```

Then symlink or copy what you need. Note: workflows must live in `.github/workflows/` of the consuming repo to run.

---

## After Adoption

See [docs/ADOPTION_CHECKLIST.md](docs/ADOPTION_CHECKLIST.md) for the full setup checklist.
