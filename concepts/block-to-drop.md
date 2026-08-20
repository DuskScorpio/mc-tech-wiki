---
type: concept
title: Block-to-Drop Conversion
created: 2026-08-18
updated: 2026-08-18

description: "Two main ways to turn logs/leaves into items: **wither** and **TNT**.[^gtmc-tree-farm-basics]"
edition: java
version: 1.20.1
confidence: high
tags: [methods, block-to-drop, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
  title: GTMC Tree Farm Multi Species
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Block-to-Drop Conversion

Two main ways to turn logs/leaves into items: **wither** and **TNT**.[^gtmc-tree-farm-basics]

## TNT

A **TNT duplicator** plus water flow to buffer TNT and collect drops is the common simple-farm choice.[^gtmc-tree-farm-simple-design]

## Multi-species: irregular streams

Multi-species farms produce an irregular block stream, so they use specialized chambers:[^gtmc-tree-farm-multi-species]

- **Pure milk explosion chambers** ("milk explosions")
- **b36 explosion chambers** ("push explosions")

Avoid pushing a 2-block-thick stream at once — it sharply cuts processing efficiency and final drop recovery.

## Related

- [multi-species-tree-farm](/concepts/multi-species-tree-farm.md) — why stream shape matters
- [trunk-processing](/concepts/trunk-processing.md) — what feeds the stream

[^gtmc-tree-farm-basics]: raw/articles/gtmc-tree-farm-basics.md
[^gtmc-tree-farm-simple-design]: raw/articles/gtmc-tree-farm-simple-design.md
[^gtmc-tree-farm-multi-species]: raw/articles/gtmc-tree-farm-multi-species.md
