---
title: Special Update Behaviors
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
contested: false
tags: [mechanics, updates, source-gtmc, version-sensitive]
sources: [raw/articles/gtmc-block-update-special.md]
---

# Special Update Behaviors

Several blocks break the simple 1st-order neighbor model.^[raw/articles/gtmc-block-update-special.md]

## Redstone dust — 2nd-order neighbor updates
- On power change, dust emits a **2nd-order neighbor update**: its own position AND the 6 adjacent blocks each act as update sources (Manhattan distance 2 from the dust).
- Source order is set by a hash of the dust's coordinates (the "locational nature"). 7 sources fall into 3 groups with ~97% probability: `-Y,+Z,+X` | `O` (self) | `+Y,-Z,-X`. Group arrangement is random; within-group order fixed.^[raw/articles/gtmc-block-update-special.md]

## Diagonal rails
- A diagonally placed powered rail, on powered-state change, emits two update groups (up/self/down via onStateReplaced, then self via updateNeighbors).^[raw/articles/gtmc-block-update-special.md]

## Rail chain recursive power check
- A rail receiving an NC update recursively searches the chain for a directly powered rail within **distance 8** (counting connected rails as 1 each). Recursion checks -x or +z first by orientation.
- Quirk: a flat rail may be considered connected to an apparently-unconnected diagonal rail (one-directional).^[raw/articles/gtmc-block-update-special.md]

## Lit observer placed by piston — no neighbor NC update
- When a piston pushes a lit observer into position and **no observer scheduled tick is queued at the destination**, it does NOT emit the usual piston-movement NC update to neighbors (except the output-face block). On arrival, onBlockAdded sees powered=true + no queued tick → sets powered=false (PP) and updates neighbors (NC only to output face). Net effect: neighbors don't get the standard NC update.^[raw/articles/gtmc-block-update-special.md]

## Related
- [[update-theory]] · [[continuous-updates]]
- [[dustless-wiring]] — dust redirection exploits dust's locational updates
