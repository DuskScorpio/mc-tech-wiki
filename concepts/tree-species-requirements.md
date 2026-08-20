---
type: concept
title: Tree Species Requirements
created: 2026-08-18
updated: 2026-08-18

description: For a multi-species farm, take the **union** of every species' constraints — meet the most demanding one.^[raw/articles/gtmc-tree-farm-multi-species.md]
edition: java
version: 1.20.1
confidence: high
tags: [trees, source-gtmc, source-mcwiki, version-sensitive]
sources:
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
  title: GTMC Tree Farm Multi Species
- id: gtmc-tree-farm-large-spruce
  resource: https://www.techmc.wiki/en/articles/tree-farm/large-spruce-farm
  title: GTMC Tree Farm Large Spruce
- id: mcwiki-sapling
  resource: https://minecraft.wiki/w/Sapling
  title: Minecraft Wiki (minecraft.wiki)
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Tree Species Requirements

For a multi-species farm, take the **union** of every species' constraints — meet the most demanding one.[^gtmc-tree-farm-multi-species]

| Species | Min clear space above (JE) | Key growth constraint | Processing note |
|---|---|---|---|
| **Birch** | 6 (3×3) | Fewest restrictions | Simple push/pull; ~20 leaves needed |
| **Spruce** | 6 (5×5) single; 14 (5×5 centered on NW) as 2×2 | 5×5 area centered on sapling must be clear | Triple / pseudo-double / honey-slime double recursion |
| **Acacia** | 6 (5×5) | Up to 2 logs same y-level, along x/z, ≤4 from sapling; growth detection 3×3 | Needs **side branch processing** (center consolidation or extra outputs) |
| **Jungle** | 5 (3×3) single; 11 (5×5 centered on NW) as 2×2 | Trunk up to **12 blocks** tall; sapling drop 1/40 (=2.5%) | Needs tall pusher + extra leaf coverage (avg >42 to get enough saplings) |
| **Oak** | 5 (3×3); a block in growth space forces a large variant | Can become a **large oak** (drumstick) | Height-limit block at **9th block above dirt** |
| **Dark oak** | 7 (3×3 centered on NW), **must be 2×2** | 3×7×3–3×10×3 column above NW + 5×3×5 below height; can be limited/boosted | Can be "height-boosted"; special case in multi-species (see [dark-oak-growth-mechanics](/concepts/dark-oak-growth-mechanics.md)) |
| **Cherry** | 8 (5×5), 1×1 only | Not yet in farm scope | — |

Min-clearance heights and the 2×2 search order (SE → NE → SW → NW; NW sapling is canonical) are corroborated by Minecraft Wiki.[^mcwiki-sapling] Drop rates (jungle 1/40, others 1/20) also match.[^mcwiki-sapling]

Large spruce (2x2): growth detection is **3x3 at the sapling layer (NW corner), expanding to 5x5 above**; max height 28 (29 at NW corner). Needs double recursion + honey-slime walls.[^gtmc-tree-farm-large-spruce]

> **1.14-and-below only:** jungle/acacia used a 3x3-trunk / 5x5-canopy check enabling a "height increase" module; dark oak keeps this in 1.20.1. Out of scope for 1.15+ pages.[^gtmc-tree-farm-multi-species]

## Related

- [trunk-processing](/concepts/trunk-processing.md) — which method handles each constraint
- [multi-species-tree-farm](/concepts/multi-species-tree-farm.md) — combining them
- [large-spruce-tree-farm](/concepts/large-spruce-tree-farm.md) — 2x2 deep dive

[^gtmc-tree-farm-multi-species]: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
[^mcwiki-sapling]: Minecraft Wiki (minecraft.wiki)
[^gtmc-tree-farm-large-spruce]: https://www.techmc.wiki/en/articles/tree-farm/large-spruce-farm
