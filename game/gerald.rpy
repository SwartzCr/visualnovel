## gerald.rpy — Gerald, a Sasquatch. Pronouns: he/him.
## Nobody has ever seen him out of the suit. Nobody is sure there is a suit.

label gerald_pool_1:
    "In the shallow end, a seven-foot Sasquatch is sitting in a children's innertube shaped like a duck. He holds a white teacup above the water with enormous delicacy."
    show gerald neutral with dissolve
    g "Good afternoon. Forgive me if I don't stand. I am buoyant at present, and it took some time to achieve."
    g "Gerald. A pleasure."
    menu:
        "\"Is that a real Sasquatch?\"":
            g "Is that a real person?"
            "You open your mouth to answer."
            g "Ah, ah. I find it's best not to ask. Things get so much smaller once you've asked."

        "\"Want me to hold your tea so you can actually swim?\"":
            $ gain("gerald", 2)
            g surprised "Oh. Oh, would you?"
            "You take the cup. It's still hot. It smells like smoke and pine."
            g happy "Lapsang souchong. Thank you. I have been holding that cup at shoulder height for forty minutes."
            "Gerald sinks gratefully into the water up to his chin. The fur fans out around him like seaweed."

        "\"How's the water?\"":
            $ gain("gerald", 1)
            g neutral "Wet. Chlorinated. There are a great many people's feelings in it. It's quite pleasant once you stop thinking about that."

    show gerald neutral
    "Gerald explains, at length, that chlorine is hell on fur. It takes forty years to get a coat like this. He's mostly here for the company."
    g "You'll have seen the famous film, I suppose. 1967. The one where my kind walks across the creek bed and looks back over his shoulder."
    g "That was my cousin Bernard. Bad knee. That's why he walks like that. He has been embarrassed about it for sixty years."
    g "Everyone at home has a story like that. A camera in the woods. A flash. A blur. And then a hundred years of people arguing over whether you're real."
    g "Here, nobody takes pictures. You can't imagine what that means to someone like me."

    menu:
        "\"I won't take your picture. Not this weekend, not ever. I promise.\"":
            $ gain("gerald", 2)
            g happy "I believe you."
            g "That's rarer than you'd think. Most people promise with their phone already in their hand."

        "\"Do you ever get lonely? Being a legend?\"":
            $ gain("gerald", 1)
            "Gerald is quiet for a while. A pool noodle drifts past."
            g neutral "Legends are always lonely. That's what makes them legends. Nobody throws a legend a birthday party."

        "\"You could make a fortune on YouTube, you know.\"":
            g neutral "Yes. So I'm told. By everyone. Constantly."
            "He sinks a little lower in the water."

    hide gerald with dissolve
    "When you leave, Gerald raises his teacup to you in salute. Not one drop spills."
    return


label gerald_pool_2:
    "On the pool deck, a dozen people lie flat on beach towels with their eyes closed. Gerald walks slowly between them, speaking in a voice like a cello."
    show gerald neutral with dissolve
    g "You are moss. You have been moss for a thousand years. Nothing is required of moss. Moss does not check its email."
    g happy "Ah. You. There's a towel free. Would you care to be moss?"
    "You lie down. The concrete is warm through the towel. Gerald stands over you like weather."
    show gerald neutral
    menu:
        g "And what kind of moss are you today?"

        "\"Reindeer moss. Soft, but I can survive pretty much anything.\"":
            $ gain("gerald", 2)
            g happy "Cladonia rangiferina. Excellent choice. Technically a lichen, but we don't police that here."
            g "Soft and survives anything. Yes. I can see that in you."

        "\"Just regular green moss. Doing my best.\"":
            $ gain("gerald", 1)
            g neutral "Regular green moss is the backbone of the forest. Never let anyone tell you otherwise."

        "\"I don't think I'm a moss person.\"":
            g neutral "Everyone is a moss person given enough time. Lie there a while longer."

    show gerald neutral
    "After the session, Gerald sits down beside you. The deck creaks."
    g "I live up north, in the Klamath. Old growth. Trees so tall the light goes green by the time it reaches you."
    g "It's been getting quieter there. Fewer of us every decade. Some moved to Canada. Some just stopped coming to the creek."
    g "I came here the first time because a friend said there'd be seven hundred people pretending to be strange creatures."
    g "It's the closest thing I've had to a family reunion in thirty years."

    menu:
        "\"Then I'm really glad you came. I'm glad I met you.\"":
            $ gain("gerald", 2)
            g happy "..."
            g "So am I. Very much."
            "He pats your shoulder once, very gently. His hand covers most of your back."

        "\"Do you have family, back home?\"":
            $ gain("gerald", 1)
            g neutral "A sister. Margaret. She does not believe in parties. She believes in roots, and grudges, and the creek."
            g happy "I'll tell her about you. She'll pretend not to care."

        "\"That's kind of sad, honestly.\"":
            g neutral "Yes. It is. But sad and good can sit at the same table. They often do."

    hide gerald with dissolve
    return


label gerald_night_1:
    scene bg breakfast with dissolve
    "You follow the commotion into a room transformed into a cathedral of breakfast. On one wall: the black banner of the CHURCH OF CAST IRON. On the other: the white banner of the TEMPLE OF TEFLON."
    "On the altar between them sits the Holy Skillet, a single fried egg glowing in it under a spotlight."
    "In the middle of all this, Gerald is being pulled in two directions by two people in liturgical robes."
    show gerald surprised with dissolve
    priest "The Great Hairy One has always been ours! He cooks on hot stones! Stones are the original cast iron!"
    priestess "Blasphemy! Look at him! Nothing sticks to him! He is the living embodiment of the nonstick way!"
    g "I really must protest. A great deal sticks to me. Burrs. Leaves. Small birds, occasionally."

    menu:
        "Step in: \"He's with me. We're Waffle-Iron Independents.\"":
            $ gain("gerald", 2)
            "Both clergy gasp. A heretic! A third way!"
            priest "Waffle iron... is that... is that allowed?"
            g happy "It is now. I'm its prophet. And this is my acolyte."

        "\"Gerald, what do {i}you{/i} actually cook eggs in?\"":
            $ gain("gerald", 1)
            g neutral "...A flat rock. Heated by the sun. On a good day."
            "Both cults fall silent. Somewhere in the back, someone whispers {i}the Church of the Rock{/i}, and a third religion is born."

        "Kneel before the Church of Cast Iron.":
            priest "A convert! Seize the Great Hairy One while the Teflons are distracted!"
            "Instead, the Teflons seize Gerald. It takes you ten minutes and a lot of apologizing to get him back."
            g neutral "That was... an experience."

    show gerald neutral
    "The clergy circle back. They aren't done."
    priestess "Then let the Great Hairy One's companion decide! Cast iron or Teflon? The schism must be resolved!"
    menu:
        g "I'm afraid they won't let either of us leave until someone chooses."

        "\"Why not both? Cast iron for steak. Nonstick for eggs.\"":
            $ gain("gerald", 2)
            "The room goes silent. The High Priestess of Teflon drops her spatula. The Deacon of Cast Iron begins to weep."
            priest "It was... both... all along..."
            "They embrace across the altar. Their congregations follow. Gerald leans down to you."
            g happy "Do you know, I think that's the wisest thing anyone has said all weekend."

        "\"Can I grab your hand? We're running.\"":
            $ gain("gerald", 1)
            g happy "Please."
            "You run out of the cathedral hand in enormous hand. The cults chase you for half a hallway before they get distracted by a tray of waffles."

        "\"Teflon. Obviously.\"":
            "The Church of Cast Iron howls. A pancake is thrown. A small and largely theatrical riot breaks out."
            g neutral "Well. We tried."

    hide gerald with dissolve
    return


label gerald_night_2:
    scene bg hallway with dissolve
    "Gerald is standing in front of Room 312, not going in. Rain sounds and the smell of cedar drift out through the door."
    show gerald neutral with dissolve
    g "It smells like home in there. Someone's built a whole forest. Moss and fog and creek sounds."
    g "I'm afraid that if I go in, I'll miss it too much to come back out."
    menu:
        "\"We can go in together. And we can leave the second you want to.\"":
            $ gain("gerald", 2)
            g happy "...All right. Yes. Together."

        "\"Then let's stay out here. We can listen from the doorway.\"":
            $ gain("gerald", 1)
            "You stand in the doorway with him for a long while. Eventually he takes one step in, and then another."

        "\"It's just a hotel room with moss in it, Gerald.\"":
            g neutral "Yes. Of course. You're right."
            "He goes in anyway. You're not sure if you helped."

    scene bg forest with dissolve
    show gerald neutral with dissolve
    "Inside, the carpet is moss, real moss, cool and damp under your shoes. Fog rolls across the floor. Fireflies, or something like them, blink in the dark between painted trees."
    "Gerald lies down on what used to be the hotel bed. It's covered in moss too. He fits, barely."
    g "There's a creek near my place that sounds just like this. In September, when the salmon come back."
    g "Would you sit with me? Not talk. Just be here. I find it's hard to be quiet with people. Most people want me to do something."

    menu:
        "Sit beside him in silence.":
            $ gain("gerald", 2)
            $ sat_with_gerald = True
            "You sit. The creek sounds go on. A firefly lands on Gerald's arm and stays there."
            "..."
            "..."
            "After a long time, Gerald lets out a breath so deep the fog moves."
            g happy "Thank you. I didn't know how much I needed that."

        "Hum softly, something without words.":
            $ gain("gerald", 1)
            "Gerald closes his eyes. After a minute, he hums along, an octave below you, so low you feel it in the bed frame."

        "\"So what's the actual difference between Bigfoot and Sasquatch?\"":
            g neutral "...Marketing."
            "He chuckles. It's a nice chuckle. But the quiet is gone."

    hide gerald with dissolve
    return


label gerald_night_3:
    scene bg cryptid with dissolve
    "CRYPTIDS ANONYMOUS, says the banner. Below it: you are not blurry here."
    "A circle of folding chairs. An inflatable Loch Ness Monster with a HELLO MY NAME IS sticker. The facilitator is a person in a Mothman costume with glowing red eyes, holding a styrofoam cup of coffee."
    show gerald neutral with dissolve
    "Gerald is sitting in one of the folding chairs. It's comically too small. His knees are up around his shoulders. He waves you over."
    moth "Welcome, welcome. Is there anyone who'd like to share tonight?"
    "Gerald's hand goes up halfway, then down again."
    g neutral "I... would you stay close? I've come to this meeting for four years and I have never once shared."
    "He stands. The chair stands with him for a second before falling off."
    g "My name is Gerald. And I have been... blurry. For about sixty years."
    moth "Hi, Gerald."
    "Gerald stops. He looks at the floor. The room waits."

    menu:
        "Quietly: \"Can I put my hand on your shoulder?\"":
            $ gain("gerald", 2)
            g neutral "Yes. Please."
            "You reach up. You have to reach quite a long way. His fur is warm."

        "\"Take your time. We're not going anywhere.\"":
            $ gain("gerald", 1)
            "The circle murmurs agreement. Nessie bobs gently in the air conditioning."

        "Start clapping to encourage him.":
            moth "Ah, we snap here, friend. Clapping is very loud for some of the members."
            "Everyone snaps instead. Gerald gives you a small, forgiving look."

    show gerald neutral
    g "Everyone wants proof of me. Footprints. Hair samples. A clearer photo. They've been chasing proof of me my whole life."
    g "Nobody has ever just... wanted me. Not the evidence. Me."
    g "That's all. That's my share."
    "The circle snaps for a very long time. The Mothman wipes his eyes under the mask. Then he turns to you."
    moth "And you, friend of Gerald? What are you not blurry about tonight?"

    menu:
        "\"I'm not blurry about Gerald. He's the realest person I've met all weekend.\"":
            $ gain("gerald", 2)
            $ vouched_for_gerald = True
            g blush "..."
            "Gerald doesn't say anything. But he sits back down, carefully, very close to you."

        "\"I came here not knowing who I'd be. I think I'm finding out.\"":
            $ gain("gerald", 1)
            moth "That's the whole thing, isn't it. Thank you."
            g happy "Well said."

        "\"Honestly? I'm just here for the coffee.\"":
            "The room laughs. Gerald laughs too, a big rolling laugh that knocks Nessie off her stand."
            g happy "The coffee is genuinely excellent here. You're not wrong."

    if rapport["gerald"] >= ROMANCE_THRESHOLD:
        g blush "After the ark, I'll be on the roof. It's the only place tall enough for me to see the sunrise properly. If you'd like to see it too."
    else:
        g neutral "Enjoy the ark. Don't let them get you in the eye with the confetti. It's biodegradable but it is relentless."
    hide gerald with dissolve
    return


label gerald_romance:
    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 5:52 AM"
    "The stairwell to the roof is propped open with a waffle iron. Someone from the Breakfast Schism has left it there, as a blessing or a warning."
    "At the top, the air is cold and smells like eucalyptus. The string lights have mostly burned out. The rigging that held the ark hangs slack."
    "Gerald is sitting on the edge by the water tank, enormous against the pink sky, holding two teacups. One of them is for you. It's still warm."
    show gerald happy with dissolve
    g "You came. I had a speech prepared in case you didn't. It was very dignified. Lots of nature metaphors. A bit about a fallen log."
    g neutral "I'm glad I don't need it. It was mostly about the log."
    "You sit beside him. The bench creaks under his weight and then, with a kind of resignation, holds."
    g "Lapsang souchong. I brought my own leaves. The tea bar means well, but they keep putting cardamom in everything."

    menu:
        g "Did you enjoy the ark? I confess I wept. A great deal. I had to borrow a towel from Wren."

        "\"I cried too. Over a rubber duck.\"":
            g happy "Over a rubber duck. Yes. Seven hundred people. One duck. It was the most profound thing I've seen in decades."
        "\"I mostly watched you crying.\"":
            g blush "Oh dear. Was it very loud? I'm told I sound like a foghorn when I'm moved."
            g happy "...It was a beautiful duck, though."

    show gerald neutral
    "For a while you just watch the light come up. A bird starts somewhere down in the eucalyptus, then another one."
    if sat_with_gerald:
        g "When we were in the forest room, you sat with me without saying anything. Do you remember? For a long time."
        g "I haven't done that with anyone since I was young. Just sat. It's the hardest thing to find, a person who'll just sit."
    else:
        g "Do you know what I'll remember from this weekend? Not the rooms. Not even the ark. The quiet bits in between, with you."
        g "It's the hardest thing to find, a person who'll just sit."
    if vouched_for_gerald:
        g "And at the meeting. When the Mothman asked. What you said about me."
        g blush "I've thought of very little else, if I'm honest."

    show gerald neutral
    g "I go home tomorrow. Back to the creek. My sister Margaret will ask where I've been and I'll say {i}nowhere{/i}, which is what we always say."
    g "That's how it is with my kind. We are always coming from nowhere and going nowhere, so nobody can follow us there."
    g blush "But I'd like to say {i}somewhere{/i} this time. I'd like there to be a somewhere. And a someone in it."

    menu:
        "\"There is. I'm right here.\"":
            g blush "Yes. You are. You're entirely in focus."
        "Lean against his side.":
            "Gerald goes very still, the way you'd go still if a deer walked up to you. Then, slowly, an arm the size of a tree branch settles around your shoulders."
            g blush "Oh. Oh, that's... yes. That's very good. Let's stay exactly like this."

    show gerald neutral
    "The sun touches the top of the hills. Everything turns gold: the gravel, the water tank, the fur on Gerald's arm."
    g "May I tell you something about the famous film? Not Bernard's. Mine."
    g "There's a hiker in Oregon, 1994, who got a picture of me by a river. Blurry, naturally. She sold it to a magazine. It's still in a museum somewhere, labeled HOAX."
    g "I was crying in that picture. I'd just lost someone. And for thirty years I've been a hoax who was crying."
    g happy "This weekend I've just been Gerald. Nobody wanted proof. You least of all."

    menu:
        "\"You were never a hoax.\"":
            g blush "...Thank you. I may need to hear that several more times. Over a number of years."
        "\"I'd still like to know you better than any photo.\"":
            g blush "Then you'll have to come to the creek. The salmon come back in September. It's very loud and very smelly and I think you'd love it."

    if pool_seen["gerald"] >= 2:
        g blush "May I ask you something very forward? I've been thinking about it since the moss."
    else:
        g blush "May I ask you something very forward? I've been thinking about it all weekend."
    g "May I kiss you? I'll understand completely if the logistics seem... daunting."

    menu:
        "\"Yes. I'll meet you halfway.\"":
            "He bends down. You stretch up. It takes some engineering, and at one point a teacup goes over the edge of the roof."
            "It's worth it. His fur smells like cedar smoke and pool water. He kisses like he's afraid you're a mirage, very gently, ready to stop."
            "You don't let him stop."
        "Stand up on the bench so you're eye to eye.":
            g happy "Oh, that's clever. That's very clever."
            "Eye to eye, he's suddenly shy. You close the distance. He kisses you so gently you could almost think you imagined it, except you know you didn't."

    show gerald happy
    g "Well. I'm going to have to tell Margaret {i}something{/i} now."

    scene bg roof_dawn with slowfade
    "The sun clears the hills. Down in the parking lot, somebody with a camera looks up at the roof, squints, and sees only a blur."
    "Gerald laughs so hard the water tank rings like a bell."
    "You stay up there until the last cars leave, until the Pool People fold their banner, until Wren comes up to tell you the hotel is technically closed and has been since 1987."
    scene black with slowfade
    "{i}Three weeks later, a package arrives with no return address. Inside: a tin of lapsang souchong, a pressed fern, a smooth gray stone from a creek, and a postcard of the Klamath.{/i}"
    "{i}On the back, in very careful handwriting:{/i}"
    g "The salmon are back. Margaret says to bring a raincoat and that she doesn't care either way if you come. She has cleaned the whole cabin twice. — G."
    g "P.S. The stone is for your pocket. Ours are full of them. It's how we remember where we've been."
    $ chosen = "gerald"
    $ ending_name = "Not Blurry"
    jump ending_card


label gerald_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show gerald happy with dissolve
    "As the cars pull out on Monday morning, you find Gerald at the edge of the parking lot, packing an absurdly small suitcase."
    g "Ah. My friend. I hoped I'd see you before the road."
    g neutral "I've been coming to these for years and I usually leave the way I came. Quietly. From nowhere, to nowhere."
    g happy "This time I'm leaving with a friend. It's a very strange feeling. Like having a pocket full of warm stones."
    "He presses a teabag into your hand. Lapsang souchong. It smells like a campfire in the rain."
    g "If you're ever up north, follow the creek. Don't bring a camera. Just call my name. I'll hear."
    "He walks up the road toward the hills, a teacup in one hand. At the top he turns and waves, once, over his shoulder."
    "It looks exactly like the famous film. Except it isn't blurry at all."
    return


