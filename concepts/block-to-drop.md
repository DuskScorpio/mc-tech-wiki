---
title: Block-to-Drop Conversion
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [methods, block-to-drop, source-gtmc]
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

- [[multi-species-tree-farm]] — why stream shape matters
- [[trunk-processing]] — what feeds the stream
