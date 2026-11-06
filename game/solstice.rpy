## solstice.rpy — Solstice, a raver in fur leg warmers and an LED top. Pronouns: she/her.
## Everyone loves her when the lights are on. The route is about the lights going off.

label solstice_pool_1:
    "A woman in rainbow fur leg warmers, holographic shorts and a black crop top studded with little LEDs is working her way down the row of loungers, handing out glitter like it's communion."
    "She has goggles pushed up on her forehead and a sticker of a star under one eye. She reaches you and lights up, literally. Her top flickers through the rainbow."
    show solstice happy with dissolve
    s "HI! Hi hi. You're new. You have new-person energy. It's so cute. Hold out your hand. No, the other one. Perfect."
    "She produces a bracelet of plastic beads from somewhere. It says, in lettered beads, PLUR4LIFE."
    menu:
        "Hold out your wrist and let her put it on.":
            $ gain("solstice", 1)
            s happy "There. Now you're one of us. Welcome to the party! Now stop being so shy!"

        "\"Wait, I want to give you something too.\"":
            $ gain("solstice", 2)
            "You dig in your pockets. All you have is a hotel mint, slightly warm."
            s surprised "For me?"
            s blush "Oh my god. No one ever gifts back. Everyone just takes the beads and runs."
            "She holds the mint up to the light like a jewel, then puts it very carefully into a pocket on her leg warmer."
            s happy "I'm going to keep this forever, as evidence. Or eat it at three in the morning. One of the two."

        "\"Oh, I didn't bring anything to trade.\"":
            s neutral "It's not a trade! It's a gift! Free of charge!"
            "She puts the bracelet on you despite your reluctance, with a firm little pat. She seems like she's had a lot of practice."

    show solstice happy
    s "I'm Solstice. Like the longest day of the year. Because I go all night and all day. Sometimes naturally, sometimes with a little help if you know what I mean ;)"
    s "Okay, important question."
    menu:
        s "Can I give you a light show?"

        "\"Light me up.\"":
            $ gain("solstice", 2)
            s "Ok, stare into my chest."
            "The LEDs of her bra flash in hypnotizing colors, while Solstice shakes her chest. She's moving to the beat and the lights begin to hypnotize you."
            "You get the feeling that Solstice notices you starting to go into a trance and she stops before you completely lose control. She stops abruptly, but with a smile on her face."
            s happy "Welcome to the church of LIGHT. You are SAVED."

        "\"Just a little, I'm pretty light sensitive.\"":
            $ gain("solstice", 1)
            "She presses a button on her glasses, and all of the lights on her costume pulse in unison, to her heart beat."
            s happy "Huh! I didn't expect my heartbeat to be so slow, I must feel comfortable around you."

        "\"I'm good, thanks. I'm supposed to limit my exposure to artificial light, that is if I want to sleep on time.\"":
            s neutral "Respect! Consent is sexy! Gotta get your beauty sleep if you're going to keep partying for the rest of the weekend."
            "She's trying not to act dejected, but you can see her looking around the room for other people to talk to."

    s happy "See you on the dance floor, new person!"
    hide solstice with dissolve
    "She bounces off to the next lounger. Her top blinks HAPPY HAPPY HAPPY to the beat of the music the DJ is playing."
    return


label solstice_pool_2:
    "Solstice is asleep on a lounger right under one of the pool hall's big orange heat lamps. Her LED top is switched off. Her goggles are over her eyes. Her shoulders are going pink."
    "Without the lights and the noise, she looks younger. And very tired."
    menu:
        "Quietly swing the heat lamp away from her.":
            $ gain("solstice", 2)
            "You swivel the heat lamp away, slowly, so it doesn't squeak. The orange glow slides off her face."
            "A few minutes later she stirs, pushes up her goggles and looks at the heat lamp, then at you."
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
    "She sits up. She doesn't turn her costume back on."
    s "I don't like to think about what I do in the default world. It's draining, and grim, and well, y'know."
    s "And then I come here and dance like everything is okay. Every year. I think if I stop dancing, the other thing catches up."
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
            s happy "Mutual investment! We own each other now! That's basically marriage at this party!"

        "Short-sell Solstice.":
            $ gain("solstice", 1)
            "The clown gasps silently and hands you a little paper slip marked SHORT. Her ticker dips."
            s surprised "You CAPITALIST PIG!"
            s happy "I respect it. I hate it, but I respect it. Maybe I like it a little when people take advantage of me."

        "Don't trade. Just watch the chaos.":
            "The clown stops. They look at you with enormous, sad, painted eyes, and mime a slow jackoff motion. No spectators, right."
            "Then they gently place a share of yourself in your hand and run away."
            s neutral "Ha. They do that. Nobody gets to just watch. Unless you're in the cuck chair."

    "A siren wails. Every clown freezes, then slowly they tear at their wigs in silent anguish. The tickers flash red: MARKET CRASH. EVERYTHING ▼100."
    show solstice surprised
    menu:
        s "Oh no. Oh no, the crash. Quick, what do we do?"

        "\"Can I grab your hand? We're getting out of here.\"":
            $ gain("solstice", 2)
            s happy "YES. Run!"
            "You run hand in hand through a blizzard of stock ticker confetti and out into the hallway, and you're both laughing so hard you have to sit down on the carpet."
            s blush "That's the best I've felt in like a month. That was so stupid. Thank you."

        "\"Hodl! Never sell. Diamond hands.\"":
            $ gain("solstice", 1)
            s happy "DIAMOND HANDS! APE STRONG! THANK YOU FOR THE DIP!"
            "You both hold up your hands, defiant, as the market crumbles around you. A clown salutes you with a single tear."

        "\"Sell everything and give your earnings to the next person who walks in.\"":
            $ gain("solstice", 1)
            s happy "Sharing is caring! Well I guess here you shared the joy of buying into capitalism. A bit of a downer I guess, but what else can you do but laugh."

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
            "You sing, with enormous drama, that you're bad at puzzles. You can't even solve a single one without help."
            s happy "NO. Not even the ones that Chuk makes?? Those ones are for CHILDREN."

        "Refuse to sing.":
            "The booth plays a very sad trombone sound. Several people boo, lovingly."
            s neutral "Ha. Okay. Okay, that's fair. Not everyone's ready to confess on a Saturday. Maybe later you can confess something ... just to me."

    hide solstice with dissolve
    return


label solstice_night_3:
    scene bg ballroom with dissolve
    "The ballroom on Sunday night is pure light. Lasers cut the haze. Geometric projections crawl over seven hundred dancing bodies."
    "And in the middle of the floor, under the disco ball, Solstice is dancing like it's the last song on Earth. Her LED top is blazing every color at once."
    show solstice happy with dissolve
    s "YOU CAME! DANCE WITH ME!"
    "You can barely hear her over the music, but you dance. It's ridiculous and good. And then, mid-song, with a little electronic sigh, every light on her top goes out at once."
    show solstice surprised
    "Battery's dead. She's just a dark shape in the crowd now. She freezes in the middle of the floor like someone pulled her plug too."

    menu:
        "Keep dancing with her, right there in the dark.":
            $ gain("solstice", 2)
            "You don't stop. After a second, she starts again, slower. Nobody's watching her now. She's just dancing."
            s blush "You stayed."

        "Hold up your phone's flashlight like a tiny moon.":
            $ gain("solstice", 1)
            s happy "Ha! My little moon! Usually I'm the one shining lights on other people. Okay, okay, I can get used to this."
            "She dances in the circle of your phone light like it's a spotlight. It's the smallest stage in the ballroom."

        "\"Let's go find you some batteries!\"":
            s neutral "Yeah. Yeah, good idea. Can't be dark at the end."
            "You hunt for batteries. By the time you find some, the DJ set is over."

    show solstice neutral
    s "Nobody's ever stayed when the lights went out. People like Solstice. Solstice is fun. When she runs out, they go find the next fun thing."
    menu:
        s "Hey. Can I tell you my real name?"

        "\"I'd love that.\"":
            pass

    s "But first I think I need a little bump of courage, do you think you can help me out?"
    menu:
        "\"Of course, anything for my friends\"":
            $ gain("solstice", 2)
            s blush "YAY! We're friends, it's official! Ok, but maybe not right now. I'll let you know when."

        "\"Uh sure, but I don't have anything on me right now\"":
            $ gain("solstice", 2)
            s blush "Don't worry, maybe we can meet up later, and I'll reveal more than my name."

        "\"Uh, I'm not sure what you're talking about. You're not a cop right?\"":
            s neutral "...Maybe not. Never mind. I'll see you around."
            "The music swells. She turns back to the dance floor, and the moment's gone."

    if rapport["solstice"] >= ROMANCE_THRESHOLD:
        s blush "After the big event... come find me on the roof? I want to see a sunrise, with you there maybe it'll glow extra bright."
    else:
        s happy "Okay! Big event time soon! Go get a good spot, new person!"
    hide solstice with dissolve
    return


label solstice_romance:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 5:48 AM"
    "The ballroom lets out around five. Seven hundred people spill into the hallways sticky with confetti, hugging strangers, trading gifts, crying a little."
    "You find Solstice exactly where she said she'd be: on the roof, in a borrowed hoodie three sizes too big, leg warmers still on, LED top dead and dark underneath."
    "She's sitting on the bench with two cups of tea, and she's not dancing. You're not sure you've ever seen her sit still."
    show solstice blush with dissolve
    s "Hi. I got you tea. It's the cardamom one. I didn't know if you were coming, so I've been drinking both of them in turns, which means you get half."
    "You sit. The bench is cold. She shifts over until her shoulder is against yours, and the hoodie smells like the ballroom: fog machine, sunscreen, glitter, if glitter has a smell."

    menu:
        s "Okay. Real question. Did you have fun? Like, actually?"

        "\"The most fun I've had in years. Mostly because of you.\"":
            s blush "Stop. Stop it. You can't just... okay, keep going, actually."
            "You pull out the small bag you brought, just in case the party wasn't over."
        "\"I brought a little something for us, that is if you want to keep partying for a bit longer\"":
            "You pull out a small bag."
            s happy "Ha! Fair. I'm not going to sleep anyway. Let me see that."

    "She takes the bag, and then her expression turns serious. Before you know it, she's slipped a handcuff around your right hand, and the other end to the railing."
    "She flips the lights on her bra back on, and gets them real close to your eyes. You kind of like it. Being handcuffed to the railing, no longer in control. A cop trying to entrap you. You feel a guilty rush, but it's a rush nonetheless."

    show solstice neutral
    s "Hey. Before we do this can I tell you something? My real name. Nobody here knows it."
    s blush "It's Dana. Dana. Now we both have some dirt on each other, you can blow my cover anytime you want."
    "The sun is just coming over the mountains now. It turns her glitter gold, every last fleck of it, so she looks like she's been dipped in it."

    menu:
        "\"I'm not going to blow your cover, not now not ever.\"":
            s blush "I love it when you're obedient. Well if you're not going to blow my cover I guess you'll just have to blow something else."
            "You let yourself become hypnotized, and before you know it it's morning."
        "Hand her the bag again.":
            s "You're naughty! Tempting me while I'm on the job. Ok, maybe just this once, just because we're finally alone."

    s blush "Can I kiss you? Or is that too much? I know I'm in control here, but consent is still sexy."

    menu:
        "\"Yes. Lights off. Just us.\"":
            "She leans in. She tastes like cardamom and smells like sunscreen and the end of a very long weekend."
            "It's a slow kiss. A slow-song kiss. You feel guilty but a little smug that you've been able to corrupt a fed."
        "\"You fucking pig. I'm sick of getting fucked by the state.\"":
            s surprised "Oh!"
            s blush "I love it when you talk to me like that. Again, please."
            "So you do it again, slower. She's smiling so hard it barely feels like an insult."

    "The night blurs, fluids and powders are shared, clothes are removed. The handcuffs stay on."
    show solstice happy
    s "Okay. The sun's up. I've officially seen one. Thanks for helping me really party for once."

    scene bg roof_dawn with slowfade
    "The longest day of the year was months ago. This one feels longer, in the best way."
    "Below, someone in the parking lot starts playing Fight The Power on a shitty car stereo. Solstice laughs so hard she spills both teas."
    "She uncuffs you and pulls you up off the bench and you embrace, swaying slowly, with no lights at all, until the song ends and the car drives away."
    scene black with slowfade
    "{i}Wednesday, 4:12 AM. A text.{/i}"
    s "I quit the force, and now I'm living my raver lifestyle, but not as a cover."
    s "I stayed up all night at decompression. It's sunrise in like an hour. I'm going to go watch it from the top of an art car, not worrying about what drugs the people below are on. first one I've watched on purpose that wasn't with you"
    s "thinking about you. Next year can I be your +1? No fake names, but I'm still happy to handcuff you if you'd like ;)"
    $ chosen = "solstice"
    $ ending_name = "The Longest Day"
    jump ending_card


label solstice_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show solstice happy with dissolve
    "Solstice tackles you in the parking lot with a full-body hug and a fresh handful of glitter. Some of it goes in your mouth. That's the price."
    s "THERE you are! I was going to leave a note on your windshield made of glitter but now I don't have to."
    s neutral "Real talk for one second. This weekend was the first one in a long time I didn't feel like I was running on fumes."
    s "Some of that's the party. Some of it's you. You're good at the quiet parts. I'm bad at the quiet parts."
    "She ties a new bracelet onto your wrist next to the first one. This one says, in lettered beads, {i}call me{/i}."
    s happy "You're my person on the inside now. Friendship bracelet is legally binding."
    s "And if you ever want to watch a sunrise, I hear they're good. I've seen one. I'm basically an expert."
    return


