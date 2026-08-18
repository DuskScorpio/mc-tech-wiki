---
title: High-Speed Tree Farms
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [farms, high-speed, tree-farm, source-gtmc]
sources: [raw/articles/gtmc-tree-farm-high-speed.md]
---

# High-Speed Tree Farms

"High-speed" means moving functionality from inter-tick timing into intra-tick timing (via [[0-tick]] and [[dustless-wiring]]) and integrating the modules into a tight **base**.^[raw/articles/gtmc-tree-farm-high-speed.md]

## The "base"

For high-speed farms, design **bonemealing**, **detection**, **trunk processing**, and **sapling cycling** as one integrated unit called the **base**.^[raw/articles/gtmc-tree-farm-high-speed.md]

### Trunk processing — suction over push

- **Downward suction** → plant as early as 3gt
- **Side suction** → as fast as 0gt
- **Upward push** → only ~6gt and now largely abandoned (jungle can exceed piston push limit; acacia side branches complicate it)^[raw/articles/gtmc-tree-farm-high-speed.md]

### Bonemealing — stacking dispensers

Stack dispensers to widen the growth window; introduces **cross bonemealing** (stagger fire by ~2gt). See [[bonemealing]].^[raw/articles/gtmc-tree-farm-high-speed.md]

### Push-limit detection

The most important detection unit (Bright_Observer), 8gt cycle, stack four layers staggered 2gt to align with the cross-bonemealing clock. See [[detection-methods]].^[raw/articles/gtmc-tree-farm-high-speed.md]

## Architecture = the real bottleneck

The architecture determines the minimum operating cycle. Faster architectures come from reducing piston actions that must occur at different macro timings. A good architecture is the most important prerequisite.^[raw/articles/gtmc-tree-farm-high-speed.md]

## Related

- [[0-tick]] · [[dustless-wiring]] · [[bonemealing]] · [[detection-methods]]
- [[4gt-tree-farm]] · [[multi-species-tree-farm]] — concrete high-speed designs
