---
type: source
source_url: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
ingested: 2026-08-18
sha256: 037b93d76028f6c789b22fab2a06f86bd31318e671abb63681c391da111e0954
---

# 03 Attempting to Design a Multi-Species Tree Farm (GTMC)

In the previous section, we completed the simplest tree farm. However, this tree farm can only process birch trees. To solve this, we attempt to design a multi-species tree farm.

## 1 Core Architecture Design

For a multi-species tree farm, the architecture needs to accommodate the growth requirements of every tree species it handles — taking the union, meeting the requirements of the most demanding species. We focus on five classic tree species: **Birch, Oak, Jungle, Spruce, and Acacia**.

### 1.1 Spruce Architecture Requirements
Spruce requires a 5x5 area centered on the sapling with no blocks obstructing growth. For trunk processing, we can use **triple recursion**, **pseudo-double recursion**, or **honey-slime double recursion**.

### 1.2 Acacia Architecture Requirements
Acacia grows up to 2 logs on the same y-level, extending along the x or z axis and at most 4 blocks away from the sapling. These logs can form straight lines, corners, etc. The main pusher alone cannot clear all the logs, so we need **side branch processing**. Two design approaches: **center consolidation** and **additional log outputs**.

### 1.3 Jungle Architecture Requirements
Jungle tree trunks can grow up to **12 blocks** tall, so we need a tall enough main pusher. Jungle saplings have a **1/40** drop rate, so we need extra leaf processing. From a top-down view, if no more than 5 columns of leaves within the 5x5 range go unprocessed, the farm can still collect enough jungle saplings. Strictly, you'd calculate average processing coverage; generally an average above 42 is enough to get sufficient jungle saplings.

### 1.4 Oak Architecture Requirements
Oak trees can randomly grow into **large oaks** (drumstick trees), so we need to height-limit them. The height-limiting block goes at **the 9th block above the dirt**.

For our example: **honey-slime triple recursion** on the main pusher, **center consolidation** for side branches, **honey-slime walls** for leaf processing, and manually placed obsidian for height limiting.

## 2 Block Stream to Drops Architecture Design

Because multi-species tree farms produce an irregular block stream output, we need to reorganize the block stream before feeding it into an explosion chamber.

For our example, all logs are output to the front of the trunk, with at most two blocks output per operating cycle. We can use two rows of pistons side by side to merge the two log outputs into a single 2-wide output, or a side-suction base to convert the two outputs into two outputs with a fixed interval (typically 6gt).

We try to avoid pushing out a 2-block-thick stream at once, because that greatly reduces the explosion chamber's processing efficiency and final drop recovery rate.

For multi-species tree farms, we can use two specialized explosion structures: **pure milk explosion chambers** ("milk explosions") and **b36 explosion chambers** ("push explosions") to handle large volumes of irregular block streams.

## 3 Wiring — Mode Switching and Speed Limiter

### 3.1 Acacia Timing Switching
For every tree species except acacia, we can push out both side honey-slime walls at the same time, shortening the processing cycle. Switching from normal timing to acacia timing is simply adding delay to the two side walls.

### 3.2 Automatic Oak Height Limiting
Many players find manually placing obsidian tedious. A solution: place a block that the main pusher can't push in the right spot to achieve height limiting. To send that block down (usually via a flying machine), we can only use pushable blocks.

### 3.3 Jungle and Acacia Height Increase (1.14 and below)
In version 1.14 and below, jungle and acacia growth detection checks a 3x3 area for the trunk and 5x5 for the canopy. This means we can place blocks within the 5x5 area below a certain height (typically 5 blocks above the dirt) to force jungle and acacia trees that would grow too short to reach a minimum height. Even in 1.20.1, dark oak retains the same growth requirements (centered on the northwest corner sapling), so we can still "height-boost" dark oak.

### 3.4 Speed Limiter
Trees can grow before the architecture has fully reset, triggering the detection structure prematurely and breaking the farm. So we add a speed limiter to the detection structure. The limiter's timing must also account for the operating timing (reset time) of the rest of the farm in each mode.

*Created: 2024-12-28 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
