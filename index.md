# Wiki Index

> Content catalog. Read this first to find relevant pages.
> Last updated: 2026-08-18
> Domain: Technical Minecraft (Java) — currently tree farms + core mechanics; expanding to other tech-MC topics.
> Sources tracked in the "Designated source repositories" table below.

## Designated source repositories (provenance)

These are the upstream repos referenced by TechMCTranslationWorkflow — adopted as our sources too:

| Repo | What it is | Status |
|---|---|---|
| `techmc-wiki/articles` | Canonical GTMC articles (EN + ZH pairs) — what we ingest via the site | ingested (EN via site; ZH available) |
| `TechMCDocs/pages` | Technical Minecraft Wiki (TMWiki) | ingested (tree-farm-relevant) |
| `TechMC-Glossary/TechMC-Glossary` | Multi-language term glossary (CN names) | ingested → `concepts/glossary.md` + `raw/sources/techmc-glossary.csv` |
| `lovexyn0827/Discovering-Minecraft` | Mechanics wiki (3rd cross-source) | available, not yet ingested |
| `acaciachan/tree-hole` | CN technical-MC knowledge base | available, not yet ingested |
| `Youmiel/ArticlesAndDevNotes` | Translator's own dev notes | available, not yet ingested |

Source attribution (CC BY-NC-SA where applicable) is recorded per raw file in `raw/articles/` and `raw/sources/`.

## Concepts

- [[tree-farm-overview]] — what a tree farm is, its 5 modules, version scope
- [[mc-timing-model]] — inter/intra-tick, gt phases (NU→TT→BE→TE), depth
- [[updates-nc-pp]] — NC vs PP updates; BUDs vs observers
- [[update-theory]] — NC/PP/Comparator/Self-inspection, QC, setBlockState flags
- [[continuous-updates]] — DFS propagation, NC/PP order analysis
- [[special-update-behaviors]] — dust 2nd-order, diagonal rails, lit-observer quirk
- [[tick-micro-timing]] — game tick, inter/intra-tick phases, component phase table
- [[piston-mechanics]] — self-check, QC, push limit, b36, instant placement
- [[block-nature]] — Block vs BlockState (pointer)
- [[piston-action-timing]] — 3gt default action, 1gt/2gt costs, 0-tick basis
- [[trunk-processing]] — main + root processing methods, side-branch handling
- [[leaf-processing]] — pistons/honey-slime walls; sapling drop 1/20 vs 1/40
- [[bonemealing]] — dispensers, stacking, cross vs synchronized bonemealing
- [[sapling-recycling]] — hoppers / water / hopper minecarts
- [[block-to-drop]] — wither vs TNT; milk/b36 explosion chambers
- [[glossary]] — TechMC-Glossary terms + authoritative Chinese names (translation reference) + speed limiter
- [[high-speed-tree-farms]] — the integrated "base", suction over push
- [[0-tick]] — generators (TT order, redstone dust, redirection)
- [[dustless-wiring]] — rails+observers, power types, slime sticks, redirection
- [[tree-species-requirements]] — per-species growth constraints table
- [[multi-species-tree-farm]] — 5-species union design + stream reorganization
- [[4gt-tree-farm]] — 4gt-clock designs, dustless 0t, suction-to-push
- [[large-spruce-tree-farm]] — 2x2 large spruce, speed history, planting caveats
- [[moving-block-b36]] — B36 properties, hitbox offset, NBT (source-tmwiki + gtmc)
- [[zero-tick-farming-crops]] — crop zero-tick (patched 1.16+); NOT the redstone 0-tick used in farms

## Raw Sources

All under `raw/articles/` — immutable GTMC captures (sha256-tracked):

- gtmc-tree-farm-foreword.md
- gtmc-tree-farm-basics.md
- gtmc-tree-farm-simple-design.md
- gtmc-tree-farm-multi-species.md
- gtmc-tree-farm-high-speed.md
- gtmc-tree-farm-dustless-wiring.md
- gtmc-tree-farm-4gt.md
- gtmc-tree-farm-large-spruce.md
- bilibili-dark-oak-growth.md — Scorpio, edited 2025-02-09, Java ~1.21.x
- gtmc-block-update-concepts.md
- gtmc-block-update-continuous.md
- gtmc-block-update-special.md
- gtmc-micro-timing-ticks.md
- gtmc-micro-timing-intra-tick.md
- gtmc-pistons.md
- gtmc-block-mechanics.md
- gltmc-intra-tick-timing.md
- gltmc-scheduled-ticks.md
- gltmc-block-events.md
- gltmc-block-entities.md
- gltmc-blocks-and-states.md
- gltmc-block-changes.md
- tmwiki-block-updates.md — TechMCDocs/pages (Technical Minecraft Wiki), independent 2nd source
- tmwiki-piston.md
- tmwiki-moving-block36.md
- tmwiki-zero-tick-farms.md
- tmwiki-tile-ticks.md
- tmwiki-game-tick.md

## Sibling vaults (for cross-linking terms later)

- `C:\GitHub Related\TechMC-Glossary` — GTMC glossary
- `C:\GitHub Related\tmc-glossary-web` — web build of the glossary

## TODO (tree-farm section, not yet compiled)

- GTMC chapter 06 (listed in TOC but URL not yet fetched) — high-speed continuation
- Detailed timing tables per farm (PTHSUTF 21gt acacia, TT1998 6gt jungle, etc.)
- Per-farm example-world downloads referenced by GTMC (ZIP links)
