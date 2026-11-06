## encounters.rpy — random hallway encounters.
##
## Each night, before you choose where to wander, one random encounter plays.
## Encounters never repeat within a playthrough. Most are pure flavor with a
## quick choice. The six art-room encounters each have a guest version that plays
## if you've met that guest (Penguin Post: Juni, Fanny Bar: Gerald, Tentacletopia:
## Solstice, Zany Optical: Zyx, Let It Go: Wren, Platonic Speed Dating: everyone
## you've met); those can earn +1 rapport, as can the note.
##
## To add one: write a label named enc_<something> that ends in `return`, and
## add its name to ENCOUNTERS below.

define ENCOUNTERS = [
    "enc_wedding", "enc_vampire", "enc_flu_shot", "enc_elder",
    "enc_gurus", "enc_heist", "enc_alices", "enc_note",
    "enc_penguin_post", "enc_fanny_bar", "enc_tentacletopia", "enc_zany_optical",
    "enc_speed_dating", "enc_let_it_go",
]

default encounters_seen = []
default note_for = None
default note_name = ""

init python:

    def pick_encounter():
        """Choose an encounter that hasn't happened yet this playthrough."""
        left = [e for e in ENCOUNTERS if e not in store.encounters_seen]
        if not left:
            return None
        if getattr(store, "vn_testing", False):
            # The test player cycles through them in order so every one gets played.
            choice = vn_next_encounter(left)
        else:
            choice = renpy.random.choice(left)
        store.encounters_seen.append(choice)
        return choice


label random_encounter:
    $ _enc = pick_encounter()
    if _enc is not None:
        scene bg hallway with dissolve
        "On your way down the hall, something finds you first."
        call expression _enc
    return


label enc_wedding:
    "Two mute clowns in bras and fishnets block the corridor. One is holding a bouquet of plastic forks. The other is weeping silently into a handkerchief that goes on forever."
    "They see you and gasp, enormously, without making a sound. One points at you. Then at a hand-lettered sign: WITNESS NEEDED."
    "It's a wedding. They need a witness. You are, apparently, it."
    menu:
        "What kind of witness are you?"

        "A solemn one. Nod gravely at every vow they mime.":
            "The vows go on for some time. One involves a juggling pin. You nod gravely through all of it."
            "At the end they kiss through their red noses, and the clown with the handkerchief hands you one end of it to keep. It is still going."
        "An emotional one. Weep openly.":
            "You weep. They're delighted. Soon all three of you are weeping in perfect silence, and a passerby stops to weep too, just in case."
        "Object. Loudly.":
            "Both clowns turn to you in slow-motion horror. Then they mime, very clearly: {i}speak now or forever hold your peace.{/i}"
            "You hold your peace. They forgive you with a single shared honk of a bicycle horn, and the wedding resumes."
    "As they leave, one of them presses a plastic fork into your hand. It feels like an honor."
    return


label enc_vampire:
    "Halfway down the hall, a coffin is propped against the wall with its lid open. Inside, a vampire in full Victorian dress is lying very still with his arms crossed."
    "One eye opens."
    "He whispers: \"Is it night yet? I can't tell in here. The fog machine is very confusing.\""
    menu:
        "\"It's night. Rise.\"":
            "He sits up in one smooth, theatrical motion, cape flaring. \"At last.\" Then he notices his leg is asleep and has to lie back down."
        "\"It's actually morning. Go back to sleep.\"":
            "\"Oh no,\" he whispers, and pulls the lid closed. From inside: \"Wake me at the big event. Thank you, mortal.\""
        "\"Is there room in there for two?\"":
            "He considers this seriously. \"Ask before you touch,\" he says. \"But yes. It's a double. The party thought of everything.\""
            "You lie in a vampire's coffin for exactly one minute. It's surprisingly comfortable. He smells like cloves."
    return


label enc_flu_shot:
    "Two nurses in vintage uniforms and very large paper hats roll a squeaking cart down the hallway. The cart has a sign: EMOTIONAL FLU SHOTS. NO NEEDLES. SOME FEELINGS."
    "\"You there,\" says one. \"When was your last emotional flu shot?\""
    menu:
        "\"Never. Give me the full dose.\"":
            "They tap a jellybean gently against your arm and make you say one thing you're proud of out loud."
            "It's harder than it sounds. When you manage it, they clap and stick a gold star on your sleeve. It says BRAVE PATIENT."
        "\"I'm afraid of feelings. Is there a smaller dose?\"":
            "\"The pediatric dose,\" says the other nurse kindly, and hands you a lollipop. \"For later. When you're ready.\""
        "Run.":
            "You run. They don't chase you. They just call after you, very warmly: \"We'll be here when you're ready!\" It somehow feels worse."
    return


label enc_elder:
    scene bg livingroom with dissolve
    "You duck into the tea bar for a minute. At the counter, an old man in a rumpled white suit is rocking slowly back and forth, sweating, his eyes fixed on something you can't see."
    "He must be well past seventy. He looks like he's somewhere very far away."
    menu:
        "Gently check in: \"Hey. Are you doing okay?\"":
            "He stops rocking. He turns and gives you a look that is compassionate and absolutely immovable, like a mountain being patient with a pebble."
            "\"Friend,\" he says, \"I have seen things in the last hour that you would not believe in a thousand years. But thank you for checking.\""
            "He pats your hand twice and goes back to wherever he was. You leave feeling oddly blessed, and slightly put in your place."
        "Let him be, but sit nearby with your tea.":
            "You sit two stools down. After a while he starts humming. After a longer while you realize you're humming too. Neither of you says a word."
            "When you leave, he raises his teacup to you without looking. You raise yours back."
    return


label enc_gurus:
    scene bg ballroom with dissolve
    "At the edge of the ballroom, two gurus are holding competing seminars twenty feet apart, each with a small and devoted crowd."
    "One, in flowing white, is teaching that inner peace comes from surrender. The other, in a fleece vest with a headset mic, is teaching that it comes from a 5 AM routine and a cold plunge."
    "They both spot you at the same moment. \"You,\" they say in unison. \"Which way to inner peace?\""
    menu:
        "\"Both. Surrender to the cold plunge.\"":
            "A long silence. Then the white-robed guru begins to weep, and the fleece-vest guru begins to weep, and they embrace across the gap."
            "Their followers merge into one confused, joyful seminar. Someone starts a guided meditation in an ice bath. You slip away while you can."
        "\"Surrender. Obviously.\"":
            "The white-robed guru bows to you. The fleece-vest guru adds you to an email list. You don't know how. You never gave an email."
        "\"Cold plunge. Obviously.\"":
            "You are handed a towel and a schedule. Your wake-up time tomorrow is listed as 4:45 AM. You quietly put the schedule in a plant."
    return


label enc_heist:
    scene bg exchange with dissolve
    "Someone has built a pawn shop entirely out of cardboard in the corner of the stock exchange. Cardboard guitars, cardboard watches, a cardboard taxidermied moose."
    "Three people in ski masks with cardboard guns burst in just as you arrive. \"NOBODY MOVE,\" one of them shouts. \"THIS IS A STICK-UP. THE STICKS ARE CARDBOARD.\""
    menu:
        "Join the heist. Grab the cardboard moose.":
            "You flee with the moose under your arm. Ten minutes later, the robbers return in plain clothes and try to sell the moose back to the shop."
            "The shopkeeper offers forty dollars of cardboard money. You split it four ways. It's the most honest money you've ever made."
        "Be a brave customer. Refuse to put your hands up.":
            "The robbers confer in whispers. One of them hands you a cardboard medal for valor and apologizes. Then they rob the shop anyway."
        "Offer to be the hostage.":
            "\"Oh, thank god,\" says a robber. \"We forgot to plan for that.\" You're led out with great tenderness and released two doors down with a cardboard sandwich."
    return


label enc_alices:
    "A conga line of Alices comes around the corner. Alices of every age, every shape, every gender, in blue dresses and white pinafores, holding each other's waists."
    "At the end of the line, a six-foot caterpillar is smoking a bubble pipe. It points the pipe at you."
    "\"WHO,\" it says, \"ARE YOU?\""
    menu:
        "\"I'm not sure yet. That's sort of why I came.\"":
            "The caterpillar blows a long, thoughtful stream of bubbles. \"Good answer,\" it says. \"Most people lie.\" It gestures, and the Alices open a space for you in the line."
            "You conga for one full lap of the second floor. It is better than you'd think."
        "\"An Alice. Obviously.\"":
            "Several Alices cheer. One gives you her headband. You are now an Alice. You conga for a full lap of the second floor."
        "\"Just passing through.\"":
            "\"No one,\" says the caterpillar, \"is just passing through.\" The Alices conga onward without you. You feel vaguely judged by an insect."
    return


label enc_note:
    python:
        _met = [g for g in GUESTS if g in met]
        note_for = renpy.random.choice(_met) if (_met and not getattr(store, "vn_testing", False)) else (_met[0] if _met else None)
        note_name = GUEST_INFO[note_for][0] if note_for else ""
    "Someone in black jogs up to you, out of breath, headset askew. Not Wren. Someone newer, holding a folded slip of hotel stationery."
    if note_for is not None:
        "\"Hey, you're friends with [note_name], right? They left this at the tea bar. Can you get it to them? I'm drowning tonight.\""
        menu:
            "Take the note and promise to deliver it.":
                $ gain(note_for, 1)
                "You find [note_name] an hour later and hand it over. They read it, laugh out loud, and fold it into a pocket."
                "\"It's a list I made,\" they say, \"of people I wanted to talk to this weekend. I forgot it. You were already on it.\""
            "Read it first. Just a peek.":
                "You unfold it. It's a list, in [note_name]'s handwriting, of people they wanted to talk to this weekend. Your description is on it. Third line."
                "You fold it back up, feeling slightly guilty and extremely pleased, and deliver it without saying a word."
    else:
        "\"This is for... huh. It just says {i}for whoever you meet tonight.{/i} Can you take it?\""
        "You unfold it. It says, in careful handwriting: {i}Go into one room you'd normally walk past.{/i}"
        "You put it in your pocket. It feels like a dare."
    return


################################################################################
## Art-room encounters: rooms that pull you in on your way down the hall.
################################################################################

default postcard_for = None
default postcard_name = ""
default dating_match = None
default dating_match_name = ""

init python:

    def pick_met_guest():
        """A guest you've already met, for encounters that involve one. Deterministic while testing."""
        met_list = [g for g in GUESTS if g in store.met]
        if not met_list:
            return None, ""
        g = met_list[0] if getattr(store, "vn_testing", False) else renpy.random.choice(met_list)
        return g, GUEST_INFO[g][0]


label enc_penguin_post:
    if "juni" in met:
        jump enc_penguin_post_juni
    scene bg penguinpost with dissolve
    "A line snakes out of a doorway and halfway down the hall. At the front, a sign glows in pink and blue neon: PENGUIN POST. PLEASE TAKE A NUMBER."
    "You take a number. It's 4,812. The display above the counter reads NOW SERVING: 3."
    "Inside it's a post office at the South Pole, sometime around the year 3000. Ice and snow everywhere, all of it sparkly and fake and freezing-looking under the neon. Behind the counter, three penguins in tiny postal caps are stamping things with enormous seriousness."
    "The line, it turns out, is the main event. A penguin with a clipboard walks up and down it running Line Activities: line trivia, line stretches, a line-wide game of telephone that starts as {i}I love you{/i} and ends as {i}iceberg lettuce{/i}."
    "Eventually a penguin waddles over, looks at your ticket, looks at you, and waves you straight to the front. Nobody ever finds out why."
    python:
        postcard_for, postcard_name = pick_met_guest()
    menu:
        "\"How can Penguin Post serve you today?\""

        "Write a postcard to [postcard_name]." if postcard_for is not None:
            "The stationery has prompts printed on it. Yours reads: {i}Tell them one thing you noticed about them that they probably think nobody noticed.{/i}"
            "You write it. It's harder than you expected, and then it isn't."
            "A penguin stamps it with a stamp shaped like a fish and slaps it into a mailbag. \"Delivered within the hour,\" it honks. \"Or your money back. You paid no money.\""
            $ gain(postcard_for, 1)
            "Later that night, across a hallway, you see [postcard_name] reading a postcard with a fish on it. They look up and find you. They don't say anything. They don't have to."
        "Ask to be mailed.":
            "The penguins confer. One of them gets out the bubble wrap."
            "You are wrapped, stamped on the forehead (FRAGILE: CONTAINS FEELINGS), loaded onto a hand truck and wheeled at great speed down the hallway by two penguins who are clearly having the time of their lives."
            "You are delivered to the tea bar. Someone signs for you. You are unwrapped, handed a cup of tea, and released back into the wild."
        "Sign up for mail carrier orientation.":
            "Orientation takes eleven minutes. You learn the Penguin Oath, the Penguin Waddle, and the correct way to hold a mailbag (with dignity, and both flippers)."
            "You graduate with a paper postal cap and a bag of letters addressed to rooms you've never heard of. You deliver four of them. One of them is to yourself. It says: {i}Welcome to the flock.{/i}"
    "On your way out, the NOW SERVING sign clicks over to 4. The line cheers."
    return


label enc_fanny_bar:
    if "gerald" in met:
        jump enc_fanny_bar_gerald
    scene bg ballroom with dissolve
    "The heat on the dance floor is unbearable. Somebody's glitter is melting. The bass is coming up through the carpet like it's trying to escape."
    "Then a cool breeze hits you. A woman in a blue hard hat and a hi-vis vest has set up an enormous box fan at the edge of the dance floor and is aiming it at the crowd like a firefighter."
    "She hands you a business card. It matches the sticker on her fan:"
    "{i}FEELING HOTT? Come to Room 313 for a Blow Job at the OnlyFans Fanny Bar!!{/i}"
    "She winks. \"Fan Technician. I'm licensed.\""
    scene bg fanbar with dissolve
    "Room 313 is an oasis. Every surface has a fan on it: box fans, desk fans, ceiling fans, a fan that oscillates so dramatically it might be dancing. A basket of folding hand fans sits by the door under a sign: FOR SUBSCRIBERS ONLY!"
    "Hand-lettered signs on every wall beg: PLEASE SUBSCRIBE!! SMASH THAT SUBSCRIBE!! WE ARE BEGGING YOU!!"
    "A projector on the wall plays glitched-out clips of every movie scene that has ever had a fan in it, on loop."
    menu:
        "A clipboard by the door has a space for your name."

        "Subscribe.":
            "You write your name. A bell rings. Somebody throws a little confetti at you, then fans it away."
            "As a subscriber, you are entitled to the Fanny Bar. It doesn't serve drinks. It serves mist. A bartender in a bow tie offers you a spray bottle fan: \"Lemon or lilac?\""
            "You choose lilac. It is the best thing that has happened to your face all night."
        "Refuse to subscribe, on principle.":
            "You stand in the middle of the room, unsubscribed and sweating, as fans blow cool air on everyone except you."
            "It's a kind of protest. Nobody notices. One of the fans turns slowly toward you, almost apologetically, and then turns away again."
        "Check out the booth in the corner.":
            "In the corner is an old-fashioned video booth with a blue-and-yellow sign: NUTBUSTER VIDEO. A rack of VHS tapes has titles like {i}Fan Girls Go Wild{/i} and {i}Hotties Cool Off{/i}."
            "You check out {i}Fan Girls Go Wild{/i} and put it in the VCR."
            "It is forty minutes of women holding fans. Just fans. Electric fans, paper fans, one very large fan made of ostrich feathers. Nobody ever does anything but fan."
            "You watch the whole thing. It's weirdly relaxing. A soft voice-over describes the sensation of moving air."
    "Then the power cuts out."
    "Every fan in the room winds down at once with a long, sad, descending whine, like a choir of tiny dying engines. In the silence, the heat rushes back in."
    "\"NEVER FEAR!\" shouts the Fan Technician from the doorway. \"WE HAVE PALM FRONDS! FOR SUBSCRIBERS ONLY!\""
    "The last few holdouts stampede toward the clipboard."
    "You leave fully cooled, with a folding hand fan and a pair of tiny propeller pasties you will explain to no one, ever."
    return


label enc_tentacletopia:
    if "solstice" in met:
        jump enc_tentacletopia_solstice
    scene bg tentacletopia with dissolve
    "A round hatch in the wall is marked AIRLOCK. A person in a full shrimp costume pokes their head out and beckons you in with a feeler."
    "\"Adventurer! Thank the tides. The world is searching for the tech that'll save us all, and our sources say the answer lies in the Lost City of Miami.\""
    "\"It sank into the ocean centuries ago. The jellyfish run it now. They have evolved. They have opinions.\""
    "\"We, the crustaceans, will guide you. In exchange we only ask for one thing: an extended broadcast of our favorite program, {i}Shrimp Justice: A Crustacean Courtroom Show{/i}.\""
    "They hand you a snorkel, a pair of swim goggles and a flashlight that has been painted to look like a much better flashlight. You step through the airlock."
    "Beyond it is the bottom of the sea. A kelp forest sways under blue light. The sunken art-deco towers of Miami lean in the gloom, their neon signs still faintly glowing. Giant jellyfish drift overhead, trailing their tentacles."
    menu:
        "Where do you search for the savior tech?"

        "Poke around the coral wall.":
            "The coral wall is full of tiny hidden dioramas, each about the size of a shoebox. A shrimp wedding. A shrimp tax office. A shrimp lying on a tiny shrimp therapist's couch, describing its childhood."
            "Behind the last diorama, wedged in the coral, something glints."
        "Duck through the jellyfish.":
            "You weave between the jellyfish, ducking tentacles. One brushes your shoulder. It's made of streamers and it smells faintly of fog machine."
            "At the heart of the swarm, the jellyfish part, as if they've been guarding something. Something glints."
        "Stop to watch an episode of Shrimp Justice.":
            "A tiny TV half-buried in the sand is playing {i}Shrimp Justice{/i}. Today's case: a hermit crab is suing another hermit crab over a shell."
            "You are, apparently, the jury. You find for the plaintiff. The shrimp guides weep with joy. As a reward, one of them points a feeler at the kelp, where something glints."
    "You dig it out of the sand and hold it up. It's a disco ball."
    "Every shrimp in the room gasps. Somewhere a speaker kicks on and starts playing a 1977 disco hit. The jellyfish begin, very slowly, to dance."
    "\"DISCO,\" says your shrimp guide, overcome. \"Of course. It was always disco. The shrimp have always known.\""
    return


label enc_zany_optical:
    if "zyx" in met:
        jump enc_zany_optical_zyx
    scene bg optical with dissolve
    "A door is propped open by a giant inflatable eyeball. Inside, it's an optometrist's office from a strip mall, run through a vaporwave blender: neon pink and teal, palm-tree wallpaper, synth music that sounds like the 1980s imagining the future."
    "The receptionist is an iPad on a stand, with a cheerful AI face. Behind it, an enormous motorized googly eye rolls slowly around in its socket."
    "\"Welcome to ZANY OPTICAL, a subsidiary of Manic Medical!\" says the iPad. \"Do you have vision insurance? Do you have a vision? Do you have insurance? Please don't answer, I'm an iPad.\""
    "A doctor in a lab coat and a pair of glasses with tiny windshield wipers on them waves you into the exam chair."
    "\"Let's begin. Look through here and tell me: which is better, A or B?\""
    menu:
        "Lens A: the world, but everyone is a little bit more of a golden retriever.\n\nLens B: the world, but every plant is softly whispering encouragement."

        "A is better.":
            "\"Interesting. Very interesting,\" says the doctor, writing {i}golden retriever{/i} on a clipboard and underlining it."
        "B is better.":
            "\"Mm-hm. Mm-hm,\" says the doctor, writing {i}plants{/i} on a clipboard and drawing a little heart next to it."
        "They're the same.":
            "The doctor puts down the clipboard. \"Nobody has ever said that,\" they whisper. \"You may have perfect vision.\" They pick the clipboard back up. \"Let's keep going anyway.\""
    "The doctor flips a switch. The room floods with a sodium-yellow light that drains every color into shades of grey. \"Just checking your color vision. Now: what color is this flag?\""
    "They hold up a flag. In the strange light, it could be anything."
    menu:
        "\"Red.\"":
            "\"Correct! You can spot a red flag. That's rare in here.\""
        "\"Green.\"":
            "\"Hm. You see green flags where others see red. Optimist. We have a lens for that, but we don't recommend it.\""
        "\"It depends on the relationship.\"":
            "The doctor nods slowly. \"Diagnosis: wisdom. Extremely rare. Not covered by insurance.\""
    "Your prescription is a pair of glasses that bend your vision ninety degrees upward. You wear them for five minutes in the back of the clinic, staring at the ceiling, while a stranger in matching glasses lies down on the floor so you can talk face to face."
    "It's one of the best conversations you've had all weekend. You never see their face."
    "On your way out, the iPad flips around: HOW MUCH WOULD YOU LIKE TO TIP YOUR PROVIDER TODAY? The options are 18%%, 20%%, 25%% and A Compliment. You choose A Compliment. The giant googly eye rolls happily."
    return


label enc_speed_dating:
    if speed_cast():
        $ speed_sides = {}
        $ speed_cast_names = ", ".join(GUEST_INFO[g][0] for g in speed_cast())
        jump enc_speed_dating_cast
    scene bg speeddating with dissolve
    "A sign on a door reads PLATONIC SPEED DATING: FIND YOUR SURVIVAL BUDDY. Inside, a crowd is standing in the middle of a ballroom side-room. Two volunteers stand at opposite walls holding small whiteboards."
    "The host, in a sequined blazer and a headset microphone, spots you. \"A newcomer! Perfect. In you come. Every round, I ask a question. You pick a side. Everyone quietly judges each other. Then I loudly judge everyone. Ready?\""
    "Round one. The host writes on a whiteboard paddle and holds it up: ONLY ONE CAN EXIST."
    menu:
        "Electric guitar, or electric synths?"

        "Electric guitar.":
            "You stand with the guitars. A man in a leather jacket nods at you with deep respect."
        "Electric synths.":
            "You stand with the synths. Someone next to you hums an arpeggio, very quietly, to welcome you."
        "Stand exactly in the middle.":
            "\"A FENCE SITTER,\" booms the host. The whole room turns to look at you. \"Bold. Wrong, but bold.\""
    "Round two. WOULD YOU RATHER."
    menu:
        "Know every language, or be able to talk to animals?"

        "Every language.":
            "You stand with the polyglots. The host asks your name and introduces you to a woman who says she's learning Klingon \"for the love of the game.\""
        "Talk to animals.":
            "You stand with the animal people. It's a bigger crowd than you'd think. A man in a duck costume gives you a solemn nod."
        "Talk to animals, but only pigeons.":
            "The host stares at you. \"That wasn't an option.\" Then, after a long pause: \"I'll allow it.\" You stand alone in a third, newly drawn pigeon section."
    python:
        dating_match, dating_match_name = pick_met_guest()
    "After a few more rounds, the host walks the room, pairing people who chose the same side every single time."
    if dating_match is not None:
        "And there, on your side for every single question, is [dating_match_name]. You hadn't even noticed them in the crowd."
        "\"You two!\" says the host. \"Kindred spirits. Draw a mission.\" You pull a handwritten tag from a grab bag: {i}Go somewhere neither of you has been yet this weekend. Report back.{/i}"
        $ gain(dating_match, 1)
        "You and [dating_match_name] spend twenty minutes looking for a room neither of you has been in. You find a supply closet with a single disco light in it. You both agree it counts."
    else:
        "You've ended up on the same side as a woman in a tinfoil cape every single time. The host introduces you. \"Survival buddies! Draw a mission.\""
        "Your tag reads: {i}Find the strangest room on this floor and rate it out of ten.{/i} You do. It's a seven. She says eight. You agree to disagree, and part as friends forever."
    return


label enc_let_it_go:
    if "wren" in met:
        jump enc_let_it_go_wren
    scene bg letitgo with dissolve
    "Outside a door, a person with a clipboard and a calm, professional smile stops you. A sign beside them reads LET IT GO: A WORKSHOP."
    "\"Before we begin, a few intake questions. On a typical day, how often do you look at your phone?\""
    menu:
        "\"A healthy amount.\"":
            "\"Mm,\" they say, writing {i}denial{/i} on the clipboard."
        "\"Constantly. It's a problem.\"":
            "\"Thank you for your honesty,\" they say, writing {i}ready{/i} on the clipboard."
        "\"I've used it as a flashlight all weekend.\"":
            "They look up, impressed. \"You're further along than most.\" They write {i}advanced{/i} on the clipboard."
    "Inside, folding chairs face a small stage. The presenter, in a turtleneck and a headset mic, clicks to the first slide of a presentation titled GOODBYE, MY BELOVED: LIFE AFTER THE PHONE."
    "Four slides in, the projector dies. Without missing a beat, the presenter pulls out a stack of hand-drawn posterboard slides and continues the presentation analog, flipping each one with a dramatic flourish."
    "There are exercises. You're asked to name the first app you open every morning, then to say goodbye to it out loud. Someone in the second row breaks down weeping while saying goodbye to a weather app."
    "At the end, the presenter gestures to a table at the side of the room. On it is a pile of blank wooden phone-shaped blocks, a hot-glue gun, and an overwhelming amount of glitter."
    "\"Every graduate may adopt an Emotional Support Phone. It can't do anything. That's the point. It's just there for you.\""
    menu:
        "Decorate an Emotional Support Phone.":
            "You give yours googly eyes, a glittery case and a little drawn-on screen that just says {i}you're doing great{/i}."
            "You put it in your pocket. Every so often for the rest of the weekend, you reach for your phone out of habit and find this one instead. It's always a good surprise."
        "Leave with nothing. You're ready.":
            "The presenter places a hand over their heart. \"That,\" they say quietly, \"is the most advanced thing I have ever seen.\""
            "The room gives you a standing ovation as you leave. You feel incredibly, absurdly free."
    return


################################################################################
## Guest versions of the art-room encounters.
## If you've met the guest, the room plays as a scene with them instead.
################################################################################

label enc_penguin_post_juni:
    scene bg penguinpost with dissolve
    "A line snakes out of a doorway and halfway down the hall. At the front, a sign glows in pink and blue neon: PENGUIN POST. PLEASE TAKE A NUMBER."
    "You take a number: 4,812. Directly in front of you, holding ticket 4,811 in both sleeves like a prize, is a pink axolotl."
    show juni happy with dissolve
    j "Oh! Hi! You're in the line! Isn't the line great?"
    j neutral "I've been here forty minutes. I love it. A line is a room you're allowed to stand outside of. Nobody expects you to go in yet."
    "A penguin with a clipboard waddles past, running Line Activities. Line trivia. Line stretches. A game of telephone that starts as {i}I love you{/i} and reaches you as {i}iceberg lettuce{/i}."
    j happy "Iceberg lettuce. Pass it on."
    "Eventually a penguin waves you both to the counter together. It slides two postcards across, with prompts printed on them."
    "Juni's says: {i}Write to the person standing behind you in line.{/i} Yours says: {i}Tell them one thing you noticed about them that they think nobody noticed.{/i}"
    j surprised "Oh no. Oh, that's... okay. Okay. Don't look."
    menu:
        "What do you write?"

        "\"You laugh like it surprises you every time.\"":
            $ gain("juni", 1)
            "You hand it over. Juni reads it, and goes quiet, and then the hood goes very pink."
            j blush "...Nobody's ever noticed that. I didn't know I did that."
        "\"You hold your sleeves when you're nervous. It's very cute.\"":
            $ gain("juni", 1)
            j blush "I'm not nervous. I'm... okay, I'm holding my sleeves right now."
            "They don't let go of them. They hold the postcard against their chest instead."
        "\"See you at the big event!\"":
            j neutral "Oh. Ha. Yeah! See you at the big event."
            "They look at the card a beat longer than a card that says {i}see you at the big event{/i} needs."
    "A penguin stamps Juni's postcard with a fish and tosses it into a mailbag."
    j neutral "You'll get it within the hour. Or your money back. You paid no money."
    "Forty minutes later, a penguin finds you in the hallway, salutes, and hands you a postcard. It's covered in tiny drawn axolotls. In the middle, in careful handwriting:"
    "{i}You're the first person I didn't wait outside a door for. — J.{/i}"
    hide juni with dissolve
    return


label enc_fanny_bar_gerald:
    scene bg ballroom with dissolve
    "The heat on the dance floor is unbearable. A Fan Technician in a blue hard hat hands you a business card:"
    "{i}FEELING HOTT? Come to Room 313 for a Blow Job at the OnlyFans Fanny Bar!!{/i}"
    scene bg fanbar with dissolve
    "Room 313 is an oasis of fans: box fans, desk fans, a ceiling fan spinning so hard it might take off. Signs beg PLEASE SUBSCRIBE!!"
    "Directly in front of the biggest box fan, eyes closed, fur streaming backward like a flag in a gale, sits a Sasquatch."
    show gerald happy with dissolve
    g "Oh. Oh, hello. Forgive me. I've been sitting here for half an hour. I may never move again."
    g neutral "I have been wearing this coat since 1961. It does not come off. The dance floor was, if I may say, an ordeal."
    g "They tell me I must subscribe to stay. I tried. The clipboard wanted a name. I'm afraid I signed it with a footprint, out of habit. They seem unsure whether it counts."
    menu:
        "What do you do?"

        "Drag a second fan over and aim it at him.":
            $ gain("gerald", 1)
            "You drag a pedestal fan across the room and point it at his other side. His fur now blows in two directions at once, like a dandelion."
            g happy "Oh. Oh, that's... yes. Stereo. You've given me stereo."
        "Sign the clipboard for both of you.":
            $ gain("gerald", 1)
            "You write your name, and next to it: {i}+1 (Sasquatch).{/i} A bell rings. A volunteer throws confetti at you both and then, apologetically, fans it away."
            g happy "Subscribed. How modern. I feel tremendously current."
        "Ask what he thinks of the Nutbuster booth.":
            g surprised "Ah. I... yes. I did investigate the booth. For research."
            g blush "It's only fans. All of the tapes. Just people with fans. I watched {i}Hotties Cool Off{/i} three times. It was the most relaxing hour of my weekend. Please don't tell Margaret."
    "Then the power cuts out."
    "Every fan in the room winds down at once with a long, sad, descending whine. The heat rushes back in. People cry out. Someone shouts about palm fronds, for subscribers only."
    "Gerald doesn't move. He just sighs contentedly, reaches into his fur and produces a full-sized fern."
    g happy "I'm from the woods. We've never had electricity. Allow me."
    "He stands up, all seven feet of him, and begins to fan the entire room with one slow, enormous sweep after another. The crowd turns toward him like sunflowers."
    "When the power comes back, the room gives him a standing ovation. The Fan Technician gives him an honorary blue hard hat. It's much too small. He wears it anyway."
    hide gerald with dissolve
    return


label enc_tentacletopia_solstice:
    scene bg tentacletopia with dissolve
    "A round hatch in the wall is marked AIRLOCK. Inside, a person in a full shrimp costume is briefing a raver who has put a snorkel on over her goggles."
    show solstice happy with dissolve
    s "Oh my god, hi! Get in here! We're going to the bottom of the sea! The shrimp say the world needs saving and the answer's in the Lost City of Miami!"
    "The shrimp guide nods gravely. \"The jellyfish run it now. They have evolved. They have opinions. We ask only one thing in return: an extended broadcast of {i}Shrimp Justice: A Crustacean Courtroom Show{/i}.\""
    s "I already said yes. I've seen four episodes. The hermit crab one is devastating."
    "Beyond the airlock: kelp swaying under blue light, sunken art-deco towers, neon signs still faintly glowing in the gloom. Giant jellyfish drift overhead. Solstice's LED top lights up the water around her like a little submarine."
    s neutral "Okay. Savior tech. Where do we look?"
    "You dig together through the coral dioramas: a shrimp wedding, a shrimp tax office, a shrimp on a tiny therapist's couch. Then Solstice shrieks and holds something up."
    "It's a disco ball."
    show solstice surprised
    s "DISCO. It's DISCO. The savior tech is DISCO. I KNEW it! I've been saying this for YEARS!"
    "A speaker kicks on. A 1977 disco track fills the sea. The shrimp weep with joy. The jellyfish, very slowly, begin to dance."
    menu:
        s happy "Come on! The jellyfish are dancing! We have to dance with the jellyfish! It's literally the end of the world!"

        "Dance with her and the jellyfish.":
            $ gain("solstice", 1)
            "You dance at the bottom of the sea with a raver and a swarm of evolved jellyfish. Solstice is laughing so hard her snorkel fills with air."
            s blush "This is the best rave I've ever been to. And it's in a hotel room. And it's underwater. And it's with you."
        "Hold up the disco ball so it catches her lights.":
            $ gain("solstice", 1)
            "You hold the disco ball up over her head. Her LED top throws a thousand tiny colored lights across the whole ocean floor, the towers, the kelp, the jellyfish."
            s blush "Oh. Oh wow. Look what we made."
        "Sit on the coral and watch.":
            "You sit down on the reef. Solstice stops dancing and points at you, scandalized."
            s neutral "Hey! No spectators! It's the rule! Even at the bottom of the sea!"
            "She drags you up by both hands anyway. The jellyfish make room."
    "As you leave, the shrimp crown Solstice Disco Queen of the Lost City of Miami with a crown made of bottle caps. She wears it for the rest of the night."
    hide solstice with dissolve
    return


label enc_zany_optical_zyx:
    scene bg optical with dissolve
    "Through a door propped open by a giant inflatable eyeball: a vaporwave optometrist's office, pink and teal neon, synth music, an enormous googly eye rolling slowly on the wall."
    "At the reception desk, a silver alien is deep in an argument with an iPad."
    show zyx neutral with dissolve
    z "This one's insurance is from the Outer Drift. It is very comprehensive. It covers meteors."
    "\"I'm sorry,\" chirps the iPad, \"we don't accept Outer Drift. Have you considered paying with a compliment?\""
    z happy "Earthling! You are here. Good. This one requires an emergency contact for an eye exam. You have experience in this field."
    "A doctor in glasses with tiny windshield wipers leads you both into the exam room, sits Zyx in the chair, looks into their face, and drops the clipboard."
    "\"That's three eyes,\" the doctor whispers. \"I've only ever examined two at a time. This is the greatest day of my career.\""
    "The diagnosis comes quickly: third-eye astigmatism, mild. Then the doctor floods the room with a strange yellow light that drains all color away, and holds up a flag."
    "\"Ambassador. What color is this flag?\""
    z neutral "Magenta."
    "\"There's no magenta flag,\" says the doctor. \"There's red, and there's green.\""
    z "There is magenta. It means: proceed, but with feelings. We use it constantly at home."
    "The doctor writes it down, reverently. Then they bring out a tray of frames, each with three lenses."
    menu:
        z "Earthling. You will choose this one's glasses. This one trusts your Earth taste."

        "The sparkly cat-eye ones.":
            $ gain("zyx", 1)
            z blush "Fabulous. This one is fabulous. Write that down for the report."
        "The ones with tiny windshield wipers, like the doctor's.":
            $ gain("zyx", 1)
            "The wipers go back and forth across all three lenses. Zyx is delighted beyond words, which for Zyx is a lot of words."
            z happy "For meteors. Practical. The insurance company will be thrilled."
        "\"Honestly? You look perfect without them.\"":
            $ gain("zyx", 1)
            "Zyx goes very still. Their antennae glow, slowly, pink."
            z blush "...Then this one will wear them only for science."
    "On the way out, the iPad flips around: HOW MUCH WOULD YOU LIKE TO TIP YOUR PROVIDER TODAY? Zyx chooses A Compliment, leans in close to the giant googly eye and says, very formally:"
    z neutral "Your eye is extremely round. On behalf of the Outer Drift, well done."
    "The googly eye rolls with what can only be described as joy."
    hide zyx with dissolve
    return


label enc_let_it_go_wren:
    scene bg letitgo with dissolve
    "Outside a door, a sign reads LET IT GO: A WORKSHOP. Beside it, looking like someone who has been sentenced, stands Wren."
    show wren neutral with dissolve
    w "Don't. Don't say anything. Pilar signed me up. She called it a {i}wellness intervention{/i}. In front of the whole crew."
    w "It's about saying goodbye to your phone. I don't even have my phone on me. I have this."
    "They hold up their walkie-talkie like you've asked to see their ID."
    "Inside, folding chairs face a small stage. The presenter, in a turtleneck and headset mic, asks everyone to place their device in a wicker basket at the front. One by one, people do. Some of them are crying."
    "Wren doesn't move. Their hand is wrapped around the walkie so tightly their knuckles are white."
    menu:
        "What do you do?"

        "\"I'll keep an ear on it. If anything comes through, I'll get you.\"":
            $ gain("wren", 1)
            "You hold out your hand. They look at it for a long time, then put the walkie in it, like they're handing over something alive."
            w blush "Okay. Okay. If it says {i}fire{/i}, you come get me. It will say fire. If it says anything about a flamingo, ignore it."
        "Put your own phone in the basket, then look at them.":
            $ gain("wren", 1)
            "You walk to the front and drop your phone into the basket. Then you turn around and look at them."
            w surprised "Oh, that's... that's peer pressure. That's really effective peer pressure."
            "They walk up and lay the walkie gently on top of your phone, like tucking it into bed."
        "\"You don't have to. It's okay.\"":
            w neutral "...Thanks. Yeah. I'll just... turn it down a little."
            "They turn the volume down one notch. It's something."
    "The presenter clicks to the first slide. Four slides in, the projector dies, and the talk continues on hand-drawn posterboard."
    "Wren lasts four minutes and thirty seconds before their hand starts drifting toward the basket. Then five minutes. Then, somewhere around minute eight, they stop reaching altogether, sit back, and actually listen."
    "At the end, there's a crafting table: blank wooden phones, googly eyes, glitter. Everyone gets to make an Emotional Support Phone."
    "Wren makes an Emotional Support Walkie instead. It's a block of wood with a pipe-cleaner antenna, two googly eyes, and a strip of gaffer tape on the back that says OFF DUTY. It doesn't do anything."
    w happy "It's perfect. Nobody can reach me on it. Not a single person."
    "When you walk out, the real walkie is back on their belt. But the wooden one is in their hand."
    hide wren with dissolve
    return


label enc_speed_dating_cast:
    scene bg speeddating with dissolve
    "A sign on a door reads PLATONIC SPEED DATING: FIND YOUR SURVIVAL BUDDY. Inside, a crowd is milling around a side-room of the ballroom, with a strip of yellow tape down the middle of the floor."
    "And it's not just strangers. You spot familiar faces in the crowd: [speed_cast_names]."
    "The host, in a sequined blazer and a headset microphone, claps. \"Every round, I ask a question. You pick a side. Everyone quietly judges each other. Then I loudly judge everyone.\""
    "Round one. The host holds up a whiteboard paddle: ONLY ONE CAN EXIST."
    menu:
        "Electric guitar, or electric synths?"

        "Electric guitar." (side="a"):
            $ speed_pick(1, "a")
        "Electric synths." (side="b"):
            $ speed_pick(1, "b")
        "Stand exactly in the middle." (side="c"):
            $ speed_pick(1, "c")
    $ speed_react(1)
    "Round two. WOULD YOU RATHER."
    menu:
        "Know every language, or be able to talk to animals?"

        "Every language." (side="a"):
            $ speed_pick(2, "a")
        "Talk to animals." (side="b"):
            $ speed_pick(2, "b")
        "Talk to animals, but only pigeons." (side="c"):
            $ speed_pick(2, "c")
    $ speed_react(2)
    "Round three. THIS OR THAT."
    menu:
        "Sunrise, or sunset?"

        "Sunrise." (side="a"):
            $ speed_pick(3, "a")
        "Sunset." (side="b"):
            $ speed_pick(3, "b")
        "\"I've never stayed up to see either.\"" (side="c"):
            $ speed_pick(3, "c")
    $ speed_react(3)
    $ dating_match, dating_match_name = speed_match()
    "The host walks the room, matching people who kept ending up on the same side."
    "\"You!\" They point at you, then at [dating_match_name]. \"Survival buddies. I've been watching. Draw a mission.\""
    $ gain(dating_match, 1)
    "You pull a handwritten tag from the grab bag: {i}Go somewhere neither of you has been yet this weekend. Report back.{/i}"
    call expression "speed_mission_" + dating_match
    return


init python:

    # Each guest's answers: round -> side.
    SPEED_ANSWERS = {
        "juni":     {1: "b", 2: "b", 3: "c"},
        "gerald":   {1: "a", 2: "b", 3: "a"},
        "solstice": {1: "b", 2: "a", 3: "c"},
        "wren":     {1: "a", 2: "a", 3: "a"},
        "zyx":      {1: "c", 2: "c", 3: "b"},
    }

    # What each guest does when you end up on the same side.
    SPEED_LINES = {
        ("juni", 1): ("j", "happy", "Synths! Synths are like... music that doesn't need you to be cool about it."),
        ("gerald", 1): ("g", "happy", "Guitar. My cousin Bernard played. Badly. Movingly."),
        ("solstice", 1): ("s", "happy", "SYNTHS. I'm going to hug everyone on this side. Brace."),
        ("wren", 1): ("w", "neutral", "Guitar. You can fix a guitar with tape. You can't fix a synth with tape. I've tried."),
        ("zyx", 1): ("z", "neutral", "The middle. This one is gathering data from both sides. Also, this one is a fence."),
        ("juni", 2): ("j", "happy", "Animals. They don't need you to make small talk. Lotl agrees."),
        ("gerald", 2): ("g", "neutral", "I already talk to animals. I thought everyone did. This is very upsetting news."),
        ("solstice", 2): ("s", "happy", "Every language! Imagine telling people they're doing great in like four hundred languages."),
        ("wren", 2): ("w", "neutral", "Every language. Then I could finally read the manuals for every fog machine. They're never in English."),
        ("zyx", 2): ("z", "happy", "Pigeons. Yes. This one already speaks pigeon. They are excellent diplomats."),
        ("juni", 3): ("j", "blush", "Neither. I've never stayed up. Maybe this weekend. If I'm with someone."),
        ("gerald", 3): ("g", "happy", "Sunrise. Always sunrise. It's the only time the forest is completely honest."),
        ("solstice", 3): ("s", "blush", "Neither! I'm always inside, dancing. That's... wow, that sounded sadder out loud."),
        ("wren", 3): ("w", "neutral", "Sunrise. Usually through a crack in a loading dock door, holding a toolbox. But still. Sunrise."),
        ("zyx", 3): ("z", "neutral", "Sunset. At home, sunset lasts four years. This one finds yours very brisk."),
    }

    def speed_cast():
        return [g for g in GUESTS if g in store.met]

    def speed_pick(rnd, side):
        store.speed_sides[rnd] = side

    def speed_react(rnd):
        side = store.speed_sides.get(rnd)
        same = [g for g in speed_cast() if SPEED_ANSWERS[g][rnd] == side]
        if not same:
            renpy.say(None, "You look around. Nobody you know is on your side this time. The host notices and nods at you, impressed: \"A lone wolf.\"")
            return
        for g in same:
            who, expr, line = SPEED_LINES[(g, rnd)]
            renpy.show((g, expr))
            renpy.say(getattr(store, who), line)
            renpy.hide(g)

    def speed_match():
        cast = speed_cast()
        def score(g):
            return (sum(1 for r in (1, 2, 3) if SPEED_ANSWERS[g][r] == store.speed_sides.get(r)), store.rapport[g])
        best = max(cast, key=score)
        return best, GUEST_INFO[best][0]

default speed_sides = {}
default speed_cast_names = ""


label speed_mission_juni:
    show juni happy with dissolve
    "You and Juni wander the halls looking for a room neither of you has been in. Juni stops at every door. Then, at a door marked SUPPLY, they take a breath and walk in first."
    j blush "I went in first. Did you see that? I went in first."
    hide juni with dissolve
    return

label speed_mission_gerald:
    show gerald happy with dissolve
    "You and Gerald find a room neither of you has been in: the hotel's old boiler room, warm and humming. Gerald declares it the coziest cave he's been in since 1974. You report back: ten out of ten, would hibernate."
    hide gerald with dissolve
    return

label speed_mission_solstice:
    show solstice happy with dissolve
    "You and Solstice find a room neither of you has been in: a tiny closet with one disco light and nobody in it. She turns off her LED top. You stand there in the slow-turning light, not dancing, just talking. It's her favorite room of the weekend."
    hide solstice with dissolve
    return

label speed_mission_wren:
    show wren happy with dissolve
    "You and Wren try to find a room neither of you has been in. This is impossible: Wren has been in every room. Finally they lead you to a broom closet they've never opened, because it's labeled FOR WREN ONLY and they didn't make that sign. Inside is a single folding chair and a note: {i}Sit down. — Pilar.{/i} They do, for a full minute."
    hide wren with dissolve
    return

label speed_mission_zyx:
    show zyx happy with dissolve
    "You and Zyx find a room neither of you has been in: the hotel laundry. Zyx stands in front of the dryers for a long time, watching the clothes go round. \"Small planets,\" they whisper. \"Warm, tumbling planets.\" They take extensive notes."
    hide zyx with dissolve
    return
