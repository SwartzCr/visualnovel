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
    show text "{size=48}{color=#ff5fb8}DO NOT DISTURB{/color}{/size}\n\n{size=22}{color=#c8b8ff}three nights at the Hotel Paradiso{/color}{/size}" at truecenter as title with dissolve
    pause 2.5
    hide title with dissolve
    $ quick_menu = True

    scene bg exterior with slowfade
    $ time_label = "Friday — Arrival"

    "It was a long drive, but you're finally there - your friend said to come, but was light on details. Your plan is to just see where it goes. Maybe you'll spend the weekend hiding in your room or maybe you'll find your soulmate - who knows!"
    "The Hotel Paradiso is a sixteen-story hotel-casino on the Nevada shore of Lake Tahoe, built in 1971 and showing every year of it. The people on the casino floor pumping quarters into slot machines are too hypnotized to notice the parade of weirdly dressed people streaming in. You take a deep breath and walk on through, keeping your eyes down."


    scene bg lobby with dissolve
    $ time_label = "Friday — The Lobby"
    "The lobby still has its 1970s carpet, a migraine of orange and purple swirls. You shuffle towards the front desk only raising your eyes when you hear a voice."
    show wren neutral with dissolve

    w "Hi. Welcome to the Paradiso. I'm Wren, crew. Usually I'm working behind the scenes with Black Ops, but I'm filling in here for now. I'd say 'Welcome Home' but this isn't {i}that{/i} party."
    w "Is this your first time? Don't worry, everything's going to go great - I'll see to that. We don't bite ... mostly ;)"

    menu:
        w "Any questions before I let you loose?"

        "\"Is there anything you need help with right now?\"":
            $ gain("wren", 1)
            w surprised "Huh. Nobody asks crew that."
            w neutral "I'm all set here, you're one of the last people to arrive. But hold that thought. I might cash it in at 3 AM when the Carpet Master catches fire."

        "\"What if I can't handle it?\"":
            w "Find your way to The Cozy and Auntie Acid will fix you right up. If things get really bad come find me."

        "\"So what {i}is{/i} this, exactly?\"":
            w "A safe container for you to express yourself. It'll get weird, but just maybe you will too."

    w neutral "Here's the only advice I give first-timers. Don't watch, participate. We are all the actors and the whole hotel is a stage."
    w "Push your boundaries. Walk into the room you'd normally walk past. Say the thing you'd normally keep to yourself. Be whoever you actually are. This is the one weekend nobody's going to laugh at you for it."
    w neutral "Oh right, the pool's on the ground floor. You can hang out there in the afternoons. The hallways will be popping all night. Now get out there and be yourself. Welcome to the party!"
    hide wren with dissolve

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
        "{b}THE DAILY STICK{/b} — Saturday Edition"
        "{i}HEADLINE: The body accuses the mind of having \"Lost The Thread\" while new guests complain about the amount of in jokes. More on page 3.{/i}"
        "{i}HOROSCOPE (all signs): Today someone will tell you a secret about themselves. Try to listen, do not make it about you.{/i}"
        "{i}IN: Metafiction, callbacks, romantasy. OUT: Veiled metaphors, doomerism, clown car-culture.{/i}"
    else:
        "Sunday. The light through the window is the color of weak tea. Somewhere below you can hear the faint pounding of bass from a renegade sound system."
        "{b}THE DAILY STICK{/b} — Sunday (Final) Edition"
        "{i}HEADLINE: SOURCES CONFIRM SOMETHING ARRIVES AT 11:11. BEST TO MAKE YOUR WISHES NOW.{/i}"
        "{i}HOROSCOPE (all signs): The last night of anything is the one you'll remember. Try to stay sober enough to follow through.{/i}"
        "{i}MARKET REPORT: The Free Hugs booth has capitulated to market forces, hugs will now be available only for those with a monthly subscription. Shrugs will remain free. {/i}"

    return


################################################################################
## Days at the pool
################################################################################

label pool_time:
    scene bg pool with slowfade
    $ time_label = ("", "Friday", "Saturday", "Sunday")[day] + " — The Pool"

    if day == 1:
        "The pool is the bright, (somewhat) ordinary half of the party: an indoor pool on the ground floor, under a big old glass atrium roof gone green at the seams. The smell of chlorine permeates the air."
        "Most of the costumes have been swapped for swimsuits. Some have not. To the extent that they can people are letting their freak flags fly. Someone brought in a sound system and you can barely make conversation over the sound of the music, but you try anyway."
    elif day == 2:
        "The pool on Saturday afternoon is full of people recovering from Friday night. Someone is teaching a slow-motion water aerobics class to no music at all. You revel in the silence."
    else:
        "Last afternoon. The pool has the sleepy tenderness of a place where a lot of people have cried in a good way.  The party isn't over but most people blew their wads already. You've still got a little left in the tank."

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

        "A raver covered in kandi beads, handing out glitter like communion and asking a lot of questions." (guest="solstice") if pool_seen["solstice"] == 0:
            $ who = "solstice"
        "Solstice, asleep on a lounger right under one of the big heat lamps, LED bikini top switched off." (guest="solstice") if pool_seen["solstice"] == 1:
            $ who = "solstice"

        "A person in black fishing a disco ball out of the deep end with a net." (guest="wren") if pool_seen["wren"] == 0:
            $ who = "wren"
        "Wren, eating a sad sandwich behind the towel hut." (guest="wren") if pool_seen["wren"] == 1:
            $ who = "wren"

        "A silver alien under a beach umbrella, indoors, studying the pool with great suspicion." (guest="zyx") if pool_seen["zyx"] == 0:
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
        "Night falls and the Paradiso turns inside out. Every door is open, inviting you."
        "Bass comes up through the carpet from the ballroom. A group of people tied together with a giant ball of yarn stumble past you."
    elif day == 2:
        "Saturday night. The hallways are louder and stranger. A troupe of mute clowns in fishnets moves through the crowd writing notes on invisible clipboards and nodding in approval."
    else:
        "Sunday night. The last night. The clocks in the stairwell all read the same thing: 11:11."
        "Everyone looks slightly fried, like they're on the edge of breaking into laughter or tears. You take a few deep breaths trying to recenter yourself for another adventure."

    call random_encounter
    call hallway_encounter
    scene bg hallway with dissolve
    if day == 3:
        "It's 10:40. You have time for one more thing before the big show."
    else:
        "The night isn't over. The hallway takes you back."
    call hallway_encounter

    if day < 3:
        scene bg hallway with slowfade
        "Somewhere around four in the morning, the hallway finally gets quiet enough to hear the ice machine humming to itself. You find your room by touch."
    return


label hallway_encounter:
    scene bg hallway with dissolve
    menu:
        "Which way do you wander?"

        "A pink glowing tail disappears into a room piled to the ceiling with stuffed animals." (guest="juni") if night_seen["juni"] == 0 and "juni" not in met_tonight:
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

        "Behind a door marked BACKSTAGE, something is sparking. A voice says: \"No no no no no.\"" (guest="wren") if night_seen["wren"] == 0 and "wren" not in met_tonight:
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
        "You follow the smell of cardamom to a suite with a hand-painted sign on the door: THE COZY. Inside, someone has rebuilt your grandmothers living room, down to the doilies."
        oz "Sit, sit. You look confused, and maybe a little tired. Don't be, take a seat and have some tea."
        "Auntie Acid is maybe sixty-five, in a kaftan covered in hand-sewn mirrors. She rocks. She buzzes with an inner energy. She has, you'd bet, seen some things."
        oz "First time? You've got first-time eyes. That's all right. Everyone here was new once. Even the Sasquatch."
        oz "Here's the only advice I give, sweetheart. Be yourself, feel good as yourself, then go be kind to somebody."
        "You leave feeling oddly blessed, only remembering later that you forgot to drink your tea."
    elif wanders == 2:
        scene bg exchange with dissolve
        "You wander into the Human Stock Exchange alone. An Auguste clown in a pointed bra and fishnets immediately pantomimes, with great urgency, that you must sell shares of yourself."
        "You sell eleven percent of yourself to a woman dressed as sexy Garfield. The ticker above you reads YOU ▲0.4."
        "It feels great to be on the winning side of capitalism for once. You feel weirdly giddy and guilty, and rush out the door before the market can correct."
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
    "Seven hundred people in costume shuffle into the ballroom in the dark, holding their breath. Someone whispers {i}is it happening{/i} and fifty people go {i}shhhhhh{/i}."
    "At 11:11 the doors at the back of the ballroom swing open."
    scene bg ballroom_ark with flash
    "A procession of people in silver alien suits carries a golden ark through the crowd. It's covered in psychedelic patterns. On the front, in big friendly letters: DON'T PANIC."
    "Up on the stage, the leader of the covenant grabs a mic and delivers a rousing speech. You only catch bits and pieces, something about grabbing life by the cockles, and riding the bubbles pop into the sunset."
    "The aliens set the ark between them and open the lid."
    "Inside it's empty, your enthusiasm is what fills it. You realize that society is also a shared hallucination. This doesn't end here."
    "The ballroom is completely silent for three full seconds."
    "Then the bass drops so hard the chandelier swings. Seven hundred people scream. Confetti falls from everywhere."
    "It is incredibly goofy, but heartfelt. You feel yourself beginning to tear up."
    return
