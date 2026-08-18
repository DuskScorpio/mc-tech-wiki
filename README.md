# MC Technical Wiki (Tree Farms)

Personal Obsidian vault + LLM-compiled knowledge base for Technical Minecraft tree-farm mechanics.

- **Edition:** Java only (no Bedrock coverage, by design).
- **Version tagging:** every page carries `edition:` + `version:` + `confidence:` + `sources:` in frontmatter. GTMC baseline is `1.20.1`; other pages tagged to their own version.
- **Correctness model:** every mechanical claim ends with a `^[raw/articles/file.md]` marker tracing it back to an immutable source. Raw sources are sha256-tracked so edits upstream are caught.

## Structure

| Path | Purpose |
|---|---|
| `SCHEMA.md` | Correctness rules + tag taxonomy |
| `index.md` | Content catalog (read first) |
| `log.md` | Append-only changelog |
| `raw/articles/` | Immutable source captures (sha256-tracked) |
| `concepts/` | Compiled wiki pages |

## Sources

- **Graduate Texts in Minecraft (GTMC)** — `techmc.wiki`, CC BY-NC-SA 4.0
- **Bilibili** — individual authors (e.g. Scorpio 天蝎君), per-article attribution
- **Minecraft Wiki** (`minecraft.wiki`) — cross-check / corroboration

## Use

Open this folder directly in Obsidian as a vault. `[[wikilinks]]` and Graph View work out of the box.
