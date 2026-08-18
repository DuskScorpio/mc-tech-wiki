---
title: Piston Action Timing
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, timing, source-gtmc]
sources: [raw/articles/gtmc-tree-farm-basics.md]
---

# Piston Action Timing

In tree farms, a single piston action (push / pull / 0-tick) takes **3gt by default**.^[raw/articles/gtmc-tree-farm-basics.md]

| Power duration before action | Resulting action cost |
|---|---|
| default | 3gt |
| 1gt powering | 4gt |
| 2gt powering | 5gt |

## 0-tick

A **0-tick action** happens when a piston receives a rising edge at one depth and a falling edge at a *deeper* depth within the same BE phase — it extends on the rising edge, then retracts on the deeper falling edge. For sticky pistons, the pushed block arrives one piston depth deeper than the falling edge; pulling behaves normally.^[raw/articles/gtmc-tree-farm-basics.md]

Controlling the *rising* vs *falling* edge depth is the basis of [[0-tick]] generators and [[dustless-wiring]].

## Related

- [[mc-timing-model]] — depth and BE ordering
- [[0-tick]] — generators built on edge depth
