
.PHONY: feature-catalog
feature-catalog:
	python3 scripts/render_feature_catalog.py

.PHONY: coherence-pr-comment
coherence-pr-comment:
	python3 scripts/coherence_pr_comment.py

.PHONY: version-sync
version-sync:
	python3 scripts/version_sync.py
