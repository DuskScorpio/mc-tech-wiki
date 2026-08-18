# Wiki Index

> Content catalog. Read this first to find relevant pages.
> Last updated: 2026-08-18 | Total concept pages: 16 | Raw sources: 8
> Domain: Technical Minecraft (tree farms), Java 1.20.1, sourced from GTMC.

## Concepts

- [[tree-farm-overview]] — what a tree farm is, its 5 modules, version scope
- [[mc-timing-model]] — inter/intra-tick, gt phases (NU→TT→BE→TE), depth
- [[updates-nc-pp]] — NC vs PP updates; BUDs vs observers
- [[piston-action-timing]] — 3gt default action, 1gt/2gt costs, 0-tick basis
- [[trunk-processing]] — main + root processing methods, side-branch handling
- [[leaf-processing]] — pistons/honey-slime walls; sapling drop 1/40 vs 1/20
- [[bonemealing]] — dispensers, stacking, cross vs synchronized bonemealing
- [[sapling-recycling]] — hoppers / water / hopper minecarts
- [[block-to-drop]] — wither vs TNT; milk/b36 explosion chambers
- [[detection-methods]] — comparator / QC / BUD / push-limit + speed limiter
- [[high-speed-tree-farms]] — the integrated "base", suction over push
- [[0-tick]] — generators (TT order, redstone dust, redirection)
- [[dustless-wiring]] — rails+observers, power types, slime sticks, redirection
- [[tree-species-requirements]] — per-species growth constraints table
- [[multi-species-tree-farm]] — 5-species union design + stream reorganization
- [[4gt-tree-farm]] — 4gt-clock designs, dustless 0t, suction-to-push
- [[large-spruce-tree-farm]] — 2x2 large spruce, speed history, planting caveats
- [[dark-oak-growth-mechanics]] — 2x2 code-level growth: trunk bend, side branches, leaves (Java ~1.21.x)

## Raw Sources

All under `raw/articles/` — immutable GTMC captures (sha256-tracked):

- gltmc-tree-farm-foreword.md
- gltmc-tree-farm-basics.md
- gltmc-tree-farm-simple-design.md
- gltmc-tree-farm-multi-species.md
- gltmc-tree-farm-high-speed.md
- gltmc-tree-farm-dustless-wiring.md
- gltmc-tree-farm-4gt.md
- gltmc-tree-farm-large-spruce.md
- bilibili-dark-oak-growth.md — Scorpio, edited 2025-02-09, Java ~1.21.x

## Sibling vaults (for cross-linking terms later)

- `C:\GitHub Related\TechMC-Glossary` — GTMC glossary
- `C:\GitHub Related\tmc-glossary-web` — web build of the glossary

## TODO (tree-farm section, not yet compiled)

- GTMC chapter 06 (listed in TOC but URL not yet fetched) — high-speed continuation
- Detailed timing tables per farm (PTHSUTF 21gt acacia, TT1998 6gt jungle, etc.)
- Per-farm example-world downloads referenced by GTMC (ZIP links)
