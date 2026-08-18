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
## [2026-08-18] ingest | GTMC mechanics backbone (7 articles) + Technical Minecraft Wiki check
- Ingested 7 GTMC foundational-mechanics articles into raw/articles/ (sha256 tracked):
  block-update (concepts/continuous/special), micro-timing (ticks/intra-tick), pistons, block-mechanics
- Compiled 7 concept pages: update-theory, continuous-updates, special-update-behaviors,
  tick-micro-timing, piston-mechanics, block-nature (pointer), plus prior dark-oak page
- Technical Minecraft Wiki (techmcdocs.github.io) checked: its GitHub repo (TechMCDocs/TechMCDocs.github.io)
  master branch contains ONLY the Jekyll scaffold (index.md, _includes, _layouts) — NO article markdown.
  So there is currently nothing to ingest from it. Logged; will re-check if user points at real article URLs.
- Noted: EN intra-tick page flagged "Outdated translation" (1 commit + 2 days lag) — version-sensitive tag applied.
- Updated SCHEMA taxonomy (added mechanics tags), index.md (concepts + raw lists), cross-linked pages.
- Total concept pages now 24, raw sources 16.

## [2026-08-18] ingest | TechMCDocs/pages (Technical Minecraft Wiki) — 2nd source, tree-farm-relevant
- Corrected earlier miss: real content repo is TechMCDocs/pages (not TechMCDocs.github.io, which is the Jekyll scaffold).
- Ingested 6 tree-farm-relevant pages (sha256 tracked): BlockUpdates, Piston, MovingBlock36,
  ZeroTickFarms, TileTicks, GameTick. (Skipped MobTick/UpdateSuppression/Blocks as out of scope.)
- Compiled/augmented concept pages: moving-block-b36 (new), zero-tick-farming-crops (new, with explicit
  distinction from the working redstone 0-tick generators), and cross-source notes on piston-mechanics,
  tick-micro-timing, update-theory.
- Cross-check outcome: TMWiki's NC/PP model, piston arrival (3gt), repeater/comparator delays, and phase
  order all ALIGN with GTMC. No contradictions found. Flagged: crop zero-tick is patched 1.16+ and is a
  DIFFERENT mechanic from the redstone 0-tick used in tree farms.
- Tagged new raw as source-tmwiki; concept pages carry both source-gtmc and source-tmwiki where corroborated.
- Total concept pages now 26, raw sources 22.

## [2026-08-18] tier-a lint + upgrade mc-timing-model from medium to high
- Tier A lint results: 2 medium-confidence pages (block-nature, mc-timing-model); 7 version-sensitive tags (expected);
  2 orphans (zero-tick-farming-crops, tree-farm-overview — both have outbound links but no inbound; acceptable, index links them).
  No broken wikilinks, all frontmatter complete.
- Read GTMC's full timing-theory chapters (intra-tick, scheduled-ticks, block-events, block-entities) — these SUPERSEDE
  the simplified "basics" page. Captured 4 new raw files (sha256 tracked).
- Upgraded [[mc-timing-model]] to confidence: high. Corrected the intra-tick phase order (was loosely AT→TT→BE→TE;
  now authoritative WTU→TT→CT→BE→EU→TE→AT, player input LAST). TMWiki GameTick corroborates. Added component phase
  table, BED/depth explanation (0t bottom-retraction base example), scheduled-tick execution order, 4gt-observer basis.
- Fixed stale phase-order references in tick-micro-timing.md and piston-mechanics.md (added correction notes).
- Upgrade [[block-nature]] to high: ingested GTMC block-mechanics sub-articles (blocks-and-states, block-changes); rewrote page with Block/BlockState model, palettes, setBlockState flags, placement/breaking flow. Removed last medium-confidence page.
- Tier B proofread of all 15 farm concept pages against raw sources: all numeric claims verified present in source; drop rates (1/40 jungle, 1/20 others), species heights, piston 3gt/4gt/5gt timings, 4gt clock, detection methods all match GTMC raw. Added two honesty clarifications (overview module-count nuance; large-spruce 1.21/llama-boat version caveat).
- Adopted TechMCTranslationWorkflow's upstream source repos as our provenance (techmc-wiki/articles, TechMCDocs/pages, TechMC-Glossary, Discovering-Minecraft, tree-hole, ArticlesAndDevNotes) — recorded in index.md source-repo table.
- Built `concepts/glossary.md` as an English term+definition reference (68 terms, sourced from TechMC-Glossary). Per user direction the wiki is **English-only** — no Chinese translations in page bodies; removed the CN glossary CSV.
- **Scope correction:** wiki is general Technical Minecraft (tree farms are just the first area ingested), not tree-farm-only. Updated README.md + index.md header + SCHEMA.md Domain line.
- **Language rule written into SCHEMA.md** (English only; term definitions in glossary as English term+definition; rationale recorded). This is now a hard schema rule, not re-derivable.
- Stripped residual CN from detection-methods / dustless-wiring glossary links. dark-oak-growth-mechanics keeps original-author Chinese names only as source attribution (proper nouns, not translation).
- Ingested GTMC `redstone-components/rails` (NC-update emission order, direct/indirect activation, directional search/diode connectivity) + TMWiki `GameMechanics/RailBudding` (corroborates above→self→below notifier order, 9-rail search, rail BUD). Built `concepts/rails.md` (high confidence). Wired into dustless-wiring + piston-mechanics. This is the first non-tree-farm mechanics ingest since scope widened to general Tech MC.
- 28 concept pages, 30 raw sources, no broken wikilinks.

