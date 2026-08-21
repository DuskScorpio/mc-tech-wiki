---
type: concept
title: Glossary (Technical Minecraft terms)
created: 2026-08-18
updated: 2026-08-18

description: English term + definition reference for Technical Minecraft (Java).
edition: java
version: any
confidence: high
tags: [glossary, reference]
sources:
- id: techmc-glossary
  resource: https://github.com/TechMC-Glossary/TechMC-Glossary
  title: TechMC Glossary (GitHub)
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Glossary

English term + definition reference for Technical Minecraft (Java).
Terms sourced from the TechMC-Glossary project (community-standard definitions).[^techmc-glossary]

> This wiki is English-only. Term definitions here are for disambiguation within the vault;
> for in-game item/block names, Mojang official naming applies.

## General / Mechanics

- **0-tick** (`0t`) — Usually refers to a redstone signal that is shorter than 1gt. Also used to describe a piston extending and retracting within the same game tick.
- **Block 36 (aka Moving Piston)** (`B36`)
- **Block Entity (aka Tile Entity)**
- **Block Event** (`BE`)
- **Block Event Delay/Depth** (`BED`) — Usually refers to piston updating other pistons in a chain reaction within a single game tick. Since pistons activate during the block event phase of the tick (kind of) and things execute in the order they are scheduled, having something be activated by a piston that was updated by a chain of three other pistons before it (BED 3) will always happen before something that was activated by a BED 5 event.
- **Block Tick (aka Tile Tick)**
- **Block Update Detector** (`BUD`) — A device that has something happen when it receives an update.
- **Chunk Tick** (`CT`)
- **Chunk Ticket**
- **Comparator Update**
- **Comparator Update Detector (aka Tile Entity Update Detector)** (`CUD`) — Refers to a comparator that will change its signal once it either receives a block or inventory update. It is based on the behavior inherent to comparators where they don't notice inventory changes when reading it through a solid block (including an inventory being moved away or put in place, like a composter being moved by a piston). The CUD will then change it's signal once it either receives a block or inventory update.
- **Data Update Detector (aka Comparator Update Detector)** (`DUD`) — Refers to a comparator that will change its signal once it either receives a block or inventory update. It is based on the behavior inherent to comparators where they don't notice inventory changes when reading it through a solid block (including an inventory being moved away or put in place, like a composter being moved by a piston). The CUD will then change it's signal once it either receives a block or inventory update.
- **Dust Updateless** — Some contraptions are not Dustless, but the dust they use does not get updated (does not change ss). This can be because it is either used to steadily power a component, or because it's used by redirecting it, but not changing ss. Redirecting dust is really lag friendly, as lag usage goes. These terms are therefore often used interchangeably.
- **Dustless** (`DL`) — Usually refers to dust update-less contraption, but it can also be used to state the absence of redstone dust within a contraption.
- **Entity Update** (`EU`)
- **Farm** — Machines for the production of resources in particular
- **Game Tick (aka Tick)** (`gt`) — Minecraft iteratively runs its processing code in a loop. One cycle of this loop is called a Tick or Gametick (gt). Gameticks are also used as the default measurement of time while working with redstone. The game attempts to run 20 gameticks a second (20tps), but will fail to do so and slow down the game if the server is lagging (>50mspt).
- **Honey Slime** (`HS`) — Honey and slime blocks
- **Hopper Line**
- **Instant**
- **Instant Wire** — Refers to a contraption or wiring that can send signal instantly
- **Liquid Update Detector** (`LUD`) — Refers to a device that uses liquids to detect a special set of updates, some of which can be detected with a Block Update Detector, with a Comparator Update Detector or with an observer, but some of which are exclusively detected by LUDs. After detecting the update and triggering, it usually resets the liquid to a state where it can detect an update again.
- **MicroTiming**
- **Milliseconds Per Tick** (`MSPT`) — A measurement of how many milliseconds it takes to process each gametick. If a server exceeds 50MSPT in total, then the game will slow down, as there is no longer enough time to process all 20 ticks per second. MSPT is also used as a measure of how performance-intensive a contraption is by seeing how much the MSPT increases by running/loading it.
- **Moving Piston (aka Block 36)**
- **Neighbor Change** (`NC`)
- **Nether Tree** — Refers to huge fungus.
- **Network Update/Async Task** (`NU/AT`)
- **Next Tick Entry(aka Tile Tick)** (`NTE`)
- **Pistonless** — Used to tag contraptions that makes no use of pistons.
- **Post Placement (aka Shape Update)** (`PP`)
- **Quasi Connectivity** (`QC`) — The effect of quasi-powering a piston, dropper or dispenser. A good way to visualize when a block is being quasi-powering is to imagine a redstone lamp above the component. If that lamp was to be on in that location, the block is quasi-powered. Quasi-powering usually doesn't update the component being QCed, which results in the component not "realizing" it should activate or deactivate until it receives an update. For this reason, QC is often used for Block Update Detector, and people even sometimes say "BUD powered" rather than "quasi powered".
- **Random Tick & Climate (RTC)**
- **Redstone Tick** (`rt`)
- **Scheduled Tick (aka Tile Tick)**
- **Shape Update(aka Post Placement)**
- **Slime-less** — Adjective. Usually refers to the absence of slime ball and slime blocks of a contraption.
- **Slimestone** — Flying machine related technology.
- **Smart Piston** — Usually referred to a piston that automatically extends when a block is placed in front of it
- **TNT Duping**
- **TNT Looting**
- **Tick (aka Game Tick)** (`t`) — Minecraft iteratively runs its processing code in a loop. One cycle of this loop is called a Tick or Gametick (gt). Gameticks are also used as the default measurement of time while working with redstone. The game attempts to run 20 gameticks a second (20tps), but will fail to do so and slow down the game if the server is lagging (>50mspt).
- **Ticks Per Second** (`TPS`) — A measurement of how many gameticks are happening each second. The game normally operates at 20TPS, but if MSPT exceeds 50ms then the game will start to slow down. Mods such as Carpet Mod are able to stop, slow down, or speed up the tick speed of a server, which can be useful for testing.
- **Tile Entity (aka Block Entity)** (`TE`)
- **Tile Entity Update Detector (aka Comparator Update Detector)** (`TEUD`) — Refers to a comparator that will change its signal once it either receives a block or inventory update. It is based on the behavior inherent to comparators where they don't notice inventory changes when reading it through a solid block (including an inventory being moved away or put in place, like a composter being moved by a piston). The CUD will then change it's signal once it either receives a block or inventory update.
- **Tile Tick (aka Block Tick)** (`TT`)
- **Tile Tick Priority** (`TTP`)
- **Update Order**
- **Wither Skeleton** (`Wiske`)
- **World Time Update** (`WTU`)
- **{count} tick** (`{count}t`) — {count} amount of game ticks.
## Glitch

- **CCE Suppression (aka Cast (Update) Suppression/Shulker Suppression)** — Refers to a type of update suppression/suppressor based on CCE that is state-less and does not require reset, broken in ≥1.20.2. This can be achieved by using Tile Entity Swap to make a shulker box have a tile entity that is not a container, and make a comparator read from the box. Updating the comparator (with Block Update or Comparator Update) will make the box attempt to treat the non-container tile entity as container tile entity to calculate output, which then throws a CCE. The suppressor can also be toggled by powering the comparator.
- **Cast (Update) Suppression (aka CCE Suppression/Shulker Suppression)** — Refers to a type of update suppression/suppressor based on CCE that is state-less and does not require reset, broken in ≥1.20.2. This can be achieved by using Tile Entity Swap to make a shulker box have a tile entity that is not a container, and make a comparator read from the box. Updating the comparator (with Block Update or Comparator Update) will make the box attempt to treat the non-container tile entity as container tile entity to calculate output, which then throws a CCE. The suppressor can also be toggled by powering the comparator.
- **OOM (Update) Suppression** — Short for OutOfMemory Suppression. A type of update suppression by filling up the memory and causing an OOM error.
- **Shulker Suppression (aka Cast (Update) Suppression/CCE Suppression)** — Refers to a type of update suppression/suppressor based on CCE that is state-less and does not require reset, broken in ≥1.20.2. This can be achieved by using Tile Entity Swap to make a shulker box have a tile entity that is not a container, and make a comparator read from the box. Updating the comparator (with Block Update or Comparator Update) will make the box attempt to treat the non-container tile entity as container tile entity to calculate output, which then throws a CCE. The suppressor can also be toggled by powering the comparator.
- **Stack Overflow (Update) Suppression**
## Mechanical

- **Double Piston Extender** (`DPE`)
- **Triple Piston Extender** (`TPE`)
## Tree Farm

- **Balloon Oak** — A fancy oak generated with the smallest size possible. It consists of a tall trunk and leaves that form a spherical shape, similar to a balloon. However, it is also sometimes being referred as the fancy oak itself.
- **Corner Retraction** — Tree farming term. Refers to a type of bottom log processing for big spruce tree farms by removing the corner log first in gt0 to allow sapling planting at that spot.
- **Cross Bone Meal** (`XBM`) — Tree farming term. Asynchronous application of bone meal to a sapling with multiple dispensers, usually used to differentiate from synced bone meal
- **Dark Oak** (`Doak`)
- **Leaf Detection** — Tree farming term. Refers to a method of detecting tree growth by utlising the updates from leaves branching out from the bottom log when tree grows.
- **N Core** — In huge fungus farming community, it refers to a farm with multiple tileable cores (usually n≫1) that the player travels between planting consecutively at each one
- **Push Limit Detection/Detector** (`PLD`) — A method or contraption that outputs when the input is push limited, usually used in tree farming community.
- **Retract Through Dirt** — Tree farming term. Refers to log being retracted downwards through the planting block (dirt or nylium) with pistons and being moved away
- **Side Retraction** — Usually refers to pulling a block sideways, often used to describe bottom log processing in tree farm community.
- **Synced Bone Meal** — Tree farming term. Synchronous application of bone meal to a sapling with all the dispensers, usually used to differentiate from cross bone meal

## Related
- [tree-farm-overview](/concepts/tree-farm-overview.md) — terms used across the farm pages
- [mc-timing-model](/concepts/mc-timing-model.md) — gt, tile tick, micro-timing

[^techmc-glossary]: [techmc-glossary.md](raw/articles/techmc-glossary.md)