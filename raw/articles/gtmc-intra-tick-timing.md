---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
ingested: 2026-08-18
sha256: 86178fc2fce7ad35dde20bcdc034be8554094281e3e76ffc10a04fb4cc04a606
---

# 02 A First Look at Intra-Tick Timing (GTMC)

## 1 Observing intra-tick timing
MC is single-threaded; within one gt events always execute in a fixed priority order. The fine timing within one gt is **intra-tick timing**. Observed via contraptions where everything is "same gt" but still sequences.

## 2 Micro-Timing Theory
### 2.1 Phase division (authoritative order within 1gt):
1. **World Tick Update (WTU)** — world "timer" increments by 1; nth tick = WTU that brings timer to n.
2. **Scheduled Tick / Tile Tick / NTE (TT)** — delayed components (repeater/comparator/etc.) execute here.
3. **Chunk Tick (CT)** — lightning, snow, Random Tick (crop growth, grass spread, water freeze) for chunks near player.
4. **Block Event (BE)** — piston push/pull, note block sound. Piston adds block event when actual state != powered state; BE-phase-added events run same phase, others queue for next BE. Piston places b36 at target during BE.
5. **Entity Update (EU)** — entity movement, AI, TNT explosions, monster attacks; non-player pressure-plate/tripwire activation (redstone) here.
6. **Block Entity / Tile Entity (TE)** — hoppers absorb/transfer; b36 pushes entities during first two TE after creation, reverts on third TE.
7. **Async Task / Network Update (AT/NU)** — player actions (network packets) executed at END of each tick.

### 2.2 Instant
Behavior occurs in ANY phase, triggered only by block updates = **instant component**. (redstone dust, rails, fence gates, trapdoors, note/bell state, dispenser/dropper state, hopper state, lamps on, buttons/plates/tripwire on, falling-block decide+fall is EU not instant)

### 2.3 Delayed
Scheduled-tick-controlled, fixed phase (TT). (repeater/comparator/observer on-off, lamp off, dispenser dispense, falling-block decide)

### 2.4 Component phase table (key rows)
- Command block run: TT
- Repeater/Comparator/Redstone Torch/Observer on-off: TT
- Redstone Dust, Rails state change: Instant
- Fence Gates, Trapdoors: Instant
- Hopper state change: Instant; Hopper absorb/transfer: TE
- Note/Bell state: Instant; sound: BE
- Dispenser/Dropper state: Instant; dispense/drop: TT
- Redstone Lamp on: Instant; off: TT
- Button/Plate/Tripwire on: Instant; off: TT
- Falling block decide: TT; fall/land: EU
- Piston extend/retract: BE
- b36 push entity: TE; b36 natural land: TE; b36 retracted+landed by sticky piston: BE

### 2.5 Basic analysis example
Rising edge: 0AT lever pulled -> 0AT piston adds BE -> 1BE extend -> 3TE redstone block lands -> 3TE 2nd piston adds BE -> 4TT cmd reads 4 -> 4BE 2nd piston extends -> 6TE block lands -> 7TT cmd reads 7.
Falling edge: 0AT off -> 0AT piston adds BE -> 1BE retract -> 1BE block removed -> 1BE 2nd piston adds BE -> 1BE 2nd retract -> 3TE both land -> 4TT both read 4.
