# Vault todo

## Done
- Check all raw and make sure aligns with source, no contamination. DONE 2026-08-20: 6 raw files had injected annotations + [[wikilinks]] stripped; 0/37 raw + 0/31 concept problems verified.
- Footnote rollout (option A). DONE 2026-08-20: all 31 concept files repointed; every [^id]: def points to local raw/articles/<id>.md (0 URL defs, 0 dangling). Downloaded the 2 missing Minecraft Wiki mirrors (mcwiki-dark-oak, mcwiki-tree-farming). Full vault lint: 0/37 raw + 0/31 concept problems.

## Rebuild on `raw-only` branch (IN PROGRESS)
Branch set up: `raw-only` from master, concepts/ stripped, raw/ + linter + hook + SCHEMA kept. master = 31-concept backup.

Workflow rule: build concept pages one at a time, faithful to sources (SCHEMA Claim-to-source rule). It is FINE to leave a concept page unlinked from the hub and connect it later — the linter does NOT require concept->concept links, only raw->concept. So: write the page, commit it standalone, wire it into the hub's "Built concept pages" list whenever convenient. Do not forward-link (/concepts/x.md) to pages not built yet.

Done so far: tree-farm.md (hub), tree-farm-detection.md.

Build queue (raw source articles, each -> its own concept):
- tree-farm-basics
- tree-farm-simple-design
- tree-farm-high-speed
- tree-farm-4gt
- tree-farm-multi-species
- tree-farm-large-spruce
- tree-farm-dustless-wiring
- then non-tree-farm areas (timing, piston, block-nature, etc.) as their sources allow

Guardrail: vault_lint.py pre-commit hook blocks HIGH/MED (raw purity, sha256, strict YAML, OKF, footnote formatting/clickability, source->concept graph). claim_audit.py = optional manual aid for citation accuracy. LOW "not built yet" warnings are expected during rebuild.
