---
type: concept
title: 0-tick
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: A 0-tick action moves functionality from inter-tick into intra-tick timing — the main way to speed up a tree farm.
edition: java
version: 1.20.1
confidence: high
tags: [techniques, 0-tick, timing, source-gtmc]
resource: "https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro"
sources: [raw/articles/gtmc-tree-farm-high-speed.md, raw/articles/gtmc-tree-farm-dustless-wiring.md]
---

# 0-tick

A 0-tick action moves functionality from inter-tick into intra-tick timing — the main way to speed up a tree farm. See [piston-action-timing](concepts/piston-action-timing.md) for the mechanism (rising edge at one depth, deeper falling edge in the same BE).^[raw/articles/gtmc-tree-farm-high-speed.md]

## Common generators

- **Comparator/repeater order (TT):** repeaters generally out-prioritize comparators, creating a falling edge after the 0-tick piston extends.^[raw/articles/gtmc-tree-farm-high-speed.md]
- **Redstone dust:** redstone dust is instantaneous; a QC'd sticky piston creates a rising edge at 1 piston depth and a falling edge at 2. (Dust turning only sends PP updates — extra NC updates are needed to complete the rising edge.)^[raw/articles/gtmc-tree-farm-high-speed.md]
- **Redstone redirection (dustless):** the only dustless method that outputs a *zero-delay rising edge* — see [dustless-wiring](concepts/dustless-wiring.md).^[raw/articles/gtmc-tree-farm-dustless-wiring.md]

## Related

- [piston-action-timing](concepts/piston-action-timing.md) — the 3gt default vs 0-tick
- [dustless-wiring](concepts/dustless-wiring.md) — 0t generators without dust
- [high-speed-tree-farms](concepts/high-speed-tree-farms.md) — why 0-tick matters
