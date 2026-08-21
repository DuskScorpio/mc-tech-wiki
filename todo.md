# Vault todo

## Done
- Check all raw and make sure aligns with source, no contamination. DONE 2026-08-20: 6 raw files had injected annotations + [[wikilinks]] stripped; 0/37 raw + 0/31 concept problems verified.
- Footnote rollout (option A). DONE 2026-08-20: all 31 concept files repointed; every [^id]: def points to local raw/articles/<id>.md (0 URL defs, 0 dangling). Downloaded the 2 missing Minecraft Wiki mirrors (mcwiki-dark-oak, mcwiki-tree-farming). Full vault lint: 0/37 raw + 0/31 concept problems.

## Rebuild on `raw-only` branch (IN PROGRESS)
Branch set up: `raw-only` from master, concepts/ stripped, raw/ + linter + hook + SCHEMA kept. master = 31-concept backup.

Workflow rule: build concept pages one at a time, faithful to sources (SCHEMA Claim-to-source rule). It is FINE to leave a concept page unlinked from the hub and connect it later — the linter does NOT require concept->concept links, only raw->concept. So: write the page, commit it standalone, wire it into the hub's "Built concept pages" list whenever convenient. Do not forward-link (/concepts/x.md) to pages not built yet.

Done so far: tree-farm.md (hub), tree-farm-detection.md.

PRINCIPLE — PER-TREE-TYPE PAGES: every tree type gets at least one dedicated
growth-mechanics page, because growth mechanics differ substantially (space/light
rules, 2x2 grid logic, bone-meal behavior, special cases). A shared
`tree-growth-mechanics` page holds the COMMON mechanics (growth probability,
bone-meal, light/space checks) and LINKS OUT to each per-type page — it does
not repeat per-type specifics. Per-type pages are GROWTH-ONLY (space/light/
bone-meal/special-case); farm design lives on the design/farm pages.

Per-type page set (naming: <type>-growth):
- 1x1: oak-growth, birch-growth, spruce-growth (1x1), jungle-growth (pre-1.14
  height-increase detection), acacia-growth (pre-1.14), cherry-growth,
  azalea-growth, mangrove-growth (underwater + propagule-from-leaves, Minecraft Wiki)
- 2x2: dark-oak-growth (2x2 grid, can't grow alone, Fortune sapling economy),
  large-spruce-growth (3x3->5x5 detection range, retractable wall, double recursion)
- shared: tree-growth-mechanics (common rules; links to all per-type pages)

Source mapping per type: GTMC basics + Minecraft Wiki Sapling for general;
gtmc-tree-farm-large-spruce for large spruce; bilibili-dark-oak-growth(+en) for
dark oak; mcwiki-tree-farming for mangrove; mcwiki-dark-oak for 2x2 grid rule.

Source material available to draw from (NOT a 1:1 page list — regroup as above):
- GTMC tree-farm series: basics, simple-design, high-speed, 4gt, multi-species, large-spruce, dustless-wiring
- Minecraft Wiki: Tree farming, Sapling, Dark Oak, (Mangrove — cite via Tree farming)
- Bilibili: dark-oak-growth (CN + EN translation)
- Then non-tree-farm areas (timing, piston, block-nature, etc.) as their sources allow

Guardrail: vault_lint.py pre-commit hook blocks HIGH/MED (raw purity, sha256, strict YAML, OKF, footnote formatting/clickability, source->concept graph). claim_audit.py = optional manual aid for citation accuracy. LOW "not built yet" warnings are expected during rebuild.
