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
| `games/first-wave-grid.html` | First Wave Grid: new wave, synth-pop and post-punk trivia grid built from a Spotify playlist, with Medium and Hard modes. |
| `games/ride-grid.html` | Ride Grid: Disney parks trivia grid (parks × ride types, franchises and crossover attractions), with Medium and Hard modes. |
| `games/wizard-grid.html` | Wizard Grid: Harry Potter trivia grid (houses and groups × character traits, from the seven books), with Medium and Hard modes. |
| `games/galaxy-grid.html` | Galaxy Grid: Star Wars trivia grid, Episodes I–VI only (films and factions × character traits), with Medium and Hard modes. |
| `games/throne-grid.html` | Throne Grid: Game of Thrones trivia grid, HBO show only (houses and groups × fates and titles), with Medium and Hard modes. |
| `games/scranton-grid.html` | Scranton Grid: The Office (US) trivia grid (departments × life events), styled like the show's typewriter title card, with Medium and Hard modes. |
| `games/flannel-grid.html` | '90s alternative trivia grid built from a 327-song Spotify playlist (bands × chart, mood and release facts), with Medium and Hard modes. |

The trivia grids share one engine: 9 guesses, a seeded daily grid, random grids, and a "1 of N" rarity count. Progress is saved in the browser's local storage.

The game pages are written as artifact bodies (no `<html>`/`<head>` wrapper). They still open in any browser, because browsers add the missing tags.

## Public site with shared stats (`site/`)

`site/` holds standalone copies of the five music grids, Ride Grid, Wizard Grid, Galaxy Grid, Throne Grid and Scranton Grid plus a home page (`site/index.html`), meant for GitHub Pages so anyone with the link can play. These copies add shared daily stats through Supabase: a player count, the percent of players who picked each correct answer, the most-picked answer per square, and a tap-to-see list of every answer that worked.

- `supabase/schema.sql` sets up the database (run once in the Supabase SQL Editor). Tables are locked; visitors can only add guesses and read totals.
- `build/add_stats.py <publishable key>` rebuilds `site/` from the artifact versions of the games.
- Players are identified by a random ID stored in their browser, with no names or sign-in. Random grids record nothing.

## Data and build scripts (`build/`)

Facts come from Wikipedia (text available under CC BY-SA 4.0): NBA draft pages, Billboard year-end and top-10 lists, Grammy pages, album track listings, and singles discographies. Some categories were tagged by hand, and the scripts say which. These include lyric themes (stored as tags only, with no lyrics), artist types, and pre-2000 basketball awards.

| Folder | Game | Main files |
| --- | --- | --- |
| `build/hardwood/` | Hardwood Grid | `parse.py` (draft pages → `draft.json`), `extra.txt` (hand facts), `build2.py` (merge → `data.json`) |
| `build/pop/` | Hook Grid | `parse.py` (charts → `songs.json`), `types.py` (artist types), `build.py` (→ `data.json`), `template.html` (shared grid engine) |
| `build/ts/` | Swiftie Grid | `parse.py`, `tags.py` (hand tags), `build.py` (→ `data.json`), `head.js` (categories) |
| `build/lz/` | Zeppelin Grid | `parse.py`, `build.py` (hand tags inside), `head.js` (categories) |
| `build/flannel/` | Flannel Grid | `charts.py` (Billboard No. 1 lists → `charts.json`), `build.py` (playlist CSV + charts + hand band types → `data.json`). The Spotify CSV export is not committed; put it at `in/playlist.csv` to rebuild. |
| `build/rides/` | Ride Grid | `rides.txt` (hand-compiled list of about 110 attractions across 12 parks, with ride-type tags), `build_data.py` (→ `data.json`). Page built by `build_ride.py` (made by `make_ride_builder.py`). |
| `build/wizards/` | Wizard Grid | `characters.txt` (hand-compiled list of about 130 characters with houses, groups and traits from the books), `build_data.py` (→ `data.json`). Page built by `build_wiz.py` (made by `make_wiz_builder.py`). |
| `build/galaxy/` | Galaxy Grid | `characters.txt` (hand-compiled list of about 90 characters with film appearances, factions and traits), `build_data.py` (→ `data.json`). Page built by `build_galaxy.py` (made by `make_galaxy_builder.py` from the Wizard builder). |
| `build/thrones/` | Throne Grid | `characters.txt` (hand-compiled list of about 110 characters with houses, groups, titles and death season), `build_data.py` (→ `data.json`). Page built by `build_got.py` (made by `make_got_builder.py`), then `tweak_got.py` allows single-answer squares because the show's houses are small. |
| `build/office/` | Scranton Grid | `characters.txt` (hand-compiled list of about 45 characters with departments and life events), `build_data.py` (→ `data.json`). Page built by `build_office.py` (made by `make_office_builder.py`), then `tweak_office.py` allows single-answer squares and styles the title card. |
| `build/wave/` | First Wave Grid | `build.py` (playlist CSV + US top-10 and UK No. 1 pages + hand band types → `data.json`). The playlist CSV and chart pages are not committed. |
| `build/` | | `build_sg.py`, `build_lz_base.py`, `build_lith.py` and `build_wave.py` (made by `make_wave_builder.py`) turn `pop/template.html` plus a game's `head.js` and `data.json` into a game page. |
| `build/checks/` | | Playwright smoke tests that load a page at phone size and generate 300 random grids. |

The raw Wikipedia downloads are not committed. To rebuild a game, download that game's Wikipedia pages into a `raw/` folder next to its `parse.py`, then run the scripts in order. The scripts use relative paths that match the folder layout they were written in, so a few paths may need adjusting.
