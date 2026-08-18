---
title: Tree Species Requirements
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [trees, source-gtmc, version-sensitive]
sources: [raw/articles/gltmc-tree-farm-multi-species.md, raw/articles/gltmc-tree-farm-large-spruce.md]
---

# Tree Species Requirements

For a multi-species farm, take the **union** of every species' constraints — meet the most demanding one.^[raw/articles/gltmc-tree-farm-multi-species.md]

| Species | Key growth constraint | Processing note |
|---|---|---|
| **Birch** | Fewest restrictions | Simple push/pull; ~20 leaves needed |
| **Spruce** | 5x5 area centered on sapling must be clear | Triple / pseudo-double / honey-slime double recursion |
| **Acacia** | Up to 2 logs same y-level, along x/z, ≤4 from sapling; growth detection 3x3 | Needs **side branch processing** (center consolidation or extra outputs) |
| **Jungle** | Trunk up to **12 blocks** tall; sapling drop 1/40 | Needs tall pusher + extra leaf coverage (avg >42 to get enough saplings) |
| **Oak** | Can become a **large oak** (drumstick) | Height-limit block at **9th block above dirt** |
| **Dark oak** | 2x2 (NW corner); 3x7x3–3x10x3 column above NW + 5x3x5 below height; can be limited/boosted | Can be "height-boosted"; special case in multi-species (see [[dark-oak-growth-mechanics]]) |

Large spruce (2x2): growth detection is **3x3 at the sapling layer (NW corner), expanding to 5x5 above**; max height 28 (29 at NW corner). Needs double recursion + honey-slime walls.^[raw/articles/gltmc-tree-farm-large-spruce.md]

> **1.14-and-below only:** jungle/acacia used a 3x3-trunk / 5x5-canopy check enabling a "height increase" module; dark oak keeps this in 1.20.1. Out of scope for 1.15+ pages.^[raw/articles/gltmc-tree-farm-multi-species.md]

## Related

- [[trunk-processing]] — which method handles each constraint
- [[multi-species-tree-farm]] — combining them
- [[large-spruce-tree-farm]] — 2x2 deep dive
