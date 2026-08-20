---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
ingested: 2026-08-18
sha256: 1d3ae2dc5bfe1f4e34684f96e7eb48dfe383c43c1a104767565b41649cc3f4f9
---

# 02 A First Look at Intra-Tick Timing (GTMC)

> Note: this EN page is flagged "Outdated translation" (lag: 1 source commit + 2 days) at fetch time. Decompiled against 1.20.1-yarn.

## Intra-tick timing
- Within a single 1gt there is finer ordering ("micro-timing"). MC runs single-threaded, so same-gt events still execute in a priority order.
- Observing intra-tick: build a contraption where two things are "same gt" yet sequence appears (e.g. one piston extends, other doesn't).

## Phase division of 1gt
MC roughly follows this intra-tick sequence (main phases for analysis):
AT (Player Action) -> NU (Network/?) -> TT (Tile Tick / Scheduled Tick) -> BE (Block Event) -> TE (Block Entity / Tick Entity) -> EU (Entity Update) -> ... (full order per GTMC source analysis).

- **Instant components**: behavior can occur in any phase, triggered only by block updates. E.g. redstone dust, rails, fence gates, trapdoors, note blocks, dispensers/droppers, redstone lamp on.
- **Delayed components**: controlled by scheduled ticks, occur in specific phase (TT). E.g. repeater/comparator/observer on-off (TT), redstone lamp off (TT), dispenser dispense (TT), falling block decide (TT).

## Common component operating phases (table)
| Component | Phase |
| Command block runs | TT |
| Repeater/Comparator/Redstone Torch/Observer on-off | TT |
| Redstone Dust, Rails state change | Instant |
| Fence Gates, Trapdoors | Instant |
| Hopper state change (redstone) | Instant |
| Hopper absorb/transfer items | TE |
| Note Block/Bell state change | Instant |
| Note Block/Bell sound | BE |
| Dispenser/Dropper state change | Instant |
| Dispenser dispense / Dropper drop | TT |
| Redstone Lamp on | Instant |
| Redstone Lamp off | TT |
| Button/Pressure Plate/Tripwire on | Instant (limited to EU/AT in practice) |
| Button/Pressure Plate/Tripwire off | TT |
| Falling block decide | TT |
| Falling block fall/land | EU |
| Piston extend/retract | BE |
| b36 (moving_piston) pushes entity | TE |
| b36 natural land | TE |
| b36 retracted+landed by sticky piston | BE |

*Created 2024-12-21 | Last edited 2026-07-12. License CC BY-NC-SA 4.0.*
