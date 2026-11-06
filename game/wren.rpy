## wren.rpy — Wren, crew, dressed in black. Pronouns: they/them.
## They're the party's fixer: the art and the tech behind the scenes. They found
## themself at one of these parties years ago, and now they build the space so
## other people can too, which only works if nothing breaks. They spend the
## weekend putting out fires and never get to be at the party. The route is
## about pulling them into it, a few minutes at a time.

label wren_pool_1:
    "A person in head-to-toe black is standing at the edge of the deep end with a long pool net, trying to fish a disco ball out from the water. It keeps rolling off the net."
    show wren neutral with dissolve
    w "Come on. Come on. You were installed in a ballroom. You were not installed in a pool. How did you even get here?"
    "It's Wren, from check-in. Sweat is running down from under their headset."

    menu:
        "Grab the other net off the wall and help.":
            $ gain("wren", 2)
            "You work it from the opposite side. It takes three tries, a lot of teamwork, and one undignified lunge, but the disco ball comes out of the water dripping and spinning."
            w happy "Yes! YES. Finally a little less chaos... for now."
            w neutral "Thank you. Seriously. You didn't have to."

        "\"Need a hand?\"":
            $ gain("wren", 1)
            w neutral "...Yes. God. Yes."
            "Between the two of you, the disco ball eventually surrenders."

        "\"Isn't that someone else's job?\"":
            w neutral "Everything here is someone else's job until it breaks. Then it's mine."
            "Wren gets it out on the seventh try, alone."

    show wren neutral
    "They sit down on the edge of a lounger with the wet disco ball in their lap, like a cat that's been rescued from a tree."
    w "Six years I've been crew. First year I came as a guest. Didn't know a single person here."
    w "By Sunday I was cracking a whip, leading people around on leashes, finding a side of myself I never knew existed. This hotel means a lot to me."
    w "The magic only happens if the spell holds. The second the lasers die or the fog machine catches fire, everyone remembers they're standing in an old hotel, not a magical party. So now I'm the one who makes sure nothing breaks."

    menu:
        "\"Do you ever get to just... be at the party?\"":
            $ gain("wren", 2)
            w surprised "Ha."
            w neutral "Sometimes. For about six minutes at a time. Between fires."
            w "Nobody's asked me that in a long time. People mostly ask me to fix their art."

        "\"That's a really beautiful reason.\"":
            $ gain("wren", 1)
            w blush "It's... yeah. Thanks. Don't tell anyone, I have a reputation for being dead inside."

        "\"Sounds like a lot of unpaid labor.\"":
            w neutral "It's volunteering. It's different."
            w "...It's a little bit unpaid labor."

    walkie "Wren, someone's trying to fuck the ATM. ON THE CASINO FLOOR!"
    w neutral "Copy. Be right there."
    hide wren with dissolve
    return


label wren_pool_2:
    "Behind the towel hut at the far end of the pool hall, out of sight, Wren is sitting on an upturned bucket eating a sandwich. It's a very sad sandwich far past it's prime."
    show wren surprised with dissolve
    w "Oh. Hi. You found my secret place. I have a fifteen-minute break. I've had it for six minutes so I've got nine minutes to spare."

    menu:
        "Offer them half of the fancy pastry you grabbed from the pastriarchy cart.":
            $ gain("wren", 2)
            $ shared_bun = True
            w surprised "Is that the cardamom bun? I've never gotten one, I'm always on shift when they do the renegades."
            w happy "Oh my god, it's so good. I'm going to cry. I can't cry, I'm crew, gotta keep my game face on."

        "Sit down on the floor next to Wren and say nothing.":
            $ gain("wren", 1)
            "You sit. They eat their sad sandwich. The pool noises go on around the corner."
            w neutral "This is nice. Nothing's on fire right now. It's like being underwater."

        "\"Want me to leave so you can actually have your break?\"":
            $ gain("wren", 1)
            w neutral "No. Stay. It's nice to talk to someone who isn't telling me something's broken."

    show wren neutral
    "Wren turns the walkie down to its lowest setting. You can tell it costs them something."
    w "I'm on duty for the big event tomorrow. It all comes down from the ballroom ceiling at 11:11 on a rig I built. Seven hundred people in the dark. If anything jams, I have about ninety seconds to fix it before anyone notices."
    w "Last year the confetti cannon jammed, then caught on fire. Small fire. Supportive fire. But still."

    menu:
        "\"It'll go fine. And if it doesn't, it'll be a better story.\"":
            $ gain("wren", 2)
            w happy "Ha. Okay. True. I was a hit at the wrap party."
            w neutral "Thank you for saying it'll be okay. I needed somebody to say that, and I've been saying it to everyone else."

        "\"Can I help? Running errands, carrying stuff, anything?\"":
            $ gain("wren", 1)
            w neutral "Guests aren't supposed to work. But I'll... keep that in mind. Seriously."

        "\"You should let someone else handle it.\"":
            w neutral "There isn't someone else. That's the whole job."

    walkie "Wren, the Carpet Master is making prophecies again. It won't stop and it's freaking people out."
    w neutral "Copy."
    w happy "Thanks for the break. That was the best few minutes of my weekend."
    hide wren with dissolve
    return


label wren_night_1:
    scene bg backstage with dissolve
    "Behind a door marked BACKSTAGE: a forest of scaffolding, cables thick as pythons, road cases stenciled with names like PARTY HARDER and FRAGILE: FEELINGS. Through a gap in the curtain, the ballroom roars."
    "Except the lasers have gone dark. The DJ is vamping. Seven hundred people are dancing under nothing but the exit signs, and it's starting to feel like a hotel ballroom again."
    show wren neutral with dissolve
    "Halfway up a ladder, with a flashlight in their teeth and a screwdriver behind their ear, is Wren."
    w "Mmf. Oh, thank god, it's you. Don't touch anything red."
    w "The laser rig went down mid-set. I've got maybe one more song before people start noticing the carpet."

    menu:
        "\"What do you need?\"":
            $ gain("wren", 2)
            "They point at the flashlight in their mouth. You climb up and take it, and hold it exactly where they point, while they rewire something with the speed and deftness of a surgeon."
            w neutral "Little left. Little more. Perfect. Don't breathe."
        "\"Have you tried turning it off and on again?\"":
            $ gain("wren", 1)
            w neutral "..."
            "They stare at you. Then they reach over and flip the master switch off and on again."
            "Somewhere above you, the rig whirs back to life."
            w blush "Do not tell anyone that worked."
        "\"Shouldn't someone with a real job be doing this?\"":
            w neutral "I am someone with a real job. It's this. Since no one else seems to want to help."

    "The lasers blaze back on. Pink and cyan beams sweep the haze, the bass drops, and seven hundred people scream like it was all part of the show."
    "None of them will ever know anything went wrong. Wren climbs down the ladder, sits on a road case, and watches them through the gap in the curtain."
    show wren happy
    w "That's the job. Nobody's supposed to know. If they notice, the spell breaks."
    show wren neutral
    w "Every year someone walks in here as one person and walks out as somebody else. I just keep the lights on while it happens."

    menu:
        "\"Who keeps the lights on for you?\"":
            $ gain("wren", 2)
            "Wren doesn't answer for a long time. The lasers sweep over their face, pink, then cyan, then pink."
            w blush "...Nobody's asked me that. I don't know. But thank you, I'll think on that."
        "\"Come out there for one song.\"":
            $ gain("wren", 1)
            w neutral "One song. If anything breaks, I'm—"
            "You pull them through the curtain. They stand at the very edge of the dance floor and don't dance, exactly, but they sway. For one song."
            w blush "...Okay. That was nice. Don't tell the rest of the crew."
        "\"You look exhausted.\"":
            w neutral "Thanks. I'm aware. I have a mirror."

    walkie "Wren, there's a wizard of the 9th floor, waving his, um, big stick around if you catch my drift."
    w neutral "Copy. On my way."
    w happy "Thanks for the flashlight. Or the moral support. Whichever it was."
    hide wren with dissolve
    return


label wren_night_2:
    scene bg mission with dissolve
    "STAFF ONLY. Inside, a linen closet has been turned into the crew's control station. On one wall, a big hand-drawn map of the hotel, studded with little red magnets: one for everything that's currently broken. There are a lot of red magnets."
    "Walkie-talkies charge in a row. Clean towels are stacked to the ceiling. A toolbox the size of a coffin sits open on the floor."
    show wren neutral with dissolve
    w "You found me. Don't tell anyone this room exists. I'll have to kill you. Gently. With towels."
    w "Actually, I could use a hand. The fog machine in Room 312 is stuck on. The forest is turning into soup."
    "They point to a panel of big glowing buttons: FOG KILL. LASERS. BIG EVENT RIG. PANIC."
    w "The fog kill switch is flaky. It has to be held down for exactly three seconds while I reset the unit, or it reboots and floods the room. On my count. Three, two—"

    menu:
        "Hold FOG KILL down, perfectly steady, for exactly three seconds.":
            $ gain("wren", 2)
            $ called_fog_cue = True
            "You hold it. One. Two. Three. On the monitor, the fog in the forest room thins to a soft, pretty haze. Someone in there gasps, delighted."
            w happy "Perfect. That was {i}perfect.{/i} You have no idea how rare steady hands are on this crew. You'd make good crew."
        "Hold it down, panic, and let go a second early.":
            "The fog in the forest room surges, then settles. On the monitor, someone in there sneezes."
            w neutral "That was early. It's fine. The forest got a little extra mood. Fog's very forgiving."
        "Press PANIC, because how could you not.":
            $ gain("wren", 1)
            "A small door opens on the control panel and a fake snake jumps out, over your head."
            w surprised "Oh my god. Nobody's ever pressed that. In six years."
            w happy "Thank god it's just a joke. I guess I needed a good laugh."

    show wren neutral
    "Between fires, the two of you sit on stacks of towels in the dark, lit by the monitors. It's very quiet in here. You can feel the bass through the floor like a heartbeat."
    "Every so often they get up and move a red magnet to the other side of the map. Fixed."
    w "This is my favorite part of the whole weekend. Everybody out there having the best night of their life, and in here it's just quiet and the map, and the magnets going from red to done."
    walkie "Wren, the Ice Machine Planetarium's star projector just went dark. I'm worried we've lost power to the whole rotunda."
    w neutral "Copy."

    menu:
        w "I have to go fix the sky. You should go enjoy the party. Or—I mean. You could come with me. You can hold the flashlight. You're good at it."

        "\"Wherever you are is the party. I'm coming.\"":
            $ gain("wren", 2)
            w blush "...Okay. Yeah. Grab the flashlight."
            "You walk the hallways side by side. They let you carry the flashlight. Ten minutes later, the stars come back on in the planetarium, and a whole room of people says {i}oooh{/i} at once."
        "\"I'll hold down the fort here.\"":
            $ gain("wren", 1)
            w surprised "You'd... yeah. Okay. Don't press anything. Except PANIC. You seem good at that one."
            "They toss you a spare walkie on their way out. For the next twenty minutes you're crew. You move two magnets. It feels incredible."
        "\"I'll see you later, then.\"":
            w neutral "Yeah. Later. Have fun."

    hide wren with dissolve
    return


label wren_night_3:
    scene bg roof with dissolve
    "The roof of the hotel tower. Above you, a sky full of stars. Far below, the black mirror of the lake and the glitter of the other casinos along the shore. Under your feet, the bass. Thick cables run down from the rigging into the ballroom skylight, where in a few minutes the big event will begin."
    show wren neutral with dissolve
    "Wren is toolbox in hand, checking every knot. They look up when the door clangs."
    w "Hey. I have seven minutes until I need to be under the stage. The rig's checked. Triple-checked."
    w "Seven minutes. What do people do with seven minutes?"

    menu:
        "\"Sit down. Look at the stars. I'll watch the clock for you.\"":
            $ gain("wren", 2)
            "You hold out your hand. After a long second, they give you the walkie."
            "They lie flat on their back on the gravel roof, arms out, and look up. They don't say anything for three whole minutes."
            w blush "I forgot there were stars here. Six years. I forgot."

        "\"Dance with me. No music.\"":
            $ gain("wren", 1)
            w surprised "There's music. It's coming up through the roof. It's... actually, okay."
            "You dance, badly, on the roof. They're stiff for a minute and then they aren't."

        "\"Shouldn't you be double-checking the rigging?\"":
            w neutral "Triple. I said triple. ...You're right. I'll check it again."
            "They spend the seven minutes checking knots."

    show wren neutral
    w "Can I tell you something stupid? I've never seen the big event. Not once. Six years."
    w "During the big event I'm under the stage with a fire extinguisher and a roll of gaffer tape, watching it on a monitor the size of a sandwich. In case anything breaks. Ninety seconds, remember."
    w "Everyone says it's the best moment of the whole weekend. I wouldn't know."

    menu:
        "\"After the big event, come find me. Watch the end of it with me.\"":
            $ gain("wren", 2)
            w surprised "I can't just—"
            w blush "...After it lands. If nothing's broken. Maybe I could. Maybe I could, actually."

        "\"Next year, let someone else take fire duty. Come as a guest.\"":
            $ gain("wren", 1)
            w neutral "Ha. Maybe. That's... maybe."

        "\"You'll see it someday.\"":
            w neutral "Yeah. Someday."

    walkie "Wren, five minutes to the big event. Rig's yours."
    w neutral "Copy. On my way."
    if rapport["wren"] >= ROMANCE_THRESHOLD:
        w blush "My shift ends at 11:12. One minute after the big event. I've never once left on time. Tonight I'm going to."
    else:
        w neutral "Go get a spot near the front. Trust me. It's worth seeing in person."
    hide wren with dissolve
    return


label wren_romance:
    scene bg ballroom with slowfade
    $ time_label = "Sunday — 11:12 PM"
    "At 11:12, while the ballroom is still screaming and the confetti is still falling, someone taps you on the shoulder."
    show wren happy with dissolve
    "Wren. No toolbox. The headset is around their neck instead of on their head, and they look like someone who has just jumped off a high diving board."
    w "Nothing broke. Do you understand? Six years, and for the first time, nothing broke. Not one thing. I stood under that stage with a fire extinguisher and nothing caught fire."
    w "So I handed the toolbox to Pilar. Pilar's been begging for it for two years. And I just... walked out."
    w "I watched them open the ark from the back of the room. In person. With my actual eyes. It was so stupid. I cried so much."
    w surprised "I don't know what to do with my hands. They keep reaching for a screwdriver."
    menu:
        w "What do guests do now? After the big moment? I've genuinely never known."

        "\"They dance. Badly. Come on.\"":
            "You pull them into the crowd. They dance like someone who has seen a thousand people dance and never once done it themself, stiff, then less stiff, then laughing."
        "\"They go find a quiet corner and talk until the sun comes up.\"":
            w happy "That sounds... incredible, honestly. I know every quiet corner in this building. I've fixed the lights in all of them."

    scene bg roof_dawn with slowfade
    $ time_label = "Monday — 6:07 AM"
    show wren neutral with dissolve
    "Hours later, you're both back on the roof, where you were before the ark. The rigging hangs slack. The sky is going gold over the mountains, and the lake below is turning from black to silver."
    "Wren is sitting on the gravel with their back against the water tank, boots off, a stolen cardamom bun in each hand. They give you one."
    if shared_bun:
        w "You gave me half of one on Saturday. I've been waiting all weekend to pay you back. With interest."
    else:
        w "There were twelve of these. Now there are zero. I have abused my position. I regret nothing."
    w "This is the first sunrise in six years I've watched without a radio on."
    "They take the headset off their neck and set it on the gravel between you. It crackles once. They don't touch it."

    menu:
        "\"How does it feel?\"":
            w blush "Terrifying. Amazing. Like I left the stove on, except the stove is a whole hotel."
            w "...But it's fine. It's fine without me for one morning. Huh."
        "Lean your shoulder against theirs.":
            "They lean back. All of them, for once. You can feel how tired they are, and how much lighter."

    show wren neutral
    w "Can I tell you what this weekend was supposed to be? For me? Toolbox, radio, eleven hours of sleep across three days, the lasers die, the fog machine catches fire, someone puts a disco ball in the pool."
    if called_fog_cue:
        w happy "And instead some guest walks into my linen closet and holds a kill switch steadier than half my crew. Do you know how annoying that is? I trained Pilar for a year."
    w "I keep thinking about my first year. The shower-curtain cape. The conga line. Saying things out loud I'd never said to anyone. I found out who I was in those hallways."
    w "Every year since, I've been building the place so other people get to find out too. And somewhere along the way I stopped thinking I was allowed to be one of them."
    w blush "And then you just... kept pulling me back in. Over and over. A flashlight, a bun, a song. You kept asking if I needed anything."

    menu:
        "\"You always needed something. You just never got to ask.\"":
            w blush "..."
            w "Okay. That's... you can't just say that at sunrise. I'm going to think about that for a year."
        "\"I liked being near you. That's all it was.\"":
            w blush "That's all? That's everything. That's the whole reason I build any of this, actually. So people can just be near each other."

    "The sun clears the mountains. Far below, in the parking lot, a crew member is coiling cables and singing to themselves. It isn't Wren's problem. For once, nothing is."
    if pool_seen["wren"] >= 1:
        w blush "I've been wanting to ask you something since the disco ball. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now."
    else:
        w blush "I've been wanting to ask you something all weekend. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now."
    w "Is it okay if I kiss you?"

    menu:
        "\"Yes. Very much yes.\"":
            "They kiss you like they've been planning it for three days, which it turns out they have. They're precise about it. Steady hands. Nothing breaks."
            w happy "Fixed."
        "\"Only if I get to count it down. Three, two—\"":
            w happy "Oh, you're—"
            "On one, they do."
            w happy "Perfect timing. You really would make good crew."

    show wren happy
    w "I have to go help strike the set in about an hour. That's the deal. Everyone helps strike."
    w blush "But this hour's mine. I'm not giving it to anyone."

    scene bg roof_dawn with slowfade
    "On the gravel between you, the walkie crackles: {i}Wren? Wren, where are the extra towels? Wren, the flamingo is back in the ice machine.{/i}"
    "They reach over, very calmly, and turn it off. Then they lie back on the gravel next to you and watch the whole sky go from pink to blue over the lake."
    scene black with slowfade
    "{i}A week later, an envelope arrives. Inside: a crew badge, laminated. It doesn't say CREW. It says GUEST.{/i}"
    "{i}On the back, in neat handwriting:{/i}"
    w "Next year we both come as guests. I already asked. Pilar's on fire duty for the ark. I'm watching it with you, from the front, with my eyes. That's the whole plan."
    w "Also I'm free Saturday. Not a shift, not a fire. Just free. I had to look up what people do. Apparently it's brunch. — W"
    $ chosen = "wren"
    $ ending_name = "Off Duty"
    jump ending_card


label wren_friend:
    scene bg exterior with slowfade
    $ time_label = "Monday — Checkout"
    show wren happy with dissolve
    "Wren is coiling cables under the hotel's big neon sign on Monday morning, headset back on, already somewhere in the middle of tomorrow. They see you and lift one hand."
    w "Hey. You survived. Most people look worse than you on Monday. You look about forty percent worse. That's good."
    w neutral "Thanks for this weekend. Seriously. You kept checking on me. Crew doesn't get checked on. It's... it was nice."
    walkie "Wren, the moss in the forest room is smoking. Small smoke. Supportive smoke."
    w "Copy. Give me five."
    w happy "You're on the list now. If you ever want to crew, I'll train you myself. You'd be good at it. You notice things right before they break."
    "They hand you a spare walkie-talkie, switched off, as a souvenir. It has a strip of gaffer tape on the back that says FIX IT."
    return
