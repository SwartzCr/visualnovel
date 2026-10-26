## solstice.rpy — Solstice, a raver in fur leg warmers and an LED top. Pronouns: she/her.
## Everyone loves her when the lights are on. The route is about the lights going off.

label solstice_pool_1:
    "A woman in rainbow fur leg warmers, holographic shorts and a black crop top studded with little LEDs is working her way down the row of loungers, handing out glitter like it's communion."
    "She has goggles pushed up on her forehead and a sticker of a star under one eye. She reaches you and lights up, literally. Her top flickers through the rainbow."
    show solstice happy with dissolve
    s "HI! Hi hi. You're new. You have new-person energy. It's so cute. Hold out your hand. No, the other one. Perfect."
    "She produces a bracelet of plastic beads from somewhere. It says, in lettered beads, ur doing great."
    menu:
        "Hold out your wrist and let her put it on.":
            $ gain("solstice", 1)
            s happy "There. Now you're one of us. That's how it works. That's literally the whole ritual."

        "\"Wait, I want to give you something too.\"":
            $ gain("solstice", 2)
            "You dig in your pockets. All you have is a hotel mint, slightly warm."
            s surprised "For me?"
            s blush "Oh my god. No one ever gifts back. Everyone just takes the glitter and runs."
            "She holds the mint up to the sun like a jewel, then puts it very carefully into a pocket on her leg warmer."
            s happy "I'm going to keep this forever. Or eat it at three in the morning. One of the two."

        "\"Oh, I didn't bring anything to trade.\"":
            s neutral "It's not a trade! It's a gift! Gifts don't do math!"
            "She puts the bracelet on you anyway, with a firm little pat."

    show solstice happy
    s "I'm Solstice. Like the longest day of the year. Because I go all night and all day. Also because I get up at four in the morning most days, so the joke works both ways."
    s "Okay, important question."
    menu:
        s "Can I give you a glitter baptism?"

        "\"Baptize me.\"":
            $ gain("solstice", 2)
            "She upends an entire jar over your head. It is a lot of glitter. It will still be in your ears in March."
            s happy "Welcome to the church of SPARKLE. You are SAVED."

        "\"Just a little. On the cheeks.\"":
            $ gain("solstice", 1)
            "She dabs glitter under your eyes with one fingertip, very gently, like painting a tiny face."
            s happy "Perfect. Subtle. Mysterious. You look like a sad disco ghost. I mean that as the highest compliment."

        "\"I'm good, thanks.\"":
            s neutral "Respect! Consent is sexy! Also glitter is forever, so honestly, smart call."

    s happy "See you on the dance floor, new person!"
    hide solstice with dissolve
    "She bounces off to the next lounger. Her top blinks HAPPY HAPPY HAPPY in scrolling letters across her back."
    return


label solstice_pool_2:
    "Solstice is asleep on a lounger in the full afternoon sun. Her LED top is switched off. Her goggles are over her eyes. Her shoulders are going pink."
    "Without the lights and the noise, she looks younger. And very tired."
    menu:
        "Quietly move the umbrella so she's in the shade.":
            $ gain("solstice", 2)
            "You drag the big striped umbrella over, slowly, so it doesn't scrape. The shadow slides over her face."
            "A few minutes later she stirs, pushes up her goggles and looks at the umbrella, then at you."
            show solstice blush with dissolve
            s "Did you... do that? For me?"
            s "Huh. Nobody does stuff for me. I'm usually the one doing stuff."

        "Gently wake her: \"Hey. You're getting burned.\"":
            $ gain("solstice", 1)
            show solstice surprised with dissolve
            s "Wha—oh. OH. Oh no, I'm a lobster. Thank you. Thank you, oh my god."

        "Let her sleep. She clearly needs it.":
            "You leave her be. Half an hour later you hear a shriek from across the deck."
            show solstice surprised with dissolve
            s "OW. Why didn't anyone—ha. It's fine. It's fine! I'll be a shiny red raver. New look."

    show solstice neutral
    "She sits up. She doesn't turn the lights back on."
    s "I'm a nurse. ICU. Nights. I spend all week with people on the worst night of their lives."
    s "And then I come here and dance like it's the best one. Every year. I think if I stop dancing, the other thing catches up."
    s "When the lights are on, everyone loves me. Solstice! Glitter girl! When they're off, I'm just... tired. Really, really tired."

    menu:
        "\"I like you with the lights off too.\"":
            $ gain("solstice", 2)
            s blush "..."
            s "That's... wow. Okay. You can't just say things like that at the pool. That's a ballroom thing to say. At least."

        "\"That sounds exhausting. Do you ever get to rest?\"":
            $ gain("solstice", 1)
            s neutral "Rest is... I'm bad at rest. Rest is where the thoughts are."
            s "But this was nice. Right now. This was rest, kind of."

        "\"Turn them back on! You're so much fun when they're on.\"":
            s neutral "Yeah. Ha. Yeah."
            "She flicks the switch. The top blazes back to life. Her smile comes on with it, a half-second late."

    hide solstice with dissolve
    return


label solstice_night_1:
    scene bg exchange with dissolve
    "The Human Stock Exchange is roaring. Tickers crawl across the walls in red and green: SELF ▲4.2. VIBES ▼1.1. GLITTER ▲99."
    "Mute clowns in bras and fishnets run between the trading desks, pantomiming panic and euphoria. The air is full of confetti."
    show solstice happy with dissolve
    s "THERE you are! Okay, I just bought forty percent of you! Don't let me down! Diversify your feelings!"
    "A clown runs up to you and mimes, frantically, an offer. They're pointing at Solstice. Her ticker is on the wall: SOLSTICE ▲2.0."
    menu:
        "Buy as many shares of Solstice as you can.":
            $ gain("solstice", 2)
            "You buy and buy. The clown mimes a heart attack of joy. On the wall, her ticker rockets: SOLSTICE ▲88.8."
            s surprised "Oh my god. I'm a blue chip. I'm a BLUE CHIP!"
            s happy "Mutual investment! We own each other now! That's basically marriage on this floor!"

        "Short-sell Solstice.":
            $ gain("solstice", 1)
            "The clown gasps silently and hands you a little paper slip marked SHORT. Her ticker dips."
            s surprised "You absolute CAPITALIST!"
            s happy "I respect it. I hate it. I respect it."

        "Don't trade. Just watch the chaos.":
            "The clown stops. They look at you with enormous, sad, painted eyes, and mime: no spectators."
            "Then they gently place a share of somebody's grandmother in your hand and run away."
            s neutral "Ha. They do that. Nobody gets to just watch here."

    "A siren wails. Every clown freezes, then slowly tears their own hair in silent anguish. The tickers flash red: MARKET CRASH. EVERYTHING ▼100."
    show solstice surprised
    menu:
        s "Oh no. Oh no, the crash. Quick, what do we do?"

        "\"Can I grab your hand? We're getting out of here.\"":
            $ gain("solstice", 2)
            s happy "YES. Run!"
            "You run hand in hand through a blizzard of confetti and out into the hallway, and you're both laughing so hard you have to sit down on the carpet."
            s blush "That's the best I've felt in like a month. That was so stupid. Thank you."

        "\"Hold. Never sell. Diamond hands.\"":
            $ gain("solstice", 1)
            s happy "DIAMOND HANDS!"
            "You both hold up your hands, defiant, as the market crumbles around you. A clown salutes you with a single tear."

        "\"Sell everything and buy tea.\"":
            $ gain("solstice", 1)
            s happy "Honestly the most financially sound decision anyone's made in this room."

    hide solstice with dissolve
    return


label solstice_night_2:
    scene bg karaoke with dissolve
    "The confession booth karaoke room is draped in velvet. A neon sign on one wall says CONFESS. On the other, ABSOLVED."
    "The rules, printed on a card: Pick a song. Replace the words with something true. Everybody claps either way."
    show solstice neutral with dissolve
    "Solstice is coming out of the booth. Her LED top is on its dimmest setting. She sees you and goes pink under the glitter."
    s blush "Oh no. Did you hear that?"
    s "I confessed that I don't actually like techno. I like slow songs. Sad, slow country songs about trucks and divorce. I've been lying to the scene for six years."
    s neutral "Okay. Your turn. You have to. That's the rule."

    menu:
        "Confess something real.":
            $ gain("solstice", 2)
            "You go into the booth. You pick a slow song. In place of the words, you sing something you haven't said out loud to anyone."
            "It isn't good singing. It doesn't need to be. When you come out, Solstice is standing very still."
            s blush "...Hey. That was brave. That was, like, the real version."

        "Confess something silly.":
            $ gain("solstice", 1)
            "You sing, with enormous drama, that you have never once understood how crosswords work. Not once. Not even the easy ones."
            s happy "NO. Not even Monday?? The Monday ones are for CHILDREN."

        "Refuse to sing.":
            "The booth plays a very sad trombone sound. Several people boo, lovingly."
            s neutral "Ha. Okay. Okay, that's fair. Not everyone's ready to confess on a Saturday."

    show solstice neutral
    menu:
        s "Hey, so. There's a slow one up next. A real one. Will you... sing it with me?"

        "Sing the slow one with her.":
            $ gain("solstice", 2)
            "The two of you squeeze into the booth. The song is about a truck and a dog and a long road home. You don't know the words. She does."
            "Halfway through, her voice cracks and she laughs and keeps going, and you sing the harmony that doesn't exist."
            s blush "Okay. That's... okay. I'm going to remember that one."

        "\"Only if you take the goggles off.\"":
            $ gain("solstice", 1)
            "She hesitates. Then she pulls them off and hangs them on the mic stand. Her eyes look naked without them."
            s neutral "Fine. Deal. Don't look at me while I sing, I make faces."

        "\"Let's do something faster.\"":
            s neutral "Oh. Sure! Yeah! Something with a drop!"
            "She turns the lights on her top back up. The slow song goes to the next people in line."

    hide solstice with dissolve
    return


label solstice_night_3:
    scene bg ballroom with dissolve
    "The ballroom on Sunday night is pure light. Lasers cut the haze. Projections of slow geometry crawl over seven hundred dancing bodies."
    "And in the middle of the floor, under the disco ball, Solstice is dancing like it's the last song on Earth. Her LED top is blazing every color at once."
    show solstice happy with dissolve
    s "YOU CAME! DANCE WITH ME!"
    "You dance. It's ridiculous and good. And then, mid-song, with a little electronic sigh, every light on her top goes out at once."
    show solstice surprised
    "Battery's dead. She's just a dark shape in the crowd now. She freezes in the middle of the floor like someone pulled her plug too."

    menu:
        "Keep dancing with her, right there in the dark.":
            $ gain("solstice", 2)
            "You don't stop. After a second, she starts again, slower. Nobody's watching her now. She's just dancing."
            s blush "You stayed."

        "Hold up your phone's flashlight like a tiny moon.":
            $ gain("solstice", 1)
            s happy "Ha! My little moon! Okay, okay."
            "She dances in the circle of your phone light like it's a spotlight. It's the smallest stage in the ballroom."

        "\"Let's go find you some batteries!\"":
            s neutral "Yeah. Yeah, good idea. Can't be dark at the end."
            "You hunt for batteries. By the time you find some, the song is over."

    show solstice neutral
    s "Nobody's ever stayed when the lights went out. People like Solstice. Solstice is fun. When she runs out, they go find the next fun thing."
    menu:
        s "Hey. Can I tell you my real name?"

        "\"I'd love that.\"":
            $ gain("solstice", 2)
            s blush "It's Dana. Dana. It's so boring. It's a dentist's name."
            s "Nobody here knows it. Now you do."

        "\"Only if you want to. I like Solstice too.\"":
            $ gain("solstice", 2)
            s blush "I want to. It's Dana."
            s "And you like Solstice too. Huh. Then maybe you'd like both."

        "\"Does it matter?\"":
            s neutral "...Maybe not. Never mind."
            "The music swells. She turns back to the dance floor, and the moment's gone."

    if rapport["solstice"] >= ROMANCE_THRESHOLD:
        s blush "After the ark... come find me on the roof? I want to see a sunrise without being high on anything but, like. Life. Ew. You know what I mean."
    else:
        s happy "Okay! Ark time soon! Go get a good spot, new person!"
    hide solstice with dissolve
    return


label solstice_romance:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 6:01 AM"
    "Solstice is on the roof in a borrowed hoodie, leg warmers still on, her LED top dead and dark underneath. She's sitting on the bench with two cups of tea."
    show solstice blush with dissolve
    s "Hi. I got you tea. It's the cardamom one. I didn't know if you were coming, so I've been drinking both of them in turns."
    "You sit. The sky is going pink and gold over the hills."
    s neutral "I've been to twenty festivals. I've never once watched the sunrise. I'm always inside, dancing, so I don't have to think."
    s "Tomorrow I go back to the ICU. Night shift Tuesday. Somebody's going to have the worst night of their life and I'm going to be there."
    s blush "But I think I'll be a little less tired. Because I'll know there's a sunrise. And I saw it. With you."

    menu:
        "\"Hi, Dana.\"":
            s blush "Oh, that's unfair. That's so unfair. Say it again."
            "You do. She covers her face with her hands."

        "Take her hand.":
            "Her fingers are cold from the morning and covered in glitter. She squeezes back hard."

    s blush "Can I kiss you? Or is that too much? I'm really bad at doing things without lights on. I'm figuring it out."

    menu:
        "\"Yes. Lights off. Just us.\"":
            "She leans in. She tastes like cardamom and smells like sunscreen and the end of a very long weekend."
            "It's a slow kiss. A slow-song kiss. Somewhere a bird sings the harmony that doesn't exist."

        "Kiss her first, gently.":
            s surprised "Oh!"
            s blush "Oh. Okay. Yeah. Yes. Again, please."

    scene bg roof_dawn with slowfade
    "The sun comes up. The longest day of the year was months ago. This feels longer."
    "Below, someone in the parking lot starts playing a slow country song about a truck from their car speakers. Solstice laughs so hard she spills both teas."
    scene black with slowfade
    "{i}Wednesday, 4:12 AM. A text.{/i}"
    s "on break. someone made it through the night. it's sunrise in like an hour. thinking about you. it's dana btw. obviously."
    $ chosen = "solstice"
    $ ending_name = "The Longest Day"
    jump ending_card


label solstice_friend:
    scene bg exterior with slowfade
    show solstice happy with dissolve
    "Solstice tackles you in the parking lot with a full-body hug and a fresh handful of glitter."
    s "You're stuck with me now. Friendship bracelet is legally binding. Next festival, you're on my camp. No excuses!"
    return
