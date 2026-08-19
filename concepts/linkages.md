---
type: concept
title: Linkages (Slime Tech)
created: 2026-08-18
updated: 2026-08-18

description: Zero-delay piston-chain motion transfer in Slime Tech — sticky-piston retraction has zero delay; BUD-state pistons move instantly on update. The timing backbone of large movable structures.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, slime-tech, linkage, source-gtmc]
resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/linkages
sources:
- id: gtmc-linkages
  resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/linkages
  title: GTMC Linkages
generated: { by: /, at: 2026-08-18T00:00:00Z }
status: stable
---

# Linkages (Slime Tech)

A **linkage** passes "motion" along a chain of pistons (each pushes only 12 blocks). Chains need carefully tuned delays; longer chains = trickier timing. The valuable kind is the **zero-delay linkage**.[^gtmc-linkages]

## Zero-delay piston retraction
- Sticky pistons respond instantly extending **or** retracting: the instant they act, pushed/pulled blocks convert to `b36`, then 2gt later (motion done) convert back.[^gtmc-linkages]
- **Extension chain:** the next piston only fires after the block settles, so each piston adds delay.
- **Retraction chain:** the instant the Redstone Block becomes `b36`, the signal vanishes and the previous piston responds immediately -> **zero delay**.[^gtmc-linkages]
- Piston transmission timing (lever at t0): t0 AT lever; t1 BE piston1 extends; t3 TE redstone1 placed; t4 BE piston2 extends; t6 TE redstone2; t7 BE piston3; t9 TE redstone3… (extension adds per-piston delay).[^gtmc-linkages]
- Common unit: upward sticky piston for zero-delay transmission + downward regular piston to reset it. Used in ilmango's world-eater docking frame.[^gtmc-linkages]

## Bidirectional / BUD linkages
- **BUD-based retraction (Eular's narrow-trench world eater):** sticky piston activated by a Redstone Block at the BUD position; "loses power" the instant it retracts + Redstone Block becomes b36, but re-extends once settled -> must push down in the window after retract before re-extend.[^gtmc-linkages]
- **Bidirectional (comet107's expandable tunnel bore):** activatable from any position; symmetric Redstone-Block connections on both sides; transmits motion downward.[^gtmc-linkages]
- **BUD-state linkage:** a BUD piston moves when it receives an update; stationary→moving is itself an update, so the signal transmits instantly and all modules move together. Used in burst tunnel bores (if blocked at the front, the linkage oscillates in place and can't advance -> transmits burst signals).[^gtmc-linkages]

> Single GTMC source (1.20.1). The zero-delay retraction fact is precise and testable; corroborate with a 2nd source if available. Connects to [Piston Mechanics](/concepts/piston-mechanics.md) (b36, 3gt action) and [Tick Micro Timing](/concepts/tick-micro-timing.md) (BE/TE phases).

## Related
- [Piston Mechanics](/concepts/piston-mechanics.md) — b36, sticky-piston 3gt action, push limit
- [Flying Machines](/concepts/flying-machines.md) — engines these linkages synchronize
- [Slime Tech Engines and Mobility](/concepts/slime-tech-engines.md) — engine/mobility framing
- [Tick Micro Timing](/concepts/tick-micro-timing.md) — BE (piston extend) / TE (block placed) phases
- [Glossary](/concepts/glossary.md) — b36, BUD, observer definitions
[^gtmc-linkages]: https://www.techmc.wiki/en/articles/slime-tech/twisuki/linkages
