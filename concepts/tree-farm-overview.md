---
title: Tree Farm Overview
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [farms, tree-farm, source-gtmc]
sources: [raw/articles/gltmc-tree-farm-foreword.md, raw/articles/gltmc-tree-farm-basics.md]
---

# Tree Farm Overview

A tree farm is an automated structure for producing wood in Technical Minecraft Survival. GTMC places tree farms at the start of its Mechanical Redstone volume because they are representative of timing and wiring problems in redstone engineering.^[raw/articles/gltmc-tree-farm-foreword.md]

## Basic structure (Minecraft 1.15+)

A tree farm consists of five modules:^[raw/articles/gltmc-tree-farm-basics.md]

1. **[[bonemealing]]** — dispensers fire bone meal onto saplings.
2. **[[trunk-processing]]** — move the grown trunk away from where it grew.
3. **[[leaf-processing]]** — push away enough leaves to recover saplings.
4. **[[sapling-recycling]]** — collect dropped saplings back to the player.
5. **[[block-to-drop]]** — convert logs/leaves to items (TNT or wither).

Most farms also include a **[[detection-methods|detection]]** module that detects growth and triggers the farm, but this is optional.^[raw/articles/gltmc-tree-farm-basics.md]

> **Version scope:** these pages follow GTMC's 1.15+ structure. In 1.14 and below, jungle/acacia needed a height-increase module and spruce needed a retractable wall — explicitly out of scope here.^[raw/articles/gltmc-tree-farm-basics.md]

## Foundation pages

- [[mc-timing-model]] — inter-tick vs intra-tick, phases, depth
- [[updates-nc-pp]] — NC vs PP updates
- [[piston-action-timing]] — 3gt default action, 0-tick
- [[trunk-processing]] · [[leaf-processing]] · [[bonemealing]] · [[sapling-recycling]] · [[block-to-drop]]
- [[detection-methods]] — comparator / QC / BUD / push-limit

## Farm-type pages

- [[multi-species-tree-farm]] — all five classic species
- [[4gt-tree-farm]] — clock-driven 4gt designs
- [[large-spruce-tree-farm]] — 2x2 large spruce
- [[0-tick]] and [[dustless-wiring]] — speed/lag techniques
- [[tree-species-requirements]] — per-species growth constraints
