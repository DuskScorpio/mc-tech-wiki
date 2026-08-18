---
title: Block Nature (Block vs BlockState)
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: medium
tags: [mechanics, source-gtmc]
sources: [raw/articles/gtmc-block-mechanics.md]
---

# Block Nature (Block vs BlockState)

In source code, `Block` and `BlockState` are distinct concepts. This chapter frames block-state design, the full placement/breaking process, and how blocks connect to chunk mechanics and the update system.^[raw/articles/gtmc-block-mechanics.md]

> **Confidence: medium** — only the intro article was captured; detailed sub-articles (block states, placement/breaking internals) are not yet ingested. Treat this as a pointer page.

## Related
- [[update-theory]] — how block state changes emit updates
- [[piston-mechanics]] — block placement via b36
