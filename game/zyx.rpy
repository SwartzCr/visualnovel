## zyx.rpy — Zyx, Ambassador of the Outer Drift. Pronouns: they/them.
## Never breaks character. It's their first party ever, and without trying they fit in better
## than you, or than the people who've been coming for a decade, and through their eyes you get
## to see the party new again. They flirt like it's a research protocol. The romance ends
## aboard their ship, with the probe.

label zyx_pool_1:
    "Under a giant striped beach umbrella, set up indoors for reasons nobody has asked about, sits a silver alien with three eyes, two antennae and a sash that reads AMBASSADOR. They are wearing at least an inch of sunscreen anyway, and taking notes on a clipboard."
    show zyx neutral with dissolve
    z "Greetings, Earthling. This one is Zyx, Ambassador of the Outer Drift. You may approach. Slowly. The sun is very aggressive on this planet. Even through glass."
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

    "Ten minutes later, the Marco Polo players vote Zyx honorary seeker for life. Zyx has played once. You have been trying to get into that game since noon."
    "A woman who has been coming to this party for eleven years swims over to ask Zyx how they got in with the pool crowd so fast. Zyx tells her to {i}simply arrive from space.{/i} She nods and writes it down."

    show zyx neutral
    z "Observe. Seven hundred humans. None of them were made to come here. They each decided, separately, to spend a weekend being kind to strangers in costumes."
    z "On the Outer Drift, an agreement like that would take a treaty. Here it took a group chat."
    "You look back at the pool: the sunscreen, the inflatable flamingo, the grown adults shrieking POLO. An hour ago it was just a pool. It's a little hard to see it that way now."
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

    z neutral "One more observation. Unrelated to the mission."
    z blush "Your face is very symmetrical. This one checked twice. Three times, actually. This one has three eyes."
    z "Also, this one's antennae have been pointing at you since you sat down. This is not voluntary. It will be investigated."
    hide zyx with dissolve
    return


label zyx_pool_2:
    "There's a queue at the far end of the pool. Someone has made a sign out of a pizza box: THE MUSEUM OF THE OUTER DRIFT. FREE. NO PHOTOS. GIFT SHOP COMING SOON."
    "At the front, Zyx is curating a beach towel covered in EARTH ARTIFACTS: nine mismatched flip-flops, a pair of sunglasses, a single swim fin, and a paperback novel swollen to twice its size from water."
    "Two people from the art crew are taking notes on how Zyx did it. Zyx does not know it's an art piece. Zyx thinks it's a museum."
    show zyx happy with dissolve
    z "Earthling! You are here. You may skip the line. You are this one's favorite visitor. Do not tell the other visitors."
    z "Every visitor gives one artifact. It is the custom of our people. Since this morning. We invented it this morning, and now it is the custom of yours too, apparently."

    menu:
        z "What do you donate to the Outer Drift?"

        "Find a perfect smooth pebble by the planters, and explain that it's a 'nice rock.'":
            $ gain("zyx", 2)
            $ gave_rock = True
            z surprised "A nice rock."
            "They hold it up to the light from the atrium roof with all three eyes."
            z happy "On the Outer Drift, there are no nice rocks. Every rock is jagged and furious. This changes everything. This is the centerpiece."

        "Your hotel key card.":
            $ gain("zyx", 1)
            z neutral "A key to a door that already opens. Because everyone who enters is already checked in."
            z happy "Profound. It goes in the philosophy wing."

        "\"Nothing. Sorry. I need all my stuff.\"":
            z neutral "Understandable. Humans are very attached to stuff. We have noted it."

    show zyx neutral
    "You look at the towel of artifacts again. A child-size flip-flop. Sunglasses with one lens. A paperback someone read until it fell in the pool."
    z "Every object here is proof that someone had a good time and forgot about their belongings. On the Outer Drift, nobody has ever had that good a time."
    "For a second you see it the way Zyx does: not lost property, but a record of everyone who was too happy to keep track of their stuff."
    "Zyx leaves the museum in the care of a volunteer who has already, unprompted, made themself a little docent badge. Zyx sits down on a lounger next to you, close, and folds their silver hands."
    z "The Outer Drift is very quiet. Thirty-one of us, spread across a nebula. We communicate by changing color, very slowly. A conversation can take a year."
    z "No one has hugged on the Outer Drift since the third moon. We are not built for it. Too many antennae."
    z "But this one has observed many hugs here. Data suggests they are... good. This one would like a larger sample size. Of you, specifically."

    menu:
        z "Earthling. For the report. Please demonstrate a hug. Consent is requested, in the Earth style."

        "\"Yes. Come here.\"":
            $ gain("zyx", 2)
            $ hugged_zyx = True
            "You hug. Zyx is very stiff at first, like a coat hanger. Then, slowly, their arms come up around you. Their antennae droop down over your shoulder."
            z blush "Oh."
            z "Data confirmed. Data... very confirmed. This one may need to repeat the measurement. Several times. Science."

        "Offer a high five instead.":
            $ gain("zyx", 1)
            "Zyx studies your palm. Then, very carefully, presses their three-fingered glove against it, and leaves it there a little longer than a high five lasts."
            z happy "A hug for hands. Efficient. We approve. We would approve more of the full version."

        "\"Maybe later.\"":
            z neutral "Noted. Later. This one will hold you to the Earth word 'later.'"

    hide zyx with dissolve
    return


label zyx_night_1:
    scene bg fortune with dissolve
    "THE ORACLE OF PING PONG, says the sign. A boxy robot with a glass dome on its head takes ping pong balls from a lottery machine and prints fortunes on them with a tiny buzzing arm."
    "People in capes and headsets queue in the purple light. Most of them aren't queuing for the robot. They're queuing for Zyx, who has started interpreting everyone's fortunes, and is apparently better at it than the robot."
    show zyx neutral at slightright with dissolve
    z "Earthling! You are just in time. This machine is the most advanced intelligence on your planet. This one is its assistant now. Nobody asked. It simply happened."
    "A man who has run this room for six years is standing off to the side, holding a ping pong ball, looking quietly replaced."
    "The robot whirs. It spits out a ball. Zyx catches it and reads it aloud."
    robot "YOU ARE NOT THE ONLY ONE."
    show zyx surprised at slightright
    z "Not the only one. Not the only one... what? This is troubling. Interpret it, please. This one only interprets other people's."

    menu:
        "\"It means you're not alone. Here, at least.\"":
            $ gain("zyx", 2)
            z blush "Not alone."
            "They turn the ball over and over in their gloved fingers."
            z "On the Outer Drift, the nearest Zyx is four light-years away. This one had forgotten that 'not alone' was a thing a person could be."

        "\"It means there's another alien at this party.\"":
            $ gain("zyx", 1)
            z surprised "!!!"
            "Zyx spins around, scanning the crowd with all three eyes. A man in a cape waves at them. Zyx waves back, suspicious. The man looks thrilled to have been noticed."

        "\"It's a ping pong ball. It doesn't mean anything.\"":
            z neutral "Everything means something to the Oracle. But we will log your skepticism."

    show zyx neutral at slightright
    z "Do you understand what your species has done here? Someone built a robot whose only purpose is to tell strangers their fortunes. Then other strangers stood in line for an hour to hear them."
    z "Nobody is paid. Nobody wins. This one has been crying behind the dome, a little."
    "You look at the queue, at the capes and the headsets and the people reading each other's ping pong balls out loud. You'd walked past this room twice tonight without going in."
    z "Now you. Your turn. This one will read yours personally."
    "The robot whirs and prints a ball for you. Zyx reads it, and their antennae go straight up."
    robot "SOMEONE WILL TAKE YOU HOME."
    z blush "Home. Interesting. Home is four light-years away. That is a long commute."
    z "This one is willing to drive."
    menu:
        z "Will you follow the Oracle's guidance?"

        "\"Only if it's you.\"":
            $ gain("zyx", 2)
            z blush "Ah."
            z "Then it is decided. The Oracle has spoken. This one is taking you home. Eventually. For science."

        "\"Depends. Is your place nice?\"":
            $ gain("zyx", 1)
            z happy "It has a view of every star. And the lighting is very flattering. You would look excellent in it."

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
            z "...You are. Yes. Correct. This one's emergency contact. Please inform them of everything. Especially the intimate things."

        "\"I'm a friend.\"":
            $ gain("zyx", 1)
            nurse "A friend may stay. Friends are encouraged. It says so on the chart."
            z neutral "For now. A friend. For now."

        "\"Never seen them before in my life.\"":
            z surprised "Betrayal! This one will be noting this in the report! In red!"
            "The nurses let you stay anyway. They need a witness."

    show zyx neutral
    "While the nurses prepare, Zyx examines the clinic's instruments with professional interest: a tongue depressor, a reflex hammer, a rubber glove."
    z "Primitive. Charming. Ours are... more thorough. You would find them very interesting. One day this one may show you."
    nurse "May I listen to your heart, Ambassador? The stethoscope is cold. I'm asking first."
    z "...Permission granted."
    "The nurse listens for a long, long time. She frowns. She moves the stethoscope. She frowns harder."
    nurse "Heart: one. Normal size. Slightly lonely. And it's racing."
    z blush "The cause of the racing is standing right there. In the corner. Being symmetrical."
    nurse "It happens. Especially to travelers. Here's the prescription."
    "She writes on a pad and tears off the page with great ceremony: ONE (1) DANCE. TO BE TAKEN BEFORE SUNRISE. REPEAT AS NEEDED."
    show zyx neutral
    menu:
        z "The prescription requires a partner. Are you... available? For medical purposes? And other purposes?"

        "\"Doctor's orders. I'm available.\"":
            $ gain("zyx", 2)
            z blush "Medical purposes. Yes. Strictly medical. Mostly."
            "Zyx dances like an alien who's watched a lot of dancing through a telescope: very precise, very wrong. You love it."
            "So, it turns out, does everyone else. By the end of the song, thirty people in the hallway are copying it. Somebody upstairs is already calling it {i}the Zyx{/i}. You are the only one still doing it wrong."

        "\"I'll have to check my schedule.\"":
            $ gain("zyx", 1)
            z happy "A tease. Your species is called 'a tease.' We have the data. We find it very compelling."

        "\"You should ask someone else. I'm a terrible dancer.\"":
            z neutral "Understood. This one will dance alone. Doctor's orders."
            "They do, in the hallway, very precisely. Within a minute they're not alone at all. Within five, there's a line dance. Zyx leads it with a slightly puzzled expression."

    "Afterward, walking the hall with Zyx is slow, because Zyx stops at everything. The carpet. A painted sign that says {i}HYDRATE OR DIEDRATE{/i}. A man asleep in a bathtub full of balloons, which Zyx photographs with their eyes only, as per the rules."
    z "Did you see? Did you see that one? There is a door that has been painted to look like a different door."
    "You had stopped noticing the hallway hours ago. Zyx hasn't stopped once. By the elevators, you realize you're pointing things out too."
    hide zyx with dissolve
    return


label zyx_night_3:
    scene bg planetarium with dissolve
    "Someone has turned the ice machine alcove into a planetarium. Stars cover every surface. Constellations are drawn between them in faint blue lines. The ice machine glows in the middle like a small, cold sun."
    show zyx neutral with dissolve
    "Zyx is sitting on the floor in front of it, antennae dimmed, looking up."
    "Every few minutes, someone sticks their head in. A crew member asking Zyx which way the fog should go. A regular of fifteen years asking Zyx whether he's doing the party right. Zyx answers each one with total confidence, and each one leaves looking relieved."
    z "Ah. Earthling. Sit. There is room on this floor for exactly two. This one measured. Earlier. Before you arrived. Not because this one hoped."
    z "This is this one's favorite room. The ice machine dreams of the cold between stars. We understand each other."
    menu:
        z "That one, there. The faint one, near the Swan. That is home. Do you see it?"

        "\"I can't find it. Show me?\"":
            $ gain("zyx", 2)
            z neutral "May this one take your hand to point?"
            "You say yes. Their gloved fingers wrap around yours and guide your arm up to a dim, blue star. They don't let go after."
            z blush "There. Home. Now two beings on this planet know where it is. Soon, perhaps, two beings will have been there."

        "\"I see it. It's beautiful.\"":
            $ gain("zyx", 1)
            z happy "It is not, actually. It is very small and quite gray. But thank you. You are more beautiful. That is a scientific finding."

        "\"Is home even real?\"":
            z neutral "Is anything? Is the ice machine? It makes ice. That seems real enough."

    show zyx neutral
    z "For the report. This one has described the party from the outside. Describe it from the inside. Your favorite moment. Not the biggest. The favorite."
    "You think about it. It isn't any of the big rooms. It's something small: a stranger saying hi, a song in a hallway, somebody's glitter ending up on you."
    "You tell Zyx. They write it down very carefully, and when you hear it back in their voice, it sounds like the best weekend you've had in years. You think it might be."
    z "After the big event, the mission ends. The Ambassadors make their entrance into the ballroom at 11:11. Then the report is complete. And then..."
    z "Then this one is just Zyx. With no mission. On a strange planet, where everyone keeps asking this one for directions. That is the part this one is afraid of."
    menu:
        z "Most Earthlings ask what is under the suit. Would you like to know?"

        "\"Only if you want to tell me. I like Zyx.\"":
            $ gain("zyx", 2)
            "Zyx's antennae light up, very slowly, pink."
            z blush "You like Zyx."
            z "Then Zyx is what you get. Zyx is what is under the suit. All the way down. You are welcome to check. Thoroughly. Later."

        "\"No. Keep the mystery. It's yours.\"":
            $ gain("zyx", 1)
            z happy "A respecter of mysteries. Rare. Noted. This one has some mysteries of yours it would like to investigate, in return."

        "\"Yes! Who are you, really?\"":
            z neutral "This one is Zyx. That is the only answer this one has tonight."
            "The ice machine hums. It's a cold sound."

    if rapport["zyx"] >= ROMANCE_THRESHOLD:
        z blush "After the big event. When the mission is complete. Come to the roof, and wear something you can be beamed in. There is one more piece of research this one wishes to do. With you. Only with you."
    else:
        z happy "Watch for us at 11:11. We will be the ones carrying the gold box. Do not panic."
    hide zyx with dissolve
    return


label zyx_romance:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 5:55 AM"
    "After the ark, the Ambassadors of the Outer Drift vanish. One moment they're on stage in their silver suits, the next there's only the empty ark and the confetti."
    "You look for Zyx in the ballroom, in the hallways, by the ice machine. You find them on the roof, as the sky is going pink."
    "They're sitting on the bench with their sash folded in their lap, antennae glowing softly against the dawn. They keep glancing up, at a patch of sky above the lake where there isn't anything. Yet."
    show zyx neutral with dissolve
    z "Earthling. You found this one. This one was hoping you would. This one did not leave a map. That was a test."
    z happy "You passed. Obviously. Sit. Closer. Closer than that."
    if gave_rock:
        "They're holding the nice rock from the pool. They turn it over and over in their gloved fingers, the way you'd worry a lucky coin."
    z neutral "The ark has landed. The ark has been opened. It was empty, and everyone filled it anyway. The report is filed."
    z "The mission is complete."

    menu:
        z "Do you want to hear the conclusion? This one wrote it during the ark. While crying. Which was not in the mission plan."

        "\"Read it to me.\"":
            z neutral "Ahem."
        "\"Only if it says nice things about me.\"":
            z happy "It says extremely specific things about you. You will be studied for generations. Starting this morning."

    z neutral "{i}Earth is not ready for contact. Earth is loud, and confusing, and keeps its feelings in rooms labeled LOST & FOUND.{/i}"
    z "{i}Earth closes its eyes and shouts the names of dead explorers in swimming pools. Earth puts glitter on strangers. Earth gives its ice machines a planetarium.{/i}"
    z "{i}But one Earthling is ready. Recommend further study. Close study. Recommend this one brings the Earthling aboard.{/i}"
    "Hearing it read out loud, on the roof, at dawn, you realize how much of it you'd stopped seeing until Zyx pointed at it."
    show zyx blush
    z "It was approved. By this one. This one is in charge of approvals."

    if hugged_zyx:
        z "When you hugged this one by the pool, this one's antennae went a color that does not have a name at home. This one has been trying to name it since Saturday."
    if zyx_emergency_contact:
        z "And in the clinic, when you said you were this one's emergency contact. Nobody has ever been this one's anything."

    "The patch of sky above the lake isn't empty anymore. Something is lowering itself out of the dawn, silent and enormous and shaped, unmistakably, like a giant golden box. Its underside is lined with blinking lights."
    "Down in the parking lot, a raver looks up, says {i}huh{/i}, and goes back to her burrito."
    z neutral "That is this one's ride. It has been parked behind the moon all weekend. The ark was the landing beacon. You thought it was empty. It was a signal."
    z blush "This one has requested permission to bring a specimen aboard. A volunteer specimen. Consent is required, in the Earth style and in ours. Ours is forty-seven pages."
    "They produce, from somewhere in the sash, a very thick consent form and a pen shaped like a tiny rocket."

    menu:
        "Initial every single page.":
            z happy "Thorough. This one finds that very attractive. Page thirty-one is the important one."
        "\"Where do I sign?\"":
            z blush "Everywhere. And here. And here. And here, twice, because of the antennae clause."

    "A column of soft pink light comes down over the bench. It's warm, like standing in a sunbeam, and your feet leave the roof."
    scene bg ship with slowfade
    $ time_label = "Monday — Above the lake"
    "The inside of the ship looks like the ice machine planetarium, if the planetarium had been designed by someone who'd seen a lot of 1970s science fiction and taken all of it as instructions."
    "There are stars on every surface, and a padded silver table in the middle, and very good mood lighting."
    show zyx blush with dissolve
    z "Welcome aboard. Please keep your arms and legs inside the ship. Unless this one asks for them."
    z "Now. You know what happens next. Every abductee in your films asks about it. The probe."
    "Zyx holds up the probe. It glows softly. It's smaller than in the films, and it's warm, and it hums, quietly, in a key you've never heard before."
    z "This one will be extremely gentle and extremely thorough. You may say stop at any time. You may say {i}more{/i} at any time. Both are valid data."

    menu:
        "\"Proceed. For science.\"":
            z happy "For science."
        "\"Can we do the forehead thing first?\"":
            z blush "You remembered. This one did not tell you about the forehead thing. You simply... knew. Yes."
            "Zyx leans in until their forehead rests against yours, cool and smooth and smelling faintly of sunscreen. The third eye closes. For a long moment you just breathe like that."
            z "On the Outer Drift, this is how two beings say they wish to be close. Now. The Earth part. And then the Outer Drift part."
            "They kiss you. Their antennae spark. Actually spark. You're almost sure."

    "What follows is slow, and extremely thorough, and enthusiastically consensual on both sides, and at one point the whole ship changes color."
    "Zyx takes notes the entire time. At one point they need a second clipboard. At another point they drop both clipboards, and don't pick them up."
    z blush "Data... very, very confirmed. Further study required. Extensive further study."
    z "This one will need to repeat the experiment. For reproducibility. Science is very strict about this."

    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 7:20 AM"
    "When the pink light sets you back down on the roof, the sun has cleared the mountains and the lake is gold. You're holding a printout. Zyx is holding your hand."
    "At some point Zyx took off one glove. Their hand is warm. It has five fingers. You don't say anything about it, and they don't either."
    "The printout says: {i}SPECIMEN: EXCELLENT. 4%% BAT, AS SUSPECTED. RECOMMEND RETURN VISIT.{/i}"
    scene black with slowfade
    "{i}Two weeks later, a postcard arrives. The picture on the front is a gray, ordinary star.{/i}"
    "{i}Return address: THE OUTER DRIFT (it's near Oakland).{/i}"
    z "Earthling. Research continues. Thursday? This one has found a restaurant where you cook your own food on a hot rock. Gerald recommended it. Afterward, the ship is parked out back."
    if gave_rock:
        z "Bring the nice rock. This one wants to introduce it to the hot rock. It is important that rocks have friends."
    else:
        z "This one has found you a nice rock. It is waiting on this one's windowsill. It has been told about you."
    z "— Z. (The report now has a section about you. It is forty pages long and still in progress. Several pages are classified. You know which ones.)"
    $ chosen = "zyx"
    $ ending_name = "First Contact"
    jump ending_card


label zyx_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show zyx happy with dissolve
    "On Monday morning, a silver figure is standing in the hotel parking lot, waving with all three fingers at every car as it pulls out. Every car waves back. One honks the rhythm from {i}the Zyx{/i}."
    "The crew has already asked them to come back next year and run something. Zyx has agreed, without being entirely sure what they're running."
    z "Earthling! You are leaving. This one has prepared a farewell ritual. It is called 'a wave.' This one has been practicing. Apparently it has become very popular."
    z neutral "The report is filed. Earth is not ready for contact. But Earth has friends in it. This one checked. You are one of them."
    z "On the Outer Drift, friendship is shown by changing to the same color as someone. This one cannot do that. This one is stuck being silver."
    "Zyx reaches into the bag of EARTH ARTIFACTS and hands you a single lost flip-flop, very solemnly."
    z happy "This is the highest honor of our people. Do not lose it. We already lost the other one."
    z "Goodbye, Earthling! You are in the report! Section nine: Friends. You are the whole of section nine!"
    "On the drive home you catch yourself noticing things: a weird sign, a nice rock, two strangers waving at each other across a parking lot. You wonder how long it'll last. You hope a while."
    return
