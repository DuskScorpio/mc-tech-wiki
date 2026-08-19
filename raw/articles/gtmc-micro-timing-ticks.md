---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/tick-timing
ingested: 2026-08-18
sha256: 63b3b30edb1045df27814582a241ffd7b8fe69ee9666ba640e44ba1637aad9f0
---

# 01 Tick and Inter-Tick Timing (GTMC)

## Game tick
- Main loop runs ~20 times/sec = **GameTick (gt)**. RedstoneTick (rt) = 2gt.
- Lag metrics: **TPS** (ticks/sec, normally 20) and **mspt** (ms/tick; lower = less lag).
- Most redstone components have delayed (macroscopic) responses measured in gt.

## Repeater / Comparator
- Repeater delay = its gear setting (1-4 rt = 2-8gt). Comparator always 2gt.
- Repeater: amplifies any non-zero signal to strength 15 after its delay. Side powered by adjacent repeater/comparator -> "locked" (input ignored until side ends).
- Comparator: Compare mode (output front unless max(side) > front) vs Subtract mode (output front - max(side) if >=0).

## Charging theory
- Chargeable blocks have **strong charging** (powers dust in all 6 directions) vs **weak charging** (only powers repeaters/comparators/etc. facing it).
- Strong charge: by powered/active components, observer output, etc. Weak charge: by redstone dust pointing into a block, etc.
- Most blocks are chargeable; non-chargeable = glass, slabs, half-slabs, chests, pistons/sticky pistons (don't cut lines).

## Inter-tick timing / analysis
- Example: lever -> 8gt repeater -> strong charge -> comparator (subtract, 14 side / 15 front -> 2gt) -> lamp at 10gt total. Compare-mode path gives 8gt.

*Created 2024-12-14 | Last edited 2026-07-13. License CC BY-NC-SA 4.0.*
