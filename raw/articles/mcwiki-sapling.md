---
source_url: https://minecraft.wiki/w/Sapling
source_repo: Minecraft Wiki (minecraft.wiki)
ingested: 2026-08-18
sha256: cf97664d865c9ff7da80dd5612828b3816ca52eb401e873c0dee9fef42f4647b
---

# Sapling (Minecraft Wiki)

## Growth (JE relevant)
- 8 sapling variants: oak, birch, spruce, jungle, acacia, dark oak, pale oak, cherry (+ poplar upcoming).
- Grow on all dirt variants (except dirt path) or moss blocks. JE: only placeable on those normally, but can still grow on other blocks.
- Two growth stages before the tree (3rd stage). Bone meal speeds growth even without sufficient light. Otherwise light level >= 9 above required to advance stage.
- 2x2 pattern: dark oak & pale oak MUST be 2x2; oak/spruce/jungle CAN be 2x2 (mega variants); birch/acacia/cherry are 1x1 only.

## Space required above (JE)
| Sapling | 1x1 min space above | 2x2 |
|---|---|---|
| Oak | 5 (3x3 column); a block in growth space -> forced large variant | nothing |
| Birch | 6 (3x3) | nothing |
| Spruce | 6 (5x5) single; giant 14 (5x5 centered on NW sapling) as 2x2 | Mega Spruce / Mega Pine |
| Jungle | 5 (3x3) single; giant 11 (5x5 centered on NW) as 2x2 | Mega Jungle |
| Acacia | 6 (5x5) | nothing |
| Dark Oak | 7 (3x3 centered on NW sapling) and MUST be 2x2 | Dark Oak |
| Cherry | 8 (5x5) | nothing |

## 2x2 search order (JE)
- Spruce/jungle search for a 2x2 in order SE, NE, SW, NW; only first found 2x2 tries to grow; others act as obstructions.
- A sapling in >1 overlapping 2x2 always fails (later 2x2 always contains a sapling in the required space of an earlier one).
- Except giant jungle/spruce, growth not affected by nearby same-level blocks.
- JE: blocks in #replaceable_by_trees tag treated as empty; logs/wood/leaves are exceptions (don't stop growth).

## Drop rates (leaves)
- Leaves decay/broken (no shears/Silk Touch): 5% sapling drop, except jungle 2.5%.
- Fortune: I 6.25% (jungle 2.78%), II 8.33% (3.125%), III 10% (4.17%).
- Composting a sapling: 30% raise level 1; a stack averages 2.74 bone meal.

## Bone meal note
- Bone meal grows sapling even without sufficient light (matches GTMC: bonemealing forces growth attempt).
