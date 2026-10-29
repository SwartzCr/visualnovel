# Art prompts for Nano Banana

Copy-paste prompts for every background and character sprite in *Do Not Disturb*, written for Google's Nano Banana image model (Gemini image generation).

When an image is ready, save it with the file name shown and drop it in the folder listed under [Getting the images into the game](#getting-the-images-into-the-game). The game picks it up with no code changes.

## Step 1: paste a style guide at the start of each chat

Image models drift toward their own default look unless they're told very precisely what you want. These two style guides define the game's look: the medium, line art, shading, colors, lighting, proportions, framing and what to avoid. **Start every new Gemini chat by pasting the matching guide.** Gemini replies "Ready". Then paste the image prompts from step 2 one at a time.

- Use one chat **per character**: the sprite guide, then the neutral sprite, then its three expressions.
- Use one chat for **a handful of backgrounds** at a time.
- If the results start to drift from the guide, open a new chat and paste the guide again.

### Style guide for backgrounds

```text
Read this style guide and use it for every image I ask for in this conversation. Reply only with "Ready" and don't generate an image yet.

ART STYLE (applies to every image in this conversation)
- Medium: 2D digital anime illustration with the finish of a polished, commercial Japanese visual novel. Flat, clean, hand-drawn look. It is never a photograph, never a 3D render, never oil paint or watercolor, never pixel art, never chibi or super-deformed.
- Line art: clean, confident, smooth lines in dark plum-brown (#2B1A2E), never pure black. Thicker on outer silhouettes, thinner on interior details, slightly tapered at the ends.
- Coloring: cel shading. Flat base colors, one crisp shadow tone per material, and small sharp highlights. Soft airbrushed gradients only for glows, cheek blush, hair shine and skies.
- Palette: saturated and warm, never muddy or grey. Signature accent colors: hot pink #FF5FB8, violet #9B6BFF, cyan #5AE6FF, warm gold #FFC65A. Night scenes sit in deep midnight purple and indigo (#160C28) lit by those neon accents. Day scenes are warm peach, turquoise and gold under clear light.
- Lighting: clear and readable. Colored light from the environment, gentle bloom around lamps, neon and screens, and colored rim light at night (pink from one side, cyan from the other).
- World and mood: a secret, kind, absurd art party inside a run-down 1960s California motel called the Hotel Marisol, where every room has been turned into an art installation. Playful, warm, a little surreal and magical. Never grimy, gory, horror-dark, sexy or edgy.
- Text: only the exact words given in quotation marks, spelled exactly, in clean bold sans-serif lettering. No other writing, captions, signatures, watermarks, logos, borders, speech bubbles or UI.

BACKGROUND RULES
- Format: wide 16:9 landscape, filling the whole frame.
- Camera: eye level, about 35 mm lens, one- or two-point perspective with straight verticals. No fisheye, no tilted or overhead angles.
- The scene is empty of people, unless a prompt asks for silhouettes.
- Layout for a visual novel. Characters will be pasted standing in the middle and a dialogue box will cover the bottom third. So the center of the frame is open space (floor, wall, sky), the bottom third is simple floor, carpet, ground or water with little detail, and signs, props and points of interest sit in the upper two-thirds and toward the left and right sides.
- Detail: medium, with clear shapes that read at a glance at 1280x720. Painterly backdrop softness is fine, but edges stay crisp.
```

### Style guide for character sprites

```text
Read this style guide and use it for every image I ask for in this conversation. Reply only with "Ready" and don't generate an image yet.

ART STYLE (applies to every image in this conversation)
- Medium: 2D digital anime illustration with the finish of a polished, commercial Japanese visual novel. Flat, clean, hand-drawn look. It is never a photograph, never a 3D render, never oil paint or watercolor, never pixel art, never chibi or super-deformed.
- Line art: clean, confident, smooth lines in dark plum-brown (#2B1A2E), never pure black. Thicker on outer silhouettes, thinner on interior details, slightly tapered at the ends.
- Coloring: cel shading. Flat base colors, one crisp shadow tone per material, and small sharp highlights. Soft airbrushed gradients only for glows, cheek blush, hair shine and skies.
- Palette: saturated and warm, never muddy or grey. Signature accent colors: hot pink #FF5FB8, violet #9B6BFF, cyan #5AE6FF, warm gold #FFC65A. Night scenes sit in deep midnight purple and indigo (#160C28) lit by those neon accents. Day scenes are warm peach, turquoise and gold under clear light.
- Lighting: clear and readable. Colored light from the environment, gentle bloom around lamps, neon and screens, and colored rim light at night (pink from one side, cyan from the other).
- World and mood: a secret, kind, absurd art party inside a run-down 1960s California motel called the Hotel Marisol, where every room has been turned into an art installation. Playful, warm, a little surreal and magical. Never grimy, gory, horror-dark, sexy or edgy.
- Text: only the exact words given in quotation marks, spelled exactly, in clean bold sans-serif lettering. No other writing, captions, signatures, watermarks, logos, borders, speech bubbles or UI.

CHARACTER SPRITE RULES
- Exactly one character per image.
- Format: portrait orientation, with the character centered and facing the viewer (straight on or a slight three-quarter turn), standing relaxed, arms within the silhouette.
- Crop: waist-up. The body is cut off at the hips by the bottom edge of the image. The whole head, hair and anything on top of the head is inside the frame, with a small gap above.
- Background: one perfectly flat, solid fill color from edge to edge (given in each prompt). No floor, cast shadow, gradient, vignette, glow, pattern or scenery behind the character.
- Anatomy: every character is an adult, with adult proportions about seven heads tall, a defined jaw, a visible neck and adult shoulders. Never childlike, never chibi.
- Faces: large expressive anime eyes, each roughly one fifth of the face width. A thick dark upper lash line that flicks outward at the corner, a two-tone iris (darker at the top, lighter at the bottom), one large white highlight near the top and one small highlight below. A tiny suggested nose and a small mouth.
- Hair: grouped into clean pointed clumps, with one soft shine band.
- Clothing: simple clear shapes and few folds. Keep the outfit details exactly as described, because the same character is redrawn with different expressions.
- Lighting: soft, even front lighting with one cel-shadow tone, so all four expressions match.
```

## Step 2: generate, keeping things consistent

- **Use the placeholder art as a layout reference.** The repo already has a rough version of every image in `game/images/bg/` and `game/images/sprites/`. Attaching the matching one gives Nano Banana the exact layout, pose and outfit to follow, which works much better than words alone. Attach it and start your prompt with: *Redraw the attached rough placeholder as finished art in the style guide. Keep its layout, pose, outfit and colors, but improve the drawing quality completely.* Then paste the image's prompt below.
- **Set the shape.** If your Gemini interface has an aspect-ratio setting, pick **16:9** for backgrounds and the ratio listed for each character.
- **Make pairs by editing, not from scratch.** Three backgrounds are the same place at a different time (exterior → exterior at night, roof → roof at sunrise, ballroom → ballroom with the ark). Generate the first, then paste the second prompt as an edit in the same chat. Edits keep the composition and aspect ratio.
- **Make expressions by editing the neutral sprite.** Use the expression prompts as edits on the neutral image, one at a time, in the same chat. This keeps the face, outfit and framing identical, so the sprites swap cleanly mid-conversation.
- **Lock the art style.** Once one image looks right, attach it when making the next one and add: *Match the art style, line weight and shading of the attached image exactly, but draw [the new character or place].*
- **Lettering:** short quoted text renders best. If a sign garbles, ask again with fewer signs, or drop the text and add it in an image editor. The text is flavor; the game never depends on it.

### Quick fixes when a result is off

Paste one of these as a follow-up in the same chat:

| Problem | Follow-up prompt |
|---|---|
| Looks photographic, 3D or painterly | *Redo this as flat 2D anime cel shading with clean plum-brown line art, like a visual novel. No 3D rendering, no photographic lighting, no painterly texture.* |
| Character looks too young | *Redraw the character as a clear adult in their late twenties to thirties: longer face, defined jaw, visible neck, broader shoulders, adult proportions.* |
| Full body, or the head is cut off | *Reframe as a waist-up portrait: cut off at the hips by the bottom edge, with the whole head and hair inside the frame and a small gap above.* |
| Scenery or a shadow behind a sprite | *Replace everything behind the character with one perfectly flat solid fill color, edge to edge, with no shadow or gradient.* |
| People appear in a background | *Remove all people and figures. The space is empty.* |
| Too dark, grey or muddy | *Make the colors more saturated and the lighting clearer and warmer, keeping the neon pink, violet and cyan accents.* |
| Too busy behind where characters stand | *Simplify the middle and bottom third of the image into plain floor and wall, and move the details to the upper corners and sides.* |
| Garbled sign text | *Remove all text from the image.* (Then add the sign text in an image editor if you want it.) |

## Step 2 prompts: backgrounds

Size in the game: **1280×720** (16:9). Bigger is fine; it gets scaled down. Save to `game/images/bg/`.

Two things about how the game shows backgrounds, which every prompt already accounts for:

- The **dialogue box covers roughly the bottom third** of the screen, so the lower part of each scene is kept simple.
- **Characters stand in the center**, so the middle of each scene is kept open.

### Outside the hotel

#### 1. `exterior.png`

*Used for:* Friday arrival; Monday-morning goodbyes in the parking lot.

> Generate this one first, then use it for the night version below so the building matches.

```text
A faded two-story 1960s roadside motor lodge in the dry golden hills of Northern California at sunset. Peach stucco walls, terracotta trim, a row of turquoise doors on each floor and an upper walkway with a simple railing. On the right, a tall vertical vintage neon sign reads "HOTEL MAR SOL", where the I of MARISOL has burned out and left a dark gap; under it, a smaller sign reads "NO VACANCY". The sky fades from deep violet to hot pink to tangerine, with the sun low behind the hills. An empty asphalt parking lot with faded yellow lines fills the foreground.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 2. `exterior_night.png`

*Used for:* the main menu backdrop (copied to gui/main_menu.png).

> Paste this as an edit on your exterior.png result. If you're starting fresh instead, describe the building first.

```text
Edit this image: keep the same motor lodge, camera angle and composition, and turn it into a clear night. A starry indigo sky with a thin crescent moon. The neon sign glows hot pink and cyan, with "NO VACANCY" in red. Most motel windows are lit, each a different glowing color (pink, gold, cyan, violet, lime) as if every room hides a party. Strings of colorful bulb lights sag along the roofline. A soft pink glow spills across the dark parking lot.
```

### Daytime

#### 3. `lobby.png`

*Used for:* check-in with Wren.

> Optional extra sign above the cubbies: "ALL WHO ENTER ARE ALREADY CHECKED IN". It's long, so drop it if the lettering garbles.

```text
The lobby of a retro 1960s motel, turned into the entrance of a secret party. Deep green striped wallpaper, a brass chandelier with warm bulbs, and a long wooden reception desk with paneled front, a brass service bell and a small card reading "NO PHOTOS". Behind the desk, a wall of wooden key cubbies with brass keys on red fobs. A framed hand-painted sign on the left reads "TEA BAR" with an arrow. Potted palms in terracotta pots at both ends. Warm, welcoming, slightly mysterious light, a faint haze of incense.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 4. `pool.png`

*Used for:* every pool scene; Juni's sunrise ending.

```text
A sunny afternoon at a retro motel swimming pool. A turquoise kidney-shaped pool with sparkling ripples, a white concrete deck, white lounge chairs with turquoise straps, a red-and-cream striped umbrella, and a big pink inflatable flamingo floating in the water. Behind the pool, a peach two-story motel facade with turquoise doors. A homemade cloth banner strung over the deep end reads "WATER IS LOVE". A small pool rules sign reads "NO DIVING". Bright blue sky with puffy clouds, golden hills beyond. Cheerful, hazy summer light.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 5. `bedroom.png`

*Used for:* the morning scenes (with the newspaper).

```text
A small, cozy retro motel room in early morning light. A rumpled double bed with a lavender bedspread on the left, a window on the right with red curtains half open onto a pale sunrise sky, sunlight slanting across the room. Wood-paneled nightstand with a vintage lamp, and a folded newspaper on it with the masthead "THE DAILY DISTURBANCE". A framed seascape print on the cream wall. Quiet, sleepy, slightly hungover morning feeling.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

### Night: hallways and shared spaces

#### 6. `hallway.png`

*Used for:* every night in the hallways.

```text
A long retro motel corridor at night, seen in one-point perspective straight down the middle. Dark plum walls, a deep red patterned carpet, a row of doors on each side with brass room numbers, and colored light (pink, cyan, gold, violet) spilling out from under and around the half-open doors, as if every room is a different art installation. A pink neon arrow on the left wall reads "ART THIS WAY". At the far end, a glowing red "EXIT" sign. Ceiling lights glow in a row. Mysterious, inviting, electric party atmosphere.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 7. `ballroom.png`

*Used for:* Solstice's last night; the 11:11 ceremony; after midnight.

> Generate this first, then use it for the ark version below.

```text
The grand ballroom of an old hotel transformed into a psychedelic dance party. Tall columns, a huge mirrored disco ball hanging in the upper center, beams of pink, cyan, lime and violet laser light sweeping through haze, and glowing geometric shapes (triangles, hexagons) projected onto the walls. The lower part of the frame is a dense crowd of dancers seen only as dark silhouettes with arms raised, backlit by the lights.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 8. `ballroom_ark.png`

*Used for:* the moment the ark arrives at 11:11.

```text
Edit this image: keep the same ballroom, lights and crowd. Add a procession carrying an ornate golden ark high above the crowd on long poles, in the upper middle of the frame. The ark is a gilded chest covered in swirling psychedelic patterns, with the words "DON'T PANIC" on its front in friendly rounded letters, glowing with golden light. The carriers wear shiny silver alien bodysuits with large black almond-shaped eyes. Confetti falls. Awe and celebration.
```

#### 9. `livingroom.png`

*Used for:* Wren's first night; wandering (Grandma Ozone's living room).

```text
A cozy grandmother's living room recreated inside a hotel suite, as a calm refuge at a wild party. Warm patterned wallpaper with small flowers, a glowing floor lamp with a fringed shade, framed family photos, a cross-stitch sampler reading "BLESS THIS MESS". A wooden rocking chair with a pink cushion on the right, a big round braided rug with floor cushions in jewel tones, and a glass candy bowl full of strawberry candies on a small table. Golden, gentle, safe lighting.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 10. `roof.png`

*Used for:* Wren's last night.

> Generate this first, then use it for the sunrise version below.

```text
A flat gravel rooftop of an old two-story motel at night under a sky full of stars and a bright moon. An old wooden water tank on stilts on the left, strings of colorful bulb lights sagging across the roof, steel cables and a rigging frame rising on the right (used to lower something through a skylight), and a weathered wooden bench. Beyond the low parapet, dark hills and a scatter of small town lights. Quiet, intimate, a pause from the party below.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 11. `roof_dawn.png`

*Used for:* the sunrise endings (Gerald, Solstice, Wren, Zyx) and Checkout.

```text
Edit this image: keep the same rooftop, water tank, bench, rigging and string lights, and change the time to sunrise. A sky graded from soft blue at the top through lavender and pink to warm gold at the horizon, with the sun just clearing the hills and a warm glow over everything. A few last stars fade at the top. Most of the string lights have burned out. Tender, hopeful, end-of-the-night mood.
```

### Juni's art rooms

#### 12. `room404.png`

*Used for:* Juni night 1: Room 404, Room Not Found.

```text
A hotel room turned into an art installation about a missing web page. Everything is glossy white and pale grey, lit like a computer screen. Giant navy letters on the back wall read "404" with smaller text below reading "ROOM NOT FOUND". Retro computer error dialog boxes made of cardboard hang from the ceiling on fishing line, each with small "OK" buttons. Oversized white mouse cursors are stuck to the walls. Thin horizontal glitch stripes of cyan and magenta light cross the room. Funny and uncanny.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 13. `lostfound.png`

*Used for:* Juni night 2: the Lost & Found.

> If the lettering on the boxes garbles, ask for just two labels.

```text
A hotel room transformed into a warm, old-fashioned library-style lost and found for emotions. Wooden shelves fill the back wall with rows of pastel cardboard boxes, each with a handwritten label card; the readable ones say "MISPLACED CONFIDENCE", "UNSENT TEXTS", "OLD NICKNAMES" and "ONE COURAGE". A wooden counter with a little red sign reading "TAKE ONE, LEAVE ONE". Brass lamps cast amber light. Dust motes, nostalgic and gentle.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 14. `regen.png`

*Used for:* Juni night 3: the Regeneration Tank.

```text
A hotel room painted to feel like the bottom of a deep, peaceful lake. Everything is blue and teal, with rippling caustic light patterns dancing across the walls and ceiling, tall swaying green water plants at the sides, and little rising bubbles. In the middle sits a large oval waterbed glowing softly from below. Glowing cyan lettering on the back wall reads "THE REGENERATION TANK". Calm, dreamy, healing.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

### Gerald's art rooms

#### 15. `breakfast.png`

*Used for:* Gerald night 1: the Breakfast Schism.

```text
A hotel room turned into a candlelit cathedral devoted to breakfast. Warm amber gloom. On the left hangs a black gothic banner reading "CHURCH OF CAST IRON"; on the right, a white banner reading "TEMPLE OF TEFLON". In the center, a small wooden altar with rows of lit candles, holding a black cast-iron skillet with one perfect sunny-side-up egg, lit by a heavenly golden spotlight. A gilded plaque above it reads "THE HOLY SKILLET". Solemn and absurd at the same time.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 16. `forest.png`

*Used for:* Gerald night 2: Room 312, turned into a forest.

```text
A motel room completely transformed into an ancient misty redwood forest at night. Tall dark tree trunks, a floor covered in thick green moss, low fog drifting across the ground, and dozens of glowing fireflies. On the right, a hotel bed entirely overgrown with moss and ferns, beside a vintage hotel floor lamp casting a warm golden pool of light. A small brass room number "312" is still fixed to a tree trunk. Magical, hushed, homesick.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 17. `cryptid.png`

*Used for:* Gerald night 3: Cryptids Anonymous; wandering.

```text
A community support-group room inside an old hotel. Beige walls, a checkered linoleum floor, a flickering fluorescent ceiling light, a circle of grey metal folding chairs, and a folding table with a steel coffee urn and paper cups. A blue banner on the wall reads "CRYPTIDS ANONYMOUS". A poster shows a dark winged figure with glowing red eyes and the words "BELIEVE IN YOURSELF". A large green inflatable Loch Ness monster stands in the corner wearing a "HELLO MY NAME IS" sticker. Earnest, deadpan and sweet.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

### Solstice's art rooms

#### 18. `exchange.png`

*Used for:* Solstice night 1: the Human Stock Exchange; wandering.

```text
A hotel conference room turned into a chaotic, glittering stock exchange. Glowing LED ticker boards run across the top of the walls in green and red with entries like "SELF ▲4.2", "VIBES ▼1.1" and "GLITTER ▲99". A trading desk with old CRT monitors showing zigzag charts. A gold neon sign reads "HUMAN STOCK EXCHANGE". Colorful confetti hangs in the air. Dark room, dramatic neon glow, frantic energy.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 19. `karaoke.png`

*Used for:* Solstice night 2: Confession Booth Karaoke.

```text
A small hotel room turned into an intimate karaoke lounge. Deep red velvet curtains on every wall, a mirrored disco ball throwing specks of light, and a glowing karaoke screen in the center showing lyric bars. A pink neon sign on the left reads "CONFESS" and a cyan neon sign on the right reads "ABSOLVED". A vintage microphone on a stand in front of the screen. A curtained confession-booth doorway at the side. Moody purple light, warm and a little melancholy.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

### Wren's art rooms

#### 20. `mission.png`

*Used for:* Wren night 2: Mission Control (a linen closet).

```text
A hotel linen closet secretly turned into a party's mission control. Shelves stacked with folded white towels and sheets on the left. A bank of old monitors shows green hand-drawn maps of the hotel and status lists, and one shows a big red digital clock reading "11:11". Below them, a control panel of four big glowing arcade buttons labeled "FOG", "LASERS", "ARK" and "PANIC". A row of walkie-talkies charging with little green lights. A "STAFF ONLY" sign on the door. Dim, cozy, competent, backstage feeling.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

### Zyx's art rooms

#### 21. `fortune.png`

*Used for:* Zyx night 1: the Oracle of Ping Pong.

```text
A hotel room bathed in deep purple light, turned into a retro-futurist fortune-telling booth. On the left, a boxy silver 1950s robot with a glass dome head containing a glowing pink orb, a small screen with two glowing teal eyes, and a slot labeled "FORTUNES 1¢". On the right, a big clear lottery drum full of white ping-pong balls on a brass stand. Colorful capes hang on hooks by the wall. A violet neon sign at the top reads "THE ORACLE OF PING PONG". Small stars painted on the ceiling. Whimsical and mysterious.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 22. `clinic.png`

*Used for:* Zyx night 2: the Clinic of Unnecessary Procedures.

> Optional: ask for the full sign text "CLINIC OF UNNECESSARY PROCEDURES"; it may garble.

```text
A hotel room made into a whimsical retro medical clinic. Mint-green tiled walls, a white linoleum floor, an examination table with a crinkly paper sheet, and a pink privacy curtain on a rail at the right. On the wall, an eye chart made entirely of astrological and mystical symbols instead of letters, and a poster titled "YOUR AURA" showing a rainbow target. A green-lettered sign above reads "CLINIC". Bright, clean, slightly surreal.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

#### 23. `planetarium.png`

*Used for:* Zyx night 3: the Ice Machine Planetarium.

```text
A small hotel alcove transformed into a planetarium. Every surface is covered in a deep navy night sky full of stars, faint glowing constellation lines and a soft violet-pink nebula. In the center, an ordinary hotel ice machine glows from within with icy blue light, its front labeled "ICE", soft beams of pale light rising from it toward the stars. Cosmic, quiet, lonely and beautiful.

Follow the style guide from the start of this conversation: a 2D anime visual-novel background, cel-shaded, 16:9, empty of people, with the center open and the bottom third simple.
```

## Step 2 prompts: character sprites

Each character needs four images: **neutral**, **happy**, **surprised** and **blush**. Generate the neutral one with the main prompt, then make the other three as edits of it with the expression prompts.

Size in the game: up to **720 px tall**, standing at the bottom center of the screen. The current files are 560×720 (Gerald 700×720). Save to `game/images/sprites/` as `<name>_<expression>.png`, for example `juni_happy.png`.

Nano Banana doesn't reliably produce transparent backgrounds, so each prompt asks for a flat **chroma-key** color instead (green for most, blue for Zyx). Remove it afterwards to get a transparent PNG; see [Getting the images into the game](#getting-the-images-into-the-game).

All the characters are adults. The prompts say so explicitly, because anime styles tend to draw everyone younger otherwise.

### Juni (they/them)

*Aspect ratio:* 3:4 portrait. *Background:* pure chroma-key green (#00FF00).

**`juni_neutral.png`**: generate this first.

```text
Juni, an androgynous adult in their late twenties, wearing a fluffy pastel-pink axolotl kigurumi (animal onesie). The hood is up, framing their face, and the hood has its own cute axolotl face on top: two small round black eyes, a little smile and rosy cheeks. Six feathery hot-pink gill fronds fan out from the sides of the hood. The onesie has a pale pink belly panel and a front zipper, and the sleeves are too long, so their hands are hidden in them, held together shyly in front of the chest. Under the hood: warm light tan skin, short messy dark brown hair with soft bangs, big warm amber-brown eyes, slightly rosy cheeks. Shy, gentle, sweet, a little awkward, with a small closed-mouth smile.

Follow the style guide from the start of this conversation: a 2D anime visual-novel sprite of one adult, waist-up, facing the viewer, on a perfectly flat pure chroma-key green (#00FF00) background.
```

**`juni_happy.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to a big joyful smile: eyes closed into happy upward crescents, mouth open in a bright grin, a light pink blush on the cheeks.
```

**`juni_surprised.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to surprised: eyes opened wide with small pupils, eyebrows raised high, a small round open mouth.
```

**`juni_blush.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to flustered and shy: eyes glancing slightly to the side, eyebrows tilted up, a small wobbly embarrassed smile, and a strong pink blush across the cheeks with little diagonal blush lines.
```

### Gerald (he/him)

*Aspect ratio:* square 1:1 (his sprite is wider). *Background:* pure chroma-key green (#00FF00).

> Waist-up for Gerald means from mid-chest up; his size is the joke.

**`gerald_neutral.png`**: generate this first.

```text
Gerald, a gentle, friendly Sasquatch: a huge, shaggy, very tall creature covered in long chestnut-brown fur with lighter highlights, and a tufted crest on top of his head. His face is a soft tan patch framed by fur, with a heavy furry brow, kind warm brown eyes and a broad dark nose. Big gentle hands cradle a tiny white porcelain teacup with a small pink heart on it, held delicately at chest height with a wisp of steam rising. His massive shoulders fill most of the frame width. Cozy, polite, old-fashioned and dignified, like a shy grandfather, with a calm, kind closed-mouth expression. Drawn as a real creature in anime style, not a person in a costume.

Follow the style guide from the start of this conversation: a 2D anime visual-novel sprite of one adult, waist-up, facing the viewer, on a perfectly flat pure chroma-key green (#00FF00) background.
```

**`gerald_happy.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to a big joyful smile: eyes closed into happy upward crescents, mouth open in a bright grin, a light pink blush on the cheeks.
```

**`gerald_surprised.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to surprised: eyes opened wide with small pupils, eyebrows raised high, a small round open mouth.
```

**`gerald_blush.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to flustered and shy: eyes glancing slightly to the side, eyebrows tilted up, a small wobbly embarrassed smile, and a strong pink blush across the cheeks with little diagonal blush lines.
```

### Solstice (she/her)

*Aspect ratio:* 3:4 portrait. *Background:* pure chroma-key green (#00FF00).

**`solstice_neutral.png`**: generate this first.

```text
Solstice, a radiant adult woman in her early thirties and a festival raver. Warm brown skin, long voluminous wavy hair that fades from bubblegum pink at the top to pale blonde at the ends, bright teal eyes. Glitter on her cheekbones and a small gold star sticker under her left eye. Chunky goggles with round cyan lenses pushed up on her forehead. Gold hoop earrings. A black crop top studded with dozens of tiny glowing multicolored LED lights, over high-waisted holographic shorts just visible at the bottom edge. Stacks of colorful beaded kandi bracelets on both wrists. Bubbly, warm, sparkling, high-energy, with a friendly confident smile.

Follow the style guide from the start of this conversation: a 2D anime visual-novel sprite of one adult, waist-up, facing the viewer, on a perfectly flat pure chroma-key green (#00FF00) background.
```

**`solstice_happy.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to a big joyful smile: eyes closed into happy upward crescents, mouth open in a bright grin, a light pink blush on the cheeks.
```

**`solstice_surprised.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to surprised: eyes opened wide with small pupils, eyebrows raised high, a small round open mouth.
```

**`solstice_blush.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to flustered and shy: eyes glancing slightly to the side, eyebrows tilted up, a small wobbly embarrassed smile, and a strong pink blush across the cheeks with little diagonal blush lines.
```

### Wren (she/her)

*Aspect ratio:* 3:4 portrait. *Background:* pure chroma-key green (#00FF00).

**`wren_neutral.png`**: generate this first.

```text
Wren, an adult woman in her early thirties who works on the event crew. Pale skin, sleek black hair cut in an asymmetric bob, with a long side-swept fringe on one side and a short shaved undercut on the other. Tired but kind violet eyes with faint dark circles. A black over-ear headset with a small boom microphone. A plain black hoodie, a bright pink lanyard around her neck holding a white badge that reads "CREW", and a brown clipboard full of checklists hugged against her chest with one arm. A black walkie-talkie with a green light clipped at her hip. Competent, dry, a little exhausted and secretly soft, with a calm half-smile.

Follow the style guide from the start of this conversation: a 2D anime visual-novel sprite of one adult, waist-up, facing the viewer, on a perfectly flat pure chroma-key green (#00FF00) background.
```

**`wren_happy.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to a big joyful smile: eyes closed into happy upward crescents, mouth open in a bright grin, a light pink blush on the cheeks.
```

**`wren_surprised.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to surprised: eyes opened wide with small pupils, eyebrows raised high, a small round open mouth.
```

**`wren_blush.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key green (#00FF00) background. Change only the facial expression to flustered and shy: eyes glancing slightly to the side, eyebrows tilted up, a small wobbly embarrassed smile, and a strong pink blush across the cheeks with little diagonal blush lines.
```

### Zyx (they/them)

*Aspect ratio:* 3:4 portrait. *Background:* pure chroma-key blue (#0000FF).

> Zyx uses a blue background because a green one would eat into their mint skin.

**`zyx_neutral.png`**: generate this first.

```text
Zyx, an androgynous adult alien ambassador. Smooth pale mint-green skin, three large anime eyes with glossy magenta irises (two in the usual place and a smaller third eye in the center of the forehead), and small pointed ears. A sleek metallic silver bob haircut with perfectly straight bangs, shiny like chrome. Two thin antennae rise from the head, each ending in a softly glowing pink bulb. A silver metallic bodysuit with a high collar of spiky teal points, and a gold diagonal sash across the chest that reads "AMBASSADOR". One hand is raised in a friendly wave, wearing a teal three-fingered glove. Curious, formal, earnest and a little awkward, like a polite diplomat studying Earth, with a small neutral smile.

Follow the style guide from the start of this conversation: a 2D anime visual-novel sprite of one adult, waist-up, facing the viewer, on a perfectly flat pure chroma-key blue (#0000FF) background.
```

**`zyx_happy.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key blue (#0000FF) background. Change only the facial expression to a big joyful smile: eyes closed into happy upward crescents, mouth open in a bright grin, a light pink blush on the cheeks. Apply it to all three eyes, including the one on the forehead.
```

**`zyx_surprised.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key blue (#0000FF) background. Change only the facial expression to surprised: eyes opened wide with small pupils, eyebrows raised high, a small round open mouth. Apply it to all three eyes, including the one on the forehead.
```

**`zyx_blush.png`**: as an edit of the neutral image.

```text
Edit this image: keep the exact same character, outfit, pose, framing, art style and flat pure chroma-key blue (#0000FF) background. Change only the facial expression to flustered and shy: eyes glancing slightly to the side, eyebrows tilted up, a small wobbly embarrassed smile, and a strong pink blush across the cheeks with little diagonal blush lines. Apply it to all three eyes, including the one on the forehead.
```

## Menu art

The main menu shows `game/gui/main_menu.png`, which is a copy of `exterior_night.png`. The in-game menus use `game/gui/game_menu.png`, a blurred copy of the same image. Once you have a new `exterior_night.png`, copy it to `game/gui/main_menu.png`, and save a blurred version (any blur, about 8 px) as `game/gui/game_menu.png`. The left side of the main menu has a dark panel for the buttons, so a busy left edge is fine.

## Getting the images into the game

**Backgrounds:** crop to 16:9 if needed, resize to 1280×720 and save as PNG with the file name above into `game/images/bg/`, replacing the old one.

**Sprites:**

1. Remove the green (or blue) background. Free options: the *Remove background* tool in [Photopea](https://www.photopea.com), remove.bg, or any image editor's magic wand set to the key color.
2. Trim the empty space around the character, keeping the bottom edge where the body is cut off.
3. Resize so the image is at most 720 px tall, keeping the proportions.
4. Export as PNG with transparency, named `<name>_<expression>.png`, into `game/images/sprites/`.

Keep the same size and crop for all four expressions of a character, or the character will jump when their expression changes.

Commit and push, and the website rebuilds itself with the new art.
