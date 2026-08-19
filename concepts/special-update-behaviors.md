---
type: concept
title: Special Update Behaviors
created: 2026-08-18
updated: 2026-08-18

description: Several blocks break the simple 1st-order neighbor model.^[raw/articles/gtmc-block-update-special.md]
edition: java
version: 1.20.1
confidence: high
contested: False
tags: [mechanics, updates, source-gtmc, version-sensitive]
sources:
- id: gtmc-block-update-special
  resource: https://www.techmc.wiki/en/articles/block-update/special-updates
  title: GTMC Block Update Special
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Special Update Behaviors

Several blocks break the simple 1st-order neighbor model.[^gtmc-block-update-special]

## Redstone dust — 2nd-order neighbor updates
- On power change, dust emits a **2nd-order neighbor update**: its own position AND the 6 adjacent blocks each act as update sources (Manhattan distance 2 from the dust).
- Source order is set by a hash of the dust's coordinates (the "locational nature"). 7 sources fall into 3 groups with ~97% probability: `-Y,+Z,+X` | `O` (self) | `+Y,-Z,-X`. Group arrangement is random; within-group order fixed.[^gtmc-block-update-special]

## Diagonal rails
- A diagonally placed powered rail, on powered-state change, emits two update groups (up/self/down via onStateReplaced, then self via updateNeighbors).[^gtmc-block-update-special]

## Rail chain recursive power check
- A rail receiving an NC update recursively searches the chain for a directly powered rail within **distance 8** (counting connected rails as 1 each). Recursion checks -x or +z first by orientation.
- Quirk: a flat rail may be considered connected to an apparently-unconnected diagonal rail (one-directional).[^gtmc-block-update-special]

## Lit observer placed by piston — no neighbor NC update
- When a piston pushes a lit observer into position and **no observer scheduled tick is queued at the destination**, it does NOT emit the usual piston-movement NC update to neighbors (except the output-face block). On arrival, onBlockAdded sees powered=true + no queued tick → sets powered=false (PP) and updates neighbors (NC only to output face). Net effect: neighbors don't get the standard NC update.[^gtmc-block-update-special]

## Related
- [update-theory](/concepts/update-theory.md) · [continuous-updates](/concepts/continuous-updates.md)
- [dustless-wiring](/concepts/dustless-wiring.md) — dust redirection exploits dust's locational updates
[^gtmc-block-update-special]: https://www.techmc.wiki/en/articles/block-update/special-updates
