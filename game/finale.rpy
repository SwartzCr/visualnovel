## finale.rpy — after the ark: who you find, and how the weekend ends.

default who = None
default ending_name = ""
default persistent.endings = set()
default candidates = []
default friend = None
default endings_found = 0
default endings_total = 0

define ALL_ENDINGS = ["Regeneration", "Not Blurry", "The Longest Day", "Off Duty", "First Contact", "Good Company", "Checkout"]


label finale:
    call ceremony

    scene bg ballroom with dissolve
    $ time_label = "Sunday — After Midnight"
    $ candidates = romanceable()

    if candidates:
        "The party goes on around you, louder than ever. But your mind keeps drifting back to someone."
        if len(candidates) > 1:
            "More than one someone, actually. But you can only be in one place at sunrise."

        menu:
            "Where do you go?"

            "Look for Juni. You have a feeling they'll be down by the pool." (guest="juni") if "juni" in candidates:
                $ who = "juni"
            "Climb to the roof. Gerald likes to be somewhere high when the sun comes up." (guest="gerald") if "gerald" in candidates:
                $ who = "gerald"
            "Find Solstice before the sun comes up." (guest="solstice") if "solstice" in candidates:
                $ who = "solstice"
            "Wait for Wren to get off shift." (guest="wren") if "wren" in candidates:
                $ who = "wren"
            "Go find Zyx. The mission's almost over." (guest="zyx") if "zyx" in candidates:
                $ who = "zyx"
            "Don't go to anyone. Some weekends are just yours." (guest="alone"):
                $ who = None

        if who is not None:
            jump expression "%s_romance" % who

    # No romance tonight.
    $ friend = closest()
    if friend is not None:
        jump friend_ending
    jump solo_ending


label friend_ending:
    "You dance until the windows go gray. You don't fall in love this weekend. That's okay. Not every story has to end the same way."
    "But you made a friend. A real one. The kind you'll text in six months for no reason."
    call expression "%s_friend" % friend
    scene black with slowfade
    "{i}On the drive home, there's still glitter in your ears, a ping-pong ball in your pocket, and a laminated card that says you were never here.{/i}"
    "{i}You were, though.{/i}"
    $ ending_name = "Good Company"
    jump ending_card


label solo_ending:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 6:00 AM"
    "You end up on the roof alone at sunrise. The rigging is slack. The string lights have burned out one by one, like the party is going to sleep a room at a time."
    "You didn't find your person this weekend. Maybe you weren't looking. Maybe you were looking at everything else."
    "And there was a lot of everything else. A hotel room that wasn't there. Mute clowns selling shares in people. A war over water, settled by a duck in a golden box."
    "Seven hundred people in costumes being kind to each other on purpose, for three days, for no reason anyone could name."
    "You sit on the bench and watch the light come over the hills. It's quiet up here. Somewhere below, a single kazoo plays one long note and stops."
    "Down in the parking lot, Tamsin is waving both arms at you, covered in balloons, shouting something you can't hear."
    tam "THERE you are!!! I looked for you for THREE DAYS. where WERE you"
    "Everywhere, you think. You were everywhere."
    tam "ok come down I saved you a balloon. it's the good one. it says 'you were never here'"
    scene black with slowfade
    "{i}On the drive home you realize you never once took out your phone, except as a flashlight. You don't miss a single thing you didn't photograph.{/i}"
    "{i}A card arrives a month later, no return address. It says: NEXT TIME.{/i}"
    "{i}You put it on the fridge. Every morning, you look at it, and it makes you braver in some small way you can't quite explain.{/i}"
    $ ending_name = "Checkout"
    jump ending_card


label ending_card:
    $ persistent.endings.add(ending_name)
    $ endings_found = len(persistent.endings)
    $ endings_total = len(ALL_ENDINGS)
    $ time_label = ""
    scene black
    show text "{size=40}{color=#ff5fb8}ENDING: [ending_name!u]{/color}{/size}\n\n{size=20}{color=#c8b8ff}Endings found: [endings_found] of [endings_total]{/color}{/size}" at truecenter as endcard with dissolve
    pause 4.0
    hide endcard with dissolve

    if endings_found < endings_total:
        "{i}Thanks for checking in. Everyone who enters is already checked in. Come back anytime. The guests will remember you, even if the game doesn't.{/i}"
    else:
        "{i}You've found every ending. Grandma Ozone is very proud of you. Have a strawberry candy.{/i}"
    return
