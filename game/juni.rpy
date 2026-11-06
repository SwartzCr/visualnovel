## juni.rpy — Juni, a person in a pink axolotl kigurumi. Pronouns: they/them.
## The hood stays up. Whether it comes down is the whole route.

label juni_pool_1:
    "At the edge of the pool, fully zipped into a pink axolotl kigurumi, someone is sitting with their onesie feet in the water. The bottom half of the onesie is soaked, but they do not seem to care."
    "The hood has its own little face on top, with two black eyes and a smile. Feathery gills fan out from either side. Under it, a real face, very pink, very warm."
    show juni neutral with dissolve
    j "Oh. Hi. Sorry. You're standing in my, um, sun. It's fine. I don't need the sun. I'm a cold-water creature."
    menu:
        j "...Did you want to sit?"

        "\"Aren't you dying in that thing?\"":
            j "Yes. Axolotls are native to cold lakes in Mexico City. I am, therefore, suffering."
            j "But without this I don't know who I am, so probably best to keep it on."

        "\"Does your axolotl have a name?\"":
            $ gain("juni", 2)
            j surprised "Nobody's ever asked her name."
            j happy "She's called Lotl. Lotl the axolotl. I'm aware that's not creative but AI wrote this part and I'm too lazy to change it."
            j "I'm Juni. She's Lotl. We're a package deal this weekend."

        "Sit down next to them and put your feet in the water too, without saying anything.":
            $ gain("juni", 1)
            j neutral "..."
            j happy "Oh, that's nice. Most people need to say something first."
            j "I'm Juni. You can just sit. That's allowed."

    show juni neutral
    "A little while later Juni is explaining that axolotls can regrow almost anything. Legs. Tails. Parts of their own hearts. Even bits of their brains."
    j "Out there, I work in databases. I'm the person who gets messaged at two in the morning because 'the thing is down.'"
    j "In here I'm a salamander. Salamanders don't have to be impressive. They just have to be wet and kind of cute."

    menu:
        "\"Which do you feel more comfortable as, Juni or Lotl?\"":
            j surprised "Oh. Um."
            "Juni pulls the hood strings a little tighter, like a reflex."
            j neutral "I'm not sure. I feel so free here, but this is the only place I can be Lotl ... right?"

        "\"If you could regrow anything, what would it be?\"":
            $ gain("juni", 2)
            "Juni goes quiet for a long time. You take the lull in the conversation to appreciate the music playing across the pool."
            j neutral "There used to be a part of me that sang in the car. Really loud. Badly. With the windows down."
            j "It fell off around year three of the job. I think I'd regrow that."
            j blush "Sorry. That was a lot for a poolside chat. With a stranger! Well you used to be a stranger..."

        "\"Being unimpressive sounds amazing. Can I be a salamander too?\"":
            $ gain("juni", 1)
            j happy "Applications are open. You'd need a suit. And to commit to being damp."
            j "Probationary salamander. I'll allow it."

        "\"Let me ask a question to Lotl.\"":
            $ gain("juni", -1)
            "You lean down and address the little face on top of the hood, very seriously."
            j surprised "Oh. Um. Lotl doesn't... she doesn't really talk to people she just met."
            j neutral "Sorry. I think I'm going to go dry off. Or, um, get wetter. Somewhere else."
            "Juni gets up, squelching, and pads away along the edge of the pool. The little face on the hood stares back at you the whole way."
            hide juni with dissolve
            return

    "Without warning, Juni slides off the edge into the pool, fully dressed. The kigurumi balloons up around them like a pink jellyfish."
    j happy "Ahhh. Regeneration."
    hide juni with dissolve
    "You smile inside. Maybe you're not so bad at making friends after all."
    return


label juni_pool_2:
    "Juni is floating face-up on an inflatable pizza slice, hood up, gills drooping in the heat. There's a second, smaller pizza slice tied to theirs by a string."
    show juni happy with dissolve
    j "You came back. I saved you a slice."
    "You climb onto the crust. You drift together toward the deep end, where the some clowns are pantomiming having phone sex."
    show juni neutral
    menu:
        j "So, what do you do? Like, out there."

        "\"Out there I'm someone else. In here I'm still figuring out who.\"":
            $ gain("juni", 2)
            j surprised "Oh."
            j blush "Yeah. I get that. I hope you figure it.. I hope I figure it out too."

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
    j "The second year I made it to the dance floor but was too shy to talk to anyone. This year I got stuck in the revolving door and Wren had to rescue me, and somehow that broke the seal. I've talked to like nine people."
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
            j neutral "Deal. I'm so worried that someone from work will see me here that I sometimes don't want to leave my room. Or well I used to be, talking about it now, maybe I finally don't care."
            "You tell them your embarrassing thing. Being walked in on, while having sex, dressed in full clown makeup. Juni laughs so hard the pizza slice spins in a slow circle."

        "\"Is it about the kigurumi?\"":
            "They sigh, and tell you: \"never mind, it wasn't important anyway.\""

    j happy "Okay. You know my secret now. That means you're responsible for me."
    "They say it like a joke. They don't let go of the string between your pizzas for the rest of the afternoon."
    hide juni with dissolve
    return


label juni_night_1:
    scene bg pettingzoo with dissolve
    "You follow the pink tail into a room that is full of stuffed animals. They're stacked in piles, people are lying across them in all sorts of poses. This room is the Heavy Petting Zoo, and it looks like people are taking the name as a mandate."
    "A man in a beige suit stands in the middle of the room, holding a clipboard. \"Ah, look at the zoo's newest acquisitions! And what kind of animals might you be!\""
    show juni happy at slightright with dissolve
    j "A Zoo!! I mean, I'm an axolotl! This is my friend who is a probationary salamander for the weekend."
    "The man in beige smiles."
    beige "Well welcome, please make yourselves comfortable ;)"
    show juni neutral at slightright

    menu:
        "Play along: \"I should get in character! What sounds do axolotls make??\"":
            $ gain("juni", 4)
            j "Try flicking your tongue and breathing at the same time."
            "You try, it's sort of goofy, and you think Juni just wanted to see you wag your tongue around."
            "Juni makes a tiny noise of pure joy inside the hood."
            j happy "That's great, yes that's perfect, keep doing that :)"

        "\"I don't even want to think about how gross these stuffed animals are\"":
            "The man in the beige suit rolls his eyes."
            beige "You should know better than to yuck someone else's yum. Besides, isn't it good to get a bit dirty every once in a while?"
            j neutral "I expected you to be a little more willing to play along, I guess you're not great at being in character. I guess I should have known."

        "Look over at Juni to see what they do.":
            $ gain("juni", 2)
            "Juni leans in and whispers."
            j neutral "I wish I was one of those stuffed animals. Just think about what they get to see .. to feel."
            "The man in beige nods, satisfied."

    "You lie down on a pile of Ikea sharks, their teeth wrap around your arms and legs. You just sit there loosely holding each other. It feels right, to be in a sea of stuffed animals, while holding a person sized stuffed animal."
    show juni happy at slightright
    beige "For your records."
    "The man in beige hands each of you a card, it's your animal certifications attesting that you're the zoo's best attraction."
    j "OMG! I'm keeping this forever. I'm going to frame it. Above my desk at work. Where nobody will understand."
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
            "You write it on one of the little cards and drop it in UNSENT TEXTS. You feel a weight lift from your shoulders."
            j surprised "Whoa. You just... let it go."
            "Juni picks up a card, writes something, and puts it in UNCLAIMED APOLOGIES without letting you see."
            j neutral "That was an apology I've been waiting for. From someone else. I'm done waiting. It can live here now."

        "An old nickname you never liked.":
            $ gain("juni", 1)
            j happy "Oh, good one."
            "Juni writes JUNEBUG on a card and drops it in OLD NICKNAMES with a tiny flourish."
            j "My manager calls me that. But here people call me what I want to be called."

        "A single left sock.":
            j surprised "Ummm okay. I think this room is supposed to be a bit more metaphorical, but I guess maybe someone will want your gross sock ...and now I have to smell your feet."

    "Then you both notice it. The bin labeled ONE (1) COURAGE, SLIGHTLY USED. There's only one card left in it."
    show juni neutral
    menu:
        j "There's only one. You should take it. You're braver than me."

        "Take it, and hand it straight to Juni.":
            $ gain("juni", 2)
            $ juni_has_courage = True
            j blush "Oh."
            "Juni holds the card to their chest like it's warm. The hood dips down so you can't see their face, but you think they might be starting to cry."
            j "Nobody's ever... okay. Okay. I'm going to use this. I don't know on what yet. But I'm going to."

        "\"Let's tear it in half. Half each.\"":
            $ gain("juni", 1)
            $ juni_has_courage = True
            j happy "Half a courage each. That's probably the right dose for a weekend."
            "You tear it carefully down the middle. Juni tucks their half into a hidden pocket in their kigurumi."

        "Take it. You could use it.":
            j neutral "Good. You'll use it better."
            "They sound like they mean it. They also sound a little like they wanted it."

    show juni neutral
    $ knows_juicero = True
    j "Hey. Juni's short for Juicero. I know it wasn't popular, but I loved it anyways, just like I hope people love me, even though I'm useless."
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
        j "Can I ask you something? Why do you keep finding me? There are like seven hundred people here."

        "\"Because you're the most honest person here, and I admire how you're living your full self. Plus you're bright pink and easy to spot.\"":
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
        j "I've been thinking about taking it off. The party's almost over, and I guess I feel like I should face real life, right?"

        "\"You can be whoever you want, especially around me. I accept you as who you are\"":
            $ gain("juni", 2)
            j blush "Okay."
            j "Okay. Thank you. That's... it's easier when nobody's asking for it."

        "\"I'd really like to see your face. Your real face.\"":
            $ gain("juni", 1)
            j blush "You're looking at it, here I'm an axolotl - that's the real me, and I like how you look at the real me."
            "Their sleeve stays on the zipper a long time. Then it drops."

        "\"Do it now! Come on!\"":
            $ gain("juni", -1)
            j surprised "Oh. Um. No. Not now. I'm not ready yet..."
            "Juni pulls the strings of their hood tight. The hood closes around their face like a flower at night."

    if rapport["juni"] >= ROMANCE_THRESHOLD:
        j blush "Hey. After the big event... find me? If you want. I'll be the pink one."
    else:
        j neutral "I should go find my roommate before the big event. See you around, okay?"
    hide juni with dissolve
    return


label juni_romance:
    scene bg pool with slowfade
    $ time_label = "Monday — 5:41 AM"
    "The ballroom is still going when you slip out. The hallways are full of people sitting against the walls in pairs, talking quietly, costumes folded into pillows."
    "You take the back stairs down to the ground floor. The pool is empty. All that's left is party detritus and used towels."
    "The water is perfectly still. Through the old glass roof, the sky over the mountains is just starting to turn gray."
    "And at the edge of the pool, exactly where you first saw them, there's a pink shape with its onesie feet in the water."
    show juni neutral with dissolve
    j "You came."
    j "I had a whole plan if you didn't come. It involved crying into the pool. Very damp. Very on-theme."
    "You sit down next to them and put your feet in. The water is cold enough to make you gasp. Juni laughs at you, a little, which seems fair."
    j "Cold-water creature. Told you."

    menu:
        j "So. How was your first time? Honestly."

        "\"I came here not knowing who I'd meet. Now I know a salamander.\"":
            j happy "A full salamander. You're promoted. It's on your permanent record."
        "\"Honestly? The best part was the pizza slices.\"" if pool_seen["juni"] >= 2:
            j happy "I knew you'd appreciate being a pizza topping. I couldn't stop thinking about how tasty you'd be."

    show juni neutral
    if night_seen["juni"] >= 1:
        "For a while you just talk. About the petting zoo, and the man in beige who might still be in there, observing the other animals."
    else:
        "For a while you just talk. About the weekend, the rooms, the people in capes, the clown who lost his voice and became a mime."
    if juni_has_courage:
        j "I keep thinking about the courage card from the Lost & Found. I carried it around all weekend in the hood. It's soggy now. I went in the pool twice with it."
        "They hold it up. The card is warped and soft now, the word COURAGE bleeding blue at the edges."
        j "I'm going to use it now. Is that okay?"
    else:
        j "There's a Lost & Found upstairs where you can take a card that says COURAGE. I never got one. I kept chickening out."
        j "So I'm going to try it without the card. Is that okay?"
    j "You can look away if you want. Actually, don't look away. Please don't look away."
    "Juni steps out of the water, a dripping mess. The kigurumi presses to their body, and in a way it feels right, like they've become one."
    show juni blush
    j "Hi. This is... the real me."
    j "It's really cold being so wet, but somehow it feels so right, and a bit hot actually."

    menu:
        "\"Hi, Juicero.\"" if knows_juicero:
            j happy "Oh no. Oh, that's so much worse than I thought. In a good way. In a terrible, good way."
            j blush "Nobody's said it like that before. Like it wasn't a joke. I'm going to have to give you a good squeeze as punishment."
        "\"Hi, Lotl. It's nice to meet all of you.\"":
            j happy "All of me. Yeah. This is who I am, and it's nice to be seen by someone who I feel really sees me."

    show juni blush
    "The sky above the glass roof goes from gray to pale pink. Somewhere upstairs, there's a party going on, but it's far from your mind."
    j "Three years I've been coming here. Three years I've been standing outside doors, waiting for someone to pull me in."
    j "And this year I spent the whole time hoping it'd be you. And it was. Every time. Even when I didn't wait."
    j "I don't know what happens Monday. I'll go back to fixing the thing. My manager will ping me at 3 am to fix a server. My phone is still in the ice bucket, by the way."
    j "But I think I want there to be a you on Monday. If that's... if you want that too."

    menu:
        "\"I want that too.\"":
            j blush "Okay. Okay. Good. Great. I'm going to be so normal about this."
        "Take their hand, sleeve and all.":
            "You find their hand inside the sleeve. It's warm and a little damp and holding on very tightly."
            j blush "...Yeah. That's an answer."

    j blush "Can I ask you something? I'm out of courage, so I'm just going to do it raw."
    j "Can I kiss you?"

    menu:
        "\"Yes.\"":
            "Juni leans over the water. They smell like chlorine and laundry and the tea bar's cardamom."
            "It's a small kiss, a careful one. The kind that asks again halfway through. You answer."
            if night_seen["juni"] >= 1:
                "You start petting, first lightly, then heavily, like you should have done in the art room upstairs."
                "Their body is slimy but good, you embrace, you gyrate, you realize that Juni has always wanted to do this with the suit on. Maybe you do too."
                "Juni asks you to do that thing with your tongue again, the one they taught you in the petting zoo. Juni tenses, shudders, and releases."
            "When you pull apart, Juni has their eyes shut tight, like they're making a wish."

    show juni happy
    j "Okay. Okay. I regenerated something. I'm pretty sure. I don't know what yet, but something grew back."

    scene bg pool with slowfade
    "The sun comes up over the mountains and pours down through the old glass roof, across the water, gold on every ripple."
    if knows_juicero:
        j "I guess I lived up to my name and gave you a good squeeze after all."
    scene black with slowfade
    "{i}Monday, 9:14 AM. A text from an unknown number.{/i}"
    j "hi it's juni. Lotl. it's me. I wore my costume to work for Halloween. No one made fun of me, and I felt authentic for the first time"
    j "are you free thursday. I know a place where we can be ourselves"
    $ chosen = "juni"
    $ ending_name = "Regeneration"
    jump ending_card


label juni_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show juni happy with dissolve
    "In the parking lot on Monday morning, a pink kigurumi waves at you from a dented hatchback. The hood is still up. Lotl looks a little sunburned."
    j "Hey! Probationary salamander! You passed. You're a full salamander now. It's binding. There's paperwork."
    j neutral "I wanted to say... thanks. For finding me. Every time. I talked to eleven people this year. Eleven. You were most of them."
    j "Next year I'm going to try going into a room by myself. Just one. A small one. Maybe the one with the moss."
    j happy "And if I chicken out, you're responsible for me. That's the rule. You know my secret."
    "They hug you through the onesie, which is like being hugged by a very determined pillow."
    j "Same time next year? I'll stand outside a door and you can pull me in."
    return


