---
type: concept
title: Tree Farm Detection
created: 2026-08-21
updated: 2026-08-21

description: How a tree farm knows a tree has grown (detection) versus running on a self-timed clock, the clock-vs-detection tradeoff across intervals, and the four basic detection methods.
edition: java
version: 1.20.1
confidence: high
tags: [tree-farm, detection, clock, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/tree-farm/basics
  title: GTMC Tree Farm Basics
- id: gtmc-tree-farm-simple-design
  resource: https://www.techmc.wiki/en/articles/tree-farm/simple-design
  title: GTMC Simple Design
- id: gtmc-tree-farm-4gt
  resource: https://www.techmc.wiki/en/articles/tree-farm/4gt
  title: GTMC 4gt
generated: { by: /, at: "2026-08-21T00:00:00Z" }
status: stable
---

# Tree Farm Detection

A tree farm needs to know when a tree has grown so it can trigger harvesting (or, alternatively, it can ignore growth entirely and run on a fixed schedule). This page covers the two strategies and the detection methods.

## Detection vs clock

**Detection** is a subsystem that notices a sapling has grown and fires the farm's processing. It is **optional** — most tree farms include one, but not all need it.[^gtmc-tree-farm-basics]

The alternative is a **clock**: the farm activates itself on a fixed period without waiting for growth. Clocks are not limited to simple farms — 4gt designs (including complex ones) run on a 4gt clock, and 8gt/12gt mega-spruce are clock-based exceptions too.[^gtmc-tree-farm-4gt]

The usual guideline is that designs whose processing cycle is **longer than 4gt** tend to switch to detection, since a clock that slow leaves the growth window underused.[^gtmc-tree-farm-simple-design] But clock periods themselves range widely (3gt–12gt), and the choice is a **design tradeoff**, not a fixed rule — it depends on the designer and the farm's limitations (e.g. a 3gt clock needs an autoclicker for bone meal, which is traditionally not recognized, so 3gt clock farms are disfavored).[^gtmc-tree-farm-4gt]

## Basic detection methods

When detection is used, the common methods are:[^gtmc-tree-farm-simple-design]

- **Comparator detection**
- **QC detection** — a trunk-powered sapling makes the diagonally-below piston receive a QC update; one more update pushes it out, triggering processing.
- **BUD detection**
- **Push-limit detection** — currently the most important method; almost all detection-based tree-farm designs after the simple-design chapter use push-limit detection.[^gtmc-tree-farm-simple-design]

## Related

- [tree-farm](/concepts/tree-farm.md) — the three stages (growth → detection → harvesting)
- [tree-farm-basics](/concepts/tree-farm-basics.md) — growth mechanics (to be built)

[^gtmc-tree-farm-basics]: [gtmc-tree-farm-basics.md](raw/articles/gtmc-tree-farm-basics.md)
[^gtmc-tree-farm-simple-design]: [gtmc-tree-farm-simple-design.md](raw/articles/gtmc-tree-farm-simple-design.md)
[^gtmc-tree-farm-4gt]: [gtmc-tree-farm-4gt.md](raw/articles/gtmc-tree-farm-4gt.md)
