---
source_url: https://www.techmc.wiki/en/articles/block-update/special-updates
ingested: 2026-08-18
sha256: 51541b9f115f1b2814f75edea081fd304808dac6abd7ad7c10d267d2268add6e
---

# 03 Special Update Behaviors (GTMC)

## 1 Redstone Dust 2nd-order neighbor updates
- Redstone dust power change emits a **2nd-order neighbor update**: uses its own position AND the 6 adjacent blocks as update sources, each sending 6-direction NC updates. (1st-order = Manhattan distance 1; 2nd-order = distance 2.)
- Update source order determined by hash of dust coordinates (locational nature). 7 sources split into 3 groups with ~97% probability: `-Y,+Z,+X` | `O` | `+Y,-Z,-X`.
- Group order is random; within-group order fixed. Probabilities: first/last swap 24.267% each; O in middle 12.133% each; other arrangements <0.2%.

## 2 Diagonal rails
- When a diagonally placed powered rail's powered state changes, it emits two groups of updates (call-stack documented: onStateReplaced emits up/self/down, then updateNeighbors emits self).

## 3 Redstone dust code
- (Advanced; setBlockState with FLAG=3 path referenced.)

## 4 Rail chain recursive check
- A rail, when receiving NC update, checks if powered by recursively searching the chain for a directly powered rail within **distance 8**.
- Recursion always checks -x (W) or +z (S) first depending on orientation. A flat rail may be considered connected to an apparently-unconnected diagonal rail (one-directional quirk).

## 5 Lit observer placed without neighbor NC updates
- When a piston pushes a lit observer into position and no observer scheduled tick is queued at destination, it does NOT emit the usual piston-movement NC update to neighbors (except the output-face block). Uses setBlockState flags=67 then 3. On arrival, onBlockAdded sees powered=true, no scheduled tick queued -> sets powered=false (PP), updates neighbors (NC only to output face). Net: no neighbor NC update except output direction.

*Created 2024-12-30 | Last edited 2026-07-13. License CC BY-NC-SA 4.0.*
