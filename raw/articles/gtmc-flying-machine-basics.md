---
source_url: https://www.techmc.wiki/en/articles/slime-tech/twisuki/flying-machine-basics
ingested: 2026-08-18
sha256: a804e67281ddba74873b3fccd3aa51155ee5f49001e1a69dbf5cb3dcbe7d5f6c
---

# 13 Flying Machine Basics (GTMC SlimeTech / Twisuki)

## Principle
Minecraft blocks have no momentum, so a "stepping on your right foot with your left foot" trick moves a structure forward 1 block: a regular Piston ("right foot") stays put while a sticky piston pulls the rear; then the rear regular Piston pushes the front; the Observer fires and the sticky piston pulls the rear again. Insert a sequentially activating circuit -> a flying machine.

## Simple flying machines
- **9gt unidirectional:** right-facing regular Piston + left-facing sticky piston. Right = forward. Break topmost Block of Redstone to start. Sticky piston first pulls rear section; rear regular Piston (powered by Block of Redstone) pushes front; Observer fires; sticky piston pulls rear again. Period **9gt**.
- **10gt observer bidirectional:** switch both activations to Observers. Period becomes **10gt**. Observer signal is short -> sticky piston pushes without pulling back, so rear regular Piston can become a sticky piston. Centrally symmetric -> moves both directions. **Almost all simple Slime Tech flying machines are 10gt variants of this.**
- **12gt piston-BUD:** regular Piston + sticky piston + regular Piston (L->R). Pre-1.11 (no Observers), now obsolete.

## Mounting and extension
- **Mounting:** change shape + attach blocks (e.g. Mango's World Eater bomber section is a 10gt machine with pistons/Observers mounted). Can add Observers + pistons for block interaction (e.g. "Grave Marker" converts 6-high pillars to a shape).
- **Extension:** single piston 12-block push limit is a constraint, so extend via forward regular Pistons (push) or backward sticky pistons (pull). Example: 10gt engine extending forward with a 12-block dual TNT duplicator.
- Terminology: simple flying machines = "engines"; "mounting" includes extension. Door to flying machines = engines + mounting/extension + integrating multiple machines.
