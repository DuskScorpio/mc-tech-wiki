---
type: source
source_url: https://www.techmc.wiki/en/articles/slime-tech/twisuki/linkages
ingested: 2026-08-18
sha256: e96456f04100dd9d40e58d7029bc1c3cc9d167b055d63d82fdd1a31773d4319d
---

# 31 Linkages (GTMC SlimeTech / Twisuki)

"Linkage" = passing motion along a chain of pistons (each pushes only 12 blocks). Tuning delays is the hard part; longer chains = trickier timing. Focus: "zero-delay linkages".

## 1 Unidirectional linkage based on piston retraction
- Sticky piston chain **retraction has zero delay**. Sticky pistons respond instantly extending OR retracting: the instant they act, pushed/pulled blocks convert to `b36`, then 2gt later (motion finishes) convert back.
- Extension chain: next piston only fires after the block settles, so each piston adds delay.
- Retraction: the instant the Redstone Block becomes `b36`, the signal vanishes and the previous piston responds immediately -> zero delay.
- Piston transmission timing table (lever at tick 0): t0 AT lever; t1 BE piston1 extends; t3 TE redstone1 in place; t4 BE piston2 extends; t6 TE redstone2; t7 BE piston3; t9 TE redstone3... (extension adds per-piston delay).
- Common structure: each unit uses an upward sticky piston for zero-delay transmission + a downward regular piston to reset it. Used in ilmango world-eater docking frame.

## 2 Extensions
- a) BUD-based retraction linkage (Eular's narrow-trench world eater): sticky piston activated by Redstone Block at BUD position; "loses power" the instant it retracts + Redstone Block becomes b36, but re-extends once it settles -> must push down in the window after retract before re-extend. Observer at bottom fires immediately once regular piston + glass update it.
- b) Bidirectional linkage (comet107's expandable tunnel bore): activatable from any position; symmetric connection to Redstone Blocks on both sides; transmits motion downward. Green part moves first (takes Redstone Block), blue part later (slight micro-timing difference).

## 3 BUD-based linkages
- A BUD-state piston moves on receiving an update; stationary->moving is itself an update, so signal transmits instantly and all modules move together.
- Used in burst tunnel bores: if blocked at the front, the linkage oscillates in place and can't advance -> useful for transmitting burst signals.

## 4 Other linkages
- "Linkage" originally means zero-delay, but functionally any structure moving multiple modules together counts.
