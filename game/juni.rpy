## juni.rpy — Juni, a person in a pink axolotl kigurumi. Pronouns: they/them.
## The hood stays up. Whether it comes down is the whole route.

label juni_pool_1:
    "At the edge of the pool, fully zipped into a pink axolotl kigurumi, someone is sitting with their onesie feet in the water. The feet are soaked. They do not seem to care."
    "The hood has its own little face on top, with two black eyes and a smile. Feathery gills fan out from either side. Under it, a real face, very pink, very warm."
    show juni neutral with dissolve
    j "Oh. Hi. Sorry. You're standing in my, um, sun. It's fine. I don't need the sun. I'm a cold-water creature."
    menu:
        j "...Did you want to sit?"

        "\"Aren't you dying in that thing?\"":
            j "Yes. Axolotls are native to cold lakes in Mexico City. I am, therefore, suffering."
            j "It's fine. I'm used to it. The hood is load-bearing."

        "\"Does your axolotl have a name?\"":
            $ gain("juni", 2)
            j surprised "Nobody's ever asked her name."
            j happy "She's called Lotl. Lotl the axolotl. I'm aware that's not creative. She doesn't mind."
            j "I'm Juni. She's Lotl. We're a package deal this weekend."

        "Sit down next to them and put your feet in the water too, without saying anything.":
            $ gain("juni", 1)
            j neutral "..."
            j happy "Oh, that's nice. Most people need to say something first."
            j "I'm Juni. You can just sit. That's allowed."

    show juni neutral
    "A little while later Juni is explaining that axolotls can regrow almost anything. Legs. Tails. Parts of their own hearts. Even bits of their brains."
    j "Out there, I work in databases. I'm the person who gets messaged at two in the morning because 'the thing is down.' I'm the guy who fixes the thing."
    j "In here I'm a salamander. Salamanders don't have to be impressive. They just have to be wet and kind of cute."

    menu:
        "\"Do you ever take the hood off?\"":
            j surprised "Oh. Um."
            "Juni pulls the hood strings a little tighter, like a reflex."
            j neutral "Not yet. Maybe never. Maybe Sunday. I don't know. It's... a thing."

        "\"If you could regrow anything, what would it be?\"":
            $ gain("juni", 2)
            "Juni goes quiet for a long time. The Pool People's banner snaps in the wind."
            j neutral "There used to be a part of me that sang in the car. Really loud. Badly. With the windows down."
            j "It fell off around year three of the job. I think I'd regrow that."
            j blush "Sorry. That was a lot for a pool."

        "\"Being unimpressive sounds amazing. Can I be a salamander too?\"":
            $ gain("juni", 1)
            j happy "Applications are open. You'd need a hood. And to commit to being damp."
            j "Probationary salamander. I'll allow it."

    "Without warning, Juni slides off the edge into the pool, fully dressed. The kigurumi balloons up around them like a pink jellyfish."
    j happy "Ahhh. Regeneration."
    hide juni with dissolve
    "You decide that's the best thing you've seen all day."
    return


label juni_pool_2:
    "Juni is floating face-up on an inflatable pizza slice, hood up, gills drooping in the heat. There's a second, smaller pizza slice tied to theirs by a string."
    show juni happy with dissolve
    j "You came back. I saved you a slice. It's the crust one. Nobody wants the crust one, but it's very stable."
    "You climb onto the crust. You drift together toward the deep end, where the herald is shouting about pool noodles."
    show juni neutral
    menu:
        j "So, what do you do? Like, out there."

        "\"Out there I'm someone else. In here I'm still figuring out who.\"":
            $ gain("juni", 2)
            j surprised "Oh."
            j blush "Yeah. Exactly that. That's exactly it."

        "\"Honestly? I'd rather not talk about work this weekend.\"":
            $ gain("juni", 1)
            j happy "Oh thank god. Me neither. I put my work phone in a ziplock bag in the hotel ice bucket."
            j "It's an aquarium now. It's very calm in there."

        "Make something up: \"I'm a professional lighthouse.\"":
            $ gain("juni", 1)
            j happy "Hah! Is it hard? Being a lighthouse?"
            j "Actually don't answer. I want to imagine it. You just stand on a rock being helpful at boats."

    show juni neutral
    "Juni tells you this is their third year. Their roommate vouched for them the first time. That year they didn't leave their hotel room until Saturday."
    j "The second year I made it to the pool. This year I got stuck in the revolving door and Wren had to rescue me, and somehow that broke the seal. I've talked to like nine people."
    j "Ten. Ten with you."

    menu:
        j "Can I tell you something embarrassing?"

        "\"Always.\"":
            $ gain("juni", 2)
            j blush "I've been coming here three years and I've never once gone into an art room alone."
            j "I wait outside until somebody pulls me in. Like a cat at a door."
            j "I think I'm... sort of hoping it's you who pulls me in. This weekend. If that's not weird."

        "\"Only if I get to tell you one back.\"":
            $ gain("juni", 1)
            j neutral "Deal. I've never gone into an art room by myself. I wait outside until somebody pulls me in."
            "You tell them your embarrassing thing. Juni laughs so hard the pizza slice spins in a slow circle."

        "\"Is it about the hood?\"":
            j neutral "Everything is about the hood."
            "They sigh, and tell you anyway: three years, and they've never gone into an art room alone."

    j happy "Okay. You know my secret now. That means you're responsible for me."
    "They say it like a joke. They don't let go of the string between your pizzas for the rest of the afternoon."
    hide juni with dissolve
    return


label juni_night_1:
    scene bg room404 with dissolve
    "You follow the pink tail into a room that is blinding white. Error messages hang from the ceiling on fishing line. A giant sign on the wall reads 404 — ROOM NOT FOUND."
    "A man in a beige suit stands in the middle of the room, holding a clipboard, looking straight through you."
    show juni happy at slightright with dissolve
    j "Oh my god. Oh my god. It's a 404 room. This is for me specifically. Someone made this for me."
    beige "Please note: you are not in Room 404. There is no Room 404. You are not here."
    show juni neutral at slightright

    menu:
        "Play along: \"Sorry. I'm also not here.\"":
            $ gain("juni", 2)
            beige "Thank you. Most people argue."
            "Juni makes a tiny noise of pure joy inside the hood."
            j happy "I'm not here either! Lotl's not here! None of us exist!"

        "\"I mean... it's right here, though?\"":
            beige "Literalism detected."
            "He hands you a small laminated card. It says ERROR: TOOK IT TOO SERIOUSLY."
            j neutral "Oof. You have to keep that."

        "Look over at Juni to see what they do.":
            $ gain("juni", 1)
            "Juni leans in and whispers."
            j neutral "Pretend you're a missing file. Just like... look a little corrupted."
            "You do your best. The man in beige nods, satisfied."

    "A dialog box pops up on an old monitor in front of Juni. It says: ARE YOU SURE YOU WANT TO BE HERE? There are two buttons. YES. ALSO YES."
    show juni surprised at slightright
    menu:
        j "Which one do I press? It feels like a trick. It's always a trick."

        "\"Press YES. I'll press ALSO YES. We'll both be sure.\"":
            $ gain("juni", 2)
            "You press your buttons at the same time. The monitor plays a tinny little fanfare. Confetti made of hole-punched paper falls from the ceiling."
            j happy "We're both sure! That's the most sure I've been about anything in months."

        "\"There's no wrong answer. That's the trick.\"":
            $ gain("juni", 1)
            j neutral "...Huh. Yeah. Okay."
            "Juni presses ALSO YES. Paper confetti falls from the ceiling."

        "\"Neither. Let's go find a room that actually exists.\"":
            j neutral "Oh. Right. Yeah, sure."
            "Juni presses nothing. The dialog box waits patiently. You feel like you've made it sad."

    show juni happy at slightright
    beige "For your records."
    "The man in beige hands each of you a card: THIS CERTIFIES THAT THE BEARER WAS NEVER HERE."
    j "I'm keeping this forever. I'm going to frame it. Above my desk. At work. Where nobody will understand."
    hide juni with dissolve
    return


label juni_night_2:
    scene bg lostfound with dissolve
    "The Lost & Found is lit like an old library. Bins line the shelves, each one labeled in careful handwriting: MISPLACED CONFIDENCE. UNCLAIMED APOLOGIES. SPARE EXCUSES. OLD NICKNAMES."
    "A sign on the counter says: TAKE ONE. LEAVE ONE."
    show juni neutral with dissolve
    j "I've been standing here for twenty minutes. I can't decide what to leave. Everything I own feels load-bearing."
    j "You go first. Show me how it's done."

    menu:
        "What do you leave?"

        "An unsent text you've been carrying around for a year.":
            $ gain("juni", 2)
            "You write it on one of the little cards and drop it in UNSENT TEXTS. It's lighter than you expected."
            j surprised "Whoa. You just... let it go."
            "Juni picks up a card, writes something, and puts it in UNCLAIMED APOLOGIES without letting you see."
            j neutral "That was an apology I've been waiting for. From someone else. I'm done waiting. It can live here now."

        "An old nickname you never liked.":
            $ gain("juni", 1)
            j happy "Oh, good one."
            "Juni writes JUNEBUG on a card and drops it in OLD NICKNAMES with a tiny flourish."
            j "My manager calls me that. Not anymore. Not in here."

        "A single left sock.":
            $ gain("juni", 1)
            j happy "Ha! The classic. Left socks are always the ones that get lost. Science can't explain it."

    "Then you both notice it. The bin labeled ONE (1) COURAGE, SLIGHTLY USED. There's only one card left in it."
    show juni neutral
    menu:
        j "There's only one. You should take it. You're braver than me."

        "Take it, and hand it straight to Juni.":
            $ gain("juni", 2)
            j blush "Oh."
            "Juni holds the card in both sleeves like it's warm. The hood dips down so you can't see their face."
            j "Nobody's ever... okay. Okay. I'm going to use this. I don't know on what yet. But I'm going to."

        "\"Let's tear it in half. Half each.\"":
            $ gain("juni", 1)
            j happy "Half a courage each. That's probably the right dose for a weekend."
            "You tear it carefully down the middle. Juni tucks their half into the hood."

        "Take it. You could use it.":
            j neutral "Good. You'll use it better."
            "They sound like they mean it. They also sound a little like they wanted it."

    show juni neutral
    j "Hey. Juni's short for Juniper. Nobody calls me Juniper. My mom, when I'm in trouble."
    j happy "You can know that. You don't have to use it. I just wanted somebody here to know."
    hide juni with dissolve
    return


label juni_night_3:
    scene bg regen with dissolve
    "The Regeneration Tank is a hotel suite painted the deep blue of a lake bottom. Light ripples across the walls. A huge waterbed fills the middle of the room. A sign says: LIE DOWN. GROW SOMETHING BACK."
    show juni neutral with dissolve
    j "You came in with me. I didn't even have to stand outside."
    "You lie down on the waterbed side by side. It sloshes. The kigurumi squeaks. Juni's gills are fanned out on the pillow like a halo."
    j "This is the last night. I feel like I should say something important and I don't know what it is."

    menu:
        j "Can I ask you something? Why do you keep finding me? There are seven hundred people here."

        "\"Because you're the most honest person here, and you're dressed as a salamander.\"":
            $ gain("juni", 2)
            j happy "Hah. That's... okay, that's the nicest thing anyone's said to me in a long time."

        "\"I don't know. I just like being near you.\"":
            $ gain("juni", 2)
            j blush "Oh."
            j "Me too. Near you, I mean. Not near me. I'm always near me. You know what I mean."

        "\"Coincidence, probably.\"":
            j neutral "Oh. Right. Yeah."
            "The waterbed sloshes. The ripples on the ceiling keep moving."

    "Juni's sleeve drifts up toward the hood strings. It hovers there."
    show juni neutral
    menu:
        j "I've been thinking about taking it down. The hood. Not right now. But... soon. Would that be weird?"

        "\"Whenever you want. Or never. Both are good.\"":
            $ gain("juni", 2)
            j blush "Okay."
            j "Okay. Thank you. That's... it's easier when nobody's waiting for it."

        "\"I'd really like to see your face. Your whole face.\"":
            $ gain("juni", 1)
            j neutral "...Soon. I think. Maybe."
            "Their sleeve stays on the strings a long time. Then it drops."

        "\"Do it now! Come on!\"":
            $ gain("juni", -1)
            j surprised "Oh. Um. No. Not now."
            "Juni pulls the strings tight. The hood closes around their face like a flower at night."

    if rapport["juni"] >= ROMANCE_THRESHOLD:
        j blush "Hey. After the ark... find me? If you want. I'll be the pink one."
    else:
        j neutral "I should go find my roommate before the ark. See you around, okay?"
    hide juni with dissolve
    return


label juni_romance:
    scene bg pool with slowfade
    $ time_label = "Monday — 5:58 AM"
    "You find Juni at the pool, an hour before dawn. Everyone else has gone to bed or to the ballroom. The water is perfectly still. The sky over the hills is just starting to turn gray."
    show juni neutral with dissolve
    j "You came. I had a whole plan if you didn't come. It involved crying into the pool. Very damp."
    "They're sitting at the edge where you first met them, onesie feet in the water. They're holding the half of a card that says COURAGE."
    j "I'm going to use it now. Is that okay? You can look away if you want. Actually, don't look away. Don't look away."
    "Juni reaches up with both sleeves and pulls the hood strings loose. Then, slowly, they push the hood back."
    "Lotl falls down their back, gills and all. Underneath is short dark hair stuck flat with sweat, and ears you've never seen, and a face that's all the way there for the first time all weekend."
    show juni blush
    j "Hi. This is... the rest of me."
    j "It's really cold out here without it. Huh. I forgot what air felt like."

    menu:
        "\"Hi, Juniper.\"":
            j happy "Oh no. Oh, that's so much worse than I thought. In a good way. In a terrible, good way."

        "\"Hi, Juni. It's nice to meet all of you.\"":
            j happy "All of me. Yeah. That's everyone. That's the whole cast."

    show juni blush
    j "Can I... I want to ask you something and I've already used up my courage card, so I'm just going to do it raw."
    j "Can I kiss you?"

    menu:
        "\"Yes.\"":
            "Juni leans over the water. They smell like chlorine and laundry and the tea bar's cardamom."
            "It's a small kiss, a careful one. The kind that asks again halfway through. You answer."

        "\"Can I hold your hand first?\"":
            j happy "Yes. Yes, please. Sleeve's empty, it's just a hand in there."
            "Their hand finds yours inside the sleeve. Warm and a little damp. After a while it's the most natural thing in the world to lean in, and so you both do."

    scene bg pool with slowfade
    "The sun comes up over the Hotel Mar Sol. Juni's hood floats behind them in the pool, gills spread out on the water, smiling up at the sky."
    "Neither of you goes to fish it out."
    scene black with slowfade
    "{i}Monday, 9:14 AM. A text from an unknown number.{/i}"
    j "hi it's juni. juniper. it's me. I sang in the car the whole way home. windows down. it was so bad. are you free thursday"
    $ chosen = "juni"
    $ ending_name = "Regeneration"
    jump ending_card


label juni_friend:
    scene bg exterior with slowfade
    show juni happy with dissolve
    "In the parking lot on Monday morning, a pink kigurumi waves at you from a dented hatchback."
    j "Hey! Probationary salamander! You passed. You're a full salamander now."
    j "Same time next year? I'll stand outside a room and you can pull me in."
    return
