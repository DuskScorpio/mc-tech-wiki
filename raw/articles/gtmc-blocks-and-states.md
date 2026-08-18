---
source_url: https://www.techmc.wiki/en/articles/block-mechanics/blocks-and-states
ingested: 2026-08-18
sha256: 4d848be2979cc2f2ce022781bb7acf7f0ee92f7af33c2a53ca6956613b58bed3
---

# 01 Blocks and Block States (GTMC, decompiled 1.20.1-yarn)

## 1 Block = rule set; BlockState = current values
`Block` is the shared rules for one kind of block (all oak stairs share one StairsBlock instance). `BlockState` records the current values (facing, half, shape, waterlogged). Block defines "what it can become + how rules change"; BlockState records "current values".

## 2 Properties & values
A BlockState = set of Property + values. Constraints: cannot add a new property on the fly. StairsBlock declares 4 properties: facing(4) × half(2) × shape(5) × waterlogged(2) = 80 states, all pre-generated at registration; O(1) lookup via withTable. `state.with(property,value)` does NOT mutate; returns another prebuilt immutable state; out-of-range value throws.

## 3 One coordinate -> one BlockState (not just Block)
World query returns BlockState. Subchunk stores `PalettedContainer<BlockState>`. Same-state blocks share the same immutable BlockState object.

## 4 Subchunks & palettes
Subchunk = ChunkSection, 16×16×16, up to 24 per chunk (Y -64..319). Palette stores "which states appear" as IDs + 4096-index array (like indexed color). Not 4096 objects.

## 5 Default state
`StateManager.getDefaultState()` = first enumerated combination. Piston default facing=north, extended=false. NOT "all new pistons face north" — placement uses `getPlacementState` from default + .with(player look). Default state = starting point; all states reachable via finite .with() calls.

## 6 What BlockState can store
Finite-valued: facing, on/off, power, age, waterlogged. Variable data (chest 27 slots, sign text, hopper cooldown) -> BlockEntity (NBT). BlockEntity ≠ Entity. Not every block has BE; presence decided by BlockState; stored as NBT in chunk's BE section (separate from palette).

## 7 NBT
Named Binary Tag = "JSON with types". BlockStateTag (item), BlockEntityTag. Division: BlockState = "what/where/facing/on-off"; NBT = "chest contents / sign text / hopper cooldown".

## 8 Fluid state
`getFluidState` derives from BlockState (e.g. waterlogged=true -> water). Not separately stored.

## 9 Why state changes matter
Lever pull / trapdoor / dust power: block TYPE unchanged; BlockState changes; still rewritten to chunk -> may trigger updates.

## 11.6 Block flag constants (in setBlockState flags)
NOTIFY_NEIGHBORS=1 (NC updates); NOTIFY_LISTENERS=2 (client sync); NOTIFY_ALL=3; NO_REDRAW=4; REDRAW_ON_MAIN_THREAD=8; FORCE_STATE=16 (skip PP chain); SKIP_DROPS=32; MOVED=64 (piston-moved).
