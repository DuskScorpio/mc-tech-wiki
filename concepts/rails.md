---
type: concept
title: Rails (Powered / Activator / Detector)
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: Rails are a core redstone component (and a favorite in dustless wiring).
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, rails, redstone-phase, source-gtmc, source-tmwiki]
resource: "https://www.techmc.wiki/en/articles/redstone-components/rails"
sources: [raw/articles/gtmc-rails.md, raw/articles/tmwiki-rail-budding.md]
---

# Rails (Powered / Activator / Detector)

Rails are a core redstone component (and a favorite in dustless wiring). Powered and Activator Rails share the `PoweredRailBlock` class, so their update behavior is identical at the source level; their differing effects on minecarts are handled by the minecart, not the rail.^[raw/articles/gtmc-rails.md]

## NC update emission (when activation state changes)
- **Flat rail:** emits **4** NC updates, sources **itself → below → itself → below**.^[raw/articles/gtmc-rails.md]
- **Sloped rail:** emits **6** NC updates, sources **above → itself → below → itself → below → above** (top-end notifiers only when sloped).^[raw/articles/gtmc-rails.md]

TMWiki independently confirms the above→self→below notifier order (top only if sloped): "Block updates notifiers are always from above to below, top notifier if the rail is sloped, then notifier on self, and finally notifier below."^[raw/articles/tmwiki-rail-budding.md]

These NC updates are what let a rail drive adjacent pistons, BUDs, and dustless 0t generators — a rail changing state is an **instant** component.

## Activation: direct vs indirect
A rail activates either:
- **Directly** — adjacent to a redstone signal source; or
- **Indirectly** — among the 8 rails *connected* to it, at least one is directly adjacent to a signal source.^[raw/articles/gtmc-rails.md]

## "Connected" is a directional search (diode behavior)
A non-directly-activated rail **searches** along the chain (up to 8 blocks, TMWiki says 9 including itself) for a connected, directly-activated rail:
- **Flat rail** checks: both ends at same height; both ends one block lower.
- **Sloped rail** checks: lower end at same height; lower end one block lower; higher end one block higher.
- Connectivity depends only on the rail's **own** shape, the next rail's **position**, and the next rail's **direction** — **not** the next rail's shape.^[raw/articles/gtmc-rails.md]

Therefore **connectivity is unidirectional**: rail A may consider B connected while B does not consider A connected. This yields one-directional rail chains that act like a diode.^[raw/articles/gtmc-rails.md] ^[raw/articles/tmwiki-rail-budding.md]

**Search direction order:** each end searched independently, unidirectionally (no backtracking). N–S rails search south then north; E–W rails search west then east. Which rails count as connected thus depends on distance *and* search-direction order.^[raw/articles/gtmc-rails.md]

## Rail BUD (budding)
If a rail is updated but is already in the correct state, it sends **no further updates** — so a chain can become BUDded (stuck powered with no source within range). General BUD methods (dust redirection, moving detector rail) also work on rails; long budded lines can be rebudded to make instant BUD wires.^[raw/articles/tmwiki-rail-budding.md]

> **Confidence:** high. GTMC rails article (1.20.1) and TMWiki RailBudding independently agree on the NC-notifier order and the directional/diode connectivity. TMWiki states the search limit as 9 rails including itself vs GTMC's "within 8 blocks" — minor wording difference (9 inclusive vs 8 exclusive); both describe the same reach. Detector Rail update behavior is not yet documented in either source (GTMC marks it incomplete).

## Related
- [dustless-wiring](/concepts/dustless-wiring.md) — rails are the instant component that makes dustless 0t generators work
- [piston-mechanics](/concepts/piston-mechanics.md) — rails drive adjacent pistons via the NC updates above
- [update-theory](/concepts/update-theory.md) — NC updates emitted by rails
- [special-update-behaviors](/concepts/special-update-behaviors.md) — rails in the "instant component" class
- [glossary](/concepts/glossary.md) — rail-related term definitions
