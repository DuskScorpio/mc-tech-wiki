---
type: source
source_url: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
ingested: 2026-08-18
sha256: 7687c99c6e290bd65faea452329236ae30c68e36eb202817da51b4be597fa3df
---

# 05 Why Your Tree Farm Stalls — Introduction to Dustless Wiring (GTMC)

Dustless has never been the goal—it's a means to an end. The ultimate objective should be to reduce lag, not to force dustless designs. Forcing dustless designs can easily lead to increased lag, which goes against the very point of dustless wiring.

## 1 Rails and Observers
Rails **emit PP updates simultaneously** when their activation state changes, and can be detected by Observers. Together, they form the most basic dustless signal transmission method. In tree farms, Pistons are generally arranged vertically; we activate a vertical column of Observers simultaneously to activate an entire row of Pistons at once. You can also use BUD rails for zero-delay signal transmission.

## 2 Tree Power / Scaffolding Power / Wall Power

### 2.1 Tree Power
Starting from 1.14, after receiving a PP update, leaves schedule a tick (if in TT, it executes immediately; otherwise it executes in the TT, 1gt later) to check their distance from logs. If the distance changes, they emit NC and PP updates. We generally push or pull logs with Pistons or Slime Blocks to trigger distance changes. Tree power's update mechanism works somewhat like Redstone Dust.

Tree power detection: the tree farm's growth module runs within TT, so trees grow and place logs within TT. Leaves immediately execute the check within TT, then emit NC and PP updates, triggering the BUD and achieving growth detection.

### 2.2 Scaffolding Power
When a scaffold receives a PP update, it schedules a tick to check its horizontal distance from the supporting block. If the distance changes (and is not greater than 6), it emits NC and PP updates. Scaffolding power adds 1gt delay per scaffold. We generally trigger it through trapdoor state changes below the scaffold.

### 2.3 Wall Power
Starting from 1.16, if there are connecting blocks on both the x and z axes, the wall is low; otherwise it's high. If there's one high wall in an entire column of walls, then starting from that wall, all walls below become high walls. We generally trigger wall state changes by opening/closing fence gates above the topmost wall or opening/closing doors/trapdoors on the side. Walls are **instant components**. All wall state changes emit PP updates and can be detected by Observers.

## 3 Signal Transmission Without Macro Delay

### 3.1 Slime Sticks
Slime sticks use Slime Blocks to pull things and transmit signals. When a Piston pushes or pulls a chain of blocks, it deletes the blocks from their original positions during the BE phase, so it can change another Piston's activation state within the same gt, eliminating macro delay. For sticky Pistons in such chains, falling edge transmission has no macro delay, but rising edges have 3gt delay per Piston. We add an auto-reset device to each stick that resets at 3gt.

### 3.2 Rails + BUD
Rails are instant components. By using rails to update BUDs, and having the BUD change the activation state of another chain of rails, we keep the signal propagating within the BE phase.

## 4 Redstone Redirection
This is the **only method in a dustless environment that can output rising edge signals with zero delay**. Redstone Dust only powers in the direction it points, so if we create a powered Redstone Dust that doesn't point in a certain direction, and then when a rising edge signal arrives, redirect it to point in that direction, we can output a rising edge signal in that direction with zero delay. Redstone Dust is redirected by certain blocks; the movable ones are the most important. Note that redstone redirection only produces PP updates; to activate certain components, we need to provide NC updates separately.

### 4.1 Columns — arrange several redstone redirections vertically.
### 4.2 3gt Generator — standard 3gt generator (3gt push, 3gt pull Piston action).
### 4.3 0t Generator — based on redstone redirection.

*Created: 2024-12-28 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
