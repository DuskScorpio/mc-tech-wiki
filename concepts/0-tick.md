---
title: 0-tick
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [techniques, 0-tick, timing, source-gtmc]
sources: [raw/articles/gltmc-tree-farm-high-speed.md, raw/articles/gltmc-tree-farm-dustless-wiring.md]
---

# 0-tick

A 0-tick action moves functionality from inter-tick into intra-tick timing — the main way to speed up a tree farm. See [[piston-action-timing]] for the mechanism (rising edge at one depth, deeper falling edge in the same BE).^[raw/articles/gltmc-tree-farm-high-speed.md]

## Common generators

- **Comparator/repeater order (TT):** repeaters generally out-prioritize comparators, creating a falling edge after the 0-tick piston extends.^[raw/articles/gltmc-tree-farm-high-speed.md]
- **Redstone dust:** redstone dust is instantaneous; a QC'd sticky piston creates a rising edge at 1 piston depth and a falling edge at 2. (Dust turning only sends PP updates — extra NC updates are needed to complete the rising edge.)^[raw/articles/gltmc-tree-farm-high-speed.md]
- **Redstone redirection (dustless):** the only dustless method that outputs a *zero-delay rising edge* — see [[dustless-wiring]].^[raw/articles/gltmc-tree-farm-dustless-wiring.md]

## Related

- [[piston-action-timing]] — the 3gt default vs 0-tick
- [[dustless-wiring]] — 0t generators without dust
- [[high-speed-tree-farms]] — why 0-tick matters
