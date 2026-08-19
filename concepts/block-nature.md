---
type: concept
title: Block Nature (Block vs BlockState)
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: In source, **`Block`** and **`BlockState`** are distinct.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, source-gtmc]
resource: "https://www.techmc.wiki/en/articles/block-mechanics"
sources: [raw/articles/gtmc-block-mechanics.md, raw/articles/gtmc-blocks-and-states.md, raw/articles/gtmc-block-changes.md]
---

# Block Nature (Block vs BlockState)

In source, **`Block`** and **`BlockState`** are distinct. `Block` is the shared rule set for one kind of block (all oak stairs share one `StairsBlock` instance); `BlockState` records the current property values (facing, half, shape, waterlogged). A `Block` defines *what a block can become and how its rules change*; a `BlockState` records *which values it currently has*.^[raw/articles/gtmc-blocks-and-states.md]

## Properties and finite states
A `BlockState` is a fixed set of `Property` → value pairs. You **cannot** add a property on the fly; out-of-range `.with()` throws. Example: `StairsBlock` declares `facing(4) × half(2) × shape(5) × waterlogged(2) = 80` states, all pre-generated at registration and looked up in O(1) via a with-table. `state.with(p,v)` returns another **immutable** prebuilt state — it never mutates the original.^[raw/articles/gtmc-blocks-and-states.md]

## Storage: subchunks + palettes
A subchunk (`ChunkSection`, 16×16×16, up to 24 per chunk at Y −64…319) stores `PalettedContainer<BlockState>` — a palette of which states appear plus 4096 IDs, **not** 4096 objects. Same-state blocks share one immutable `BlockState` instance.^[raw/articles/gtmc-blocks-and-states.md]

## Default state
`StateManager.getDefaultState()` is the first enumerated combination (e.g. piston default `facing=north, extended=false`). It is the **starting point** for constructing other states — placement runs `getPlacementState` from it via `.with(player look)`, it does NOT mean all placed pistons face north.^[raw/articles/gtmc-blocks-and-states.md]

## BlockState vs BlockEntity vs NBT
`BlockState` holds finite-valued data (facing, on/off, power, age, waterlogged). Variable data (chest 27 slots, sign text, hopper cooldown) lives in a **`BlockEntity`** as **NBT** ("JSON with types"). `BlockEntity ≠ Entity`. Whether a position has a BE is decided first by its `BlockState`; BE data is stored separately from the palette. Fluid state is *derived* from `BlockState` (e.g. `waterlogged=true`).^[raw/articles/gtmc-blocks-and-states.md]

## The write path: `World#setBlockState`
In 1.20.1 nearly every block change flows through `World#setBlockState(pos, state, flags)`:
1. bounds check;
2. `WorldChunk#setBlockState` writes subchunk palette + heightmaps + lighting + block entity;
3. notify per `flags`.^[raw/articles/gtmc-block-changes.md]

**Flag constants** (drive post-write behavior): `NOTIFY_NEIGHBORS=1` (NC updates), `NOTIFY_LISTENERS=2` (client sync), `NOTIFY_ALL=3`, `FORCE_STATE=16` (skip PP chain), `SKIP_DROPS=32`, `MOVED=64` (piston-moved).^[raw/articles/gtmc-blocks-and-states.md]

**Placement** (`BlockItem#place`): computes the correct state *first* via `getPlacementState`, then writes with `NOTIFY_ALL | REDRAW_ON_MAIN_THREAD`. If the write fails, follow-up logic is skipped.^[raw/articles/gtmc-block-changes.md]

**Breaking** (`ServerPlayerInteractionManager#tryBreakBlock`): `onBreak → removeBlock → onBroken → tool damage → drops`. `removeBlock` replaces the position with the **fluid state**, not air — so a waterlogged block leaves water behind (the water was never a separate block placed after). `breakBlock` (commands/updates) additionally drops items *before* replacing the state.^[raw/articles/gtmc-block-changes.md]

> **Confidence note:** upgraded from `medium` to `high` after ingesting GTMC's two `block-mechanics` sub-articles (blocks-and-states, block-changes), which fully specify the Block/BlockState model and the `setBlockState` write path for 1.20.1.

## Related
- [piston-mechanics](/concepts/piston-mechanics.md) — piston uses BlockState EXTENDED + getPlacementState; FORCE_STATE skips PP (QC)
- [update-theory](/concepts/update-theory.md) — NC/PP updates emitted by setBlockState
- [tick-micro-timing](/concepts/tick-micro-timing.md) — block changes trigger updates that propagate intra-tick
- [moving-block-b36](/concepts/moving-block-b36.md) — b36 is a BlockState of moving_piston
