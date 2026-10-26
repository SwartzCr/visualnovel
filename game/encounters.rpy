## encounters.rpy — random hallway encounters.
##
## Each night, before you choose where to wander, one random encounter plays.
## Encounters never repeat within a playthrough. Most are pure flavor with a
## quick choice; "the note" can earn a little rapport with someone you've met.
##
## To add one: write a label named enc_<something> that ends in `return`, and
## add its name to ENCOUNTERS below.

define ENCOUNTERS = [
    "enc_wedding", "enc_vampire", "enc_flu_shot", "enc_elder",
    "enc_gurus", "enc_heist", "enc_alices", "enc_note",
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
            "\"Oh no,\" he whispers, and pulls the lid closed. From inside: \"Wake me at the ark. Thank you, mortal.\""
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
