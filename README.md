---
type: doc
---

# MC Technical Wiki

Personal Obsidian vault + LLM-compiled knowledge base for **Technical Minecraft (Java)**, structured as a **Google Open Knowledge Format (OKF) v0.1** bundle (agent-readable knowledge graph).

- **Edition:** Java only (no Bedrock coverage, by design).
- **Scope:** general Technical Minecraft — started with tree farms, expanding to other tech-MC topics (mechanics, farms, contraptions). Tree farms are just the first area ingested, not the whole subject.
- **Language:** English only. No Chinese / other-language translations in page bodies (see SCHEMA.md Language rule).
- **Format:** OKF v0.1. Every concept is one `.md` file with required `type` + recommended `description`/`timestamp`/`resource` in frontmatter; concept-to-concept links are markdown path links that form the knowledge graph. `index.md` is the progressive-disclosure entry point; `log.md` is the changelog.
- **Correctness model:** every mechanical claim carries a `^[raw/articles/file.md]` marker tracing it to an immutable, sha256-tracked source. Cross-source claims are corroborated (GTMC + TMWiki + Minecraft Wiki).

## Structure

| Path | Purpose |
|---|---|
| `SCHEMA.md` | Correctness rules, OKF compliance contract, tag taxonomy, language rule |
| `index.md` | OKF entry point (concepts grouped by type, path links) |
| `log.md` | Append-only changelog |
| `raw/articles/` | Immutable source captures (sha256-tracked) |
| `concepts/` | Compiled wiki pages (the OKF concepts) |

## Sources

- **Graduate Texts in Minecraft (GTMC)** — `techmc.wiki` / `techmc-wiki/articles`, CC BY-NC-SA 4.0 (primary)
- **Technical Minecraft Wiki (TMWiki)** — `TechMCDocs/pages` (independent 2nd source)
- **Minecraft Wiki** — `minecraft.wiki` (3rd cross-source, e.g. Sapling)
- **TechMC-Glossary** — `TechMC-Glossary/TechMC-Glossary` (term definitions)
- **Bilibili** — individual authors (e.g. Scorpio 天蝎君), per-article attribution

All source material is CC BY-NC-SA where applicable; attribution is preserved per raw file. This vault is a personal reference, not a redistribution.

## Use

- **In Obsidian:** open the folder as a vault. `[[wikilinks]]` + Graph View work; path links render too.
- **As an OKF bundle:** start at `index.md`, follow concept links (each `[label](/concepts/NAME)` with the `.md` suffix). Any OKF consumer can ingest it without translation.
