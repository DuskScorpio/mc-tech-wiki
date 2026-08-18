# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-08-18] create | Wiki initialized (tree-farm focus)
- Domain: Technical Minecraft tree farms, Java 1.20.1, GTMC source
- Vault path: `C:\GitHub Related\mc-tech-wiki`
- Wrote SCHEMA.md (edition/version/confidence provenance rules)
- Ingested 8 GTMC tree-farm pages into raw/articles/ (sha256 computed for drift detection)
- Compiled 16 concept pages from sources:
  tree-farm-overview, mc-timing-model, updates-nc-pp, piston-action-timing,
  trunk-processing, leaf-processing, bonemealing, sapling-recycling, block-to-drop,
  detection-methods, 0-tick, dustless-wiring, tree-species-requirements,
  multi-species-tree-farm, 4gt-tree-farm, large-spruce-tree-farm
- Wrote index.md and this log.md
- Not yet done: GTMC ch.06 (URL not fetched), detailed timing tables, example-world ZIPs

## [2026-08-18] ingest | Dark oak growth mechanics (Bilibili) + Minecraft Wiki cross-check
- Ingestion source: https://www.bilibili.com/opus/1031059770508836903 (Scorpio 深色橡木生长机制, edited 2025-02-09, Java ~1.21.x)
- web_extract succeeded on retry; browser load failed (Chrome remote-debugging approval prompt) — noted, not blocking
- Wrote raw/articles/bilibili-dark-oak-growth.md (Chinese original, sha256 tracked)
- Compiled concepts/dark-oak-growth-mechanics.md (edition:java, version:1.21, confidence:high)
- Corroborated shared facts against Minecraft Wiki (minecraft.wiki/w/Dark_Oak, /w/Sapling, /w/Tree):
  * 2x2 NW-corner requirement + 3x3 column >=7 above NW + 5x5 top-3-layers — MATCHES
  * sapling drop 1/20, jungle 1/40 — MATCHES GTMC (already in leaf-processing.md)
  * minor divergence: Wiki says dark oak "typically 6-8" tall; Bilibili code range is 6-9 — recorded on page, not contested (Wiki is loose wording)
- Translation reference adopted: https://github.com/Youmiel/TechMCTranslationWorkflow (will consult before asking user for CN translation)
- Updated index.md (new page + raw entry) and tree-species-requirements.md (dark oak row expanded)

