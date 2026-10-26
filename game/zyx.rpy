## zyx.rpy — Zyx, Ambassador of the Outer Drift. Pronouns: they/them.
## Never breaks character. Whether there's a person under the suit is not the point.

label zyx_pool_1:
    "Under a giant striped umbrella sits a silver alien with three eyes, two antennae and a sash that reads AMBASSADOR. They are wearing at least an inch of sunscreen and taking notes on a clipboard."
    show zyx neutral with dissolve
    z "Greetings, Earthling. This one is Zyx, Ambassador of the Outer Drift. You may approach. Slowly. The sun is very aggressive on this planet."
    z "Please explain the following ritual."
    "They point at the pool, where a dozen adults have their eyes closed, splashing around and screaming the same two words at each other."
    z "Why do humans close their eyes and shout the name of a dead Venetian explorer?"

    menu:
        "Explain Marco Polo as seriously as possible.":
            $ gain("zyx", 2)
            "You explain the rules in full. The seeker. The call. The response. The fish-out-of-water rule, which you're not sure is real."
            z happy "Fascinating. A game of trust and echolocation. Your species is part bat. We suspected."
            "They write {i}PART BAT{/i} in large letters on the clipboard and underline it twice."

        "\"Just play it with me. You'll get it.\"":
            $ gain("zyx", 1)
            "You drag them into the shallow end. Zyx is the seeker. They close all three eyes."
            z surprised "MARCO."
            "Everyone shouts POLO. Zyx's antennae go limp with delight."
            z happy "Again. AGAIN."

        "\"Are you... actually an alien?\"":
            z neutral "Are you actually a human?"
            z "Do not answer. It would ruin it. For both of us."

    show zyx neutral
    "Zyx explains that they are here on a research mission: to determine whether Earth is ready for contact."
    z "Our current findings: Earth is not ready. Earth is very, very fun. These two findings are in tension. The report is going poorly."

    menu:
        z "Question for the report. Why do humans gather like this? In secret? Wearing other faces?"

        "\"Because sometimes the other face is the real one.\"":
            $ gain("zyx", 2)
            "All three of Zyx's eyes look at you at once."
            z blush "...That is the most accurate thing anyone has said for the report."
            z "This one is writing it down. With your name. No, without your name. Earth rules. No names in the report."

        "\"To have fun. That's it. That's all.\"":
            $ gain("zyx", 1)
            z happy "Simple. Elegant. This one respects it. Writing: FUN."

        "\"I'm not sure. I came here to find out.\"":
            $ gain("zyx", 1)
            z neutral "A fellow researcher. We will compare notes before the end."

    hide zyx with dissolve
    return


label zyx_pool_2:
    "Zyx is walking the pool deck with a mesh bag labeled EARTH ARTIFACTS. It contains nine mismatched flip-flops, a pair of sunglasses, a single swim fin, and a paperback novel swollen to twice its size from water."
    show zyx happy with dissolve
    z "Earthling! You are here! Good. The museum of the Outer Drift requires donations. Every visitor gives one artifact. It is the custom of our people. Just now. We invented it just now."

    menu:
        z "What do you donate to the Outer Drift?"

        "Find a perfect smooth pebble by the planters, and explain that it's a 'nice rock.'":
            $ gain("zyx", 2)
            $ gave_rock = True
            z surprised "A nice rock."
            "They hold it up to the sun with all three eyes."
            z happy "On the Outer Drift, there are no nice rocks. Every rock is jagged and furious. This changes everything. This is the centerpiece."

        "Your hotel key card.":
            $ gain("zyx", 1)
            z neutral "A key to a door that already opens. Because everyone who enters is already checked in."
            z happy "Profound. It goes in the philosophy wing."

        "\"Nothing. Sorry. I need all my stuff.\"":
            z neutral "Understandable. Humans are very attached to stuff. We have noted it."

    show zyx neutral
    "Zyx sits down on a lounger next to you and folds their silver hands."
    z "The Outer Drift is very quiet. Thirty-one of us, spread across a nebula. We communicate by changing color, very slowly. A conversation can take a year."
    z "No one has hugged on the Outer Drift since the third moon. We are not built for it. Too many antennae."
    z "But this one has observed many hugs here. Data suggests they are... good."

    menu:
        z "Earthling. For the report. Please demonstrate a hug. Consent is requested, in the Earth style."

        "\"Yes. Come here.\"":
            $ gain("zyx", 2)
            $ hugged_zyx = True
            "You hug. Zyx is very stiff at first, like a coat hanger. Then, slowly, their arms come up around you. Their antennae droop down over your shoulder."
            z blush "Oh."
            z "Data confirmed. Data... very confirmed."

        "Offer a high five instead.":
            $ gain("zyx", 1)
            "Zyx studies your palm. Then, very carefully, presses their three-fingered glove against it."
            z happy "A hug for hands. Efficient. We approve."

        "\"Maybe later.\"":
            z neutral "Noted. Later. This one will hold you to the Earth word 'later.'"

    hide zyx with dissolve
    return


label zyx_night_1:
    scene bg fortune with dissolve
    "THE ORACLE OF PING PONG, says the sign. A boxy robot with a glass dome on its head takes ping pong balls from a lottery machine and prints fortunes on them with a tiny buzzing arm."
    "People in capes and headsets queue in the purple light. At the front, Zyx is feeding the machine with great seriousness."
    show zyx neutral at slightright with dissolve
    z "Earthling! You are just in time. This machine is the most advanced intelligence on your planet. We have been consulting it for an hour."
    "The robot whirs. It spits out a ball. Zyx catches it and reads it aloud."
    robot "YOU ARE NOT THE ONLY ONE."
    show zyx surprised at slightright
    z "Not the only one. Not the only one... what? This is troubling. Interpret it, please."

    menu:
        "\"It means you're not alone. Here, at least.\"":
            $ gain("zyx", 2)
            z blush "Not alone."
            "They turn the ball over and over in their gloved fingers."
            z "On the Outer Drift, the nearest Zyx is four light-years away. This one had forgotten that 'not alone' was a thing a person could be."

        "\"It means there's another alien at this party.\"":
            $ gain("zyx", 1)
            z surprised "!!!"
            "Zyx spins around, scanning the crowd with all three eyes. A man in a cape waves at them. Zyx waves back, suspicious."

        "\"It's a ping pong ball. It doesn't mean anything.\"":
            z neutral "Everything means something to the Oracle. But we will log your skepticism."

    show zyx neutral at slightright
    z "Now you. Your turn. This one will read yours."
    "The robot whirs and prints a ball for you. Zyx reads it."
    robot "STAY UNTIL SUNRISE."
    menu:
        z "Will you follow the Oracle's guidance?"

        "\"Only if you stay too.\"":
            $ gain("zyx", 2)
            z blush "Ah."
            z "Then it is decided. The Oracle has spoken. We both stay. For science."

        "\"Probably. I'm not great at leaving things.\"":
            $ gain("zyx", 1)
            z happy "Good. Neither is this one. This one came for a weekend nine years ago."

        "\"I don't really believe in fortunes.\"":
            z neutral "The Oracle does not need your belief. It is a robot. It has a printer."

    hide zyx with dissolve
    return


label zyx_night_2:
    scene bg clinic with dissolve
    "The Clinic of Unnecessary Procedures smells like rubbing alcohol and bubblegum. An eye chart on the wall is made entirely of astrological symbols."
    "Two nurses in vintage uniforms are wheeling Zyx in on a gurney. Zyx is protesting in a language that sounds a lot like the noise a modem makes."
    show zyx surprised with dissolve
    nurse "Are you the alien's next of kin?"

    menu:
        "\"Yes. I'm their emergency contact.\"":
            $ gain("zyx", 2)
            $ zyx_emergency_contact = True
            z blush "You are?"
            z "...You are. Yes. Correct. This one's emergency contact. Please inform them of everything."

        "\"I'm a friend.\"":
            $ gain("zyx", 1)
            nurse "A friend may stay. Friends are encouraged. It says so on the chart."

        "\"Never seen them before in my life.\"":
            z surprised "Betrayal! This one will be noting this in the report! In red!"
            "The nurses let you stay anyway. They need a witness."

    show zyx neutral
    nurse "May I listen to your heart, Ambassador? The stethoscope is cold. I'm asking first."
    z "...Permission granted."
    "The nurse listens for a long, long time. She frowns. She moves the stethoscope. She frowns harder."
    nurse "Heart: one. Normal size. Slightly lonely."
    z surprised "Slightly lonely!"
    nurse "It happens. Especially to travelers. Here's the prescription."
    "She writes on a pad and tears off the page with great ceremony: ONE (1) DANCE. TO BE TAKEN BEFORE SUNRISE. REPEAT AS NEEDED."
    show zyx neutral
    menu:
        z "The prescription requires a partner. Are you... available? For medical purposes?"

        "\"Doctor's orders. I'm available.\"":
            $ gain("zyx", 2)
            z blush "Medical purposes. Yes. Strictly medical."
            "Zyx dances like an alien who's watched a lot of dancing through a telescope: very precise, very wrong. You love it."

        "\"I'll have to check my schedule.\"":
            $ gain("zyx", 1)
            z happy "A tease. Your species is called 'a tease.' We have the data."

        "\"You should ask someone else. I'm a terrible dancer.\"":
            z neutral "Understood. This one will dance alone. Doctor's orders."
            "They do, in the hallway, very precisely. It's a little sad."

    hide zyx with dissolve
    return


label zyx_night_3:
    scene bg planetarium with dissolve
    "Someone has turned the ice machine alcove into a planetarium. Stars cover every surface. Constellations are drawn between them in faint blue lines. The ice machine glows in the middle like a small, cold sun."
    show zyx neutral with dissolve
    "Zyx is sitting on the floor in front of it, antennae dimmed, looking up."
    z "Ah. Earthling. Sit. This is this one's favorite room. The ice machine dreams of the cold between stars. We understand each other."
    menu:
        z "That one, there. The faint one, near the Swan. That is home. Do you see it?"

        "\"I can't find it. Show me?\"":
            $ gain("zyx", 2)
            z neutral "May this one take your hand to point?"
            "You say yes. Their gloved fingers wrap around yours and guide your arm up to a dim, blue star."
            z blush "There. Home. Now two beings on this planet know where it is."

        "\"I see it. It's beautiful.\"":
            $ gain("zyx", 1)
            z happy "It is not, actually. It is very small and quite gray. But thank you."

        "\"Is home even real?\"":
            z neutral "Is anything? Is the ice machine? It makes ice. That seems real enough."

    show zyx neutral
    z "After the ark, the mission ends. The Ambassadors carry the ark into the ballroom at 11:11. Then the report is complete. And then..."
    z "Then this one is just Zyx. With no mission. On a strange planet. That is the part this one is afraid of."
    menu:
        z "Most Earthlings ask what is under the suit. Would you like to know?"

        "\"Only if you want to tell me. I like Zyx.\"":
            $ gain("zyx", 2)
            "Zyx's antennae light up, very slowly, pink."
            z blush "You like Zyx."
            z "Then Zyx is what you get. Zyx is what is under the suit. All the way down."

        "\"No. Keep the mystery. It's yours.\"":
            $ gain("zyx", 1)
            z happy "A respecter of mysteries. Rare. Noted."

        "\"Yes! Who are you, really?\"":
            z neutral "This one is Zyx. That is the only answer this one has tonight."
            "The ice machine hums. It's a cold sound."

    if rapport["zyx"] >= ROMANCE_THRESHOLD:
        z blush "After the ark. When the mission is complete. Come to the roof. There is one more piece of research this one wishes to do. With you. Only with you."
    else:
        z happy "Watch for us at 11:11. We will be the ones carrying the gold box. Do not panic."
    hide zyx with dissolve
    return


label zyx_romance:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 5:55 AM"
    "After the ark, the Ambassadors of the Outer Drift vanish. One moment they're on stage in their silver suits, the next there's only the duck and the confetti."
    "You look for Zyx in the ballroom, in the hallways, by the ice machine. You find them on the roof, as the sky is going pink."
    "They're sitting on the bench with their sash folded in their lap, antennae glowing softly against the dawn."
    show zyx neutral with dissolve
    z "Earthling. You found this one. This one was hoping you would. This one did not leave a map. That was a test."
    z happy "You passed. Obviously. Sit."
    if gave_rock:
        "They're holding the nice rock from the pool. They turn it over and over in their gloved fingers, the way you'd worry a lucky coin."
    z neutral "The ark has landed. The duck has been revealed. The war over the nature of water has ended in a hug. The report is filed."
    z "The mission is complete."

    menu:
        z "Do you want to hear the conclusion? This one wrote it during the ark. While crying. Which was not in the mission plan."

        "\"Read it to me.\"":
            z neutral "Ahem."
        "\"Only if it says nice things about me.\"":
            z happy "It says extremely specific things about you. You will be studied for generations."

    z neutral "{i}Earth is not ready for contact. Earth is loud, and confusing, and keeps its feelings in rooms labeled LOST & FOUND.{/i}"
    z "{i}Earth closes its eyes and shouts the names of dead explorers in swimming pools. Earth puts glitter on strangers. Earth gives its ice machines a planetarium.{/i}"
    z "{i}But one Earthling is ready. Recommend further study. Recommend this one stays.{/i}"
    show zyx blush
    z "It was approved. By this one. This one is in charge of approvals."

    menu:
        "\"So you're staying?\"":
            z blush "For a while. On Earth, there is a thing called 'a while.' It is very elastic. We intend to stretch it."
        "Sit down next to them and take their gloved hand.":
            "Three fingers fold around yours. Their antennae go from pink to a deep, warm red."

    show zyx neutral
    z "Can this one confess something? For the report. The unofficial report."
    z "On the Outer Drift, we communicate by changing color. Slowly. A conversation can take a year. There are thirty-one of us and we are very, very far apart."
    if hugged_zyx:
        z "When you hugged this one by the pool, this one's antennae went a color that does not have a name at home. This one has been trying to name it since Saturday."
    if zyx_emergency_contact:
        z "And in the clinic, when you said you were this one's emergency contact. Nobody has ever been this one's anything."
    z blush "This one would like to keep finding new colors. With you. If that is permitted under Earth law."

    menu:
        "\"It's permitted. It's encouraged.\"":
            z happy "Excellent. This one will update the legal section of the report."
        "\"What's the color now?\"":
            "Zyx's antennae are glowing a soft, warm gold, the exact color of the sun coming over the hills."
            z blush "This one is calling it... Monday."

    z blush "There is one final experiment. On the Outer Drift, when two beings wish to be close, they touch foreheads. Third eye to third eye."
    z "You have only two eyes. This is a known limitation. We will adapt."
    menu:
        "Lean in and touch foreheads.":
            "Their forehead is cool and smooth and smells faintly of sunscreen. The third eye closes."
            "For a long moment you just breathe like that, foreheads together, while the birds start up in the eucalyptus."

    z blush "And now, for comparison. The Earth version. Consent is requested."

    menu:
        "\"Granted. For science.\"":
            "You kiss the Ambassador of the Outer Drift on the roof of the Hotel Mar Sol at sunrise."
            "Their antennae spark. Actually spark. You're almost sure. It might have been the sun."
            z happy "Data... very, very confirmed. Further study required. Extensive further study."
            z "This one will need to repeat the experiment. For reproducibility. Science is very strict about this."

    scene bg roof_dawn with slowfade
    "The sun clears the hills. Down below, cars are starting in the parking lot. Neither of you moves."
    "At some point Zyx takes off one glove and holds your hand properly. Their hand is warm. It has five fingers. You don't say anything about it, and they don't either."
    scene black with slowfade
    "{i}Two weeks later, a postcard arrives. The picture on the front is a gray, ordinary star.{/i}"
    "{i}Return address: THE OUTER DRIFT (it's near Oakland).{/i}"
    z "Earthling. Research continues. Thursday? This one has found a restaurant where you cook your own food on a hot rock. Gerald recommended it."
    if gave_rock:
        z "Bring the nice rock. This one wants to introduce it to the hot rock. It is important that rocks have friends."
    else:
        z "This one has found you a nice rock. It is waiting on this one's windowsill. It has been told about you."
    z "— Z. (The report now has a section about you. It is forty pages long and still in progress.)"
    $ chosen = "zyx"
    $ ending_name = "First Contact"
    jump ending_card


label zyx_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show zyx happy with dissolve
    "On Monday morning, a silver figure is standing in the hotel parking lot, waving with all three fingers at every car as it pulls out."
    z "Earthling! You are leaving. This one has prepared a farewell ritual. It is called 'a wave.' This one has been practicing."
    z neutral "The report is filed. Earth is not ready for contact. But Earth has friends in it. This one checked. You are one of them."
    z "On the Outer Drift, friendship is shown by changing to the same color as someone. This one cannot do that. This one is stuck being silver."
    "Zyx reaches into the bag of EARTH ARTIFACTS and hands you a single lost flip-flop, very solemnly."
    z happy "This is the highest honor of our people. Do not lose it. We already lost the other one."
    z "Goodbye, Earthling! You are in the report! Section nine: Friends. You are the whole of section nine!"
    return


