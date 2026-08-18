---
source_url: https://www.techmc.wiki/en/articles/tree-farm/4gt-farms
ingested: 2026-08-18
sha256: 6a10ba95286e6bf3e0be0abecdfa169620852c507aa54e880bf171366800051f
---

# 07 Everything About 4gt Tree Farms (GTMC)

This chapter requires maximum integration of previous knowledge. Although detection-based 4gt tree farms exist and are complex, we will briefly discuss them at the end. All other tree farms here **run on a 4gt clock**.

Since a piston action takes 3gt, you could run the tree farm on a 3gt clock, but this would require using an autoclicker for bonemealing. Traditionally, any tree farm using an autoclicker is not recognized. However, 12gt and 8gt mega spruce have now become exceptions.

## 1 4gt Birch
We start with the simplest: 4gt birch. The 4gt main trunk and base are relatively independent.

### 1.1 Core Architecture and Timing Design
Two typical architectures discussed (an ancient one and Xinghe's). Each cycle contains "one piston action" (all pistons perform one synchronized action), requiring only 3gt, so this serves as a 4gt tree farm architecture.

### 1.2 4gt Base and Sapling Circulation System
For 4gt, **three-shot + side suction** is a more convenient choice. Since the side suction piston completes the retraction action at 2gt TE, we make the horizontally extending piston extend immediately and retract before 4gt BE ends. The side suction architecture leaves an AFK position: standing below the side suction, crouching (sneaking), aiming at the upper side corner of one of the dispensers.

We do bone meal supply first. Since clock-based 4gt tree farms only have one tree-growing window every 4gt, we do not use alternating bonemealing, but use **synchronized bonemealing**. For sapling circulation, since 4gt brings a large number of items, we generally use 3-4 droppers to throw saplings to the player.

## 2 Dustless 4gt Wiring — Dustless 0t Generators
Tree farms designed based on dustless 4gt wiring must be modular.

### 2.1 Observer-Related 0t Generators — observer-based 8gt cycle "single-edge" 0t generator.
### 2.2 Redstone Dust Redirection-Related 0t Generators — the most convenient 0t method for controlling the rising edge signal depth.
### 2.3 Wall Power-Based 0t Generators — simple design, not used much due to volume.

## 3 4gt Multi-Species
### 3.1 Branch Trees — Basic Timing for Acacia/Azalea/Cherry Blossom. We cannot use the birch architecture; the pseudo-double-recursion architecture becomes our only choice. All 4gt multi-species use the branch tree processing timing from Fanhua Qianmu.
### 3.2 Special Handling for Azalea and Cherry Blossom — inserting double recursion complicates rising-edge control; plexi's "just pull the piston away" solution.
### 3.3 Jungle Wood — due to jungle's 1/40 sapling drop rate, 4gt tree farms only run half of each cycle. Jungle sapling circulation is the biggest obstacle. We synchronize the pseudo-double-recursion used to extract the trunk.
### 3.4 Log Output — Suction-to-Push. For pure retraction-based pseudo-double-recursion architecture, we need suction-to-push. Methods: pull logs from above then push horizontally (good for wither processing); add a double recursion module at the end; honey-slime streams.
### 3.5 Wiring — Integrated/Independent/Modular. Integration for stability; independence (another clock) to reduce lag; modularization to assemble like building blocks.

## 4 Detection-Based 4gt Tree Farms
The biggest problem: the only dustless method that can provide zero-delay rising edge 0t is **redstone dust redirection**, which takes up a lot of space. Architecture is more important than anything. We need the detection unit able to run a 4gt cycle (make the output signal structure reset within 4gt, or make another set that resets within 8gt).

*Created: 2025-02-05 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
