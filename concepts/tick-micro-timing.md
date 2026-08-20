---
type: concept
title: Tick & Micro-Timing Model
created: 2026-08-18
updated: 2026-08-18

description: "Two timing scales: **inter-tick** (whole gt units) and **intra-tick** (ordering within one gt).^[raw/articles/gtmc-micro-timing-ticks.md] [^[raw/articles/gtmc-m…"
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, timing, source-gtmc]
sources:
- id: gtmc-micro-timing-ticks
  resource: https://www.techmc.wiki/en/articles/micro-timing/tick-timing
  title: GTMC Micro Timing Ticks
- id: gtmc-micro-timing-intra-tick
  resource: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
  title: GTMC Micro Timing Intra Tick
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Tick & Micro-Timing Model

Two timing scales: **inter-tick** (whole gt units) and **intra-tick** (ordering within one gt).[^gtmc-micro-timing-ticks] [[^gtmc-micro-timing-intra-tick]]

## Game tick
- Main loop ≈ 20/sec = **gt** (GameTick). RedstoneTick (rt) = 2gt.
- Lag metrics: **TPS** (normally 20) and **mspt** (lower = less lag).
- Most redstone components respond with a **macroscopic delay** measured in gt.[^gtmc-micro-timing-ticks]

## Repeater / Comparator delays
- Repeater: 1–4 rt = **2–8gt**. Comparator: always **2gt**.
- Repeater locked when side is powered by adjacent repeater/comparator.
- Comparator modes: Compare vs Subtract.[^gtmc-micro-timing-ticks]

## Intra-tick phases (within 1gt)
MC is single-threaded, so "same gt" events still sequence. Authoritative phase order: **WTU → TT → CT → BE → EU → TE → AT** (player actions at the END).[^gtmc-intra-tick-timing] [[^gtmc-scheduled-ticks]]

- **Instant components:** respond in any phase, triggered only by block updates — redstone dust, rails, fence gates, trapdoors, note blocks, dispensers/droppers, redstone lamp (on).
- **Delayed components:** scheduled-tick controlled, fixed phase — repeater/comparator/observer on-off (TT), redstone lamp off (TT), dispenser dispense (TT), falling-block decide (TT).[^gtmc-intra-tick-timing]

Key component phases: pistons extend/retract = **BE**; b36 pushes entity / lands = **TE**; b36 retracted+landed by sticky piston = **BE**; hopper absorb/transfer = **TE**.[^gtmc-intra-tick-timing] [[^gtmc-block-entities]]

> **Correction note:** the earlier version listed an abbreviated order ("AT→TT→BE→TE…"). The full GTMC intra-tick chapter gives the precise WTU→TT→CT→BE→EU→TE→AT order (player input last), corroborated by TMWiki's GameTick phase list. See [mc-timing-model](/concepts/mc-timing-model.md) for the authoritative order + component phase table.


> **Translation caveat:** the EN intra-tick page is flagged "Outdated translation" (lag: 1 source commit + 2 days) at fetch time. Decompiled vs 1.20.1-yarn. Treat exact phase names as version-sensitive.

> **Cross-source (TMWiki / Technical Minecraft Wiki):** `GameTick.md` lists the phase order as tile ticks → ChunkManager → BlockEvent → entities → block entities → player inputs, and notes rails/redstone dust are "recursive updators" (= our "instant" components). Substantially aligns with GTMC's AT→TT→BE→TE→EU model; difference is labeling, not contradiction. `TileTicks.md` confirms repeater 2/4/6/8gt + comparator 2gt and adds tile-tick priority (TTP) + 65536/tick cap. See [^tmwiki-game-tick] and [^tmwiki-tile-ticks].

## Related
- [update-theory](/concepts/update-theory.md) · [piston-mechanics](/concepts/piston-mechanics.md) · [piston-action-timing](/concepts/piston-action-timing.md)
- [0-tick](/concepts/0-tick.md) — depth within BE is what 0-tick exploits

[^gtmc-micro-timing-ticks]: https://www.techmc.wiki/en/articles/micro-timing/tick-timing
[^gtmc-micro-timing-intra-tick]: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
[^gtmc-intra-tick-timing]: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
[^gtmc-scheduled-ticks]: https://www.techmc.wiki/en/articles/micro-timing/scheduled-ticks
[^gtmc-block-entities]: https://www.techmc.wiki/en/articles/micro-timing/block-entities
[^tmwiki-game-tick]: TechMCDocs/pages (Technical Minecraft Wiki)
[^tmwiki-tile-ticks]: TechMCDocs/pages (Technical Minecraft Wiki)
