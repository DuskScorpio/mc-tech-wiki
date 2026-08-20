---
type: concept
title: Continuous Updates (DFS Propagation)
created: 2026-08-18
updated: 2026-08-18

description: "An update is a **process**, not a single event: NC update fires first and triggers a chain of events, then PP update fires."
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, updates, source-gtmc]
sources:
- id: gtmc-block-update-continuous
  resource: https://www.techmc.wiki/en/articles/block-update/continuous-updates
  title: GTMC Block Update Continuous
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Continuous Updates (DFS Propagation)

An update is a **process**, not a single event: NC update fires first and triggers a chain of events, then PP update fires. Blocks always emit **NC first, PP second**.[^gtmc-block-update-continuous]

## Propagation is depth-first (stack)
Think of it as exploring a cavern: pushing NC onto a stack = "going deeper", popping = "returning". A BUD rail chain example:

- NC order: `A1->B1->C1->D1->C2->B3->C3->B4`
- PP order: `D1->C1->C2->B1->C3->B3->B4->A1`[^gtmc-block-update-continuous]

## A longer chain (rails 1-5 E-W, note block pressed)
- NC order: `1->2->3->4->5->6->7`
- PP order: `5->7->6->4->3->2->1`[^gtmc-block-update-continuous]

## Direction order
NC update direction order is **West, East, Down, Up, North, South**. Order of NC updates to the block ABOVE varies (near-to-far vs far-to-near) depending on traversal direction.[^gtmc-block-update-continuous]

## Related
- [update-theory](/concepts/update-theory.md) — the update types this builds on
- [special-update-behaviors](/concepts/special-update-behaviors.md) — dust 2nd-order changes the locational order

[^gtmc-block-update-continuous]: [gtmc-block-update-continuous.md](raw/articles/gtmc-block-update-continuous.md)