---
type: concept
title: Leaf Processing
created: 2026-08-18
updated: 2026-08-18

description: Push away enough leaves (with pistons or honey-slime walls) to recover the saplings you need.[^gtmc-tree-farm-basics]
edition: java
version: 1.20.1
confidence: high
tags: [methods, leaf-processing, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Leaf Processing

Push away enough leaves (with pistons or honey-slime walls) to recover the saplings you need.[^gtmc-tree-farm-basics]

## Sapling drop chance

Each leaf block has a fixed sapling drop chance:[^gtmc-tree-farm-basics]

| Tree type | Sapling drop per leaf |
|---|---|
| Jungle | 1/40 |
| All other types | 1/20 |

Because jungle is so low (1/40), jungle-capable farms need extra leaf-processing coverage — see [tree-species-requirements](/concepts/tree-species-requirements.md) and [multi-species-tree-farm](/concepts/multi-species-tree-farm.md).

## Related

- [sapling-recycling](/concepts/sapling-recycling.md) — what happens to the dropped saplings
- [block-to-drop](/concepts/block-to-drop.md) — converting the rest to items

[^gtmc-tree-farm-basics]: https://www.techmc.wiki/en/articles/block-update
