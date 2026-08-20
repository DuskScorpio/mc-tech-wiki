---
type: concept
title: Updates — NC vs PP
created: 2026-08-18
updated: 2026-08-18

description: "Minecraft has two update types: **NC updates** (neighbor/block changes) and **PP updates** (block/state placement changes)."
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, updates, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Updates — NC vs PP

Minecraft has two update types: **NC updates** (neighbor/block changes) and **PP updates** (block/state placement changes).[^gtmc-tree-farm-basics]

## Sources of NC updates

In tree farms, NC updates mainly come from:[^gtmc-tree-farm-basics]

- **TT components**: repeaters, comparators, observers
- **Redstone dust**
- **Rails** (powered/activated)
- **Pistons** plus the blocks they push/pull
- **Note blocks**

Because tree-farm structures are mostly pistons, NC updates in farms generally arrive *with* PP updates. **Observers specifically detect PP updates**, while **BUDs detect NC updates**.[^gtmc-tree-farm-basics]

## Pure PP updates (no NC)

In tree farms, PP-without-NC typically comes from wireless-redstone power types:[^gtmc-tree-farm-basics]

- **Tree power** — through leaves (NC + PP)
- **Scaffolding power** — through scaffolding (NC + PP)
- **Wall power** — through walls, vertically (PP)

See [dustless-wiring](/concepts/dustless-wiring.md) for how these enable lag-free signal transmission.

## Related

- [mc-timing-model](/concepts/mc-timing-model.md) — updates drive the phase/depth model
- [detection-methods](/concepts/detection-methods.md) — BUDs and observers as detectors

[^gtmc-tree-farm-basics]: raw/articles/gtmc-tree-farm-basics.md
