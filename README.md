# Do Not Disturb

*Three nights at the Hotel Paradiso.*

A Ren'Py visual novel set at a secret, invite-only party in an aging 1970s hotel-casino on the shore of Lake Tahoe, where every hotel room has been turned into an interactive art piece. You (off-screen, never named) spend three days and nights meeting the guests: by the pool in the afternoons, and wandering the hallways at night, where people pull you into the art rooms. Build enough rapport with someone and, after the 11:11 ceremony on the last night, you can find them for a final scene at sunrise.

## Running it

1. Install the [Ren'Py SDK](https://www.renpy.org/latest.html) (8.x).
2. Open the Ren'Py launcher → **Preferences** → set **Projects Directory** to the folder that contains this repo (or put the repo inside your projects folder).
3. Select **visualnovel** in the launcher and click **Launch Project**.

Useful launcher actions: **Check Script (Lint)** validates the script, and **Build Distributions** packages it for Windows/Mac/Linux.

## Playing in the browser (GitHub Pages)

Every push to `main` builds a web version of the game with Ren'Py and publishes it to GitHub Pages via `.github/workflows/web.yml`. Once it's set up, the game is playable at **https://swartzcr.github.io/visualnovel/**.

One-time setup: in the repo on GitHub, go to **Settings → Pages** and set **Source** to **GitHub Actions**. Then re-run the latest workflow from the **Actions** tab (or push any commit).

Each run downloads the Ren'Py SDK and its web support (the first version in `RENPY_VERSIONS` that's available), lints the game, builds it with `renpy.sh launcher web_build`, and deploys the result. To build a web version locally instead, use **Web → Build Web Application** in the Ren'Py launcher.

## Automated tests

`game/tests.rpy` is a test player that runs through the whole game by itself. It's switched off in normal play and left out of released builds. It plays:

- the full game 15 times, following each guest in every pool and hallway menu and picking option 1, 2 or 3 in every conversation menu
- a run that wanders alone every night
- the finale set up for every ending: each romance, each friendship, several guests qualifying, and nobody
- the Guest Book screen with and without guests met

It fast-skips dialogue, catches every error instead of stopping, and checks that each run reaches the ending it should. The report lists failures, any labels never reached, and any menu options never chosen.

GitHub Actions runs it on every push, after lint and before the web build. If it fails, the site isn't redeployed and the previous version stays up. The reports are pushed to the `ci-reports` branch (`test-report.txt`, `lint.txt`, plus Ren'Py's `traceback.txt` and `log.txt` when they exist) and shown on each run's summary page.

To run it locally with the Ren'Py SDK installed:

```sh
VN_TEST=1 RENPY_PERFORMANCE_TEST=0 /path/to/renpy-sdk/renpy.sh /path/to/visualnovel
# report written to vn_test_report.txt in the project folder
```

## How the game works

| | |
|---|---|
| **Length** | 3 days. Each day: 1 conversation at the pool. Each night: 1 random encounter, then 2 hallway encounters (or wander alone). |
| **Random encounters** | 14 short run-ins with the party (a clown wedding, a vampire in a coffin, Penguin Post, the OnlyFans Fanny Bar, Tentacletopia, Zany Optical, Platonic Speed Dating, the Let It Go workshop…), one per night, never repeating within a playthrough. The six art-room encounters have guest versions that play if you've met that guest: Penguin Post with Juni, the Fanny Bar with Gerald, Tentacletopia with Solstice, Zany Optical with Zyx, Let It Go with Wren, and Platonic Speed Dating with everyone you've met (+1 rapport for a good answer). Defined in `game/encounters.rpy`; add one by writing a label and listing it in `ENCOUNTERS`. |
| **Guests** | 5, each with 2 pool chapters and 3 night chapters. Chapters always play in order, so you can follow anyone from start to finish no matter which day you pick them. |
| **Rapport** | Every conversation has 2 choices worth 0–2 points (one bad choice is −1). Pushy or dismissive answers score 0; kind, curious, consent-forward answers score 2. |
| **Romance** | 10+ rapport with a guest unlocks their sunrise scene after the ceremony. That takes at least 3 good chapters with them; picking middle-of-the-road answers in all 5 also gets you there. If several qualify, you choose. |
| **Other endings** | 5+ rapport with your closest guest → *Good Company*. Otherwise → *Checkout*. 7 endings total, tracked across playthroughs. |
| **Guest Book** | The **Guests** button in the quick menu shows everyone you've met and your rapport as hearts (5 hearts = romance-ready). |

### The guests

- **Juni** (they/them): a database engineer in a pink axolotl kigurumi. The hood stays up. Rooms: *Room 404: Room Not Found*, *The Lost & Found*, *The Regeneration Tank*.
- **Gerald** (he/him): a Sasquatch from the Klamath. Drinks lapsang souchong. Possibly not a costume. Rooms: *The Breakfast Schism* (Church of Cast Iron vs. Temple of Teflon), *Room 312: The Forest*, *Cryptids Anonymous*.
- **Solstice** (she/her): a raver in fur leg warmers and an LED crop top who's an ICU night nurse the rest of the week. Rooms: *The Human Stock Exchange*, *Confession Booth Karaoke*, *The Ballroom*.
- **Wren** (she/her): crew, dressed in black, the party's behind-the-scenes fixer. She found herself at a party like this years ago, and now spends the weekend putting out fires so the magic holds for everyone else, and never gets to be at it. Rooms: *Backstage* (the laser rig dies mid-set), *Mission Control* (a linen closet), *The Roof*.
- **Zyx** (they/them): Ambassador of the Outer Drift, here to determine whether Earth is ready for contact. Never breaks character. Rooms: *The Oracle of Ping Pong*, *The Clinic of Unnecessary Procedures*, *The Ice Machine Planetarium*.

Running through the weekend: the Pool People and the Order of the Ice Machine are at war over the true nature of water, to be resolved when the aliens' ark arrives at 11:11 on Sunday night.

## Editing the dialogue

**[DIALOGUE.md](DIALOGUE.md)** has every line of dialogue and every choice in the game, in play order, with notes on scene changes and how much each choice is worth in rapport. Edit it in any text editor, then apply the changes with `python3 tools/dialogue.py import`. The instructions are at the top of the file. Run `python3 tools/dialogue.py export` to regenerate it after the scripts change.

## Project layout

```
game/
  core.rpy        characters, image declarations, rapport system (gain(), thresholds)
  ui.rpy          the time tag and Guest Book screens
  script.rpy      arrival, the day/night loop, pool + hallway menus, mornings, the 11:11 ceremony
  juni.rpy        \
  gerald.rpy       |  each guest: 2 pool chapters, 3 night chapters,
  solstice.rpy     |  romance ending (<name>_romance), friendship ending (<name>_friend)
  wren.rpy         |
  zyx.rpy         /
  encounters.rpy  random nightly encounters
  finale.rpy      choosing who to find, the other endings, the ending card
  options.rpy, gui.rpy, screens.rpy, guisupport.rpy   Ren'Py's standard template (lightly themed)
  images/bg/      backgrounds, 1280x720
  images/sprites/ character sprites
  gui/            menu and text-box images
tools/            Python scripts that generated the placeholder art
```

To tune difficulty, change `ROMANCE_THRESHOLD` and `FRIEND_THRESHOLD` in `game/core.rpy`.

## Replacing the art

All 30 backgrounds and the 20 character sprites are finished Midjourney art. Only the UI (text box, buttons) is still drawn by the scripts in `tools/` (Pillow only). Drop in your own PNGs with the **same file names** and the game picks them up with no code changes.

**[MIDJOURNEY_PROMPTS.md](MIDJOURNEY_PROMPTS.md)** has Midjourney (Niji 7) prompts for every background, in the style of the finished lobby. **[ART_PROMPTS.md](ART_PROMPTS.md)** has ready-to-paste image-generation prompts (written for Google's Nano Banana) for every background and all 20 character sprites, plus how to keep characters consistent across expressions and how to prepare the images.

**Backgrounds** go in `game/images/bg/` and are **1280×720**:

| File | Used for |
|---|---|
| `exterior.png` | Arrival, Friday afternoon; Monday-morning goodbyes |
| `exterior_night.png` | Main menu art (copied to `gui/main_menu.png`, and blurred for `gui/game_menu.png`) |
| `lobby.png` | Check-in desk |
| `pool.png` | Every pool scene (an indoor pool under a glass atrium); Juni's ending |
| `hallway.png` | Night hallways |
| `bedroom.png` | Mornings (newspaper under the door) |
| `room404.png` | Juni night 1 |
| `lostfound.png` | Juni night 2 |
| `regen.png` | Juni night 3 |
| `breakfast.png` | Gerald night 1 |
| `forest.png` | Gerald night 2 |
| `cryptid.png` | Gerald night 3, wandering |
| `exchange.png` | Solstice night 1, wandering |
| `karaoke.png` | Solstice night 2 |
| `ballroom.png` | Solstice night 3, ceremony, after midnight |
| `ballroom_ark.png` | The ark arrives at 11:11 |
| `livingroom.png` | Wandering: Auntie Acid's room, The Cozy |
| `backstage.png` | Wren night 1 |
| `mission.png` | Wren night 2 |
| `roof.png` | Wren night 3 |
| `roof_dawn.png` | Sunrise endings (Gerald, Solstice, Wren, Zyx, Checkout) |
| `fortune.png` | Zyx night 1 |
| `clinic.png` | Zyx night 2 |
| `planetarium.png` | Zyx night 3 |
| `penguinpost.png` | Random encounter: Penguin Post |
| `fanbar.png` | Random encounter: the OnlyFans Fanny Bar |
| `tentacletopia.png` | Random encounter: Tentacletopia |
| `optical.png` | Random encounter: Zany Optical |
| `speeddating.png` | Random encounter: Platonic Speed Dating |
| `letitgo.png` | Random encounter: the Let It Go workshop |

**Sprites** go in `game/images/sprites/` and are transparent PNGs named `<guest>_<expression>.png`:

- Guests: `juni`, `gerald`, `solstice`, `wren`, `zyx`
- Expressions: `neutral`, `happy`, `surprised`, `blush`

That's 20 files. The current ones are 536×720 bust-ups (Gerald is 937×720). Any size works: sprites are anchored to the bottom-center of the screen, so keep them at most about 720 px tall and leave the bottom edge where the character is cropped.

**Menu art:** `game/gui/main_menu.png` and `game/gui/game_menu.png` (1280×720).

To import a Midjourney expression sheet (one row of four panels, see the end of MIDJOURNEY_PROMPTS.md):

```sh
python3 tools/import_sprite_sheet.py sheet.png juni --height 720
# panels in a different order, or skip one with -:
python3 tools/import_sprite_sheet.py --height 720 sheet.png wren -- neutral,blush,happy,surprised
```

It removes the flat background (any color), trims stray bits of the neighboring panels and saves `game/images/sprites/<name>_<expression>.png`. Requires Pillow and numpy.

To regenerate the UI: `python3 tools/make_gui.py` (requires Pillow). **Don't run `tools/make_backgrounds.py` or `tools/make_sprites.py`**: they would overwrite the Midjourney art with the old procedural versions.

## Tone notes

The party is inspired by Bay Area immersive "secret parties": no photos, ask before touching, a tea bar instead of a bar, a volunteer care crew, an elder's living room (here, Auntie Acid's The Cozy) for anyone having a hard time, absurdist running mythology, and no spectators. Substances are never shown. Romance scenes are tender, explicitly consensual, and end at a kiss.
