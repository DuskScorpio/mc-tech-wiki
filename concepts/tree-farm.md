---
type: concept
title: Tree Farm
created: 2026-08-21
updated: 2026-08-21

description: Hub for tree farming in Technical Minecraft (Java). Taxonomy (1×1 vs 2×2; speed tiers), the three subsystems every farm needs (growth, detection, harvesting), and pointers to design-specific pages.
edition: java
version: 1.20.1
confidence: high
tags: [tree-farm, hub, source-gtmc, source-mcwiki]
sources:
- id: gtmc-tree-farm-foreword
  resource: https://www.techmc.wiki/en/articles/tree-farm
  title: GTMC Tree Farm Foreword
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/tree-farm/basics
  title: GTMC Tree Farm Basics
- id: gtmc-tree-farm-simple-design
  resource: https://www.techmc.wiki/en/articles/tree-farm/simple-design
  title: GTMC Simple Design
- id: gtmc-tree-farm-high-speed
  resource: https://www.techmc.wiki/en/articles/tree-farm/high-speed
  title: GTMC High-Speed
- id: gtmc-tree-farm-4gt
  resource: https://www.techmc.wiki/en/articles/tree-farm/4gt
  title: GTMC 4gt
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species
  title: GTMC Multi-Species
- id: gtmc-tree-farm-large-spruce
  resource: https://www.techmc.wiki/en/articles/tree-farm/large-spruce
  title: GTMC Large Spruce
- id: gtmc-tree-farm-dustless-wiring
  resource: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
  title: GTMC Dustless Wiring
- id: mcwiki-tree-farming
  resource: https://minecraft.wiki/w/Tutorial:Tree_farming
  title: Minecraft Wiki — Tutorial:Tree farming
- id: mcwiki-sapling
  resource: https://minecraft.wiki/w/Sapling
  title: Minecraft Wiki — Sapling
- id: mcwiki-dark-oak
  resource: https://minecraft.wiki/w/Dark_Oak
  title: Minecraft Wiki — Dark Oak
generated: { by: /, at: "2026-08-21T00:00:00Z" }
status: stable
---

# Tree Farm

A **tree farm** plants many saplings, grows them into trees, and harvests logs (and more saplings) on a loop — making wood a renewable resource.[^mcwiki-tree-farming] Tree farms are the foundational Mechanical-Redstone topic because they exercise the same mechanics the rest of the wiki depends on: growth, tile-tick scheduling, and dustless wiring.[^gtmc-tree-farm-foreword]

## Taxonomy

Tree farms split on two independent axes:

**By trunk size** (the dominant design split):
- **1×1 farms** — oak, birch, spruce, jungle, acacia, cherry, **mangrove**. Grown from a single sapling. Mangrove is unique: it can be planted **underwater** and creates mangrove roots (extra fuel); bone meal on its leaves yields a guaranteed propagule.[^mcwiki-tree-farming]
- **2×2 farms** — dark oak (and large spruce, which uses a 2×2 spruce plant). Grown from a 2×2 sapling grid; can't grow individually.[^mcwiki-dark-oak]

**By speed / technique tier:**
- **Simple** — straightforward, lower throughput.[^gtmc-tree-farm-simple-design]
- **High-speed (HS)** — faster designs.[^gtmc-tree-farm-high-speed]
- **4gt** — all-tree-species at a 4gt period.[^gtmc-tree-farm-4gt]
- **Multi-species** — one farm handling several species.[^gtmc-tree-farm-multi-species]
- **Large spruce** — 8gt large-spruce specialist.[^gtmc-tree-farm-large-spruce]
- **Dustless** — wiring technique (cross-cuts all tiers) aimed at lag reduction, not dustlessness for its own sake.[^gtmc-tree-farm-dustless-wiring]

## The three stages (growth → detection → harvesting)

Regardless of tier, a tree farm moves a sapling through three stages:

1. **Growth** — getting saplings to actually grow (species requirements, space, bone meal). See [Sapling](raw/articles/mcwiki-sapling.md) and growth mechanics.
2. **Detection** *(optional)* — knowing the tree has grown so the farm can trigger harvesting, vs running on a self-timed **clock**. Optional; the clock-vs-detection tradeoff and the four detection methods are covered on [tree-farm-detection](/concepts/tree-farm-detection.md).[^gtmc-tree-farm-basics]
3. **Harvesting** — chopping the tree and collecting logs + saplings (often automated with pistons/slime).

## Why this is the on-ramp

Because growth detection and dustless wiring are the same timing/wiring problems found in the rest of Mechanical Redstone, tree farms are the natural entry point to the timing and redstone areas of this wiki.

## Child pages

**Built concept pages:**
- [tree-farm-detection](/concepts/tree-farm-detection.md) — detection vs clock, the four methods

**Raw source articles** (each becomes its own concept as the vault is built):

- [gtmc-tree-farm-basics](raw/articles/gtmc-tree-farm-basics.md)
- [gtmc-tree-farm-simple-design](raw/articles/gtmc-tree-farm-simple-design.md)
- [gtmc-tree-farm-high-speed](raw/articles/gtmc-tree-farm-high-speed.md)
- [gtmc-tree-farm-4gt](raw/articles/gtmc-tree-farm-4gt.md)
- [gtmc-tree-farm-multi-species](raw/articles/gtmc-tree-farm-multi-species.md)
- [gtmc-tree-farm-large-spruce](raw/articles/gtmc-tree-farm-large-spruce.md)
- [gtmc-tree-farm-dustless-wiring](raw/articles/gtmc-tree-farm-dustless-wiring.md)
- [mcwiki-tree-farming](raw/articles/mcwiki-tree-farming.md)
- [mcwiki-sapling](raw/articles/mcwiki-sapling.md)

## Related

- Build-up continues: child concept pages replace the raw links above as they are added.

[^gtmc-tree-farm-foreword]: [gtmc-tree-farm-foreword.md](raw/articles/gtmc-tree-farm-foreword.md)
[^gtmc-tree-farm-basics]: [gtmc-tree-farm-basics.md](raw/articles/gtmc-tree-farm-basics.md)
[^gtmc-tree-farm-simple-design]: [gtmc-tree-farm-simple-design.md](raw/articles/gtmc-tree-farm-simple-design.md)
[^gtmc-tree-farm-high-speed]: [gtmc-tree-farm-high-speed.md](raw/articles/gtmc-tree-farm-high-speed.md)
[^gtmc-tree-farm-4gt]: [gtmc-tree-farm-4gt.md](raw/articles/gtmc-tree-farm-4gt.md)
[^gtmc-tree-farm-multi-species]: [gtmc-tree-farm-multi-species.md](raw/articles/gtmc-tree-farm-multi-species.md)
[^gtmc-tree-farm-large-spruce]: [gtmc-tree-farm-large-spruce.md](raw/articles/gtmc-tree-farm-large-spruce.md)
[^gtmc-tree-farm-dustless-wiring]: [gtmc-tree-farm-dustless-wiring.md](raw/articles/gtmc-tree-farm-dustless-wiring.md)
[^mcwiki-tree-farming]: [mcwiki-tree-farming.md](raw/articles/mcwiki-tree-farming.md)
[^mcwiki-sapling]: [mcwiki-sapling.md](raw/articles/mcwiki-sapling.md)
[^mcwiki-dark-oak]: [mcwiki-dark-oak.md](raw/articles/mcwiki-dark-oak.md)
