---
type: source
source_url: https://www.techmc.wiki/en/articles/block-update/update-concepts
ingested: 2026-08-18
sha256: 72b6087008866547d967a62b0b7d36511adb3d4a84bfc710f02cdd540a4d847f
---

# 01 Update Concepts and Update Types (GTMC)

Blocks notify each other of changes via "updates." An update carries no details about what changed.

## Update types
- **NC Update** (neighborChanged / updateNeighbors): emitted on place, break, or significant state change. Order is **West East Down Up North South**. Detected by BUD devices.
- **PP Update** (updateShape / getStateForNeighborUpdate): almost all changes emit it. Order is **West East North South Down Up**. Detected by Observers. Reflects change to the block itself; NC notifies neighbors to recheck.
- **Comparator Update**: special notification for comparators when container contents change. Does not affect non-comparator blocks.
- **Self-inspection** (onPlaced): redstone components check state on placement. Note blocks skip it; pistons self-inspect after extending and after retracting.

## NC update properties
- Update source = the block emitting. For most blocks it's the block itself.
- NC order W E D U N S. PP order W E N S D U.
- Blocks whose current state differs from intended state are **BUD devices** (Block Update Detectors).
- **QC (quasi-connectivity):** pistons, sticky pistons, droppers, dispensers count as powered when the block ABOVE them (even air) receives power. Powering via the space above = QC powering. A QC-powered piston that hasn't received an NC update is in a BUD state.

## Comparator updates
- Emitted by: container item-count changes, composter fill changes, etc.
- Reaches comparators horizontally adjacent or within 2nd-order range through a signal-transmitting block.
- Signal strength: general containers = avg fill ratio * 14 + 1; lecterns = (page-1)/(pages-1)*14 + 1.
- **CUD** (Comparator Update Detector): comparator whose state differs from intended.

## setBlockState flags (9-bit)
- NOTIFY_NEIGHBORS=1 (NC update), NOTIFY_LISTENERS=2 (sync), NO_REDRAW=4, REDRAW_ON_MAIN_THREAD=8, FORCE_STATE=16, SKIP_DROPS=32, MOVED=64, SKIP_REDSTONE_WIRE_STATE_REPLACEMENT=128, SKIP_BLOCK_ENTITY_REPLACED_CALLBACK=256, SKIP_BLOCK_ADDED_CALLBACK=512.
- NOTIFY_ALL=3 (NC+listeners). FLAG bit4=0 generates PP update.

## Observer exception
Observer emits PP-first-then-NC on toggle (calls setBlockState in scheduledTick for PP, then updateNeighbors for NC) — opposite of most blocks.

*Created/Last edited per GTMC. License CC BY-NC-SA 4.0.*
