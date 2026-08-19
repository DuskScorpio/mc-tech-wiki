---
type: source
source_url: https://www.techmc.wiki/en/articles/block-mechanics/block-changes
ingested: 2026-08-18
sha256: 83e35f8d6dc8eb9e626c21772e6648586204ba9c511f1459645c6b704b50b1c2
---

# 02 Placing, Changing, and Breaking Blocks (GTMC, decompiled 1.20.1-yarn)

## 1 Common entry: World#setBlockState(pos, state, flags)
All block changes pass through this in 1.20.1. Steps: (1) check height limits; (2) WorldChunk#setBlockState writes subchunk/palette/heightmaps/lighting/block-entities; (3) notify systems per flags (client sync, NC updates, PP chain).
Three-step model: Determine pos+new state -> Write into chunk -> Notify per flags.

## 2 Placing (BlockItem#place)
- Determines correct state FIRST via getPlacementState (player look / environment), THEN writes. Not default-then-adjust.
- Default flags: NOTIFY_ALL | REDRAW_ON_MAIN_THREAD.
- After write: BlockStateTag (from item NBT), onPlaced, BLOCK_PLACE game event, consume item (non-creative). If write fails, follow-up skipped.

## 3 Changing existing block state
Lever/button/trapdoor take new state from old, call setBlockState same pos. Block type unchanged; BlockState replaced. flags control NC/PP.

## 4 Block entity changes
On chunk state write, compares whether old/new states require a BE. BE cannot exist without BlockState.

## 5 Player breaking (ServerPlayerInteractionManager#tryBreakBlock)
Flow: tool canMine check -> operator perm -> adventure restriction -> onBreak -> removeBlock (-> setBlockState) -> onBroken -> tool damage -> drops (if harvestable). removeBlock(false) => MOVED flag NOT set.
Subtle: breaking WATERLOGGED block -> coords become FLUID state, not air. World#removeBlock gets FluidState then writes fluid's block state. Not an extra water placed after.

## 6 Why chain of updates after write
One local write changes "what is at coords"; to keep neighbors consistent, game may emit NC/PP. This is where block-update theory starts.

## 8.1 setBlockState source
3 steps: write chunk; notify per flags; run PP chain (if FORCE_STATE not set and maxUpdateDepth>0). maxUpdateDepth default 512 limits PP propagation.

## 8.4 removeBlock
`removeBlock` -> setBlockState(pos, fluidState.getBlockState(), NOTIFY_ALL | (move?MOVED:0)). => water remains after waterlogged break.

## 8.5 breakBlock
General entry (commands/updates). Differs from player mining: handles drops BEFORE replacing state.

## 8.6 tryBreakBlock
permission -> onBreak -> removeBlock -> onBroken -> tool damage -> drops.
