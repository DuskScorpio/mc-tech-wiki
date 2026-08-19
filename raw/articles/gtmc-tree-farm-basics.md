---
type: source
source_url: https://www.techmc.wiki/en/articles/block-update
ingested: 2026-08-18
sha256: 6b2f1612fd660d51aa94b7987edde937f53114b777738b3e5fc77b9aacc491ad
---

# 01 Prerequisites and the Basic Structure of Tree Farms (GTMC)

## 1 Prerequisites

This section briefly covers the basics you need before diving into tree farm research. For simplicity, some content here is technically "incorrect." For fuller explanations, see the Update Theory and Timing Theory sections of GTMC.

### 1.1 Updates

In Minecraft, updates come in two types: **NC updates** and **PP updates**.

The main sources of **NC updates** in tree farms are **TT (Tile Tick) components** (typically Redstone Repeaters, Comparators, and Observers), **Redstone Dust**, **powered or activated rails** (called "rails" from here on, since tree farms rarely involve the other two types), **Pistons** along with the blocks they push/pull, and **Note Blocks**.

When these components change state (e.g., becoming powered or activated, or a block changing), they send **NC updates**. These are **NC updates** and can be detected by **BUDs**.

Since tree farm structures are mostly made of Pistons, all **NC updates** in tree farms generally come with **PP updates** as well. Observers specifically detect **PP updates**.

In tree farms, pure PP updates (without accompanying NC updates) typically come from: [wireless redstone section — tree power, scaffolding power, wall power].

### 1.2 Timing

In Minecraft, timing comes in two forms: **inter-tick timing** and **intra-tick timing**.

Each second is split into 20 game ticks, or gt. Some components have fixed macroscopic delays, such as Repeaters (2-8gt), Comparators and Observers (2gt). Apart from TT components, other components used in tree farms generally have no macroscopic delay.

Each gt is further divided into multiple phases that execute different operations. The phases most relevant to tree farms, in order of execution, are: [NU, TT, BE, TE — names per GTMC].

Apart from the components listed above, **instant components** execute their operations immediately upon receiving an update, regardless of which phase the update is in. Common instant components include Redstone Dust and rails, Fence Gates and Trapdoors, Note Blocks, Droppers and Dispensers.

The execution order of TT components depends on macroscopic timing, TT priority, and sub-order. In practice, TT components execute in this order: Any Repeater >= Comparator pointing to a Comparator > general Comparator or Observer.

BE components (Pistons and Note Blocks) execute in the order they receive updates and confirm a state change is needed. This ordering is sometimes called **depth**. Note Blocks do not increase depth (i.e., they don't delay the execution of the components they update within BE).

When analyzing timing, look at macroscopic timing first, then which phase the operation falls in, and finally the execution order within that phase.

In tree farms, each Piston action (push/pull/0t) takes **3gt** by default. Piston actions triggered by **1gt and 2gt** powering take **4gt and 5gt** respectively.

## 2 Basic Structure of Tree Farms

From Minecraft 1.15 onward, a tree farm's basic structure consists of:

- Bonemealing
- Trunk Processing
- Leaf Processing
- Sapling Recycling

Most tree farms also include a **detection** module that detects sapling growth and triggers the farm, but this isn't required.

In Minecraft 1.14 and below, jungle and acacia trees have special growth detection requirements, so tree farms sometimes need a **height increase** module. Spruce trees require no logs in a 5x5 area to grow, which means a **retractable wall** is needed. This article focuses on 1.15+ tree farms, so we'll skip these cases for now.

### 2.1 Bonemealing
Typically, **Dispensers** fire Bone Meal onto saplings. Since Dispensers hold very little Bone Meal, it's usually fed in through **Hoppers or Droppers**, with an **unloader** transferring Bone Meal from Shulker Boxes into the Hopper or Dropper chain.

### 2.2 Trunk Processing
Main trunk processing is straightforward: move the trunk away from where it grew. The basic approaches are **triple push extension** and **pseudo double push extension**. For birch and oak, a simple push/pull setup works fine.

The most widely used design today is honey-slime wall double push extension.

Root processing generally has four approaches: processing alongside the main trunk, **upward push**, **downward pull**, and **side pull**. For dark oak, an **upward pull** method is sometimes used.

### 2.3 Leaf Processing
Use Pistons or honey-slime walls to push away enough leaves to get the saplings you need. Each leaf block has a fixed chance to drop a sapling: jungle 1/40, all other tree types 1/20.

### 2.4 Sapling Recycling
Saplings dropped by the leaf processing module are collected near the player using **Hoppers**, **water flow**, or similar methods. In tree farms with fast processing cycles and tight internal space, **Hopper Minecarts** are sometimes used.

### 2.5 Block-to-Drop Conversion
There are two main methods: **Wither** and **TNT**.

*Created: 2025-02-02 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
