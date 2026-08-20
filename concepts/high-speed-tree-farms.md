---
type: concept
title: High-Speed Tree Farms
created: 2026-08-18
updated: 2026-08-18

description: '"High-speed" means moving functionality from inter-tick timing into intra-tick timing (via [[0-tick]] and [[dustless-wiring]]) and integrating the modules into …'
edition: java
version: 1.20.1
confidence: high
tags: [farms, high-speed, tree-farm, source-gtmc]
sources:
- id: gtmc-tree-farm-high-speed
  resource: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
  title: GTMC Tree Farm High Speed
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# High-Speed Tree Farms

"High-speed" means moving functionality from inter-tick timing into intra-tick timing (via [0-tick](/concepts/0-tick.md) and [dustless-wiring](/concepts/dustless-wiring.md)) and integrating the modules into a tight **base**.[^gtmc-tree-farm-high-speed]

## The "base"

For high-speed farms, design **bonemealing**, **detection**, **trunk processing**, and **sapling cycling** as one integrated unit called the **base**.[^gtmc-tree-farm-high-speed]

### Trunk processing — suction over push

- **Downward suction** → plant as early as 3gt
- **Side suction** → as fast as 0gt
- **Upward push** → only ~6gt and now largely abandoned (jungle can exceed piston push limit; acacia side branches complicate it)[^gtmc-tree-farm-high-speed]

### Bonemealing — stacking dispensers

Stack dispensers to widen the growth window; introduces **cross bonemealing** (stagger fire by ~2gt). See [bonemealing](/concepts/bonemealing.md).[^gtmc-tree-farm-high-speed]

### Push-limit detection

The most important detection unit (Bright_Observer), 8gt cycle, stack four layers staggered 2gt to align with the cross-bonemealing clock. See [detection-methods](/concepts/detection-methods.md).[^gtmc-tree-farm-high-speed]

## Architecture = the real bottleneck

The architecture determines the minimum operating cycle. Faster architectures come from reducing piston actions that must occur at different macro timings. A good architecture is the most important prerequisite.[^gtmc-tree-farm-high-speed]

## Related

- [0-tick](/concepts/0-tick.md) · [dustless-wiring](/concepts/dustless-wiring.md) · [bonemealing](/concepts/bonemealing.md) · [detection-methods](/concepts/detection-methods.md)
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) · [multi-species-tree-farm](/concepts/multi-species-tree-farm.md) — concrete high-speed designs

[^gtmc-tree-farm-high-speed]: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
