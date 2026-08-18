---
title: 4gt Tree Farm
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [farms, 4gt, tree-farm, high-speed, source-gtmc]
sources: [raw/articles/gtmc-tree-farm-4gt.md]
---

# 4gt Tree Farm

Tree farms that **run on a 4gt clock**. A piston action is 3gt, leaving 1gt idle per cycle. (A 3gt clock would need an autoclicker for bonemealing, which is traditionally not recognized — though 12gt/8gt mega spruce are exceptions.)^[raw/articles/gtmc-tree-farm-4gt.md]

## 4gt Birch

- **Three-shot + side suction** base; side-suction piston retracts at 2gt TE, so the horizontal piston extends immediately and retracts before 4gt BE.
- **Synchronized bonemealing** (one growth window per 4gt, so no cross bonemealing).
- AFK spot: crouch below the side suction, aim at the upper side corner of a dispenser.^[raw/articles/gtmc-tree-farm-4gt.md]

## Dustless 0t generators

Modular by necessity. Three families:^[raw/articles/gtmc-tree-farm-4gt.md]

- **Observer-based** (8gt single-edge 0t)
- **Redstone dust redirection** — best for controlling rising-edge depth
- **Wall power-based** — simple but bulky

Observation: you don't always need 0t — the observer's 2gt signal also works and is a key lag-reduction technique.^[raw/articles/gtmc-tree-farm-4gt.md]

## 4gt Multi-Species

- Uses **pseudo-double-recursion** (birch architecture can't handle branch trees). Branch timing from Fanhua Qianmu.
- **Jungle** only runs half a cycle (1/40 sapling rate); synchronize pseudo-double-recursions to process more leaves. Active sapling circulation historically needed, now eased by high leaf capacity.
- **Suction-to-push** log output: pull from above + push horizontally (wither-friendly), end double-recursion module, or honey-slime streams (less 0t, less lag).^[raw/articles/gtmc-tree-farm-4gt.md]

## Detection-based 4gt

The only dustless zero-delay rising-edge 0t is **redstone dust redirection** — space-hungry, so architecture matters most. Detection unit must reset within 4gt (or two sets within 8gt).^[raw/articles/gtmc-tree-farm-4gt.md]

## Related

- [[dustless-wiring]] · [[0-tick]] · [[bonemealing]] · [[tree-species-requirements]]
