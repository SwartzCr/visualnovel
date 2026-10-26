## script.rpy — arrival, the three-day loop, and the 11:11 ceremony.
##
## Structure
##   Each day:   one conversation at the pool          (pool_time)
##   Each night: two encounters in the hallways        (night_time)
##               which usually lead into an art room
##   Night three ends with the ark at 11:11, then the finale.
##
## Each guest has two pool chapters and three night chapters. Chapters play in
## order no matter which day or night you choose them, so any guest can be
## followed from start to finish.

label start:
    $ quick_menu = False
    scene black
    pause 0.6
    show text "{size=48}{color=#ff5fb8}DO NOT DISTURB{/color}{/size}\n\n{size=22}{color=#c8b8ff}three nights at the Hotel Marisol{/color}{/size}" at truecenter as title with dissolve
    pause 2.5
    hide title with dissolve
    $ quick_menu = True

    scene bg exterior with slowfade
    $ time_label = "Friday — Arrival"

    "The invitation came as a paper card with no return address. One side said FRIDAY, 3PM. The other side said {i}You were never here.{/i}"
    "Your friend Tamsin vouched for you. That's how it works. Somebody who's been coming for years puts their name next to yours, and if you can't hang, neither can they."
    "No photos. No posting. No saying the name of the thing out loud. Nobody seems sure it has a name."
    "The Hotel Marisol is a two-story motor lodge in the hills that has been closing down since 1987. Somebody has rented every room for the weekend."
    "The neon sign has lost its I. It now reads HOTEL MAR SOL, which several people in the parking lot are already treating as a prophecy."

    tam "omg you're here?? ok I'm already in a room full of balloons and I can't find the door"
    tam "go check in. find the person in black with the clipboard. ask before touching. drink tea. let it get weird"
    tam "I'll find you!!!"

    "You will not see Tamsin again until Sunday."

    scene bg lobby with dissolve
    $ time_label = "Friday — The Lobby"

    "The lobby smells like incense, chlorine, and something baking. A brass bell sits on the desk next to a hand-lettered sign: NO PHOTOS."
    "Behind the desk, a person in head-to-toe black is talking into a headset while writing on a clipboard while handing someone a key."

    show wren neutral with dissolve

    w "—no, the fog machine in 312 is {i}supposed{/i} to be in the forest. Yes. The whole forest. Copy."
    w "Sorry. Hi. Welcome to the Marisol. You're not checking in, because everyone who enters is already checked in. It's on the sign."
    w "I'm Wren. Crew. Care team, logistics, lost keys, lost people. If anything goes sideways this weekend, find someone dressed like me."

    menu:
        w "Any questions before I hand you the rules? I have to say them out loud. Legally. Spiritually."

        "\"Is there anything you need help with right now?\"":
            $ gain("wren", 1)
            show wren surprised
            w "Huh. Nobody asks crew that."
            show wren neutral
            w "I'm fine. But thank you. Hold that thought. I might cash it in at 3 AM."

        "\"What happens if I break a rule?\"":
            w "Depends on the rule. Most of them are about being kind, so mostly you'll have to sit with having been unkind, which is worse than being kicked out."
            w "The few that get you kicked out, you'll know."

        "\"So what {i}is{/i} this, exactly?\"":
            w "That's the one question nobody here can answer. I've been crewing for six years and I'm not allowed to say."
            w "Not because it's a secret. Because the second anyone says it out loud, it turns into a brochure."

    show wren neutral
    w "Okay. The rules."
    w "One: no photos, no posting. Your phone is a flashlight and an alarm clock this weekend."
    w "Two: ask before you touch anyone. Ask before you touch their costume. Some of these costumes took four hundred hours."
    w "Three: there's no bar. There's a tea bar. Alcohol is where most of the bad nights in the world start."
    w "Four: there are no spectators here. If you walk into a room, you're part of the room."
    w "Five: if you're having a hard time, find someone in black, or find Grandma Ozone's living room. Second floor. Follow the smell of cardamom."
    w "This weekend, the Pool People and the Order of the Ice Machine are at war over the true nature of water. That will be resolved Sunday at 11:11 PM. Probably."
    w "Pool's open in the afternoons. Hallways are open all night. Welcome."

    walkie "Wren, the axolotl is stuck in the revolving door again."
    show wren happy
    w "Copy. On my way. That one's a regular."
    hide wren with dissolve

    "And just like that, you're in."
    "Tip: open the {color=#ff5fb8}Guests{/color} menu at the bottom of the screen to see everyone you've met."

    jump the_weekend


label the_weekend:
    while day <= 3:
        if day > 1:
            call morning
        call pool_time
        call night_time
        $ day += 1

    jump finale


################################################################################
## Mornings
################################################################################

label morning:
    scene bg bedroom with slowfade
    $ time_label = ("", "", "Saturday — Morning", "Sunday — Morning")[day]

    if day == 2:
        "You wake up on top of the covers in your shoes, in a room you're fairly sure is yours. Someone has drawn a small, friendly eye on the bathroom mirror in lipstick."
        "A newspaper has been slid under the door."
        "{b}THE DAILY DISTURBANCE{/b} — Saturday Edition"
        "{i}HEADLINE: POOL PEOPLE ACCUSE ICE MACHINE OF 'COLDNESS.' ICE MACHINE: 'WE ARE THE SAME WATER.'{/i}"
        "{i}HOROSCOPE (all signs): Today someone will tell you a secret about themselves. Do not make it about you. Do not make it a podcast.{/i}"
        "{i}LOST AND FOUND: One (1) Sasquatch footprint, left foot. Please return to the tea bar.{/i}"
    else:
        "Sunday. The light through the window is the color of weak tea. Somewhere below, a single kazoo is playing what might be the national anthem of a country that doesn't exist yet."
        "{b}THE DAILY DISTURBANCE{/b} — Sunday (Final) Edition"
        "{i}HEADLINE: SOURCES CONFIRM SOMETHING ARRIVES AT 11:11. SOURCES DECLINE TO SAY WHAT. SOURCES ARE ALIENS.{/i}"
        "{i}HOROSCOPE (all signs): The last night of anything is the one you'll remember. Say the thing. Ask first. Then say the thing.{/i}"
        "{i}CLASSIFIEDS: Have you seen my friend? Answers to Tamsin. Last seen inside a balloon. — Tamsin{/i}"

    return


################################################################################
## Days at the pool
################################################################################

label pool_time:
    scene bg pool with slowfade
    $ time_label = ("", "Friday", "Saturday", "Sunday")[day] + " — The Pool"

    if day == 1:
        "The pool is the bright, ordinary half of the party. Sunscreen, towels, the Pool People's banner flapping over the deep end: WATER IS WARM. WATER IS LOVE."
        "Most of the costumes have been swapped for swimsuits. Some have not. Some never will be."
    elif day == 2:
        "The pool on Saturday afternoon is full of people recovering from Friday night. Someone is teaching a slow-motion water aerobics class to no music at all."
        "A herald in a gold cape walks the deck with a scroll."
        herald "HEAR YE! The Order of the Ice Machine has frozen three of our pool noodles! The Pool People demand reparations in the form of warmth!"
    else:
        "Last afternoon. The pool has the sleepy tenderness of a place where a lot of people have cried in a good way."
        "The Pool People have lowered their banner to half mast, out of respect, or because the rope broke."

    menu:
        "Who do you spend the afternoon with?"

        "A pink axolotl kigurumi, sitting fully dressed at the pool's edge, looking very hot." (guest="juni") if pool_seen["juni"] == 0:
            $ who = "juni"
        "Juni the axolotl, floating face-up on a pizza-shaped inflatable." (guest="juni") if pool_seen["juni"] == 1:
            $ who = "juni"

        "A Sasquatch in an innertube in the shallow end, holding a teacup above the water." (guest="gerald") if pool_seen["gerald"] == 0:
            $ who = "gerald"
        "Gerald, leading a very slow 'forest bathing' session on the pool deck." (guest="gerald") if pool_seen["gerald"] == 1:
            $ who = "gerald"

        "A raver in fur leg warmers, handing out glitter like communion." (guest="solstice") if pool_seen["solstice"] == 0:
            $ who = "solstice"
        "Solstice, asleep on a lounger in the full sun, LED top switched off." (guest="solstice") if pool_seen["solstice"] == 1:
            $ who = "solstice"

        "A person in black fishing a disco ball out of the deep end with a net." (guest="wren") if pool_seen["wren"] == 0:
            $ who = "wren"
        "Wren, eating a sad sandwich behind the towel hut." (guest="wren") if pool_seen["wren"] == 1:
            $ who = "wren"

        "A silver alien under a giant umbrella, studying the pool with great suspicion." (guest="zyx") if pool_seen["zyx"] == 0:
            $ who = "zyx"
        "Zyx, collecting lost flip-flops in a bag labeled EARTH ARTIFACTS." (guest="zyx") if pool_seen["zyx"] == 1:
            $ who = "zyx"

    $ pool_seen[who] += 1
    $ met.add(who)
    call expression "%s_pool_%d" % (who, pool_seen[who])
    return


################################################################################
## Nights in the hallways
################################################################################

label night_time:
    $ met_tonight = []
    $ time_label = ("", "Friday", "Saturday", "Sunday")[day] + " — Night"
    scene bg hallway with slowfade

    if day == 1:
        "Night falls and the Marisol turns inside out. Every door is open. Every room is something else now."
        "Bass comes up through the carpet from the ballroom. Someone in a cape runs past you holding a lit candle and a stapler, apologizing."
    elif day == 2:
        "Saturday night. The hallways are louder and stranger. A troupe of mute clowns in fishnets moves through the crowd selling shares in people."
        "A walkie-talkie taped to the ceiling crackles: {i}Room 404 has been located. Repeat. Room 404 has been located.{/i}"
    else:
        "Sunday night. The last night. The tickers in the stairwell all read the same thing: 11:11."
        "People are hugging in doorways for no reason. You catch yourself doing it too."

    call hallway_encounter
    scene bg hallway with dissolve
    if day == 3:
        "It's 10:40. You have time for one more thing before the ark."
    else:
        "The night isn't over. The hallway takes you back."
    call hallway_encounter

    if day < 3:
        scene bg hallway with slowfade
        "Somewhere around four in the morning, the hallway gets quiet enough to hear the ice machine humming to itself. You find your room by touch."
    return


label hallway_encounter:
    scene bg hallway with dissolve
    menu:
        "Which way do you wander?"

        "A pink glowing tail disappears into a room with no number." (guest="juni") if night_seen["juni"] == 0 and "juni" not in met_tonight:
            $ who = "juni"
        "Juni is standing very still in front of a door labeled LOST & FOUND." (guest="juni") if night_seen["juni"] == 1 and "juni" not in met_tonight:
            $ who = "juni"
        "Blue light pours out of a room that sounds like the bottom of a lake. An axolotl hood bobs in the doorway." (guest="juni") if night_seen["juni"] == 2 and "juni" not in met_tonight:
            $ who = "juni"

        "A very tall shape is being dragged down the hall by two rival breakfast cults." (guest="gerald") if night_seen["gerald"] == 0 and "gerald" not in met_tonight:
            $ who = "gerald"
        "Room 312 smells like rain and cedar. A Sasquatch is standing in the doorway, not going in." (guest="gerald") if night_seen["gerald"] == 1 and "gerald" not in met_tonight:
            $ who = "gerald"
        "Through a door marked SUPPORT GROUP, you see Gerald in a folding chair that is much too small." (guest="gerald") if night_seen["gerald"] == 2 and "gerald" not in met_tonight:
            $ who = "gerald"

        "LED lights and a cheering crowd: someone is buying and selling people on the stock exchange." (guest="solstice") if night_seen["solstice"] == 0 and "solstice" not in met_tonight:
            $ who = "solstice"
        "From a curtained booth, Solstice's voice, singing a confession very badly and very sincerely." (guest="solstice") if night_seen["solstice"] == 1 and "solstice" not in met_tonight:
            $ who = "solstice"
        "The ballroom. Lasers. In the middle of the floor, Solstice, dancing like it's the last song on Earth." (guest="solstice") if night_seen["solstice"] == 2 and "solstice" not in met_tonight:
            $ who = "solstice"

        "Wren is half-carrying a man in pajamas toward the smell of cardamom." (guest="wren") if night_seen["wren"] == 0 and "wren" not in met_tonight:
            $ who = "wren"
        "A door marked STAFF ONLY is open a crack. Inside, someone in a headset says your name." (guest="wren") if night_seen["wren"] == 1 and "wren" not in met_tonight:
            $ who = "wren"
        "The stairwell to the roof is propped open. Wren's walkie is chirping somewhere above." (guest="wren") if night_seen["wren"] == 2 and "wren" not in met_tonight:
            $ who = "wren"

        "A silver figure is feeding ping-pong balls into a robot and taking notes." (guest="zyx") if night_seen["zyx"] == 0 and "zyx" not in met_tonight:
            $ who = "zyx"
        "Two nurses are wheeling a protesting alien into the Clinic of Unnecessary Procedures." (guest="zyx") if night_seen["zyx"] == 1 and "zyx" not in met_tonight:
            $ who = "zyx"
        "The ice machine alcove is glowing. Zyx's antennae are silhouetted against a field of stars." (guest="zyx") if night_seen["zyx"] == 2 and "zyx" not in met_tonight:
            $ who = "zyx"

        "Don't follow anyone. Just wander." (guest="wander"):
            $ who = None

    if who is None:
        call wander
    else:
        $ night_seen[who] += 1
        $ met.add(who)
        $ met_tonight.append(who)
        call expression "%s_night_%d" % (who, night_seen[who])
    return


label wander:
    $ wanders += 1
    if wanders == 1:
        scene bg livingroom with dissolve
        "You follow the smell of cardamom into a living room someone has rebuilt inside a hotel suite, down to the doilies."
        oz "Sit, sit. Have a candy. They're strawberry. Everything here is strawberry, that's the rule."
        "Grandma Ozone is maybe seventy, in a cardigan covered in hand-sewn mirrors. She rocks. She hums. She has, you'd bet, seen some things."
        oz "First time? You've got first-time eyes. That's all right. Everyone here was new once. Even the Sasquatch."
        oz "Here's the only advice I give, sweetheart. Don't come to watch. Come to be watched by something bigger than you. Then go be kind to somebody."
        "You eat the candy. It's very strawberry. You leave feeling oddly blessed."
    elif wanders == 2:
        scene bg exchange with dissolve
        "You wander into the Human Stock Exchange alone. A mute clown in a bra and fishnets immediately pantomimes, with great urgency, that you must sell shares of yourself."
        "You sell eleven percent of yourself to a woman dressed as a lighthouse. The ticker above you reads YOU ▲0.4."
        "It feels great. You don't know why. You leave before the market can correct."
    else:
        scene bg cryptid with dissolve
        "You find an empty folding-chair circle in a room labeled CRYPTIDS ANONYMOUS. There's an inflatable Loch Ness Monster wearing a name tag."
        "You sit down for a second. The silence is really nice. Nessie doesn't judge."
        "When you get up, someone has left a small note on your chair: {i}you are not blurry here.{/i}"
    return


################################################################################
## Sunday, 11:11
################################################################################

label ceremony:
    scene bg ballroom with slowfade
    $ time_label = "Sunday — 11:11 PM"
    "At 11:05 the music stops."
    "Seven hundred people in costume stand in the ballroom in the dark, breathing. Someone whispers {i}is it happening{/i} and fifty people go {i}shhhhhh{/i}."
    "At 11:11 the doors at the back of the ballroom swing open."
    scene bg ballroom_ark with flash
    "A procession of people in silver alien suits carries a golden ark through the crowd. It's covered in psychedelic patterns. On the front, in big friendly letters: DON'T PANIC."
    "Up on the stage, the leader of the Pool People and the High Abbot of the Ice Machine face each other. They have been at war over the true nature of water all weekend."
    "The aliens set the ark between them and open the lid."
    "Inside is a single rubber duck."
    "The ballroom is completely silent for three full seconds."
    "Then the High Abbot of the Ice Machine starts to cry, and the leader of the Pool People starts to cry, and they hug, because of course. Ice is water. A pool is water. A duck floats on both. They were never at war."
    "The bass drops so hard the chandelier swings. Seven hundred people scream. Confetti falls from somewhere it couldn't possibly have been hidden."
    "It is incredibly stupid. You are crying too."
    return
