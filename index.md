# Wiki Index — OKF bundle entry point

> Content catalog (OKF progressive disclosure). An agent starts here, then follows concept links (each `[label](/concepts/NAME)` with the `.md` suffix) to traverse the knowledge graph.
> Domain: Technical Minecraft (Java). English-only (see SCHEMA.md).

- [README](README.md) — repo overview, usage, sources
- [SCHEMA](SCHEMA.md) — vault + OKF v0.2 contract (authoritative rules)

## Designated source repositories (provenance)

These upstream repos are our sources (adopted from TechMCTranslationWorkflow):

| Repo | What it is | Status |
|---|---|---|
| `techmc-wiki/articles` | Canonical GTMC articles (EN + ZH pairs) | ingested (EN via site) |
| `TechMCDocs/pages` | Technical Minecraft Wiki (TMWiki) | ingested (tree-farm + piston/rail relevant) |
| `TechMC-Glossary/TechMC-Glossary` | Multi-language term glossary | ingested → `concepts/glossary.md` |
| `minecraft.wiki` | Minecraft Wiki (3rd cross-source) | partial (Sapling captured) |
| `lovexyn0827/Discovering-Minecraft` | Mechanics wiki | available, not yet ingested |
| `acaciachan/tree-hole` | CN technical-MC knowledge base | available, not yet ingested |
| `Youmiel/ArticlesAndDevNotes` | Translator's dev notes | available, not yet ingested |

Source attribution (CC BY-NC-SA where applicable) is recorded per raw file in `raw/articles/`.

## Concepts (by type)

### concept: tree-farm
- [Tree Farm Overview](concepts/tree-farm-overview.md) — what a tree farm is, its 5 modules, version scope
- [Tree Species Requirements](concepts/tree-species-requirements.md) — per-species growth constraints table
- [Bonemealing](concepts/bonemealing.md) — dispensers, stacking, cross vs synchronized
- [Sapling Recycling](concepts/sapling-recycling.md) — hoppers / water / hopper minecarts
- [Trunk Processing](concepts/trunk-processing.md) — main + root methods, side-branch handling
- [Leaf Processing](concepts/leaf-processing.md) — pistons/honey-slime walls; drop 1/20 vs 1/40
- [Block to Drop](concepts/block-to-drop.md) — wither vs TNT; milk/b36 chambers
- [High-Speed Tree Farms](concepts/high-speed-tree-farms.md) — the integrated "base", suction over push
- [0-Tick](concepts/0-tick.md) — generators (TT order, redstone dust, redirection)
- [Dustless Wiring](concepts/dustless-wiring.md) — rails+observers, power types, slime sticks
- [Multi-Species Tree Farm](concepts/multi-species-tree-farm.md) — 5-species union + stream reorganization
- [4gt Tree Farm](concepts/4gt-tree-farm.md) — 4gt-clock designs, dustless 0t, suction-to-push
- [Large Spruce Tree Farm](concepts/large-spruce-tree-farm.md) — 2x2 large spruce, planting caveats
- [Detection Methods](concepts/detection-methods.md) — comparator / QC / BUD / push-limit

### concept: mechanics
- [MC Timing Model](concepts/mc-timing-model.md) — inter/intra-tick, gt phases, depth
- [Updates NC vs PP](concepts/updates-nc-pp.md) — NC vs PP; BUDs vs observers
- [Update Theory](concepts/update-theory.md) — NC/PP/Comparator/Self-inspection, QC, flags
- [Continuous Updates](concepts/continuous-updates.md) — DFS propagation, NC/PP order
- [Special Update Behaviors](concepts/special-update-behaviors.md) — dust 2nd-order, diagonal rails
- [Tick Micro Timing](concepts/tick-micro-timing.md) — game tick, intra-tick phases, component table
- [Piston Mechanics](concepts/piston-mechanics.md) — self-check, QC, push limit, b36
- [Block Nature](concepts/block-nature.md) — Block vs BlockState
- [Piston Action Timing](concepts/piston-action-timing.md) — 3gt action, 1gt/2gt costs
- [Flying Machines](concepts/flying-machines.md) — 9gt/10gt/12gt, observer activation, mounting/extension
- [Slime Tech Engines and Mobility](concepts/slime-tech-engines.md) — engine = agency; mobilizing a structure directly
- [Linkages](concepts/linkages.md) — zero-delay piston-chain retraction, BUD linkages
- [Moving Block B36](concepts/moving-block-b36.md) — B36 properties, hitbox, NBT
- [Dark Oak Growth Mechanics](concepts/dark-oak-growth-mechanics.md) — 2x2 code-level growth
- [Zero-Tick Farming Crops](concepts/zero-tick-farming-crops.md) — crop 0t (patched 1.16+); not redstone 0t

### concept: glossary
- [Glossary](concepts/glossary.md) — English term + definition reference

## Raw Sources (immutable, sha256-tracked, under `raw/articles/`)

### gtmc (Graduate Texts in Minecraft)
gtmc-tree-farm-foreword.md, gtmc-tree-farm-basics.md, gtmc-tree-farm-simple-design.md,
gtmc-tree-farm-multi-species.md, gtmc-tree-farm-high-speed.md, gtmc-tree-farm-dustless-wiring.md,
gtmc-tree-farm-4gt.md, gtmc-tree-farm-large-spruce.md,
gtmc-block-update-concepts.md, gtmc-block-update-continuous.md, gtmc-block-update-special.md,
gtmc-micro-timing-ticks.md, gtmc-micro-timing-intra-tick.md,
gtmc-pistons.md, gtmc-block-mechanics.md, gtmc-blocks-and-states.md, gtmc-block-changes.md,
gtmc-rails.md, gtmc-rail-budding.md, gtmc-slime-introduction.md, gtmc-flying-machine-basics.md, gtmc-engines.md, gtmc-mobility.md, gtmc-linkages.md

### bilibili
bilibili-dark-oak-growth.md — Scorpio, edited 2025-02-09, Java ~1.21.x

### tmwiki (TechMCDocs/pages)
tmwiki-block-updates.md, tmwiki-piston.md, tmwiki-moving-block36.md, tmwiki-zero-tick-farms.md,
tmwiki-tile-ticks.md, tmwiki-game-tick.md, tmwiki-rail-budding.md

### mcwiki (minecraft.wiki)
mcwiki-sapling.md — Sapling page, 3rd cross-source for species table

## TODO (not yet compiled)
- GTMC chapter 06 (high-speed continuation) — URL not yet fetched
- Detailed timing tables per farm (PTHSUTF 21gt acacia, TT1998 6gt jungle, etc.)
- Discovering-Minecraft + tree-hole ingest (general tech-MC expansion)
