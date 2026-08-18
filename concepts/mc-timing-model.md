---
title: MC Timing Model
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: medium
tags: [mechanics, timing, source-gtmc, version-sensitive]
sources: [raw/articles/gltmc-tree-farm-basics.md]
---

# MC Timing Model

Minecraft timing has two scales: **inter-tick timing** (across game ticks) and **intra-tick timing** (within a single game tick). Moving work from inter-tick into intra-tick is the core way to speed up a tree farm.^[raw/articles/gltmc-tree-farm-basics.md]

## Game tick (gt)

- 1 second = 20 gt. A gt is further split into ordered phases; the ones relevant to tree farms execute in this order: NU → TT → BE → TE (per GTMC naming).^[raw/articles/gltmc-tree-farm-basics.md]
- **TT components** (repeaters, comparators, observers) have fixed *macroscopic* delays: repeaters 2–8gt, comparators and observers 2gt. All other tree-farm components have no macroscopic delay.^[raw/articles/gltmc-tree-farm-basics.md]
- **Instant components** act immediately on receiving an update regardless of phase: redstone dust, rails, fence gates, trapdoors, note blocks, droppers, dispensers.^[raw/articles/gltmc-tree-farm-basics.md]

## Depth (BE ordering)

Pistons and note blocks (BE components) execute in the order they *receive updates confirming a needed state change*. This order is called **depth** — deeper means later in the BE queue. Note blocks do **not** increase depth.^[raw/articles/gltmc-tree-farm-basics.md]

> **Confidence note:** GTMC's basics section is a simplified model ("technically incorrect" per the authors) and points to the full Timing Theory for rigor. Treat exact phase names and the 1gt/2gt action-cost numbers as version-sensitive.^[raw/articles/gltmc-tree-farm-basics.md]

## Related

- [[piston-action-timing]] — how depth produces 0-tick
- [[updates-nc-pp]] — what updates feed the model
- [[update-theory]] — full update taxonomy: NC/PP/Comparator/Self-inspection, QC, flags
- [[continuous-updates]] — DFS propagation order
- [[special-update-behaviors]] — dust 2nd-order, diagonal rails, lit-observer quirk
- [[tick-micro-timing]] — game tick, inter/intra-tick phases, component phase table
- [[piston-mechanics]] — self-check, QC, push limit, b36, instant placement
- [[block-nature]] — Block vs BlockState (pointer)
- [[0-tick]] — using depth for speed
