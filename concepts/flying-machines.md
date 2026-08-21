---
type: concept
title: Flying Machines (Slime Tech)
created: 2026-08-18
updated: 2026-08-18

description: Basic Slime Tech flying machines — 9gt/10gt/12gt periods, observer activation, mounting and extension; the foundation of movable contraptions.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, slime-tech, flying-machine, source-gtmc]
sources:
- id: gtmc-flying-machine-basics
  resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/flying-machine-basics
  title: GTMC Flying Machine Basics
- id: gtmc-slime-introduction
  resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/introduction
  title: GTMC Slime Introduction
generated: { by: /, at: 2026-08-18T00:00:00Z }
status: stable
---

# Flying Machines (Slime Tech)

A flying machine is a self-propelling structure built from pistons, Observers, and Slime/Honey blocks. Because Minecraft blocks have no momentum, a structure can be "walked" forward one block at a time by alternating piston pushes and pulls.[^gtmc-flying-machine-basics][^gtmc-slime-introduction]

## Principle
A regular Piston ("right foot") stays put while a sticky piston pulls the rear section; then the rear regular Piston pushes the front section into place; an Observer fires and the sticky piston pulls the rear again. Inserting a sequentially activating circuit turns this into a continuous mover.[^gtmc-flying-machine-basics]

## Simple machines (by period)
- **9gt unidirectional** — right-facing regular Piston + left-facing sticky piston (right = forward). Break the topmost Block of Redstone to start. Period **9gt**.[^gtmc-flying-machine-basics]
- **10gt observer bidirectional** — both activations via Observers; period **10gt**. Observer pulses are short, so the sticky piston pushes without pulling back and the rear regular Piston can become a sticky piston. Centrally symmetric -> moves both ways. **Almost all simple Slime Tech flying machines are 10gt variants of this.**[^gtmc-flying-machine-basics]
- **12gt piston-BUD** — regular + sticky + regular Piston (L→R). Pre-1.11 (pre-Observer); now obsolete.[^gtmc-flying-machine-basics]

## Mounting and extension
- **Mounting:** reshape + attach blocks; e.g. Mango's World Eater bomber is a 10gt machine with mounted pistons/Observers. Mounted Observers + pistons let the machine interact with the world (e.g. "Grave Marker" reshapes 6-high pillars).[^gtmc-flying-machine-basics]
- **Extension:** a single piston's 12-block push limit constrains size, so extend via forward regular Pistons (push) or backward sticky pistons (pull) — e.g. a 10gt engine extended with a 12-block dual TNT duplicator.[^gtmc-flying-machine-basics]
- Simple flying machines are called **"engines"**; "mounting" subsumes extension. Beyond this: engines + mounting/extension + integrating multiple machines.[^gtmc-flying-machine-basics]

> **Confidence:** high. Single GTMC source (SlimeTech/Twisuki, 1.20.1). Period figures (9/10/12gt) and the observer-activation mechanism are stated explicitly. No cross-source yet — Discovering-Minecraft is CN-only (out of scope per language rule), so this page is currently single-sourced; flag for corroboration if a 2nd English source is found.

## Related
- [Piston Mechanics](/concepts/piston-mechanics.md) — the pushes/pulls a flying machine sequences
- [Rails](/concepts/rails.md) — directional connectivity; flying-machine rails use similar update logic
- [0-Tick](/concepts/0-tick.md) — intra-tick timing that flying-machine circuits rely on
- [Glossary](/concepts/glossary.md) — slime/honey, observer term definitions

[^gtmc-flying-machine-basics]: [gtmc-flying-machine-basics.md](raw/articles/gtmc-flying-machine-basics.md)
[^gtmc-slime-introduction]: [gtmc-slime-introduction.md](raw/articles/gtmc-slime-introduction.md)