# claude-test

Phone-friendly browser games built with Claude Code. Each game is one self-contained HTML file in `games/`. The data is baked into the file, so it works offline.

## Games

| File | What it is |
| --- | --- |
| `games/lantern-drift.html` | One-thumb arcade game: steer a lantern, catch sparks, dodge stones. |
| `games/hardwood-grid.html` | College basketball trivia grid (schools × titles, awards, NBA draft facts). |
| `games/hook-grid.html` | 2010s pop trivia grid (artists × chart facts, featured guests, Grammy nods). |
| `games/swiftie-grid.html` | Taylor Swift trivia grid (albums × lyric themes, track positions, co-writers, charts). |
| `games/zeppelin-grid.html` | Led Zeppelin trivia grid (albums × vinyl sides, writing credits, live sets, lyric themes). |

The trivia grids share one engine: 9 guesses, a seeded daily grid, random grids, and a "1 of N" rarity count. Progress is saved in the browser's local storage.

The game pages are written as artifact bodies (no `<html>`/`<head>` wrapper). They still open in any browser, because browsers add the missing tags.

## Data and build scripts (`build/`)

Facts come from Wikipedia (text available under CC BY-SA 4.0): NBA draft pages, Billboard year-end and top-10 lists, Grammy pages, album track listings, and singles discographies. Some categories were tagged by hand, and the scripts say which. These include lyric themes (stored as tags only, with no lyrics), artist types, and pre-2000 basketball awards.

| Folder | Game | Main files |
| --- | --- | --- |
| `build/hardwood/` | Hardwood Grid | `parse.py` (draft pages → `draft.json`), `extra.txt` (hand facts), `build2.py` (merge → `data.json`) |
| `build/pop/` | Hook Grid | `parse.py` (charts → `songs.json`), `types.py` (artist types), `build.py` (→ `data.json`), `template.html` (shared grid engine) |
| `build/ts/` | Swiftie Grid | `parse.py`, `tags.py` (hand tags), `build.py` (→ `data.json`), `head.js` (categories) |
| `build/lz/` | Zeppelin Grid | `parse.py`, `build.py` (hand tags inside), `head.js` (categories) |
| `build/` | | `build_sg.py` and `build_lz_base.py` turn `pop/template.html` plus a game's `head.js` and `data.json` into a game page. |
| `build/checks/` | | Playwright smoke tests that load a page at phone size and generate 300 random grids. |

The raw Wikipedia downloads are not committed. To rebuild a game, download that game's Wikipedia pages into a `raw/` folder next to its `parse.py`, then run the scripts in order. The scripts use relative paths that match the folder layout they were written in, so a few paths may need adjusting.
