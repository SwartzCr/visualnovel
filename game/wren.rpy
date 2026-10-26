## wren.rpy — Wren, crew, dressed in black. Pronouns: she/her.
## She builds the party every year and never gets to be at it. The route is about
## helping her steal a few minutes without ever asking her to drop the job.

label wren_pool_1:
    "A person in head-to-toe black is standing at the edge of the deep end with a long pool net, trying to fish out a disco ball the size of a beach ball. It keeps rolling off the net."
    show wren neutral with dissolve
    w "Come on. Come on. You were installed in a ballroom. You were not installed in a pool. Who did this. Why would you do this."
    "It's Wren, from check-in. Sweat is running down from under her headset."

    menu:
        "Grab the other net from the fence and help.":
            $ gain("wren", 2)
            "You work it from the opposite side. It takes three tries, a lot of teamwork, and one undignified lunge, but the disco ball comes out of the water dripping and spinning."
            w happy "Yes! YES. Okay. That's the most satisfying thing that's happened to me since Thursday."
            w neutral "Thank you. Seriously. You didn't have to."

        "\"Need a hand?\"":
            $ gain("wren", 1)
            w neutral "...Yes. God. Yes."
            "Between the two of you, the disco ball eventually surrenders."

        "\"Isn't that someone else's job?\"":
            w neutral "Everything here is someone else's job until it's mine."
            "She gets it out on the seventh try, alone."

    show wren neutral
    "She sits down on the edge of a lounger with the wet disco ball in her lap, like a cat that's been rescued from a tree."
    w "Six years I've been crew. First year I came as a guest. Had a bad night. Really bad. Lost my friends, lost my shoes, lost the plot."
    w "Somebody dressed in black sat with me for four hours in a stairwell. Never got their name. Never saw them again."
    w "So now I'm the somebody in black."

    menu:
        "\"Do you ever get to just... be at the party?\"":
            $ gain("wren", 2)
            w surprised "Ha."
            w neutral "Sometimes. For about six minutes at a time. Between cues."
            w "Nobody's asked me that in a long time. People mostly ask me where the bathroom is."

        "\"That's a really beautiful reason.\"":
            $ gain("wren", 1)
            w blush "It's... yeah. Thanks. Don't tell anyone, I have a reputation for being dead inside."

        "\"Sounds like a lot of unpaid labor.\"":
            w neutral "It's volunteering. It's different."
            w "...It's a little bit unpaid labor."

    walkie "Wren, someone's put the inflatable flamingo in the ice machine."
    w neutral "Copy. Of course they have."
    hide wren with dissolve
    return


label wren_pool_2:
    "Behind the towel hut, out of sight of the pool, Wren is sitting on an upturned bucket eating a sandwich. It's a very sad sandwich. It's mostly bread."
    show wren surprised with dissolve
    w "Oh. Hi. You found my secret place. I have a fifteen-minute break. I've had it for six minutes. I've spent four of them answering the radio."

    menu:
        "Offer her half of the fancy pastry you grabbed from the tea bar.":
            $ gain("wren", 2)
            $ shared_bun = True
            w surprised "Is that the cardamom bun? There are only twelve of those. I've never gotten one. Not in six years."
            w happy "Oh my god. Oh my god, it's so good. I'm going to cry. I'm not going to cry. I'm crew."

        "Sit down on the ground next to her and say nothing.":
            $ gain("wren", 1)
            "You sit. She eats her sad sandwich. The pool noises go on around the corner."
            w neutral "This is nice. Nobody needs anything from me right now. It's like being underwater."

        "\"Want me to leave so you can actually have your break?\"":
            $ gain("wren", 1)
            w neutral "No. Stay. Actually, stay."
            w "It's nice to talk to someone who isn't lost."

    show wren neutral
    "She turns the walkie down to its lowest setting. You can tell it costs her something."
    w "I'm calling the 11:11 cue tomorrow. The ark. Seven hundred people in a room in the dark, and if I'm late by two seconds the whole thing falls apart."
    w "Last year the fog machine caught on fire. Small fire. Supportive fire. But still."

    menu:
        "\"It'll go fine. And if it doesn't, it'll be a better story.\"":
            $ gain("wren", 2)
            w happy "Ha. Okay. Yeah. The fire was a really good story, honestly."
            w neutral "Thank you. I needed somebody to say that, and I've been saying it to everyone else."

        "\"Can I help? Running errands, carrying stuff, anything?\"":
            $ gain("wren", 1)
            w neutral "Guests aren't supposed to work. But I'll... keep that in mind. Seriously."

        "\"You should let someone else handle it.\"":
            w neutral "There isn't someone else. That's the whole job."

    walkie "Wren, the herald's lost his voice. He's miming the proclamations. Nobody understands them."
    w neutral "Copy."
    w happy "Thanks for the break. That was the best four minutes of my weekend."
    hide wren with dissolve
    return


label wren_night_1:
    scene bg hallway with dissolve
    show wren neutral with dissolve
    "Wren is half-carrying a man in plaid pajamas down the hallway. He's not hurt. He just looks like the party got bigger than his head."
    w "Oh, good, it's you. Can you get his other side? We're going to Grandma Ozone's."

    scene bg livingroom with dissolve
    show wren neutral at slightright with dissolve
    "The living room is warm and close and smells like cardamom and old books. Grandma Ozone is rocking in her chair, humming, handing out strawberry candies."
    oz "Bring him here, sweetheart. Sit him on the big cushion. There we go."
    w "I'm going to get him some tea. Can you sit with him for two minutes? Two minutes. I'll be right back."
    hide wren with dissolve
    pj "Everything's so loud. Everything's so... everything. There was a vampire. In a coffin. He winked at me."

    menu:
        "Sit down next to him and ask him what he's seeing.":
            $ gain("wren", 2)
            "He tells you about the vampire, and the nurses, and a clown who sold him a share of the moon. Halfway through, he starts laughing."
            pj "It's actually really funny, isn't it. When you say it out loud."
            "When Wren comes back with the tea, he's telling you a story about his cat. She stops in the doorway and looks at you for a long second."

        "Offer him a candy from Grandma Ozone's bowl.":
            $ gain("wren", 1)
            "He takes one. Then another. Strawberry is very grounding."
            pj "These are so good. Why is everything strawberry."
            oz "Because it's the rule, sweetheart."

        "\"Should I go get Wren?\"":
            pj "She just left, babe."
            "You both sit there awkwardly until she comes back."

    show wren neutral with dissolve
    "Wren gets him settled with tea and a blanket. Then she sits down on a cushion herself, just for a second, and her whole body slumps."
    oz "Look at that one. Carries everybody up and down these halls all weekend."
    oz "Who carries her, I'd like to know."

    menu:
        "\"Who takes care of you, Wren?\"":
            $ gain("wren", 2)
            "Wren doesn't answer for a long time."
            w neutral "Grandma Ozone, apparently."
            w blush "And... I don't know. I don't know. Nobody's asked."

        "Hand her a candy without saying anything.":
            $ gain("wren", 1)
            "She takes it. Unwraps it slowly. Holds it in her mouth with her eyes closed."
            w neutral "...Thanks."

        "\"You look exhausted.\"":
            w neutral "Thanks. I'm aware. I have a mirror. It's a crew mirror. It's black."

    walkie "Wren, ice machine has achieved sentience. Repeat, sentience."
    w neutral "Copy."
    oz "Go on, sweetheart. Take a candy for the road. Take two. Give one to whoever's walking you."
    hide wren with dissolve
    return


label wren_night_2:
    scene bg mission with dissolve
    "STAFF ONLY. Inside, the linen closet has been turned into mission control. Monitors show hand-drawn maps of the hotel. Walkie-talkies charge in a row. Clean towels are stacked to the ceiling."
    show wren neutral with dissolve
    w "You found me. Don't tell anyone this room exists. I'll have to kill you. Gently. With towels."
    w "Actually, I could use a hand. Want to call a cue?"
    "She points to a panel of big glowing buttons: FOG. LASERS. ARK. PANIC."
    w "Room 312 needs fog on my count. Three, two—"

    menu:
        "Press FOG exactly on one.":
            $ gain("wren", 2)
            $ called_fog_cue = True
            "You hit it exactly on the beat. On the monitor, a soft wave of fog rolls across the forest room. Someone in there gasps, delighted."
            w happy "Perfect. That was {i}perfect.{/i} You have no idea how rare that is. You'd make good crew."

        "Press it a little early, in your excitement.":
            w neutral "That was early. It's fine. The forest got a head start. Fog's very forgiving."

        "Press PANIC, because how could you not.":
            $ gain("wren", 1)
            "Somewhere in the walls, a single kazoo plays a long, sad note."
            w surprised "Oh my god. Nobody's ever pressed that. In six years."
            w happy "It's not connected to anything. It's just a kazoo. Somebody built it as a joke. You pressed the joke."

    show wren neutral
    "Between cues, the two of you sit on stacks of towels in the dark, lit by the monitors. It's very quiet in here. You can feel the bass through the floor like a heartbeat."
    w "This is my favorite part of the whole weekend. Right here. Everybody out there having the best night of their life, and in here it's just quiet and the buttons."
    walkie "Wren, there's a guest stuck inside the ice machine alcove. Says they're 'communing.' Won't come out."
    w neutral "Copy."

    menu:
        w "I have to go deal with that. You should go enjoy the party. Or—I mean. You could come with me. If you wanted."

        "\"This is the party. I'm coming.\"":
            $ gain("wren", 2)
            w blush "...Okay. Yeah. Okay. Grab a flashlight."
            "You walk the hallways side by side. She lets you carry the flashlight. It's the most important flashlight in the building."

        "\"I'll hold down the fort here.\"":
            $ gain("wren", 1)
            w surprised "You'd... yeah. Okay. Don't press anything. Except PANIC. You can press PANIC."
            "She tosses you a spare walkie on her way out. For the next twenty minutes you're crew."

        "\"I'll see you later, then.\"":
            w neutral "Yeah. Later. Have fun."

    hide wren with dissolve
    return


label wren_night_3:
    scene bg roof with dissolve
    "The roof. Above you, a sky full of stars. Below, the bass. Thick cables run down from the rigging over the ballroom skylight, where in a few minutes the ark will be ready."
    show wren neutral with dissolve
    "Wren is clipboard in hand, checking every knot. She looks up when the door clangs."
    w "Hey. I have seven minutes until I need to be at the board. Everything's checked. Triple-checked."
    w "Seven minutes. What do people do with seven minutes?"

    menu:
        "\"Sit down. Look at the stars. I'll watch the clock for you.\"":
            $ gain("wren", 2)
            "You hold out your hand. After a long second, she gives you the walkie."
            "She lies flat on her back on the gravel roof, arms out, and looks up. She doesn't say anything for three whole minutes."
            w blush "I forgot there were stars here. Six years. I forgot."

        "\"Dance with me. No music.\"":
            $ gain("wren", 1)
            w surprised "There's music. It's coming up through the roof. It's... actually, okay."
            "You dance, badly, on the roof. She's stiff for a minute and then she isn't."

        "\"Shouldn't you be double-checking the rigging?\"":
            w neutral "Triple. I said triple. ...You're right. I'll check it again."
            "She spends the seven minutes checking knots."

    show wren neutral
    w "Can I tell you something stupid? I've never seen the ark. Not once. Six years. I call the cue from the board and I watch it on a monitor the size of a sandwich."
    w "Everyone says it's the best moment of the whole weekend. I wouldn't know."

    menu:
        "\"After the cue, come find me. Watch the end of it with me.\"":
            $ gain("wren", 2)
            w surprised "I can't just—"
            w blush "...After the cue. Once it's landed. Maybe I could. Maybe I could, actually."

        "\"Next year, let someone else call it. Come as a guest.\"":
            $ gain("wren", 1)
            w neutral "Ha. Maybe. That's... maybe."

        "\"You'll see it someday.\"":
            w neutral "Yeah. Someday."

    walkie "Wren, five minutes to ark. Board's waiting."
    w neutral "Copy. On my way."
    if rapport["wren"] >= ROMANCE_THRESHOLD:
        w blush "My shift ends at 11:12. One minute after. I've never once left on time. Tonight I'm going to."
    else:
        w neutral "Go get a spot near the front. Trust me. It's worth seeing in person."
    hide wren with dissolve
    return


label wren_romance:
    scene bg ballroom with slowfade
    $ time_label = "Sunday — 11:12 PM"
    "At 11:12, while the ballroom is still screaming and the confetti is still falling, someone taps you on the shoulder."
    show wren happy with dissolve
    "Wren. No clipboard. The headset is around her neck instead of on her head, and she looks like someone who has just jumped off a high diving board."
    w "I handed the board to Pilar. Pilar's been begging for it for two years. I just... walked out. In the middle of a cue."
    w "I watched the duck come out of the ark from the back of the room. In person. With my actual eyes. It was so stupid. I cried so much."
    w surprised "I don't know what to do with my hands. They keep reaching for a radio."
    menu:
        w "What do guests do now? After the big moment? I've genuinely never known."

        "\"They dance. Badly. Come on.\"":
            "You pull her into the crowd. She dances like someone who has seen a thousand people dance and never once done it herself, stiff, then less stiff, then laughing."
        "\"They go find a quiet corner and talk until the sun comes up.\"":
            w happy "That sounds... incredible, honestly. I know every quiet corner in this building. Professionally."

    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 6:07 AM"
    show wren neutral with dissolve
    "Hours later, you're both back on the roof, where you were before the cue. The rigging hangs slack. The sky is going gold over the hills."
    "Wren is sitting on the gravel with her back against the water tank, boots off, a stolen cardamom bun in each hand. She gives you one."
    if shared_bun:
        w "You gave me half of one on Saturday. I've been waiting all weekend to pay you back. With interest."
    else:
        w "There were twelve of these. Now there are zero. I have abused my position. I regret nothing."
    w "This is the first sunrise in six years I've watched without a radio on."
    "She takes the headset off her neck and sets it on the gravel between you. It crackles once. She doesn't touch it."

    menu:
        "\"How does it feel?\"":
            w blush "Terrifying. Amazing. Like I left the stove on, except the stove is seven hundred people."
            w "...But they're fine. They're fine without me for one morning. Huh."
        "Lean your shoulder against hers.":
            "She leans back. All of her, for once. You can feel how tired she is, and how much lighter."

    show wren neutral
    w "Can I tell you what this weekend was supposed to be? For me? Clipboard, radio, eleven hours of sleep across three days, someone throws up in the forest room, the fog machine catches fire."
    if called_fog_cue:
        w happy "And instead some guest walks into my linen closet and nails a fog cue on the first try. Do you know how annoying that is? I trained Pilar for a year."
    w "I keep thinking about my first year. The stairwell. The person in black who sat with me for four hours."
    w "I've spent six years trying to be that person for everyone else. I never thought about who'd sit with me."
    w blush "And then you just... did. Over and over. Without me asking. You kept asking if I needed anything."

    menu:
        "\"You always needed something. You just never got to ask.\"":
            w blush "..."
            w "Okay. That's... you can't just say that at sunrise. I'm going to think about that for a year."
        "\"I liked being near you. That's all it was.\"":
            w blush "That's all? That's everything. That's the whole job, actually. Being near people."

    "The sun clears the hills. Down in the parking lot, a crew member is coiling cables and singing to themselves. It isn't Wren's problem. For once, nothing is."
    if pool_seen["wren"] >= 1:
        w blush "I've been wanting to ask you something since the disco ball. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now."
    else:
        w blush "I've been wanting to ask you something all weekend. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now."
    w "Is it okay if I kiss you?"

    menu:
        "\"Yes. Very much yes.\"":
            "She kisses you like she's been planning it for three days, which it turns out she has. She's precise about it. Perfect timing. Right on the count."
            w happy "Cue."
        "\"Only if I get to call it. Three, two—\"":
            w happy "Oh, you're—"
            "On one, she does."
            w happy "Perfect timing. You really would make good crew."

    show wren happy
    w "I have to go help strike the set in about an hour. That's the deal. Everyone helps strike."
    w blush "But this hour's mine. I'm not giving it to anyone."

    scene bg roof_dawn with slowfade
    "On the gravel between you, the walkie crackles: {i}Wren? Wren, where are the extra towels? Wren, the flamingo is back in the ice machine.{/i}"
    "She reaches over, very calmly, and turns it off. Then she lies back on the gravel next to you and watches the whole sky go from pink to blue."
    scene black with slowfade
    "{i}A week later, an envelope arrives. Inside: a crew badge, laminated. It doesn't say CREW. It says GUEST.{/i}"
    "{i}On the back, in neat clipboard handwriting:{/i}"
    w "Next year we both come as guests. I already asked. Pilar is calling the ark. I'm watching it with you, from the front, with my eyes. That's the whole plan."
    w "Also I'm free Saturday. Not a cue, not a shift. Just free. I had to look up what people do. Apparently it's brunch. — W"
    $ chosen = "wren"
    $ ending_name = "Off Duty"
    jump ending_card


label wren_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show wren happy with dissolve
    "Wren is coiling cables in the parking lot on Monday morning, headset back on, already somewhere in the middle of tomorrow. She sees you and lifts one hand."
    w "Hey. You survived. Most people look worse than you on Monday. You look about forty percent worse. That's good."
    w neutral "Thanks for this weekend. Seriously. You kept checking on me. Crew doesn't get checked on. It's... it was nice."
    walkie "Wren, there's a man in pajamas asleep in the forest room. He says he lives there now."
    w "Copy. Give me five."
    w happy "You're on the list now. If you ever want to crew, I'll train you myself. You'd be good at it. You notice people."
    "She hands you a spare walkie-talkie, switched off, as a souvenir. It still has a strip of tape on the back that says CARE."
    return


