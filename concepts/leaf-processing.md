---
title: Leaf Processing
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [methods, leaf-processing, source-gtmc]
sources: [raw/articles/gtmc-tree-farm-basics.md]
---

# Leaf Processing

Push away enough leaves (with pistons or honey-slime walls) to recover the saplings you need.^[raw/articles/gtmc-tree-farm-basics.md]

## Sapling drop chance

Each leaf block has a fixed sapling drop chance:^[raw/articles/gtmc-tree-farm-basics.md]

| Tree type | Sapling drop per leaf |
|---|---|
| Jungle | 1/40 |
| All other types | 1/20 |

Because jungle is so low (1/40), jungle-capable farms need extra leaf-processing coverage — see [[tree-species-requirements]] and [[multi-species-tree-farm]].

## Related

- [[sapling-recycling]] — what happens to the dropped saplings
- [[block-to-drop]] — converting the rest to items
