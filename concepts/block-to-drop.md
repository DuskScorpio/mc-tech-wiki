---
type: concept
title: Block-to-Drop Conversion
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: "Two main ways to turn logs/leaves into items: **wither** and **TNT**.^[raw/articles/gtmc-tree-farm-basics.md]"
edition: java
version: 1.20.1
confidence: high
tags: [methods, block-to-drop, source-gtmc]
resource: "https://www.techmc.wiki/en/articles/block-update"
sources: [raw/articles/gtmc-tree-farm-basics.md, raw/articles/gtmc-tree-farm-multi-species.md]
---

# Block-to-Drop Conversion

Two main ways to turn logs/leaves into items: **wither** and **TNT**.^[raw/articles/gtmc-tree-farm-basics.md]

## TNT

A **TNT duplicator** plus water flow to buffer TNT and collect drops is the common simple-farm choice.^[raw/articles/gtmc-tree-farm-simple-design.md]

## Multi-species: irregular streams

Multi-species farms produce an irregular block stream, so they use specialized chambers:^[raw/articles/gtmc-tree-farm-multi-species.md]

- **Pure milk explosion chambers** ("milk explosions")
- **b36 explosion chambers** ("push explosions")

Avoid pushing a 2-block-thick stream at once — it sharply cuts processing efficiency and final drop recovery.

## Related

- [multi-species-tree-farm](concepts/multi-species-tree-farm.md) — why stream shape matters
- [trunk-processing](concepts/trunk-processing.md) — what feeds the stream
