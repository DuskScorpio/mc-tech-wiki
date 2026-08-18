---
source_url: https://www.techmc.wiki/en/articles/block-update/continuous-updates
ingested: 2026-08-18
sha256: 2c18e8bf9cee8a87982ca71804c5eaefab166beb98e08a04354dce1171b4897d
---

# 02 Continuous Block Updates and Analysis Methods (GTMC)

## General behavior
Blocks always emit updates in order **NC first, PP second**. An update is a "process," not a single event: NC update triggers events, those trigger more events, THEN PP update fires.

## Update order analysis (DFS)
Updates propagate depth-first (stack). "Placing torches" = pushing NC onto stack; "picking up" = popping (PP). For a BUD rail chain:
- NC update order: A1->B1->C1->D1->C2->B3->C3->B4
- PP update order: D1->C1->C2->B1->C3->B3->B4->A1

## Common analysis examples
- BUD rail chain (rails 1-5 E-W, note block pressed): NC order 1->2->3->4->5->6->7; PP order 5->7->6->4->3->2->1.
- NC update direction order: **West, East, Down, Up, North, South**.
- Order of NC updates to the block ABOVE: from north to south (near to far) in one example; from far to near in another depending on traversal.

*Created 2024-12-14 | Last edited 2026-08-01. License CC BY-NC-SA 4.0.*
