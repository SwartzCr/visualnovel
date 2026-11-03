# Midjourney prompts (Niji 7)

Prompts for every background in *Do Not Disturb*, written in the same style as the prompt that produced `game/images/bg/lobby.png`. Each one is ready to paste into Midjourney.

## Keep every scene matching the lobby

1. Upload `game/images/bg/lobby.png` to Midjourney (or use the original lobby image from your Midjourney gallery) and copy its image link.
2. Add `--sref <that link>` to the end of every prompt below. Add `--sw 200` to make the match stronger.
3. That gives all 30 backgrounds the lobby's line art, colors and shading.

## A few notes

- **Signs are left blank** because Midjourney garbles text. Under each prompt is the text to add in an image editor afterwards, if you want it.
- **Paired scenes** (the hotel by day and night, the roof at night and dawn, the ballroom before and during the ark): make the first one, then paste its image link at the very start of the second prompt with `--iw 1.5`, so the place stays the same.
- **Saving:** crop to 16:9, resize to 1280×720, save as PNG with the file name shown, and put it in `game/images/bg/`. Or send it to me and I'll drop it in.

## The lobby (done)

For reference, this is the prompt style that worked:

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the lobby of a retro 1970s hotel-casino at night, a dark wood front desk on the left under a glowing pink neon sign, a big golden chandelier, a wide archway on the right opening onto a dark casino floor with rows of slot machines strung with tiny colorful lights, swirly orange and purple patterned carpet, potted palms, glowing neon pink and cyan accents, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

## Outside the hotel

### `exterior.png`

*Used for:* Friday arrival; Monday goodbyes.

> Make this first, then use it as an image prompt for the night version.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a tall retro 1970s hotel-casino tower on the shore of Lake Tahoe at sunset, beige concrete with bands of windows, a low casino wing with an entrance canopy edged in glowing marquee bulbs, a huge vintage casino sign on a tall pylon on the right with a few dark burned-out letters, snow-capped mountains and tall pine trees behind, sky fading from violet to hot pink to tangerine, an empty parking lot in the foreground, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the big sign: HOTEL PARADIS / CASINO

### `exterior_night.png`

*Used for:* the main menu backdrop.

> Paste your exterior.png link at the very start of the prompt (before the text) so the building matches, and add --iw 1.5.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the same retro 1970s hotel-casino tower on Lake Tahoe at night, starry indigo sky and a thin crescent moon over dark mountains and pines, most windows glowing in different colors pink gold cyan violet and lime, the huge vintage casino sign blazing in pink and cyan neon, warm marquee bulbs over the entrance, a soft pink glow across the dark parking lot, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the big sign: HOTEL PARADIS / CASINO

## Daytime

### `pool.png`

*Used for:* every pool scene; Juni's sunrise ending.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, an indoor hotel pool hall on the ground floor of a retro 1970s hotel-casino, afternoon, a turquoise kidney-shaped pool with a big pink inflatable flamingo floating in it, a huge old glass atrium roof with green metal framing and sunlight pouring down, pale tiled walls with tall windows showing pine trees, potted palms, white lounge chairs, two tall orange patio heat lamps, a red and cream striped beach umbrella set up indoors, a homemade cloth banner strung over the pool, humid cheerful light, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the banner: WATER IS LOVE

### `bedroom.png`

*Used for:* the morning scenes.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a slightly dated 1970s hotel room in early morning light, a rumpled double bed with a lavender bedspread on the left, a window on the right with red curtains half open onto pine trees and a pale sunrise sky, sunbeams slanting across the room, a wood-veneer nightstand with a brass lamp and a folded newspaper, a framed print of a lake on the cream wall, quiet sleepy morning mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the newspaper masthead: THE DAILY DISTURBANCE

## Night: hallways and shared spaces

### `hallway.png`

*Used for:* every night in the hallways.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a long hotel corridor in a retro 1970s hotel-casino at night, one-point perspective straight down the middle, dark plum walls, swirly maroon orange and purple casino carpet, rows of doors on both sides with brass room numbers, half-open doors spilling pink cyan gold and violet light into the hall, brass wall sconces, a pink neon arrow sign on the left wall, a glowing red exit sign at the far end, mysterious inviting party atmosphere, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the neon arrow: ART THIS WAY

### `ballroom.png`

*Used for:* Solstice's last night, the 11:11 ceremony, after midnight.

> This is the one scene that should have people, so remove 'people' from the --no list.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the grand ballroom of an old hotel-casino turned into a psychedelic dance party, tall columns, a huge mirrored disco ball hanging high in the center, beams of pink cyan lime and violet laser light sweeping through haze, glowing geometric shapes projected on the walls, the lower part of the frame a crowd of dancers seen only as dark backlit silhouettes with raised arms, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

### `ballroom_ark.png`

*Used for:* the moment the ark arrives at 11:11.

> Remove 'people' from the --no list. Paste your ballroom.png link at the start with --iw 1.5 so the room matches.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the same psychedelic hotel ballroom party, an ornate golden ark covered in swirling psychedelic patterns carried high above a crowd of dark silhouettes on long poles by figures in shiny silver alien bodysuits with big black almond eyes, the ark glowing with golden light, confetti falling, lasers and a mirrored disco ball, awe and celebration, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* on the ark: DON'T PANIC

### `livingroom.png`

*Used for:* wandering: Auntie Acid's room, The Cozy.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a cozy auntie's living room recreated inside a hotel suite as a calm refuge at a wild party, warm floral wallpaper, a glowing floor lamp with a fringed shade, framed photos on the wall, a wooden rocking chair with a pink cushion on the right, a big round braided rug with jewel-toned floor cushions, a glass bowl of strawberry candies, a small painted wooden sign above the photos, golden gentle safe lighting, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the wooden sign: THE COZY

### `roof.png`

*Used for:* Wren's last night.

> Make this first, then use it as an image prompt for the sunrise version.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the flat gravel rooftop of a tall hotel-casino tower at night high above Lake Tahoe, a sky full of stars and a bright moon over dark snow-capped mountains, the black lake below with a glittering line of casino lights along the shore, an old wooden water tank on stilts on the left, strings of colorful bulb lights, steel cables and a rigging frame on the right, a weathered wooden bench, quiet intimate mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

### `roof_dawn.png`

*Used for:* the sunrise endings and Checkout.

> Paste your roof.png link at the start with --iw 1.5 so the rooftop matches.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, the same gravel hotel rooftop above Lake Tahoe at sunrise, sky glowing from soft blue through lavender and pink to warm gold, the sun just clearing the mountains across the lake with a path of golden light on the water, an old wooden water tank, a weathered bench, slack rigging cables, a few burned-out string lights, tender hopeful end-of-the-night mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

## Juni's art rooms

### `room404.png`

*Used for:* Juni night 1: Room 404, Room Not Found.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room turned into an art installation about a missing web page, everything glossy white and pale grey and lit like a computer screen, giant navy numbers on the back wall, retro computer error dialog boxes made of cardboard hanging from the ceiling on fishing line, oversized white mouse cursors stuck to the walls, thin cyan and magenta glitch stripes of light across the room, funny and uncanny, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the wall: 404 / ROOM NOT FOUND

### `lostfound.png`

*Used for:* Juni night 2: the Lost & Found.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room transformed into a warm old-fashioned library-style lost and found for emotions, wooden shelves filling the back wall with rows of pastel cardboard boxes each with a little handwritten label card, a wooden counter with a small red sign, brass lamps casting amber light, floating dust motes, nostalgic and gentle, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* box labels: MISPLACED CONFIDENCE, UNSENT TEXTS, OLD NICKNAMES, ONE COURAGE; counter sign: TAKE ONE, LEAVE ONE

### `regen.png`

*Used for:* Juni night 3: the Regeneration Tank.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room painted to feel like the bottom of a deep peaceful lake, everything blue and teal, rippling caustic light patterns dancing across the walls and ceiling, tall swaying green water plants at the sides, little rising bubbles, a large oval waterbed in the middle glowing softly from below, calm dreamy healing mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* glowing letters on the back wall: THE REGENERATION TANK

## Gerald's art rooms

### `breakfast.png`

*Used for:* Gerald night 1: the Breakfast Schism.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room turned into a candlelit cathedral devoted to breakfast, warm amber gloom, a black gothic banner hanging on the left and a white banner on the right, a small wooden altar in the center lined with lit candles holding a black cast-iron skillet with one perfect sunny-side-up egg, lit by a heavenly golden spotlight, solemn and absurd, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* left banner: CHURCH OF CAST IRON; right banner: TEMPLE OF TEFLON; over the altar: THE HOLY SKILLET

### `forest.png`

*Used for:* Gerald night 2: Room 312, turned into a forest.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room completely transformed into an ancient misty pine forest at night, tall dark tree trunks, a floor of thick green moss, low fog drifting across the ground, dozens of glowing fireflies, on the right a hotel bed entirely overgrown with moss and ferns beside a vintage floor lamp casting a warm golden pool of light, a small brass room number on a tree trunk, magical hushed homesick mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the room number: 312

### `cryptid.png`

*Used for:* Gerald night 3: Cryptids Anonymous.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a community support-group room inside an old hotel, beige walls, checkered linoleum floor, a fluorescent ceiling light, a circle of grey metal folding chairs, a folding table with a steel coffee urn and paper cups, a blue banner on the wall, a poster of a dark winged figure with glowing red eyes, a big green inflatable Loch Ness monster in the corner wearing a name-tag sticker, earnest deadpan and sweet, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* banner: CRYPTIDS ANONYMOUS; poster: BELIEVE IN YOURSELF; name tag: HELLO MY NAME IS

## Solstice's art rooms

### `exchange.png`

*Used for:* Solstice night 1: the Human Stock Exchange.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel conference room turned into a chaotic glittering stock exchange, glowing LED ticker boards running across the top of the walls in green and red, a trading desk with old CRT monitors showing zigzag charts, a big gold neon sign, colorful confetti hanging in the air, dark room with dramatic neon glow, frantic energy, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* the neon sign: HUMAN STOCK EXCHANGE; tickers like SELF ▲4.2, VIBES ▼1.1, GLITTER ▲99

### `karaoke.png`

*Used for:* Solstice night 2: Confession Booth Karaoke.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a small hotel room turned into an intimate karaoke lounge, deep red velvet curtains on every wall, a mirrored disco ball throwing specks of light, a glowing karaoke screen in the center showing lyric bars, a pink neon sign on the left and a cyan neon sign on the right, a vintage microphone on a stand, a curtained confession-booth doorway at the side, moody purple light, warm and a little melancholy, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* pink neon: CONFESS; cyan neon: ABSOLVED

## Wren's art rooms

### `backstage.png`

*Used for:* Wren night 1: backstage at the ballroom.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, backstage behind the ballroom stage of an old hotel-casino during a party, dark, metal scaffolding towers on both sides, thick black cables snaking across the floor, scuffed black road cases, a gap in heavy red and magenta stage curtains in the middle letting through beams of pink cyan and green laser light from the dance floor, a tall yellow ladder on the right, a single bare work light hanging at the upper left, secretly magical behind-the-scenes mood, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* stencils on the road cases: PARTY HARDER, FRAGILE: FEELINGS, LASERS

### `mission.png`

*Used for:* Wren night 2: the crew's fire station (a linen closet).

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel linen closet secretly turned into the party crew's control room, shelves stacked with folded white towels on the left, a bank of old monitors glowing green with hand-drawn maps of the hotel, a big wall map studded with little red magnets, a control panel of four big glowing arcade buttons, a row of walkie-talkies charging with little green lights, an open toolbox on the floor, dim cozy competent backstage feeling, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* buttons: FOG KILL, LASERS, ARK RIG, PANIC; door sign: STAFF ONLY; a monitor clock: 11:11

*Wren night 3 uses the roof (above).*

## Zyx's art rooms

### `fortune.png`

*Used for:* Zyx night 1: the Oracle of Ping Pong.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room bathed in deep purple light turned into a retro-futurist fortune-telling booth, on the left a boxy silver 1950s robot with a glass dome head containing a glowing pink orb and a small screen with two glowing teal eyes, on the right a big clear lottery drum full of white ping-pong balls on a brass stand, colorful capes hanging on hooks, small painted stars on the ceiling, a violet neon sign at the top, whimsical and mysterious, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* neon sign: THE ORACLE OF PING PONG; robot slot: FORTUNES 1¢

### `clinic.png`

*Used for:* Zyx night 2: the Clinic of Unnecessary Procedures.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room made into a whimsical retro medical clinic, mint-green tiled walls, a white linoleum floor, an examination table with a crinkly paper sheet, a pink privacy curtain on a rail at the right, an eye chart made entirely of astrological and mystical symbols, a poster of a rainbow aura target, a green-lettered sign above, bright clean slightly surreal, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* sign: CLINIC OF UNNECESSARY PROCEDURES; poster: YOUR AURA

### `planetarium.png`

*Used for:* Zyx night 3: the Ice Machine Planetarium.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a small hotel alcove transformed into a planetarium, every surface covered in a deep navy night sky full of stars, faint glowing constellation lines and a soft violet and pink nebula, in the center an ordinary hotel ice machine glowing from within with icy blue light, soft beams of pale light rising from it toward the stars, cosmic quiet lonely and beautiful, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* on the machine: ICE

## Random-encounter art rooms

### `penguinpost.png`

*Used for:* Penguin Post.

> This room has penguin staff, so they're fine to keep despite the --no people.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room turned into a post office at the South Pole in the far future, sparkly shiny ice and snow decor lit by blue and pink neon, icicles along the ceiling, a long white service counter with three cute cartoon penguins behind it wearing tiny navy postal caps, a wall of blue post-office boxes on the left, a stack of brown parcels on the right, a digital now-serving display, falling glitter snow, festive and frosty, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* neon sign: PENGUIN POST / PLEASE TAKE A NUMBER; display: NOW SERVING 3

### `fanbar.png`

*Used for:* the OnlyFans Fanny Bar.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room turned into a cool breezy oasis filled with every kind of electric fan, box fans desk fans pedestal fans and ceiling fans, faint white breeze lines in the air, pale aqua walls, a small pink bar counter in the center lined with spray-mister bottles under a pink neon sign, a big hand-painted banner at the top, a basket of folding hand fans by the door, a retro blue and yellow video rental booth in the corner, playful bright and airy, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* neon: FANNY BAR; banner: PLEASE SUBSCRIBE!!; booth: NUTBUSTER; basket: FOR SUBSCRIBERS ONLY!

### `tentacletopia.png`

*Used for:* Tentacletopia.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a hotel room transformed into the bottom of the sea around a sunken art deco city, leaning art deco towers on the left and right with faintly glowing pink and cyan neon signs, swaying green kelp at the edges, shafts of blue light from above, drifting bubbles, large glowing jellyfish in pink violet and pale blue floating overhead with long trailing tentacles, a sandy floor with a low wall of colorful coral, mysterious beautiful and a little silly, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* tower signs: OCEAN, HOTEL

### `optical.png`

*Used for:* Zany Optical.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a strip-mall optometrist's office remixed into 1980s vaporwave, pink-to-teal gradient walls with a palm tree pattern, a magenta and cyan neon grid floor in perspective, a dark sign with pink neon letters at the top, a cheerful tablet on a stand acting as the receptionist showing a smiley face, a classic eye chart, an exam machine with two big round lenses, an enormous googly eye mounted on the wall, goofy and bright retro-future, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* neon sign: ZANY OPTICAL; lenses: A and B

### `speeddating.png`

*Used for:* Platonic Speed Dating.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a plum-colored side room of an old hotel ballroom set up for a party game, a small gold chandelier, a hot-pink banner, two big handheld whiteboard paddles on poles on opposite walls, a strip of yellow tape running down the middle of the wooden floor dividing the room in two, a red drawstring grab bag in the corner, warm playful game-show energy, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* banner: PLATONIC SPEED DATING; paddles: THIS and THAT

### `letitgo.png`

*Used for:* the Let It Go workshop.

```text
hand-painted anime background art, 2D anime key visual, flat cel shading with two-tone shadows, bold clean line art, simplified shapes, a dim hotel conference room set up for a self-help workshop, a small low stage with a big projector screen showing a simple drawing of a phone crossed out in red, an easel with a hand-lettered posterboard slide, a craft table on the left with a row of small colorful wooden phone-shaped blocks decorated with googly eyes, rows of empty grey folding chairs facing the stage, calm earnest and gently funny, empty open space in the center, vibrant saturated colors, soft bloom --ar 16:9 --niji 7 --s 400 --no people, text, watermark, photorealistic, 3d render, photo, realistic
```

*Text to add afterwards:* screen: LET IT GO / life after the phone; posterboard: STEP 1: BREATHE
