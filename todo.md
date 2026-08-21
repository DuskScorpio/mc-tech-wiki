# Vault todo

## Done
- Check all raw and make sure aligns with source, no contamination. DONE 2026-08-20: 6 raw files had injected annotations + [[wikilinks]] stripped; 0/37 raw + 0/31 concept problems verified.
- Footnote rollout (option A). DONE 2026-08-20: all 31 concept files repointed; every [^id]: def points to local raw/articles/<id>.md (0 URL defs, 0 dangling). Downloaded the 2 missing Minecraft Wiki mirrors (mcwiki-dark-oak, mcwiki-tree-farming). Full vault lint: 0/37 raw + 0/31 concept problems.

## Rebuild on `raw-only` branch (IN PROGRESS)
Branch set up: `raw-only` from master, concepts/ stripped, raw/ + linter + hook + SCHEMA kept. master = 31-concept backup.

Workflow rule: build concept pages one at a time, faithful to sources (SCHEMA Claim-to-source rule). It is FINE to leave a concept page unlinked from the hub and connect it later — the linter does NOT require concept->concept links, only raw->concept. So: write the page, commit it standalone, wire it into the hub's "Built concept pages" list whenever convenient. Do not forward-link (/concepts/x.md) to pages not built yet.

Done so far: tree-farm.md (hub), tree-farm-detection.md.

PRINCIPLE — we do NOT copy GTMC's structure: GTMC owns the *facts* (it is a raw
source we cite), but WE own the *organization*. We are NOT building one concept
per GTMC article in GTMC's teaching order, and we are NOT bound to GTMC's scope.
Concretely, when building from the raw sources we may: merge several GTMC articles
into one concept; split one GTMC article across several concepts (already done:
tree-farm-detection was extracted from basics/simple-design/4gt); rename pages to
our taxonomy (e.g. per-species pages instead of GTMC's design-framing); and ADD
pages GTMC lacks (mangrove, clock-vs-detection tradeoff, timing/NC-PP primer).
Non-GTMC sources (Minecraft Wiki, Bilibili) are pulled in where better or to fill
gaps. The Claim-to-source rule still applies: every assertion traces to a raw
mirror, regardless of which source it came from.

Source material available to draw from (NOT a 1:1 page list — regroup as above):
- GTMC tree-farm series: basics, simple-design, high-speed, 4gt, multi-species, large-spruce, dustless-wiring
- Minecraft Wiki: Tree farming, Sapling, Dark Oak, (Mangrove — cite via Tree farming)
- Bilibili: dark-oak-growth (CN + EN translation)
- Then non-tree-farm areas (timing, piston, block-nature, etc.) as their sources allow

Guardrail: vault_lint.py pre-commit hook blocks HIGH/MED (raw purity, sha256, strict YAML, OKF, footnote formatting/clickability, source->concept graph). claim_audit.py = optional manual aid for citation accuracy. LOW "not built yet" warnings are expected during rebuild.
