---
type: concept
title: 0-tick
created: 2026-08-18
updated: 2026-08-18

description: A 0-tick action moves functionality from inter-tick into intra-tick timing — the main way to speed up a tree farm.
edition: java
version: 1.20.1
confidence: high
tags: [techniques, 0-tick, timing, source-gtmc]
sources:
- id: gtmc-tree-farm-high-speed
  resource: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
  title: GTMC Tree Farm High Speed
- id: gtmc-tree-farm-dustless-wiring
  resource: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
  title: GTMC Tree Farm Dustless Wiring
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# 0-tick

A 0-tick action moves functionality from inter-tick into intra-tick timing — the main way to speed up a tree farm. See [piston-action-timing](/concepts/piston-action-timing.md) for the mechanism (rising edge at one depth, deeper falling edge in the same BE).[^gtmc-tree-farm-high-speed]

## Common generators

- **Comparator/repeater order (TT):** repeaters generally out-prioritize comparators, creating a falling edge after the 0-tick piston extends.[^gtmc-tree-farm-high-speed]
- **Redstone dust:** redstone dust is instantaneous; a QC'd sticky piston creates a rising edge at 1 piston depth and a falling edge at 2. (Dust turning only sends PP updates — extra NC updates are needed to complete the rising edge.)[^gtmc-tree-farm-high-speed]
- **Redstone redirection (dustless):** the only dustless method that outputs a *zero-delay rising edge* — see [dustless-wiring](/concepts/dustless-wiring.md).[^gtmc-tree-farm-dustless-wiring]

## Related

- [piston-action-timing](/concepts/piston-action-timing.md) — the 3gt default vs 0-tick
- [dustless-wiring](/concepts/dustless-wiring.md) — 0t generators without dust
- [high-speed-tree-farms](/concepts/high-speed-tree-farms.md) — why 0-tick matters

[^gtmc-tree-farm-high-speed]: [gtmc-tree-farm-high-speed.md](raw/articles/gtmc-tree-farm-high-speed.md)
[^gtmc-tree-farm-dustless-wiring]: [gtmc-tree-farm-dustless-wiring.md](raw/articles/gtmc-tree-farm-dustless-wiring.md)