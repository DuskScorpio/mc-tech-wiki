---
type: concept
title: Update Theory (NC / PP / Comparator / Self-Inspection)
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: Minecraft blocks notify each other of changes via **updates**; an update carries no details about what changed.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, updates, timing, source-gtmc]
resource: "https://www.techmc.wiki/en/articles/block-update/update-concepts"
sources: [raw/articles/gtmc-block-update-concepts.md]
---

# Update Theory (NC / PP / Comparator / Self-Inspection)

Minecraft blocks notify each other of changes via **updates**; an update carries no details about what changed. Four kinds matter for redstone:^[raw/articles/gtmc-block-update-concepts.md]

## NC Update (neighborChanged / updateNeighbors)
- Emitted on place, break, or significant state change.
- **Order: West East Down Up North South.**
- Detected by **BUD devices**.

## PP Update (updateShape / getStateForNeighborUpdate)
- Almost all changes emit it. **Order: West East North South Down Up.**
- Detected by **Observers** (the face detects PP; red dot outputs).
- Reflects change to the block itself; NC notifies neighbors to recheck.

## Comparator Update
- Special notification for comparators on container-content changes. Does not affect non-comparator blocks.
- Reaches comparators horizontally adjacent or within 2nd-order range through a signal-transmitting block.
- Signal: general containers `avg fill * 14 + 1`; lecterns `(page-1)/(pages-1)*14 + 1`.
- **CUD** = comparator whose current state differs from intended.^[raw/articles/gtmc-block-update-concepts.md]

## Self-inspection (onPlaced)
- Redstone components recheck state on placement. Note blocks skip it; pistons self-inspect once after extending and once after retracting.

## QC and BUDs
- **QC (quasi-connectivity):** pistons, sticky pistons, droppers, dispensers count as powered when the block ABOVE them (even air) is powered. A QC-powered piston with no NC update is a **BUD device** (state ≠ intended).^[raw/articles/gtmc-block-update-concepts.md]
- This is why BUDs detect NC but not PP, and why QC powering needs a separate NC update to actuate.

## setBlockState flags (9-bit, for the curious)
`NOTIFY_NEIGHBORS=1` (NC), `NOTIFY_LISTENERS=2`, `FORCE_STATE=16`, `MOVED=64`, `SKIP_BLOCK_ADDED_CALLBACK=512`, `NOTIFY_ALL=3`. FLAG bit4=0 → PP update emitted.^[raw/articles/gtmc-block-update-concepts.md]

## Observer exception
Observer emits **PP-first-then-NC** on toggle (opposite of most blocks).^[raw/articles/gtmc-block-update-concepts.md]

> **Cross-source (TMWiki / Technical Minecraft Wiki):** TMWiki's "block update" = GTMC's NC, and "state update" = GTMC's PP. It independently confirms: redstone dust sends state updates diagonally in some conditions but won't trigger observers there; trapdoors send PP but NOT NC (so a piston BUD won't detect them — matches our BUD/PP distinction); comparator updates are detected only by comparators within 1-block range through a conductive block. See ^[raw/articles/tmwiki-block-updates.md].

## Related
- [continuous-updates](/concepts/continuous-updates.md) — DFS propagation & order analysis
- [special-update-behaviors](/concepts/special-update-behaviors.md) — redstone dust 2nd-order, diagonal rails, lit-observer quirk
- [mc-timing-model](/concepts/mc-timing-model.md) · [piston-mechanics](/concepts/piston-mechanics.md)
