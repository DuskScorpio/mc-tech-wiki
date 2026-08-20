---
type: concept
title: Piston Action Timing
created: 2026-08-18
updated: 2026-08-18

description: In tree farms, a single piston action (push / pull / 0-tick) takes **3gt by default**.[^gtmc-tree-farm-basics]
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, timing, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Piston Action Timing

In tree farms, a single piston action (push / pull / 0-tick) takes **3gt by default**.[^gtmc-tree-farm-basics]

| Power duration before action | Resulting action cost |
|---|---|
| default | 3gt |
| 1gt powering | 4gt |
| 2gt powering | 5gt |

## 0-tick

A **0-tick action** happens when a piston receives a rising edge at one depth and a falling edge at a *deeper* depth within the same BE phase — it extends on the rising edge, then retracts on the deeper falling edge. For sticky pistons, the pushed block arrives one piston depth deeper than the falling edge; pulling behaves normally.[^gtmc-tree-farm-basics]

Controlling the *rising* vs *falling* edge depth is the basis of [0-tick](/concepts/0-tick.md) generators and [dustless-wiring](/concepts/dustless-wiring.md).

## Related

- [mc-timing-model](/concepts/mc-timing-model.md) — depth and BE ordering
- [0-tick](/concepts/0-tick.md) — generators built on edge depth

[^gtmc-tree-farm-basics]: [gtmc-tree-farm-basics.md](raw/articles/gtmc-tree-farm-basics.md)