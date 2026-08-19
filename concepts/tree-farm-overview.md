---
type: concept
title: Tree Farm Overview
created: 2026-08-18
updated: 2026-08-18

description: A tree farm is an automated structure for producing wood in Technical Minecraft Survival.
edition: java
version: 1.20.1
confidence: high
tags: [farms, tree-farm, source-gtmc]
sources:
- id: gtmc-tree-farm-foreword
  resource: https://www.techmc.wiki/en/articles/tree-farm
  title: GTMC Tree Farm Foreword
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Tree Farm Overview

A tree farm is an automated structure for producing wood in Technical Minecraft Survival. GTMC places tree farms at the start of its Mechanical Redstone volume because they are representative of timing and wiring problems in redstone engineering.[^gtmc-tree-farm-foreword]

## Basic structure (Minecraft 1.15+)

A tree farm consists of five modules:[^gtmc-tree-farm-basics]

1. **[bonemealing](/concepts/bonemealing.md)** — dispensers fire bone meal onto saplings.
2. **[trunk-processing](/concepts/trunk-processing.md)** — move the grown trunk away from where it grew.
3. **[leaf-processing](/concepts/leaf-processing.md)** — push away enough leaves to recover saplings.
4. **[sapling-recycling](/concepts/sapling-recycling.md)** — collect dropped saplings back to the player.
5. **[block-to-drop](/concepts/block-to-drop.md)** — convert logs/leaves to items (TNT or wither).

Most farms also include a **[detection](/concepts/detection-methods.md)** module that detects growth and triggers the farm, but this is optional.[^gtmc-tree-farm-basics]

> **Module count nuance:** GTMC's "basic structure" names 4 core modules (Bonemealing, Trunk, Leaf, Sapling Recycling) and treats Detection as optional. `block-to-drop` (TNT/wither conversion) is a near-universal 5th module in practice; this wiki lists it as part of the structure because every real farm needs item conversion. Source: [^gtmc-tree-farm-basics]

## Foundation pages

- [mc-timing-model](/concepts/mc-timing-model.md) — inter-tick vs intra-tick, phases, depth
- [updates-nc-pp](/concepts/updates-nc-pp.md) — NC vs PP updates
- [piston-action-timing](/concepts/piston-action-timing.md) — 3gt default action, 0-tick
- [trunk-processing](/concepts/trunk-processing.md) · [leaf-processing](/concepts/leaf-processing.md) · [bonemealing](/concepts/bonemealing.md) · [sapling-recycling](/concepts/sapling-recycling.md) · [block-to-drop](/concepts/block-to-drop.md)
- [detection-methods](/concepts/detection-methods.md) — comparator / QC / BUD / push-limit

## Farm-type pages

- [multi-species-tree-farm](/concepts/multi-species-tree-farm.md) — all five classic species
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — clock-driven 4gt designs
- [large-spruce-tree-farm](/concepts/large-spruce-tree-farm.md) — 2x2 large spruce
- [0-tick](/concepts/0-tick.md) and [dustless-wiring](/concepts/dustless-wiring.md) — speed/lag techniques
- [tree-species-requirements](/concepts/tree-species-requirements.md) — per-species growth constraints
[^gtmc-tree-farm-foreword]: https://www.techmc.wiki/en/articles/tree-farm
[^gtmc-tree-farm-basics]: https://www.techmc.wiki/en/articles/block-update
