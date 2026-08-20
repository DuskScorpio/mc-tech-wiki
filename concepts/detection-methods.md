---
type: concept
title: Growth Detection Methods
created: 2026-08-18
updated: 2026-08-18

description: A detection module senses that a sapling has grown and triggers the farm's processing.
edition: java
version: 1.20.1
confidence: high
tags: [methods, detection, source-gtmc]
sources:
- id: gtmc-tree-farm-simple-design
  resource: https://www.techmc.wiki/en/articles/tree-farm/simple-design
  title: GTMC Tree Farm Simple Design
- id: gtmc-tree-farm-high-speed
  resource: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
  title: GTMC Tree Farm High Speed
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
  title: GTMC Tree Farm Multi Species
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Growth Detection Methods

A detection module senses that a sapling has grown and triggers the farm's processing. Four basic methods:[^gtmc-tree-farm-simple-design]

1. **Comparator detection**
2. **QC detection** — the grown trunk is powered; the diagonally-below piston gets a QC update and needs one more update to push out, triggering processing.[^gtmc-tree-farm-simple-design]
3. **BUD detection** (e.g. leaf detection)
4. **Push limit detection** — currently the most important; used in almost all detection-based designs after the basics chapter.[^gtmc-tree-farm-simple-design]

## Push-limit detection detail

A unit by Bright_Observer: when the upward-pushing piston plans its push during TT, it checks the push limit. Runs at an **8gt cycle**; stack four layers staggered by 2gt and link with slime blocks to align with the cross-bonemealing clock.[^gtmc-tree-farm-high-speed]

## Speed limiter

Trees can grow before the architecture resets, triggering detection prematurely and breaking the farm. A speed limiter on the detection structure must account for each mode's reset time. For push-limit detection, sever the link between the detector and the dirt.[^gtmc-tree-farm-multi-species]

## Related

- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — detection-based 4gt designs
- [mc-timing-model](/concepts/mc-timing-model.md) — TT/BE phases involved
- [glossary](/concepts/glossary.md) — BUD, QC, PLD term definitions

[^gtmc-tree-farm-simple-design]: [gtmc-tree-farm-simple-design.md](raw/articles/gtmc-tree-farm-simple-design.md)
[^gtmc-tree-farm-high-speed]: [gtmc-tree-farm-high-speed.md](raw/articles/gtmc-tree-farm-high-speed.md)
[^gtmc-tree-farm-multi-species]: [gtmc-tree-farm-multi-species.md](raw/articles/gtmc-tree-farm-multi-species.md)