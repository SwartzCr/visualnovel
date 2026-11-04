# Do Not Disturb: all dialogue

<!-- exported from commit 2662dd9 -->

Edit this file and send it back; the changes get applied to the game.

- **Change a line:** edit the text after its tag (the `juni:42` at the start). Keep the tag.
- **Change who speaks or their expression:** edit the bold name, e.g. `**Juni (happy):**`. Expressions are neutral, happy, surprised and blush. No bold name means narration.
- **Add a line:** write it on a new line (no tag) under the line it should follow.
- **Delete a line:** delete the whole line, tag included. Choices (lines with ▸) can be reworded but not deleted.
- Lines starting with `>` are notes on what happens (scene changes, menus, rapport). They're for context and changes to them are ignored. Rapport is how much a choice raises (or lowers) that guest's affection; 10 unlocks their romance.
- `{i}...{/i}` is italics in the game. `[name]` fills in a value while playing; leave those as they are.

---

# script.rpy

## start

> *scene black*  
> *scene bg exterior*  
`script:25` The invitation was a paper card with no return address. One side said FRIDAY, 3PM. The other said {i}You were never here.{/i}  
`script:26` The Hotel Paradiso is a sixteen-story hotel-casino on the Nevada shore of Lake Tahoe, built in 1971 and showing every year of it. The casino closed in 1987. The hotel never quite noticed.  
`script:27` This weekend, somebody has rented every room. The big neon sign out front has lost its final O. It now reads HOTEL PARADIS, which half the people in the parking lot insist is French and the other half insist is a prophecy.  
`script:29` **Tamsin (text):** omg you're here!! go check in. find the person in black. ask before touching. let it get weird  
> *scene bg lobby*  
`script:33` The lobby still has its 1970s carpet, a migraine of orange and purple swirls. Past the front desk, the old casino floor is dark, the slot machines draped in fairy lights and feather boas.  
> *show wren neutral*  
`script:36` **Wren:** Hi. Welcome to the Paradiso. I'm Wren, crew. You won't see much of me. If I'm doing my job, nothing breaks and you never know I was here.  

> **Choice**
`script:39` **Wren:** Any questions before I let you loose?  

`script:41` **▸** "Is there anything you need help with right now?"  
> *rapport +1 Wren*  
`script:43` **Wren (surprised):** Huh. Nobody asks crew that.  
`script:44` **Wren (neutral):** I'm fine. But hold that thought. I might cash it in at 3 AM when the fog machine catches fire.  

`script:46` **▸** "Are there rules?"  
`script:47` **Wren:** Two that matter. No photos, and ask before you touch anyone. Everything else is a suggestion.  

`script:49` **▸** "So what {i}is{/i} this, exactly?"  
`script:50` **Wren:** Nobody's allowed to say. The second anyone says it out loud, it turns into a brochure.  
> *(end of choice)*

`script:52` **Wren (neutral):** Here's the only advice I give first-timers. Don't watch. Nobody here is an audience.  
`script:53` **Wren:** Walk into the room you'd normally walk past. Say the thing you'd normally keep to yourself. Be whoever you actually are. This is the one weekend nobody's going to laugh at you for it.  
`script:54` **Wren (happy):** And somebody's probably going to catch your eye this weekend. It happens to everyone their first time. Let it.  
`script:55` **Wren (neutral):** Pool's on the ground floor in the afternoons. Hallways all night. Go find out who you are here.  
`script:58` Tip: open the {color=#ff5fb8}Guests{/color} menu at the bottom of the screen to see everyone you've met.  
> *→ jump the_weekend*  

## the_weekend

> *if day > 1:*  
> *→ call morning*  
> *→ call pool_time*  
> *→ call night_time*  
> *→ jump finale*  

## morning

> *scene bg bedroom*  
> *if day == 2:*  
`script:83` You wake up on top of the covers in your shoes, in a room you're fairly sure is yours. Someone has drawn a small, friendly eye on the bathroom mirror in lipstick.  
`script:84` A newspaper has been slid under the door.  
`script:85` {b}THE DAILY DISTURBANCE{/b} — Saturday Edition  
`script:86` {i}HEADLINE: POOL PEOPLE ACCUSE ICE MACHINE OF 'COLDNESS.' ICE MACHINE: 'WE ARE THE SAME WATER.'{/i}  
`script:87` {i}HOROSCOPE (all signs): Today someone will tell you a secret about themselves. Do not make it about you. Do not make it a podcast.{/i}  
`script:88` {i}LOST AND FOUND: One (1) Sasquatch footprint, left foot. Please return to the tea bar.{/i}  
> *else:*  
`script:90` Sunday. The light through the window is the color of weak tea. Somewhere below, a single kazoo is playing what might be the national anthem of a country that doesn't exist yet.  
`script:91` {b}THE DAILY DISTURBANCE{/b} — Sunday (Final) Edition  
`script:92` {i}HEADLINE: SOURCES CONFIRM SOMETHING ARRIVES AT 11:11. SOURCES DECLINE TO SAY WHAT. SOURCES ARE ALIENS.{/i}  
`script:93` {i}HOROSCOPE (all signs): The last night of anything is the one you'll remember. Say the thing. Ask first. Then say the thing.{/i}  
`script:94` {i}CLASSIFIEDS: Have you seen my friend? Answers to Tamsin. Last seen inside a balloon. — Tamsin{/i}  

## pool_time

> *scene bg pool*  
> *if day == 1:*  
`script:108` The pool is the bright, ordinary half of the party: an indoor pool hall on the ground floor, under a big old glass atrium roof gone green at the seams. Towels, chlorine, potted palms, and the Pool People's banner strung over the deep end: WATER IS WARM. WATER IS LOVE.  
`script:109` The Pool People, you gather, are at war with the Order of the Ice Machine over the true nature of water. It's supposed to be settled Sunday at 11:11 PM.  
`script:110` Most of the costumes have been swapped for swimsuits. Some have not. Some never will be.  
> *elif day == 2:*  
`script:112` The pool on Saturday afternoon is full of people recovering from Friday night. Someone is teaching a slow-motion water aerobics class to no music at all.  
`script:113` A herald in a gold cape walks the deck with a scroll.  
`script:114` **The Herald:** HEAR YE! The Order of the Ice Machine has frozen three of our pool noodles! The Pool People demand reparations in the form of warmth!  
> *else:*  
`script:116` Last afternoon. The pool has the sleepy tenderness of a place where a lot of people have cried in a good way.  
`script:117` The Pool People have lowered their banner to half mast, out of respect, or because the rope broke.  

> **Choice**
`script:120` Who do you spend the afternoon with?  

`script:122` **▸** A pink axolotl kigurumi, sitting fully dressed at the pool's edge, looking very hot.  
> *(shown if pool_seen["juni"] == 0)*  

`script:124` **▸** Juni the axolotl, floating face-up on a pizza-shaped inflatable.  
> *(shown if pool_seen["juni"] == 1)*  

`script:127` **▸** A Sasquatch in an innertube in the shallow end, holding a teacup above the water.  
> *(shown if pool_seen["gerald"] == 0)*  

`script:129` **▸** Gerald, leading a very slow 'forest bathing' session on the pool deck.  
> *(shown if pool_seen["gerald"] == 1)*  

`script:132` **▸** A raver in fur leg warmers, handing out glitter like communion.  
> *(shown if pool_seen["solstice"] == 0)*  

`script:134` **▸** Solstice, asleep on a lounger right under one of the big heat lamps, LED top switched off.  
> *(shown if pool_seen["solstice"] == 1)*  

`script:137` **▸** A person in black fishing a disco ball out of the deep end with a net.  
> *(shown if pool_seen["wren"] == 0)*  

`script:139` **▸** Wren, eating a sad sandwich behind the towel hut.  
> *(shown if pool_seen["wren"] == 1)*  

`script:142` **▸** A silver alien under a beach umbrella, indoors, studying the pool with great suspicion.  
> *(shown if pool_seen["zyx"] == 0)*  

`script:144` **▸** Zyx, collecting lost flip-flops in a bag labeled EARTH ARTIFACTS.  
> *(shown if pool_seen["zyx"] == 1)*  
> *(end of choice)*

> *→ call expression "%s_pool_%d" % (who, pool_seen[who])*  

## night_time

> *scene bg hallway*  
> *if day == 1:*  
`script:163` Night falls and the Paradiso turns inside out. Every door is open. Every room is something else now.  
`script:164` Bass comes up through the carpet from the ballroom. Someone in a cape runs past you holding a lit candle and a stapler, apologizing.  
> *elif day == 2:*  
`script:166` Saturday night. The hallways are louder and stranger. A troupe of mute clowns in fishnets moves through the crowd selling shares in people.  
`script:167` A walkie-talkie taped to the ceiling crackles: {i}Room 404 has been located. Repeat. Room 404 has been located.{/i}  
> *else:*  
`script:169` Sunday night. The last night. The tickers in the stairwell all read the same thing: 11:11.  
`script:170` People are hugging in doorways for no reason. You catch yourself doing it too.  
> *→ call random_encounter*  
> *→ call hallway_encounter*  
> *scene bg hallway*  
> *if day == 3:*  
`script:176` It's 10:40. You have time for one more thing before the ark.  
> *else:*  
`script:178` The night isn't over. The hallway takes you back.  
> *→ call hallway_encounter*  
> *if day < 3:*  
> *scene bg hallway*  
`script:183` Somewhere around four in the morning, the hallway gets quiet enough to hear the ice machine humming to itself. You find your room by touch.  

## hallway_encounter

> *scene bg hallway*  

> **Choice**
`script:190` Which way do you wander?  

`script:192` **▸** A pink glowing tail disappears into a room with no number.  
> *(shown if night_seen["juni"] == 0 and "juni" not in met_tonight)*  

`script:194` **▸** Juni is standing very still in front of a door labeled LOST & FOUND.  
> *(shown if night_seen["juni"] == 1 and "juni" not in met_tonight)*  

`script:196` **▸** Blue light pours out of a room that sounds like the bottom of a lake. An axolotl hood bobs in the doorway.  
> *(shown if night_seen["juni"] == 2 and "juni" not in met_tonight)*  

`script:199` **▸** A very tall shape is being dragged down the hall by two rival breakfast cults.  
> *(shown if night_seen["gerald"] == 0 and "gerald" not in met_tonight)*  

`script:201` **▸** Room 312 smells like rain and cedar. A Sasquatch is standing in the doorway, not going in.  
> *(shown if night_seen["gerald"] == 1 and "gerald" not in met_tonight)*  

`script:203` **▸** Through a door marked SUPPORT GROUP, you see Gerald in a folding chair that is much too small.  
> *(shown if night_seen["gerald"] == 2 and "gerald" not in met_tonight)*  

`script:206` **▸** LED lights and a cheering crowd: someone is buying and selling people on the stock exchange.  
> *(shown if night_seen["solstice"] == 0 and "solstice" not in met_tonight)*  

`script:208` **▸** From a curtained booth, Solstice's voice, singing a confession very badly and very sincerely.  
> *(shown if night_seen["solstice"] == 1 and "solstice" not in met_tonight)*  

`script:210` **▸** The ballroom. Lasers. In the middle of the floor, Solstice, dancing like it's the last song on Earth.  
> *(shown if night_seen["solstice"] == 2 and "solstice" not in met_tonight)*  

`script:213` **▸** Behind a door marked BACKSTAGE, something is sparking. A voice says: "No no no no no."  
> *(shown if night_seen["wren"] == 0 and "wren" not in met_tonight)*  

`script:215` **▸** A door marked STAFF ONLY is open a crack. Inside, someone in a headset says your name.  
> *(shown if night_seen["wren"] == 1 and "wren" not in met_tonight)*  

`script:217` **▸** The stairwell to the roof is propped open. Wren's walkie is chirping somewhere above.  
> *(shown if night_seen["wren"] == 2 and "wren" not in met_tonight)*  

`script:220` **▸** A silver figure is feeding ping-pong balls into a robot and taking notes.  
> *(shown if night_seen["zyx"] == 0 and "zyx" not in met_tonight)*  

`script:222` **▸** Two nurses are wheeling a protesting alien into the Clinic of Unnecessary Procedures.  
> *(shown if night_seen["zyx"] == 1 and "zyx" not in met_tonight)*  

`script:224` **▸** The ice machine alcove is glowing. Zyx's antennae are silhouetted against a field of stars.  
> *(shown if night_seen["zyx"] == 2 and "zyx" not in met_tonight)*  

`script:227` **▸** Don't follow anyone. Just wander.  
> *(end of choice)*

> *if who is None:*  
> *→ call wander*  
> *else:*  
> *→ call expression "%s_night_%d" % (who, night_seen[who])*  

## wander

> *if wanders == 1:*  
> *scene bg livingroom*  
`script:244` You follow the smell of cardamom to a suite with a hand-painted sign on the door: THE COZY. Inside, someone has rebuilt a whole living room, down to the doilies.  
`script:245` **Auntie Acid:** Sit, sit. Have a candy. They're strawberry. Everything here is strawberry, that's the rule.  
`script:246` Auntie Acid is maybe sixty-five, in a kaftan covered in hand-sewn mirrors. She rocks. She hums. She has, you'd bet, seen some things.  
`script:247` **Auntie Acid:** First time? You've got first-time eyes. That's all right. Everyone here was new once. Even the Sasquatch.  
`script:248` **Auntie Acid:** Here's the only advice I give, sweetheart. Don't come to watch. Come to be watched by something bigger than you. Then go be kind to somebody.  
`script:249` You eat the candy. It's very strawberry. You leave feeling oddly blessed.  
> *elif wanders == 2:*  
> *scene bg exchange*  
`script:252` You wander into the Human Stock Exchange alone. A mute clown in a bra and fishnets immediately pantomimes, with great urgency, that you must sell shares of yourself.  
`script:253` You sell eleven percent of yourself to a woman dressed as a lighthouse. The ticker above you reads YOU ▲0.4.  
`script:254` It feels great. You don't know why. You leave before the market can correct.  
> *else:*  
> *scene bg cryptid*  
`script:257` You find an empty folding-chair circle in a room labeled CRYPTIDS ANONYMOUS. There's an inflatable Loch Ness Monster wearing a name tag.  
`script:258` You sit down for a second. The silence is really nice. Nessie doesn't judge.  
`script:259` When you get up, someone has left a small note on your chair: {i}you are not blurry here.{/i}  

## ceremony

> *scene bg ballroom*  
`script:270` At 11:05 the music stops.  
`script:271` Seven hundred people in costume stand in the ballroom in the dark, breathing. Someone whispers {i}is it happening{/i} and fifty people go {i}shhhhhh{/i}.  
`script:272` At 11:11 the doors at the back of the ballroom swing open.  
> *scene bg ballroom_ark*  
`script:274` A procession of people in silver alien suits carries a golden ark through the crowd. It's covered in psychedelic patterns. On the front, in big friendly letters: DON'T PANIC.  
`script:275` Up on the stage, the leader of the Pool People and the High Abbot of the Ice Machine face each other. They have been at war over the true nature of water all weekend.  
`script:276` The aliens set the ark between them and open the lid.  
`script:277` Inside is a single rubber duck.  
`script:278` The ballroom is completely silent for three full seconds.  
`script:279` Then the High Abbot of the Ice Machine starts to cry, and the leader of the Pool People starts to cry, and they hug, because of course. Ice is water. A pool is water. A duck floats on both. They were never at war.  
`script:280` The bass drops so hard the chandelier swings. Seven hundred people scream. Confetti falls from somewhere it couldn't possibly have been hidden.  
`script:281` It is incredibly stupid. You are crying too.  

---

# juni.rpy

## juni_pool_1

`juni:5` At the edge of the pool, fully zipped into a pink axolotl kigurumi, someone is sitting with their onesie feet in the water. The feet are soaked. They do not seem to care.  
`juni:6` The hood has its own little face on top, with two black eyes and a smile. Feathery gills fan out from either side. Under it, a real face, very pink, very warm.  
> *show juni neutral*  
`juni:8` **Juni:** Oh. Hi. Sorry. You're standing in my, um, sun. It's fine. I don't need the sun. I'm a cold-water creature.  

> **Choice**
`juni:10` **Juni:** ...Did you want to sit?  

`juni:12` **▸** "Aren't you dying in that thing?"  
`juni:13` **Juni:** Yes. Axolotls are native to cold lakes in Mexico City. I am, therefore, suffering.  
`juni:14` **Juni:** It's fine. I'm used to it. The hood is load-bearing.  

`juni:16` **▸** "Does your axolotl have a name?"  
> *rapport +2 Juni*  
`juni:18` **Juni (surprised):** Nobody's ever asked her name.  
`juni:19` **Juni (happy):** She's called Lotl. Lotl the axolotl. I'm aware that's not creative. She doesn't mind.  
`juni:20` **Juni:** I'm Juni. She's Lotl. We're a package deal this weekend.  

`juni:22` **▸** Sit down next to them and put your feet in the water too, without saying anything.  
> *rapport +1 Juni*  
`juni:24` **Juni (neutral):** ...  
`juni:25` **Juni (happy):** Oh, that's nice. Most people need to say something first.  
`juni:26` **Juni:** I'm Juni. You can just sit. That's allowed.  
> *(end of choice)*

> *show juni neutral*  
`juni:29` A little while later Juni is explaining that axolotls can regrow almost anything. Legs. Tails. Parts of their own hearts. Even bits of their brains.  
`juni:30` **Juni:** Out there, I work in databases. I'm the person who gets messaged at two in the morning because 'the thing is down.' I'm the guy who fixes the thing.  
`juni:31` **Juni:** In here I'm a salamander. Salamanders don't have to be impressive. They just have to be wet and kind of cute.  

> **Choice**

`juni:34` **▸** "Do you ever take the hood off?"  
`juni:35` **Juni (surprised):** Oh. Um.  
`juni:36` Juni pulls the hood strings a little tighter, like a reflex.  
`juni:37` **Juni (neutral):** Not yet. Maybe never. Maybe Sunday. I don't know. It's... a thing.  

`juni:39` **▸** "If you could regrow anything, what would it be?"  
> *rapport +2 Juni*  
`juni:41` Juni goes quiet for a long time. The Pool People's banner snaps in the wind.  
`juni:42` **Juni (neutral):** There used to be a part of me that sang in the car. Really loud. Badly. With the windows down.  
`juni:43` **Juni:** It fell off around year three of the job. I think I'd regrow that.  
`juni:44` **Juni (blush):** Sorry. That was a lot for a pool.  

`juni:46` **▸** "Being unimpressive sounds amazing. Can I be a salamander too?"  
> *rapport +1 Juni*  
`juni:48` **Juni (happy):** Applications are open. You'd need a hood. And to commit to being damp.  
`juni:49` **Juni:** Probationary salamander. I'll allow it.  
> *(end of choice)*

`juni:51` Without warning, Juni slides off the edge into the pool, fully dressed. The kigurumi balloons up around them like a pink jellyfish.  
`juni:52` **Juni (happy):** Ahhh. Regeneration.  
`juni:54` You decide that's the best thing you've seen all day.  

## juni_pool_2

`juni:59` Juni is floating face-up on an inflatable pizza slice, hood up, gills drooping in the heat. There's a second, smaller pizza slice tied to theirs by a string.  
> *show juni happy*  
`juni:61` **Juni:** You came back. I saved you a slice. It's the crust one. Nobody wants the crust one, but it's very stable.  
`juni:62` You climb onto the crust. You drift together toward the deep end, where the herald is shouting about pool noodles.  
> *show juni neutral*  

> **Choice**
`juni:65` **Juni:** So, what do you do? Like, out there.  

`juni:67` **▸** "Out there I'm someone else. In here I'm still figuring out who."  
> *rapport +2 Juni*  
`juni:69` **Juni (surprised):** Oh.  
`juni:70` **Juni (blush):** Yeah. Exactly that. That's exactly it.  

`juni:72` **▸** "Honestly? I'd rather not talk about work this weekend."  
> *rapport +1 Juni*  
`juni:74` **Juni (happy):** Oh thank god. Me neither. I put my work phone in a ziplock bag in the hotel ice bucket.  
`juni:75` **Juni:** It's an aquarium now. It's very calm in there.  

`juni:77` **▸** Make something up: "I'm a professional lighthouse."  
> *rapport +1 Juni*  
`juni:79` **Juni (happy):** Hah! Is it hard? Being a lighthouse?  
`juni:80` **Juni:** Actually don't answer. I want to imagine it. You just stand on a rock being helpful at boats.  
> *(end of choice)*

> *show juni neutral*  
`juni:83` Juni tells you this is their third year. Their roommate vouched for them the first time. That year they didn't leave their hotel room until Saturday.  
`juni:84` **Juni:** The second year I made it to the pool. This year I got stuck in the revolving door and Wren had to rescue me, and somehow that broke the seal. I've talked to like nine people.  
`juni:85` **Juni:** Ten. Ten with you.  

> **Choice**
`juni:88` **Juni:** Can I tell you something embarrassing?  

`juni:90` **▸** "Always."  
> *rapport +2 Juni*  
`juni:92` **Juni (blush):** I've been coming here three years and I've never once gone into an art room alone.  
`juni:93` **Juni:** I wait outside until somebody pulls me in. Like a cat at a door.  
`juni:94` **Juni:** I think I'm... sort of hoping it's you who pulls me in. This weekend. If that's not weird.  

`juni:96` **▸** "Only if I get to tell you one back."  
> *rapport +1 Juni*  
`juni:98` **Juni (neutral):** Deal. I've never gone into an art room by myself. I wait outside until somebody pulls me in.  
`juni:99` You tell them your embarrassing thing. Juni laughs so hard the pizza slice spins in a slow circle.  

`juni:101` **▸** "Is it about the hood?"  
`juni:102` **Juni (neutral):** Everything is about the hood.  
`juni:103` They sigh, and tell you anyway: three years, and they've never gone into an art room alone.  
> *(end of choice)*

`juni:105` **Juni (happy):** Okay. You know my secret now. That means you're responsible for me.  
`juni:106` They say it like a joke. They don't let go of the string between your pizzas for the rest of the afternoon.  

## juni_night_1

> *scene bg room404*  
`juni:113` You follow the pink tail into a room that is blinding white. Error messages hang from the ceiling on fishing line. A giant sign on the wall reads 404 — ROOM NOT FOUND.  
`juni:114` A man in a beige suit stands in the middle of the room, holding a clipboard, looking straight through you.  
> *show juni happy at slightright*  
`juni:116` **Juni:** Oh my god. Oh my god. It's a 404 room. This is for me specifically. Someone made this for me.  
`juni:117` **Man in a Beige Suit:** Please note: you are not in Room 404. There is no Room 404. You are not here.  
> *show juni neutral at slightright*  

> **Choice**

`juni:121` **▸** Play along: "Sorry. I'm also not here."  
> *rapport +2 Juni*  
`juni:123` **Man in a Beige Suit:** Thank you. Most people argue.  
`juni:124` Juni makes a tiny noise of pure joy inside the hood.  
`juni:125` **Juni (happy):** I'm not here either! Lotl's not here! None of us exist!  

`juni:127` **▸** "I mean... it's right here, though?"  
`juni:128` **Man in a Beige Suit:** Literalism detected.  
`juni:129` He hands you a small laminated card. It says ERROR: TOOK IT TOO SERIOUSLY.  
`juni:130` **Juni (neutral):** Oof. You have to keep that.  

`juni:132` **▸** Look over at Juni to see what they do.  
> *rapport +1 Juni*  
`juni:134` Juni leans in and whispers.  
`juni:135` **Juni (neutral):** Pretend you're a missing file. Just like... look a little corrupted.  
`juni:136` You do your best. The man in beige nods, satisfied.  
> *(end of choice)*

`juni:138` A dialog box pops up on an old monitor in front of Juni. It says: ARE YOU SURE YOU WANT TO BE HERE? There are two buttons. YES. ALSO YES.  
> *show juni surprised at slightright*  

> **Choice**
`juni:141` **Juni:** Which one do I press? It feels like a trick. It's always a trick.  

`juni:143` **▸** "Press YES. I'll press ALSO YES. We'll both be sure."  
> *rapport +2 Juni*  
`juni:145` You press your buttons at the same time. The monitor plays a tinny little fanfare. Confetti made of hole-punched paper falls from the ceiling.  
`juni:146` **Juni (happy):** We're both sure! That's the most sure I've been about anything in months.  

`juni:148` **▸** "There's no wrong answer. That's the trick."  
> *rapport +1 Juni*  
`juni:150` **Juni (neutral):** ...Huh. Yeah. Okay.  
`juni:151` Juni presses ALSO YES. Paper confetti falls from the ceiling.  

`juni:153` **▸** "Neither. Let's go find a room that actually exists."  
`juni:154` **Juni (neutral):** Oh. Right. Yeah, sure.  
`juni:155` Juni presses nothing. The dialog box waits patiently. You feel like you've made it sad.  
> *(end of choice)*

> *show juni happy at slightright*  
`juni:158` **Man in a Beige Suit:** For your records.  
`juni:159` The man in beige hands each of you a card: THIS CERTIFIES THAT THE BEARER WAS NEVER HERE.  
`juni:160` **Juni:** I'm keeping this forever. I'm going to frame it. Above my desk. At work. Where nobody will understand.  

## juni_night_2

> *scene bg lostfound*  
`juni:167` The Lost & Found is lit like an old library. Bins line the shelves, each one labeled in careful handwriting: MISPLACED CONFIDENCE. UNCLAIMED APOLOGIES. SPARE EXCUSES. OLD NICKNAMES.  
`juni:168` A sign on the counter says: TAKE ONE. LEAVE ONE.  
> *show juni neutral*  
`juni:170` **Juni:** I've been standing here for twenty minutes. I can't decide what to leave. Everything I own feels load-bearing.  
`juni:171` **Juni:** You go first. Show me how it's done.  

> **Choice**
`juni:174` What do you leave?  

`juni:176` **▸** An unsent text you've been carrying around for a year.  
> *rapport +2 Juni*  
`juni:178` You write it on one of the little cards and drop it in UNSENT TEXTS. It's lighter than you expected.  
`juni:179` **Juni (surprised):** Whoa. You just... let it go.  
`juni:180` Juni picks up a card, writes something, and puts it in UNCLAIMED APOLOGIES without letting you see.  
`juni:181` **Juni (neutral):** That was an apology I've been waiting for. From someone else. I'm done waiting. It can live here now.  

`juni:183` **▸** An old nickname you never liked.  
> *rapport +1 Juni*  
`juni:185` **Juni (happy):** Oh, good one.  
`juni:186` Juni writes JUNEBUG on a card and drops it in OLD NICKNAMES with a tiny flourish.  
`juni:187` **Juni:** My manager calls me that. Not anymore. Not in here.  

`juni:189` **▸** A single left sock.  
> *rapport +1 Juni*  
`juni:191` **Juni (happy):** Ha! The classic. Left socks are always the ones that get lost. Science can't explain it.  
> *(end of choice)*

`juni:193` Then you both notice it. The bin labeled ONE (1) COURAGE, SLIGHTLY USED. There's only one card left in it.  
> *show juni neutral*  

> **Choice**
`juni:196` **Juni:** There's only one. You should take it. You're braver than me.  

`juni:198` **▸** Take it, and hand it straight to Juni.  
> *rapport +2 Juni*  
`juni:201` **Juni (blush):** Oh.  
`juni:202` Juni holds the card in both sleeves like it's warm. The hood dips down so you can't see their face.  
`juni:203` **Juni:** Nobody's ever... okay. Okay. I'm going to use this. I don't know on what yet. But I'm going to.  

`juni:205` **▸** "Let's tear it in half. Half each."  
> *rapport +1 Juni*  
`juni:208` **Juni (happy):** Half a courage each. That's probably the right dose for a weekend.  
`juni:209` You tear it carefully down the middle. Juni tucks their half into the hood.  

`juni:211` **▸** Take it. You could use it.  
`juni:212` **Juni (neutral):** Good. You'll use it better.  
`juni:213` They sound like they mean it. They also sound a little like they wanted it.  
> *(end of choice)*

> *show juni neutral*  
`juni:216` **Juni:** Hey. Juni's short for Juniper. Nobody calls me Juniper. My mom, when I'm in trouble.  
`juni:217` **Juni (happy):** You can know that. You don't have to use it. I just wanted somebody here to know.  

## juni_night_3

> *scene bg regen*  
`juni:224` The Regeneration Tank is a hotel suite painted the deep blue of a lake bottom. Light ripples across the walls. A huge waterbed fills the middle of the room. A sign says: LIE DOWN. GROW SOMETHING BACK.  
> *show juni neutral*  
`juni:226` **Juni:** You came in with me. I didn't even have to stand outside.  
`juni:227` You lie down on the waterbed side by side. It sloshes. The kigurumi squeaks. Juni's gills are fanned out on the pillow like a halo.  
`juni:228` **Juni:** This is the last night. I feel like I should say something important and I don't know what it is.  

> **Choice**
`juni:231` **Juni:** Can I ask you something? Why do you keep finding me? There are seven hundred people here.  

`juni:233` **▸** "Because you're the most honest person here, and you're dressed as a salamander."  
> *rapport +2 Juni*  
`juni:235` **Juni (happy):** Hah. That's... okay, that's the nicest thing anyone's said to me in a long time.  

`juni:237` **▸** "I don't know. I just like being near you."  
> *rapport +2 Juni*  
`juni:239` **Juni (blush):** Oh.  
`juni:240` **Juni:** Me too. Near you, I mean. Not near me. I'm always near me. You know what I mean.  

`juni:242` **▸** "Coincidence, probably."  
`juni:243` **Juni (neutral):** Oh. Right. Yeah.  
`juni:244` The waterbed sloshes. The ripples on the ceiling keep moving.  
> *(end of choice)*

`juni:246` Juni's sleeve drifts up toward the hood strings. It hovers there.  
> *show juni neutral*  

> **Choice**
`juni:249` **Juni:** I've been thinking about taking it down. The hood. Not right now. But... soon. Would that be weird?  

`juni:251` **▸** "Whenever you want. Or never. Both are good."  
> *rapport +2 Juni*  
`juni:253` **Juni (blush):** Okay.  
`juni:254` **Juni:** Okay. Thank you. That's... it's easier when nobody's waiting for it.  

`juni:256` **▸** "I'd really like to see your face. Your whole face."  
> *rapport +1 Juni*  
`juni:258` **Juni (neutral):** ...Soon. I think. Maybe.  
`juni:259` Their sleeve stays on the strings a long time. Then it drops.  

`juni:261` **▸** "Do it now! Come on!"  
> *rapport −1 Juni*  
`juni:263` **Juni (surprised):** Oh. Um. No. Not now.  
`juni:264` Juni pulls the strings tight. The hood closes around their face like a flower at night.  
> *(end of choice)*

> *if rapport["juni"] >= ROMANCE_THRESHOLD:*  
`juni:267` **Juni (blush):** Hey. After the ark... find me? If you want. I'll be the pink one.  
> *else:*  
`juni:269` **Juni (neutral):** I should go find my roommate before the ark. See you around, okay?  

## juni_romance

> *scene bg pool*  
`juni:277` The ballroom is still going when you slip out. The hallways are full of people sitting against the walls in pairs, talking quietly, capes folded into pillows.  
`juni:278` You take the back stairs down to the ground floor. The pool hall is empty. The Pool People's banner is lying in a heap by the towel hut, and somebody has tucked it in like a blanket.  
`juni:279` The water is perfectly still. Through the old glass roof, the sky over the mountains is just starting to turn gray.  
`juni:280` And at the edge of the pool, exactly where you first saw them, there's a pink shape with its onesie feet in the water.  
> *show juni neutral*  
`juni:282` **Juni:** You came.  
`juni:283` **Juni:** I had a whole plan if you didn't come. It involved crying into the pool. Very damp. Very on-theme.  
`juni:284` You sit down next to them and put your feet in. The water is cold enough to make you gasp. Juni laughs at you, a little, which seems fair.  
`juni:285` **Juni:** Cold-water creature. Told you.  

> **Choice**
`juni:288` **Juni:** So. How was your first time? Honestly.  

`juni:290` **▸** "I came here not knowing who I'd meet. Now I know a salamander."  
`juni:291` **Juni (happy):** A full salamander. You were promoted. It's on your permanent record.  

`juni:292` **▸** "Honestly? The best part was the pizza slices."  
> *(shown if pool_seen["juni"] >= 2)*  
`juni:293` **Juni (happy):** The crust one. I knew you'd appreciate the crust one. Nobody appreciates the crust one.  
> *(end of choice)*

> *show juni neutral*  
> *if night_seen["juni"] >= 1:*  
`juni:297` For a while you just talk. About Room 404, and the man in beige who might still be in there, insisting he doesn't exist.  
> *else:*  
`juni:299` For a while you just talk. About the weekend, the rooms, the people in capes, the herald who lost his voice.  
> *if juni_has_courage:*  
`juni:301` **Juni:** I keep thinking about the courage card from the Lost & Found. I carried it around all weekend in the hood. It's soggy now. I went in the pool twice with it.  
`juni:302` They hold it up. The card is warped and soft now, the word COURAGE bleeding blue at the edges.  
`juni:303` **Juni:** I'm going to use it now. Is that okay?  
> *else:*  
`juni:305` **Juni:** There's a Lost & Found upstairs where you can take a card that says COURAGE. I never got one. I kept chickening out.  
`juni:306` **Juni:** So I'm going to try it without the card. Is that okay?  
`juni:307` **Juni:** You can look away if you want. Actually, don't look away. Please don't look away.  
`juni:308` Juni reaches up with both sleeves and pulls the hood strings loose. Their hands shake a little. They take a breath like they're about to go underwater.  
`juni:309` Then, slowly, they push the hood back.  
`juni:310` Lotl falls down their back, gills and all, and lands in the pool with a soft pink splash.  
`juni:311` Underneath is short dark hair stuck flat with sweat, and ears you've never seen, and a jaw, and a neck, and a face that's all the way there for the first time all weekend.  
> *show juni blush*  
`juni:313` **Juni:** Hi. This is... the rest of me.  
`juni:314` **Juni:** It's really cold out here without it. Huh. I forgot what air felt like. On the ears. Ears are so weird.  

> **Choice**

`juni:317` **▸** "Hi, Juniper."  
`juni:318` **Juni (happy):** Oh no. Oh, that's so much worse than I thought. In a good way. In a terrible, good way.  
`juni:319` **Juni (blush):** Nobody's said it like that before. Like it wasn't a punishment.  

`juni:320` **▸** "Hi, Juni. It's nice to meet all of you."  
`juni:321` **Juni (happy):** All of me. Yeah. That's everyone. That's the whole cast.  
`juni:322` **Juni (blush):** It's a small cast. But everyone showed up.  
> *(end of choice)*

> *show juni blush*  
`juni:325` The sky above the glass roof goes from gray to pale pink. Somewhere upstairs, a single kazoo is playing something slow.  
`juni:326` **Juni:** Three years I've been coming here. Three years I've been standing outside doors, waiting for someone to pull me in.  
`juni:327` **Juni:** And this year I spent the whole time hoping it'd be you. And it was. Every time. Even when I didn't wait.  
`juni:328` **Juni:** I don't know what happens Monday. I'll go back to fixing the thing. My manager will call me Junebug. My phone is still in the ice bucket, by the way.  
`juni:329` **Juni:** But I think I want there to be a you on Monday. If that's... if you want that too.  

> **Choice**

`juni:332` **▸** "I want that too."  
`juni:333` **Juni (blush):** Okay. Okay. Good. Great. I'm going to be so normal about this.  

`juni:334` **▸** Take their hand, sleeve and all.  
`juni:335` You find their hand inside the sleeve. It's warm and a little damp and holding on very tightly.  
`juni:336` **Juni (blush):** ...Yeah. That's an answer.  
> *(end of choice)*

`juni:338` **Juni (blush):** Can I ask you something? I'm out of courage, so I'm just going to do it raw.  
`juni:339` **Juni:** Can I kiss you?  

> **Choice**

`juni:342` **▸** "Yes."  
`juni:343` Juni leans over the water. They smell like chlorine and laundry and the tea bar's cardamom.  
`juni:344` It's a small kiss, a careful one. The kind that asks again halfway through. You answer.  
`juni:345` When you pull apart, Juni has their eyes shut tight, like they're making a wish.  

`juni:346` **▸** "Can I hold your hand first?"  
`juni:347` **Juni (happy):** Yes. Yes, please. Sleeve's empty, it's just a hand in there.  
`juni:348` Their fingers lace through yours. After a while it's the most natural thing in the world to lean in, so you both do.  
`juni:349` It's a small kiss, a careful one. Juni laughs into it, just once, from pure surprise.  
> *(end of choice)*

> *show juni happy*  
`juni:352` **Juni:** Okay. Okay. I regenerated something. I'm pretty sure. I don't know what yet, but something grew back.  
> *scene bg pool*  
`juni:355` The sun comes up over the mountains and pours down through the old glass roof, across the water, gold on every ripple.  
`juni:356` Juni's hood floats behind you in the pool, gills spread out on the water, smiling up at the sky.  
`juni:357` Neither of you goes to fish it out. Eventually a Pool Person in a gold cape wades in, rescues it with great ceremony, and hangs it on the lifeguard chair to dry, like a flag.  
> *scene black*  
`juni:359` {i}Monday, 9:14 AM. A text from an unknown number.{/i}  
`juni:360` **Juni:** hi it's juni. juniper. it's me. I sang in the car the whole way home. windows down. it was so bad. a man at a stoplight clapped  
`juni:361` **Juni:** I took the phone out of the ice bucket. 41 messages from work. I answered none of them. I answered this one  
`juni:362` **Juni:** are you free thursday. I know a place with a very good crust  
> *→ jump ending_card*  

## juni_friend

> *scene bg exterior*  
> *show juni happy*  
`juni:372` In the parking lot on Monday morning, a pink kigurumi waves at you from a dented hatchback. The hood is still up. Lotl looks a little sunburned.  
`juni:373` **Juni:** Hey! Probationary salamander! You passed. You're a full salamander now. It's binding. There's paperwork.  
`juni:374` **Juni (neutral):** I wanted to say... thanks. For finding me. Every time. I talked to eleven people this year. Eleven. You were most of them.  
`juni:375` **Juni:** Next year I'm going to try going into a room by myself. Just one. A small one. Maybe the one with the moss.  
`juni:376` **Juni (happy):** And if I chicken out, you're responsible for me. That's the rule. You know my secret.  
`juni:377` They hug you through the onesie, which is like being hugged by a very determined pillow.  
`juni:378` **Juni:** Same time next year? I'll stand outside a door and you can pull me in.  

---

# gerald.rpy

## gerald_pool_1

`gerald:5` In the shallow end, a seven-foot Sasquatch is sitting in a children's innertube shaped like a duck. He holds a white teacup above the water with enormous delicacy.  
> *show gerald neutral*  
`gerald:7` **Gerald:** Good afternoon. Forgive me if I don't stand. I am buoyant at present, and it took some time to achieve.  
`gerald:8` **Gerald:** Gerald. A pleasure.  

> **Choice**

`gerald:10` **▸** "Is that a real Sasquatch?"  
`gerald:11` **Gerald:** Is that a real person?  
`gerald:12` You open your mouth to answer.  
`gerald:13` **Gerald:** Ah, ah. I find it's best not to ask. Things get so much smaller once you've asked.  

`gerald:15` **▸** "Want me to hold your tea so you can actually swim?"  
> *rapport +2 Gerald*  
`gerald:17` **Gerald (surprised):** Oh. Oh, would you?  
`gerald:18` You take the cup. It's still hot. It smells like smoke and pine.  
`gerald:19` **Gerald (happy):** Lapsang souchong. Thank you. I have been holding that cup at shoulder height for forty minutes.  
`gerald:20` Gerald sinks gratefully into the water up to his chin. The fur fans out around him like seaweed.  

`gerald:22` **▸** "How's the water?"  
> *rapport +1 Gerald*  
`gerald:24` **Gerald (neutral):** Wet. Chlorinated. There are a great many people's feelings in it. It's quite pleasant once you stop thinking about that.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:27` Gerald explains, at length, that chlorine is hell on fur. It takes forty years to get a coat like this. He's mostly here for the company.  
`gerald:28` **Gerald:** You'll have seen the famous film, I suppose. 1967. The one where my kind walks across the creek bed and looks back over his shoulder.  
`gerald:29` **Gerald:** That was my cousin Bernard. Bad knee. That's why he walks like that. He has been embarrassed about it for sixty years.  
`gerald:30` **Gerald:** Everyone at home has a story like that. A camera in the woods. A flash. A blur. And then a hundred years of people arguing over whether you're real.  
`gerald:31` **Gerald:** Here, nobody takes pictures. You can't imagine what that means to someone like me.  

> **Choice**

`gerald:34` **▸** "I won't take your picture. Not this weekend, not ever. I promise."  
> *rapport +2 Gerald*  
`gerald:36` **Gerald (happy):** I believe you.  
`gerald:37` **Gerald:** That's rarer than you'd think. Most people promise with their phone already in their hand.  

`gerald:39` **▸** "Do you ever get lonely? Being a legend?"  
> *rapport +1 Gerald*  
`gerald:41` Gerald is quiet for a while. A pool noodle drifts past.  
`gerald:42` **Gerald (neutral):** Legends are always lonely. That's what makes them legends. Nobody throws a legend a birthday party.  

`gerald:44` **▸** "You could make a fortune on YouTube, you know."  
`gerald:45` **Gerald (neutral):** Yes. So I'm told. By everyone. Constantly.  
`gerald:46` He sinks a little lower in the water.  
> *(end of choice)*

`gerald:49` When you leave, Gerald raises his teacup to you in salute. Not one drop spills.  

## gerald_pool_2

`gerald:54` On the pool deck, a dozen people lie flat on beach towels with their eyes closed. Gerald walks slowly between them, speaking in a voice like a cello.  
> *show gerald neutral*  
`gerald:56` **Gerald:** You are moss. You have been moss for a thousand years. Nothing is required of moss. Moss does not check its email.  
`gerald:57` **Gerald (happy):** Ah. You. There's a towel free. Would you care to be moss?  
`gerald:58` You lie down. The concrete is warm through the towel. Gerald stands over you like weather.  
> *show gerald neutral*  

> **Choice**
`gerald:61` **Gerald:** And what kind of moss are you today?  

`gerald:63` **▸** "Reindeer moss. Soft, but I can survive pretty much anything."  
> *rapport +2 Gerald*  
`gerald:65` **Gerald (happy):** Cladonia rangiferina. Excellent choice. Technically a lichen, but we don't police that here.  
`gerald:66` **Gerald:** Soft and survives anything. Yes. I can see that in you.  

`gerald:68` **▸** "Just regular green moss. Doing my best."  
> *rapport +1 Gerald*  
`gerald:70` **Gerald (neutral):** Regular green moss is the backbone of the forest. Never let anyone tell you otherwise.  

`gerald:72` **▸** "I don't think I'm a moss person."  
`gerald:73` **Gerald (neutral):** Everyone is a moss person given enough time. Lie there a while longer.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:76` After the session, Gerald sits down beside you. The deck creaks.  
`gerald:77` **Gerald:** I live up north, in the Klamath. Old growth. Trees so tall the light goes green by the time it reaches you.  
`gerald:78` **Gerald:** It's been getting quieter there. Fewer of us every decade. Some moved to Canada. Some just stopped coming to the creek.  
`gerald:79` **Gerald:** I came here the first time because a friend said there'd be seven hundred people pretending to be strange creatures.  
`gerald:80` **Gerald:** It's the closest thing I've had to a family reunion in thirty years.  

> **Choice**

`gerald:83` **▸** "Then I'm really glad you came. I'm glad I met you."  
> *rapport +2 Gerald*  
`gerald:85` **Gerald (happy):** ...  
`gerald:86` **Gerald:** So am I. Very much.  
`gerald:87` He pats your shoulder once, very gently. His hand covers most of your back.  

`gerald:89` **▸** "Do you have family, back home?"  
> *rapport +1 Gerald*  
`gerald:91` **Gerald (neutral):** A sister. Margaret. She does not believe in parties. She believes in roots, and grudges, and the creek.  
`gerald:92` **Gerald (happy):** I'll tell her about you. She'll pretend not to care.  

`gerald:94` **▸** "That's kind of sad, honestly."  
`gerald:95` **Gerald (neutral):** Yes. It is. But sad and good can sit at the same table. They often do.  
> *(end of choice)*

## gerald_night_1

> *scene bg breakfast*  
`gerald:103` You follow the commotion into a room transformed into a cathedral of breakfast. On one wall: the black banner of the CHURCH OF CAST IRON. On the other: the white banner of the TEMPLE OF TEFLON.  
`gerald:104` On the altar between them sits the Holy Skillet, a single fried egg glowing in it under a spotlight.  
`gerald:105` In the middle of all this, Gerald is being pulled in two directions by two people in liturgical robes.  
> *show gerald surprised*  
`gerald:107` **Deacon of Cast Iron:** The Great Hairy One has always been ours! He cooks on hot stones! Stones are the original cast iron!  
`gerald:108` **High Priestess of Teflon:** Blasphemy! Look at him! Nothing sticks to him! He is the living embodiment of the nonstick way!  
`gerald:109` **Gerald:** I really must protest. A great deal sticks to me. Burrs. Leaves. Small birds, occasionally.  

> **Choice**

`gerald:112` **▸** Step in: "He's with me. We're Waffle-Iron Independents."  
> *rapport +2 Gerald*  
`gerald:114` Both clergy gasp. A heretic! A third way!  
`gerald:115` **Deacon of Cast Iron:** Waffle iron... is that... is that allowed?  
`gerald:116` **Gerald (happy):** It is now. I'm its prophet. And this is my acolyte.  

`gerald:118` **▸** "Gerald, what do {i}you{/i} actually cook eggs in?"  
> *rapport +1 Gerald*  
`gerald:120` **Gerald (neutral):** ...A flat rock. Heated by the sun. On a good day.  
`gerald:121` Both cults fall silent. Somewhere in the back, someone whispers {i}the Church of the Rock{/i}, and a third religion is born.  

`gerald:123` **▸** Kneel before the Church of Cast Iron.  
`gerald:124` **Deacon of Cast Iron:** A convert! Seize the Great Hairy One while the Teflons are distracted!  
`gerald:125` Instead, the Teflons seize Gerald. It takes you ten minutes and a lot of apologizing to get him back.  
`gerald:126` **Gerald (neutral):** That was... an experience.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:129` The clergy circle back. They aren't done.  
`gerald:130` **High Priestess of Teflon:** Then let the Great Hairy One's companion decide! Cast iron or Teflon? The schism must be resolved!  

> **Choice**
`gerald:132` **Gerald:** I'm afraid they won't let either of us leave until someone chooses.  

`gerald:134` **▸** "Why not both? Cast iron for steak. Nonstick for eggs."  
> *rapport +2 Gerald*  
`gerald:136` The room goes silent. The High Priestess of Teflon drops her spatula. The Deacon of Cast Iron begins to weep.  
`gerald:137` **Deacon of Cast Iron:** It was... both... all along...  
`gerald:138` They embrace across the altar. Their congregations follow. Gerald leans down to you.  
`gerald:139` **Gerald (happy):** Do you know, I think that's the wisest thing anyone has said all weekend.  

`gerald:141` **▸** "Can I grab your hand? We're running."  
> *rapport +1 Gerald*  
`gerald:143` **Gerald (happy):** Please.  
`gerald:144` You run out of the cathedral hand in enormous hand. The cults chase you for half a hallway before they get distracted by a tray of waffles.  

`gerald:146` **▸** "Teflon. Obviously."  
`gerald:147` The Church of Cast Iron howls. A pancake is thrown. A small and largely theatrical riot breaks out.  
`gerald:148` **Gerald (neutral):** Well. We tried.  
> *(end of choice)*

## gerald_night_2

> *scene bg hallway*  
`gerald:156` Gerald is standing in front of Room 312, not going in. Rain sounds and the smell of cedar drift out through the door.  
> *show gerald neutral*  
`gerald:158` **Gerald:** It smells like home in there. Someone's built a whole forest. Moss and fog and creek sounds.  
`gerald:159` **Gerald:** I'm afraid that if I go in, I'll miss it too much to come back out.  

> **Choice**

`gerald:161` **▸** "We can go in together. And we can leave the second you want to."  
> *rapport +2 Gerald*  
`gerald:163` **Gerald (happy):** ...All right. Yes. Together.  

`gerald:165` **▸** "Then let's stay out here. We can listen from the doorway."  
> *rapport +1 Gerald*  
`gerald:167` You stand in the doorway with him for a long while. Eventually he takes one step in, and then another.  

`gerald:169` **▸** "It's just a hotel room with moss in it, Gerald."  
`gerald:170` **Gerald (neutral):** Yes. Of course. You're right.  
`gerald:171` He goes in anyway. You're not sure if you helped.  
> *(end of choice)*

> *scene bg forest*  
> *show gerald neutral*  
`gerald:175` Inside, the carpet is moss, real moss, cool and damp under your shoes. Fog rolls across the floor. Fireflies, or something like them, blink in the dark between painted trees.  
`gerald:176` Gerald lies down on what used to be the hotel bed. It's covered in moss too. He fits, barely.  
`gerald:177` **Gerald:** There's a creek near my place that sounds just like this. In September, when the salmon come back.  
`gerald:178` **Gerald:** Would you sit with me? Not talk. Just be here. I find it's hard to be quiet with people. Most people want me to do something.  

> **Choice**

`gerald:181` **▸** Sit beside him in silence.  
> *rapport +2 Gerald*  
`gerald:184` You sit. The creek sounds go on. A firefly lands on Gerald's arm and stays there.  
`gerald:185` ...  
`gerald:186` ...  
`gerald:187` After a long time, Gerald lets out a breath so deep the fog moves.  
`gerald:188` **Gerald (happy):** Thank you. I didn't know how much I needed that.  

`gerald:190` **▸** Hum softly, something without words.  
> *rapport +1 Gerald*  
`gerald:192` Gerald closes his eyes. After a minute, he hums along, an octave below you, so low you feel it in the bed frame.  

`gerald:194` **▸** "So what's the actual difference between Bigfoot and Sasquatch?"  
`gerald:195` **Gerald (neutral):** ...Marketing.  
`gerald:196` He chuckles. It's a nice chuckle. But the quiet is gone.  
> *(end of choice)*

## gerald_night_3

> *scene bg cryptid*  
`gerald:204` CRYPTIDS ANONYMOUS, says the banner. Below it: you are not blurry here.  
`gerald:205` A circle of folding chairs. An inflatable Loch Ness Monster with a HELLO MY NAME IS sticker. The facilitator is a person in a Mothman costume with glowing red eyes, holding a styrofoam cup of coffee.  
> *show gerald neutral*  
`gerald:207` Gerald is sitting in one of the folding chairs. It's comically too small. His knees are up around his shoulders. He waves you over.  
`gerald:208` **Mothman:** Welcome, welcome. Is there anyone who'd like to share tonight?  
`gerald:209` Gerald's hand goes up halfway, then down again.  
`gerald:210` **Gerald (neutral):** I... would you stay close? I've come to this meeting for four years and I have never once shared.  
`gerald:211` He stands. The chair stands with him for a second before falling off.  
`gerald:212` **Gerald:** My name is Gerald. And I have been... blurry. For about sixty years.  
`gerald:213` **Mothman:** Hi, Gerald.  
`gerald:214` Gerald stops. He looks at the floor. The room waits.  

> **Choice**

`gerald:217` **▸** Quietly: "Can I put my hand on your shoulder?"  
> *rapport +2 Gerald*  
`gerald:219` **Gerald (neutral):** Yes. Please.  
`gerald:220` You reach up. You have to reach quite a long way. His fur is warm.  

`gerald:222` **▸** "Take your time. We're not going anywhere."  
> *rapport +1 Gerald*  
`gerald:224` The circle murmurs agreement. Nessie bobs gently in the air conditioning.  

`gerald:226` **▸** Start clapping to encourage him.  
`gerald:227` **Mothman:** Ah, we snap here, friend. Clapping is very loud for some of the members.  
`gerald:228` Everyone snaps instead. Gerald gives you a small, forgiving look.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:231` **Gerald:** Everyone wants proof of me. Footprints. Hair samples. A clearer photo. They've been chasing proof of me my whole life.  
`gerald:232` **Gerald:** Nobody has ever just... wanted me. Not the evidence. Me.  
`gerald:233` **Gerald:** That's all. That's my share.  
`gerald:234` The circle snaps for a very long time. The Mothman wipes his eyes under the mask. Then he turns to you.  
`gerald:235` **Mothman:** And you, friend of Gerald? What are you not blurry about tonight?  

> **Choice**

`gerald:238` **▸** "I'm not blurry about Gerald. He's the realest person I've met all weekend."  
> *rapport +2 Gerald*  
`gerald:241` **Gerald (blush):** ...  
`gerald:242` Gerald doesn't say anything. But he sits back down, carefully, very close to you.  

`gerald:244` **▸** "I came here not knowing who I'd be. I think I'm finding out."  
> *rapport +1 Gerald*  
`gerald:246` **Mothman:** That's the whole thing, isn't it. Thank you.  
`gerald:247` **Gerald (happy):** Well said.  

`gerald:249` **▸** "Honestly? I'm just here for the coffee."  
`gerald:250` The room laughs. Gerald laughs too, a big rolling laugh that knocks Nessie off her stand.  
`gerald:251` **Gerald (happy):** The coffee is genuinely excellent here. You're not wrong.  
> *(end of choice)*

> *if rapport["gerald"] >= ROMANCE_THRESHOLD:*  
`gerald:254` **Gerald (blush):** After the ark, I'll be on the roof. It's the only place tall enough for me to see the sunrise properly. If you'd like to see it too.  
> *else:*  
`gerald:256` **Gerald (neutral):** Enjoy the ark. Don't let them get you in the eye with the confetti. It's biodegradable but it is relentless.  

## gerald_romance

> *scene bg roof_dawn*  
`gerald:264` The stairwell to the roof is propped open with a waffle iron. Someone from the Breakfast Schism has left it there, as a blessing or a warning.  
`gerald:265` At the top, the air is cold and smells like pine and lake water. The string lights have mostly burned out. The rigging that held the ark hangs slack.  
`gerald:266` Gerald is sitting on the edge by the water tank, enormous against the pink sky, holding two teacups. One of them is for you. It's still warm.  
> *show gerald happy*  
`gerald:268` **Gerald:** You came. I had a speech prepared in case you didn't. It was very dignified. Lots of nature metaphors. A bit about a fallen log.  
`gerald:269` **Gerald (neutral):** I'm glad I don't need it. It was mostly about the log.  
`gerald:270` You sit beside him. The bench creaks under his weight and then, with a kind of resignation, holds.  
`gerald:271` **Gerald:** Lapsang souchong. I brought my own leaves. The tea bar means well, but they keep putting cardamom in everything.  

> **Choice**
`gerald:274` **Gerald:** Did you enjoy the ark? I confess I wept. A great deal. I had to borrow a towel from Wren.  

`gerald:276` **▸** "I cried too. Over a rubber duck."  
`gerald:277` **Gerald (happy):** Over a rubber duck. Yes. Seven hundred people. One duck. It was the most profound thing I've seen in decades.  

`gerald:278` **▸** "I mostly watched you crying."  
`gerald:279` **Gerald (blush):** Oh dear. Was it very loud? I'm told I sound like a foghorn when I'm moved.  
`gerald:280` **Gerald (happy):** ...It was a beautiful duck, though.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:283` For a while you just watch the light come up. A bird starts somewhere down in the pines, then another one.  
> *if sat_with_gerald:*  
`gerald:285` **Gerald:** When we were in the forest room, you sat with me without saying anything. Do you remember? For a long time.  
`gerald:286` **Gerald:** I haven't done that with anyone since I was young. Just sat. It's the hardest thing to find, a person who'll just sit.  
> *else:*  
`gerald:288` **Gerald:** Do you know what I'll remember from this weekend? Not the rooms. Not even the ark. The quiet bits in between, with you.  
`gerald:289` **Gerald:** It's the hardest thing to find, a person who'll just sit.  
> *if vouched_for_gerald:*  
`gerald:291` **Gerald:** And at the meeting. When the Mothman asked. What you said about me.  
`gerald:292` **Gerald (blush):** I've thought of very little else, if I'm honest.  
> *show gerald neutral*  
`gerald:295` **Gerald:** I go home tomorrow. Back to the creek. My sister Margaret will ask where I've been and I'll say {i}nowhere{/i}, which is what we always say.  
`gerald:296` **Gerald:** That's how it is with my kind. We are always coming from nowhere and going nowhere, so nobody can follow us there.  
`gerald:297` **Gerald (blush):** But I'd like to say {i}somewhere{/i} this time. I'd like there to be a somewhere. And a someone in it.  

> **Choice**

`gerald:300` **▸** "There is. I'm right here."  
`gerald:301` **Gerald (blush):** Yes. You are. You're entirely in focus.  

`gerald:302` **▸** Lean against his side.  
`gerald:303` Gerald goes very still, the way you'd go still if a deer walked up to you. Then, slowly, an arm the size of a tree branch settles around your shoulders.  
`gerald:304` **Gerald (blush):** Oh. Oh, that's... yes. That's very good. Let's stay exactly like this.  
> *(end of choice)*

> *show gerald neutral*  
`gerald:307` The sun touches the top of the mountains across the lake. Everything turns gold: the gravel, the water tank, the fur on Gerald's arm.  
`gerald:308` **Gerald:** May I tell you something about the famous film? Not Bernard's. Mine.  
`gerald:309` **Gerald:** There's a hiker in Oregon, 1994, who got a picture of me by a river. Blurry, naturally. She sold it to a magazine. It's still in a museum somewhere, labeled HOAX.  
`gerald:310` **Gerald:** I was crying in that picture. I'd just lost someone. And for thirty years I've been a hoax who was crying.  
`gerald:311` **Gerald (happy):** This weekend I've just been Gerald. Nobody wanted proof. You least of all.  

> **Choice**

`gerald:314` **▸** "You were never a hoax."  
`gerald:315` **Gerald (blush):** ...Thank you. I may need to hear that several more times. Over a number of years.  

`gerald:316` **▸** "I'd still like to know you better than any photo."  
`gerald:317` **Gerald (blush):** Then you'll have to come to the creek. The salmon come back in September. It's very loud and very smelly and I think you'd love it.  
> *(end of choice)*

> *if pool_seen["gerald"] >= 2:*  
`gerald:320` **Gerald (blush):** May I ask you something very forward? I've been thinking about it since the moss.  
> *else:*  
`gerald:322` **Gerald (blush):** May I ask you something very forward? I've been thinking about it all weekend.  
`gerald:323` **Gerald:** May I kiss you? I'll understand completely if the logistics seem... daunting.  

> **Choice**

`gerald:326` **▸** "Yes. I'll meet you halfway."  
`gerald:327` He bends down. You stretch up. It takes some engineering, and at one point a teacup goes over the edge of the roof.  
`gerald:328` It's worth it. His fur smells like cedar smoke and pool water. He kisses like he's afraid you're a mirage, very gently, ready to stop.  
`gerald:329` You don't let him stop.  

`gerald:330` **▸** Stand up on the bench so you're eye to eye.  
`gerald:331` **Gerald (happy):** Oh, that's clever. That's very clever.  
`gerald:332` Eye to eye, he's suddenly shy. You close the distance. He kisses you so gently you could almost think you imagined it, except you know you didn't.  
> *(end of choice)*

> *show gerald happy*  
`gerald:335` **Gerald:** Well. I'm going to have to tell Margaret {i}something{/i} now.  
> *scene bg roof_dawn*  
`gerald:338` The sun clears the mountains. Down in the parking lot, somebody with a camera looks up at the roof, squints, and sees only a blur.  
`gerald:339` Gerald laughs so hard the water tank rings like a bell.  
`gerald:340` You stay up there until the last cars leave, until the Pool People fold their banner, until Wren comes up to tell you the casino has been closed since 1987 and the hotel is only now finding out.  
> *scene black*  
`gerald:342` {i}Three weeks later, a package arrives with no return address. Inside: a tin of lapsang souchong, a pressed fern, a smooth gray stone from a creek, and a postcard of the Klamath.{/i}  
`gerald:343` {i}On the back, in very careful handwriting:{/i}  
`gerald:344` **Gerald:** The salmon are back. Margaret says to bring a raincoat and that she doesn't care either way if you come. She has cleaned the whole cabin twice. — G.  
`gerald:345` **Gerald:** P.S. The stone is for your pocket. Ours are full of them. It's how we remember where we've been.  
> *→ jump ending_card*  

## gerald_friend

> *scene bg exterior*  
> *show gerald happy*  
`gerald:355` As the cars pull out on Monday morning, you find Gerald at the edge of the parking lot, packing an absurdly small suitcase.  
`gerald:356` **Gerald:** Ah. My friend. I hoped I'd see you before the road.  
`gerald:357` **Gerald (neutral):** I've been coming to these for years and I usually leave the way I came. Quietly. From nowhere, to nowhere.  
`gerald:358` **Gerald (happy):** This time I'm leaving with a friend. It's a very strange feeling. Like having a pocket full of warm stones.  
`gerald:359` He presses a teabag into your hand. Lapsang souchong. It smells like a campfire in the rain.  
`gerald:360` **Gerald:** If you're ever up north, follow the creek. Don't bring a camera. Just call my name. I'll hear.  
`gerald:361` He walks up the road toward the pines, a teacup in one hand. At the top he turns and waves, once, over his shoulder.  
`gerald:362` It looks exactly like the famous film. Except it isn't blurry at all.  

---

# solstice.rpy

## solstice_pool_1

`solstice:5` A woman in rainbow fur leg warmers, holographic shorts and a black crop top studded with little LEDs is working her way down the row of loungers, handing out glitter like it's communion.  
`solstice:6` She has goggles pushed up on her forehead and a sticker of a star under one eye. She reaches you and lights up, literally. Her top flickers through the rainbow.  
> *show solstice happy*  
`solstice:8` **Solstice:** HI! Hi hi. You're new. You have new-person energy. It's so cute. Hold out your hand. No, the other one. Perfect.  
`solstice:9` She produces a bracelet of plastic beads from somewhere. It says, in lettered beads, ur doing great.  

> **Choice**

`solstice:11` **▸** Hold out your wrist and let her put it on.  
> *rapport +1 Solstice*  
`solstice:13` **Solstice (happy):** There. Now you're one of us. That's how it works. That's literally the whole ritual.  

`solstice:15` **▸** "Wait, I want to give you something too."  
> *rapport +2 Solstice*  
`solstice:18` You dig in your pockets. All you have is a hotel mint, slightly warm.  
`solstice:19` **Solstice (surprised):** For me?  
`solstice:20` **Solstice (blush):** Oh my god. No one ever gifts back. Everyone just takes the glitter and runs.  
`solstice:21` She holds the mint up to the light like a jewel, then puts it very carefully into a pocket on her leg warmer.  
`solstice:22` **Solstice (happy):** I'm going to keep this forever. Or eat it at three in the morning. One of the two.  

`solstice:24` **▸** "Oh, I didn't bring anything to trade."  
`solstice:25` **Solstice (neutral):** It's not a trade! It's a gift! Gifts don't do math!  
`solstice:26` She puts the bracelet on you anyway, with a firm little pat.  
> *(end of choice)*

> *show solstice happy*  
`solstice:29` **Solstice:** I'm Solstice. Like the longest day of the year. Because I go all night and all day. Also because I get up at four in the morning most days, so the joke works both ways.  
`solstice:30` **Solstice:** Okay, important question.  

> **Choice**
`solstice:32` **Solstice:** Can I give you a glitter baptism?  

`solstice:34` **▸** "Baptize me."  
> *rapport +2 Solstice*  
`solstice:36` She upends an entire jar over your head. It is a lot of glitter. It will still be in your ears in March.  
`solstice:37` **Solstice (happy):** Welcome to the church of SPARKLE. You are SAVED.  

`solstice:39` **▸** "Just a little. On the cheeks."  
> *rapport +1 Solstice*  
`solstice:41` She dabs glitter under your eyes with one fingertip, very gently, like painting a tiny face.  
`solstice:42` **Solstice (happy):** Perfect. Subtle. Mysterious. You look like a sad disco ghost. I mean that as the highest compliment.  

`solstice:44` **▸** "I'm good, thanks."  
`solstice:45` **Solstice (neutral):** Respect! Consent is sexy! Also glitter is forever, so honestly, smart call.  
> *(end of choice)*

`solstice:47` **Solstice (happy):** See you on the dance floor, new person!  
`solstice:49` She bounces off to the next lounger. Her top blinks HAPPY HAPPY HAPPY in scrolling letters across her back.  

## solstice_pool_2

`solstice:54` Solstice is asleep on a lounger right under one of the pool hall's big orange heat lamps. Her LED top is switched off. Her goggles are over her eyes. Her shoulders are going pink.  
`solstice:55` Without the lights and the noise, she looks younger. And very tired.  

> **Choice**

`solstice:57` **▸** Quietly swing the heat lamp away from her.  
> *rapport +2 Solstice*  
`solstice:59` You swivel the heat lamp away, slowly, so it doesn't squeak. The orange glow slides off her face.  
`solstice:60` A few minutes later she stirs, pushes up her goggles and looks at the heat lamp, then at you.  
> *show solstice blush*  
`solstice:62` **Solstice:** Did you... do that? For me?  
`solstice:63` **Solstice:** Huh. Nobody does stuff for me. I'm usually the one doing stuff.  

`solstice:65` **▸** Gently wake her: "Hey. You're getting burned."  
> *rapport +1 Solstice*  
> *show solstice surprised*  
`solstice:68` **Solstice:** Wha—oh. OH. Oh no, I'm a lobster. Thank you. Thank you, oh my god.  

`solstice:70` **▸** Let her sleep. She clearly needs it.  
`solstice:71` You leave her be. Half an hour later you hear a shriek from across the deck.  
> *show solstice surprised*  
`solstice:73` **Solstice:** OW. Why didn't anyone—ha. It's fine. It's fine! I'll be a shiny red raver. New look.  
> *(end of choice)*

> *show solstice neutral*  
`solstice:76` She sits up. She doesn't turn the lights back on.  
`solstice:77` **Solstice:** I'm a nurse. ICU. Nights. I spend all week with people on the worst night of their lives.  
`solstice:78` **Solstice:** And then I come here and dance like it's the best one. Every year. I think if I stop dancing, the other thing catches up.  
`solstice:79` **Solstice:** When the lights are on, everyone loves me. Solstice! Glitter girl! When they're off, I'm just... tired. Really, really tired.  

> **Choice**

`solstice:82` **▸** "I like you with the lights off too."  
> *rapport +2 Solstice*  
`solstice:84` **Solstice (blush):** ...  
`solstice:85` **Solstice:** That's... wow. Okay. You can't just say things like that at the pool. That's a ballroom thing to say. At least.  

`solstice:87` **▸** "That sounds exhausting. Do you ever get to rest?"  
> *rapport +1 Solstice*  
`solstice:89` **Solstice (neutral):** Rest is... I'm bad at rest. Rest is where the thoughts are.  
`solstice:90` **Solstice:** But this was nice. Right now. This was rest, kind of.  

`solstice:92` **▸** "Turn them back on! You're so much fun when they're on."  
`solstice:93` **Solstice (neutral):** Yeah. Ha. Yeah.  
`solstice:94` She flicks the switch. The top blazes back to life. Her smile comes on with it, a half-second late.  
> *(end of choice)*

## solstice_night_1

> *scene bg exchange*  
`solstice:102` The Human Stock Exchange is roaring. Tickers crawl across the walls in red and green: SELF ▲4.2. VIBES ▼1.1. GLITTER ▲99.  
`solstice:103` Mute clowns in bras and fishnets run between the trading desks, pantomiming panic and euphoria. The air is full of confetti.  
> *show solstice happy*  
`solstice:105` **Solstice:** THERE you are! Okay, I just bought forty percent of you! Don't let me down! Diversify your feelings!  
`solstice:106` A clown runs up to you and mimes, frantically, an offer. They're pointing at Solstice. Her ticker is on the wall: SOLSTICE ▲2.0.  

> **Choice**

`solstice:108` **▸** Buy as many shares of Solstice as you can.  
> *rapport +2 Solstice*  
`solstice:110` You buy and buy. The clown mimes a heart attack of joy. On the wall, her ticker rockets: SOLSTICE ▲88.8.  
`solstice:111` **Solstice (surprised):** Oh my god. I'm a blue chip. I'm a BLUE CHIP!  
`solstice:112` **Solstice (happy):** Mutual investment! We own each other now! That's basically marriage on this floor!  

`solstice:114` **▸** Short-sell Solstice.  
> *rapport +1 Solstice*  
`solstice:116` The clown gasps silently and hands you a little paper slip marked SHORT. Her ticker dips.  
`solstice:117` **Solstice (surprised):** You absolute CAPITALIST!  
`solstice:118` **Solstice (happy):** I respect it. I hate it. I respect it.  

`solstice:120` **▸** Don't trade. Just watch the chaos.  
`solstice:121` The clown stops. They look at you with enormous, sad, painted eyes, and mime: no spectators.  
`solstice:122` Then they gently place a share of somebody's grandmother in your hand and run away.  
`solstice:123` **Solstice (neutral):** Ha. They do that. Nobody gets to just watch here.  
> *(end of choice)*

`solstice:125` A siren wails. Every clown freezes, then slowly tears their own hair in silent anguish. The tickers flash red: MARKET CRASH. EVERYTHING ▼100.  
> *show solstice surprised*  

> **Choice**
`solstice:128` **Solstice:** Oh no. Oh no, the crash. Quick, what do we do?  

`solstice:130` **▸** "Can I grab your hand? We're getting out of here."  
> *rapport +2 Solstice*  
`solstice:132` **Solstice (happy):** YES. Run!  
`solstice:133` You run hand in hand through a blizzard of confetti and out into the hallway, and you're both laughing so hard you have to sit down on the carpet.  
`solstice:134` **Solstice (blush):** That's the best I've felt in like a month. That was so stupid. Thank you.  

`solstice:136` **▸** "Hold. Never sell. Diamond hands."  
> *rapport +1 Solstice*  
`solstice:138` **Solstice (happy):** DIAMOND HANDS!  
`solstice:139` You both hold up your hands, defiant, as the market crumbles around you. A clown salutes you with a single tear.  

`solstice:141` **▸** "Sell everything and buy tea."  
> *rapport +1 Solstice*  
`solstice:143` **Solstice (happy):** Honestly the most financially sound decision anyone's made in this room.  
> *(end of choice)*

## solstice_night_2

> *scene bg karaoke*  
`solstice:151` The confession booth karaoke room is draped in velvet. A neon sign on one wall says CONFESS. On the other, ABSOLVED.  
`solstice:152` The rules, printed on a card: Pick a song. Replace the words with something true. Everybody claps either way.  
> *show solstice neutral*  
`solstice:154` Solstice is coming out of the booth. Her LED top is on its dimmest setting. She sees you and goes pink under the glitter.  
`solstice:155` **Solstice (blush):** Oh no. Did you hear that?  
`solstice:156` **Solstice:** I confessed that I don't actually like techno. I like slow songs. Sad, slow country songs about trucks and divorce. I've been lying to the scene for six years.  
`solstice:157` **Solstice (neutral):** Okay. Your turn. You have to. That's the rule.  

> **Choice**

`solstice:160` **▸** Confess something real.  
> *rapport +2 Solstice*  
`solstice:162` You go into the booth. You pick a slow song. In place of the words, you sing something you haven't said out loud to anyone.  
`solstice:163` It isn't good singing. It doesn't need to be. When you come out, Solstice is standing very still.  
`solstice:164` **Solstice (blush):** ...Hey. That was brave. That was, like, the real version.  

`solstice:166` **▸** Confess something silly.  
> *rapport +1 Solstice*  
`solstice:168` You sing, with enormous drama, that you have never once understood how crosswords work. Not once. Not even the easy ones.  
`solstice:169` **Solstice (happy):** NO. Not even Monday?? The Monday ones are for CHILDREN.  

`solstice:171` **▸** Refuse to sing.  
`solstice:172` The booth plays a very sad trombone sound. Several people boo, lovingly.  
`solstice:173` **Solstice (neutral):** Ha. Okay. Okay, that's fair. Not everyone's ready to confess on a Saturday.  
> *(end of choice)*

> *show solstice neutral*  

> **Choice**
`solstice:177` **Solstice:** Hey, so. There's a slow one up next. A real one. Will you... sing it with me?  

`solstice:179` **▸** Sing the slow one with her.  
> *rapport +2 Solstice*  
`solstice:182` The two of you squeeze into the booth. The song is about a truck and a dog and a long road home. You don't know the words. She does.  
`solstice:183` Halfway through, her voice cracks and she laughs and keeps going, and you sing the harmony that doesn't exist.  
`solstice:184` **Solstice (blush):** Okay. That's... okay. I'm going to remember that one.  

`solstice:186` **▸** "Only if you take the goggles off."  
> *rapport +1 Solstice*  
`solstice:188` She hesitates. Then she pulls them off and hangs them on the mic stand. Her eyes look naked without them.  
`solstice:189` **Solstice (neutral):** Fine. Deal. Don't look at me while I sing, I make faces.  

`solstice:191` **▸** "Let's do something faster."  
`solstice:192` **Solstice (neutral):** Oh. Sure! Yeah! Something with a drop!  
`solstice:193` She turns the lights on her top back up. The slow song goes to the next people in line.  
> *(end of choice)*

## solstice_night_3

> *scene bg ballroom*  
`solstice:201` The ballroom on Sunday night is pure light. Lasers cut the haze. Projections of slow geometry crawl over seven hundred dancing bodies.  
`solstice:202` And in the middle of the floor, under the disco ball, Solstice is dancing like it's the last song on Earth. Her LED top is blazing every color at once.  
> *show solstice happy*  
`solstice:204` **Solstice:** YOU CAME! DANCE WITH ME!  
`solstice:205` You dance. It's ridiculous and good. And then, mid-song, with a little electronic sigh, every light on her top goes out at once.  
> *show solstice surprised*  
`solstice:207` Battery's dead. She's just a dark shape in the crowd now. She freezes in the middle of the floor like someone pulled her plug too.  

> **Choice**

`solstice:210` **▸** Keep dancing with her, right there in the dark.  
> *rapport +2 Solstice*  
`solstice:212` You don't stop. After a second, she starts again, slower. Nobody's watching her now. She's just dancing.  
`solstice:213` **Solstice (blush):** You stayed.  

`solstice:215` **▸** Hold up your phone's flashlight like a tiny moon.  
> *rapport +1 Solstice*  
`solstice:217` **Solstice (happy):** Ha! My little moon! Okay, okay.  
`solstice:218` She dances in the circle of your phone light like it's a spotlight. It's the smallest stage in the ballroom.  

`solstice:220` **▸** "Let's go find you some batteries!"  
`solstice:221` **Solstice (neutral):** Yeah. Yeah, good idea. Can't be dark at the end.  
`solstice:222` You hunt for batteries. By the time you find some, the song is over.  
> *(end of choice)*

> *show solstice neutral*  
`solstice:225` **Solstice:** Nobody's ever stayed when the lights went out. People like Solstice. Solstice is fun. When she runs out, they go find the next fun thing.  

> **Choice**
`solstice:227` **Solstice:** Hey. Can I tell you my real name?  

`solstice:229` **▸** "I'd love that."  
> *rapport +2 Solstice*  
`solstice:232` **Solstice (blush):** It's Dana. Dana. It's so boring. It's a dentist's name.  
`solstice:233` **Solstice:** Nobody here knows it. Now you do.  

`solstice:235` **▸** "Only if you want to. I like Solstice too."  
> *rapport +2 Solstice*  
`solstice:238` **Solstice (blush):** I want to. It's Dana.  
`solstice:239` **Solstice:** And you like Solstice too. Huh. Then maybe you'd like both.  

`solstice:241` **▸** "Does it matter?"  
`solstice:242` **Solstice (neutral):** ...Maybe not. Never mind.  
`solstice:243` The music swells. She turns back to the dance floor, and the moment's gone.  
> *(end of choice)*

> *if rapport["solstice"] >= ROMANCE_THRESHOLD:*  
`solstice:246` **Solstice (blush):** After the ark... come find me on the roof? I want to see a sunrise without being high on anything but, like. Life. Ew. You know what I mean.  
> *else:*  
`solstice:248` **Solstice (happy):** Okay! Ark time soon! Go get a good spot, new person!  

## solstice_romance

> *scene bg roof_dawn*  
`solstice:256` The ballroom lets out around five. Seven hundred people spill into the hallways sticky with confetti, hugging strangers, trading kandi, crying a little.  
`solstice:257` You find Solstice exactly where she said she'd be: on the roof, in a borrowed hoodie three sizes too big, leg warmers still on, LED top dead and dark underneath.  
`solstice:258` She's sitting on the bench with two cups of tea, and she's not dancing. You're not sure you've ever seen her sit still.  
> *show solstice blush*  
`solstice:260` **Solstice:** Hi. I got you tea. It's the cardamom one. I didn't know if you were coming, so I've been drinking both of them in turns, which means you get half.  
`solstice:261` **Solstice:** That's a gift. Gifts don't do math.  
`solstice:262` You sit. The bench is cold. She shifts over until her shoulder is against yours, and the hoodie smells like the ballroom: fog machine, sunscreen, glitter, if glitter has a smell.  

> **Choice**
`solstice:265` **Solstice:** Okay. Real question. Did you have fun? Like, actually?  

`solstice:267` **▸** "The most fun I've had in years. Mostly because of you."  
`solstice:268` **Solstice (blush):** Stop. Stop it. You can't just... okay, keep going, actually.  

`solstice:269` **▸** "Ask me again after I sleep for two days."  
`solstice:270` **Solstice (happy):** Ha! Fair. I'm going to sleep until Thursday. Then I have a night shift. Then I'm going to sleep until next Thursday.  
> *(end of choice)*

> *show solstice neutral*  
`solstice:273` Below you, the parking lot is starting to empty. Someone is carrying a six-foot inflatable flamingo to a hatchback and losing.  
> *if gave_mint:*  
`solstice:275` **Solstice:** I still have your mint, by the way. The hotel mint. I didn't eat it.  
`solstice:276` She digs in the pocket of her leg warmer and holds it up: a slightly squashed white disc in cellophane, now covered in glitter.  
`solstice:277` **Solstice:** I'm going to keep it in my locker at work. Next to my badge. So I see it every shift.  
> *if sang_slow_song:*  
`solstice:279` **Solstice:** And I keep thinking about the slow song. The truck song. You didn't know any of the words.  
`solstice:280` **Solstice (happy):** You sang anyway. Nobody sings anyway.  
`solstice:281` **Solstice (neutral):** I've been to twenty festivals. I've never once watched the sunrise. I'm always inside, dancing, so I don't have to think.  
`solstice:282` **Solstice:** Tomorrow I go back to the ICU. Night shift Tuesday. Somebody's going to have the worst night of their life and I'm going to be there.  
`solstice:283` **Solstice:** Usually I come back from these things and I'm emptier than when I left. Like I spent it all. Like I'm on battery.  
`solstice:284` **Solstice (blush):** But I don't feel like that right now. I feel... charged. Is that stupid? That's stupid.  

> **Choice**

`solstice:287` **▸** "It's not stupid. I feel it too."  
`solstice:288` **Solstice (blush):** Okay. Okay, good. Because I was going to be so embarrassed.  

`solstice:289` **▸** "You don't have to be on all the time. Not with me."  
`solstice:290` **Solstice (blush):** ...  
`solstice:291` **Solstice:** Nobody's ever said that to me. People usually want me brighter. Not less bright. Just... less on.  
> *(end of choice)*

> *show solstice neutral*  
> *if knows_dana:*  
`solstice:295` **Solstice:** You know my real name. Nobody here knows it. That's not nothing.  
> *else:*  
`solstice:297` **Solstice:** Hey. Can I tell you something? My real name. Nobody here knows it.  
`solstice:298` **Solstice (blush):** It's Dana. Dana. It's a dentist's name. Don't laugh.  
`solstice:299` The sun is just coming over the mountains now. It turns her glitter gold, every last fleck of it, so she looks like she's been dipped in it.  

> **Choice**

`solstice:302` **▸** "Hi, Dana."  
`solstice:303` **Solstice (blush):** Oh, that's unfair. That's so unfair. Say it again.  
`solstice:304` You do. She covers her face with her hands, and laughs, and doesn't take them away for a while.  

`solstice:305` **▸** Take her hand.  
`solstice:306` Her fingers are cold from the morning and covered in glitter. She squeezes back hard, like she's checking you're real.  
> *(end of choice)*

`solstice:308` **Solstice (blush):** Can I kiss you? Or is that too much? I'm really bad at doing things without lights on. I'm figuring it out.  

> **Choice**

`solstice:311` **▸** "Yes. Lights off. Just us."  
`solstice:312` She leans in. She tastes like cardamom and smells like sunscreen and the end of a very long weekend.  
`solstice:313` It's a slow kiss. A slow-song kiss. Somewhere a bird sings the harmony that doesn't exist.  

`solstice:314` **▸** Kiss her first, gently.  
`solstice:315` **Solstice (surprised):** Oh!  
`solstice:316` **Solstice (blush):** Oh. Okay. Yeah. Yes. Again, please.  
`solstice:317` So you do it again, slower. She's smiling so hard it barely counts.  
> *(end of choice)*

> *show solstice happy*  
`solstice:320` **Solstice:** Okay. The sun's up. I've officially seen one. I'm going to be insufferable about it.  
> *scene bg roof_dawn*  
`solstice:323` The longest day of the year was months ago. This one feels longer, in the best way.  
`solstice:324` Below, someone in the parking lot starts playing a slow country song about a truck from their car speakers. Solstice laughs so hard she spills both teas.  
`solstice:325` She pulls you up off the bench and you dance, badly, slowly, with no lights at all, until the song ends and the car drives away.  
> *scene black*  
`solstice:327` {i}Wednesday, 4:12 AM. A text.{/i}  
`solstice:328` **Solstice:** on break. someone made it through the night. the family brought donuts for the whole floor  
`solstice:329` **Solstice:** it's sunrise in like an hour. I'm going to go watch it from the parking garage roof. first one I've watched on purpose that wasn't with you  
`solstice:330` **Solstice:** thinking about you. it's dana btw. obviously. come to the next one with me? I'll bring the tea. you bring a mint  
> *→ jump ending_card*  

## solstice_friend

> *scene bg exterior*  
> *show solstice happy*  
`solstice:340` Solstice tackles you in the parking lot with a full-body hug and a fresh handful of glitter. Some of it goes in your mouth. That's the price.  
`solstice:341` **Solstice:** THERE you are! I was going to leave a note on your windshield made of glitter. A glitter note. A glote.  
`solstice:342` **Solstice (neutral):** Real talk for one second. This weekend was the first one in a long time I didn't feel like I was running on fumes.  
`solstice:343` **Solstice:** Some of that's the party. Some of it's you. You're good at the quiet parts. I'm bad at the quiet parts.  
`solstice:344` She ties a new bracelet onto your wrist next to the first one. This one says, in lettered beads, {i}call me{/i}.  
`solstice:345` **Solstice (happy):** You're stuck with me now. Friendship bracelet is legally binding. Next festival, you're on my camp. No excuses!  
`solstice:346` **Solstice:** And if you ever want to watch a sunrise, I hear they're good. I've seen one. I'm basically an expert.  

---

# wren.rpy

## wren_pool_1

`wren:9` A person in head-to-toe black is standing at the edge of the deep end with a long pool net, trying to fish out a disco ball the size of a beach ball. It keeps rolling off the net.  
> *show wren neutral*  
`wren:11` **Wren:** Come on. Come on. You were installed in a ballroom. You were not installed in a pool. Who did this. Why would you do this.  
`wren:12` It's Wren, from check-in. Sweat is running down from under her headset.  

> **Choice**

`wren:15` **▸** Grab the other net off the wall and help.  
> *rapport +2 Wren*  
`wren:17` You work it from the opposite side. It takes three tries, a lot of teamwork, and one undignified lunge, but the disco ball comes out of the water dripping and spinning.  
`wren:18` **Wren (happy):** Yes! YES. Okay. That's the most satisfying thing that's happened to me since Thursday.  
`wren:19` **Wren (neutral):** Thank you. Seriously. You didn't have to.  

`wren:21` **▸** "Need a hand?"  
> *rapport +1 Wren*  
`wren:23` **Wren (neutral):** ...Yes. God. Yes.  
`wren:24` Between the two of you, the disco ball eventually surrenders.  

`wren:26` **▸** "Isn't that someone else's job?"  
`wren:27` **Wren (neutral):** Everything here is someone else's job until it breaks. Then it's mine.  
`wren:28` She gets it out on the seventh try, alone.  
> *(end of choice)*

> *show wren neutral*  
`wren:31` She sits down on the edge of a lounger with the wet disco ball in her lap, like a cat that's been rescued from a tree.  
`wren:32` **Wren:** Six years I've been crew. First year I came as a guest. Didn't know a single person here.  
`wren:33` **Wren:** By Sunday I was wearing a cape I'd made out of a shower curtain, leading a conga line through the old casino floor, saying things out loud I'd never said to anyone. I found out who I was in these hallways.  
`wren:34` **Wren:** That only happens if the spell holds. The second the lasers die or the fog machine catches fire, everyone remembers they're standing in an old hotel. So now I'm the one who makes sure nothing breaks.  

> **Choice**

`wren:37` **▸** "Do you ever get to just... be at the party?"  
> *rapport +2 Wren*  
`wren:39` **Wren (surprised):** Ha.  
`wren:40` **Wren (neutral):** Sometimes. For about six minutes at a time. Between fires.  
`wren:41` **Wren:** Nobody's asked me that in a long time. People mostly ask me where the bathroom is.  

`wren:43` **▸** "That's a really beautiful reason."  
> *rapport +1 Wren*  
`wren:45` **Wren (blush):** It's... yeah. Thanks. Don't tell anyone, I have a reputation for being dead inside.  

`wren:47` **▸** "Sounds like a lot of unpaid labor."  
`wren:48` **Wren (neutral):** It's volunteering. It's different.  
`wren:49` **Wren:** ...It's a little bit unpaid labor.  
> *(end of choice)*

`wren:51` **Walkie-talkie:** Wren, someone's put the inflatable flamingo in the ice machine.  
`wren:52` **Wren (neutral):** Copy. Of course they have.  

## wren_pool_2

`wren:58` Behind the towel hut at the far end of the pool hall, out of sight, Wren is sitting on an upturned bucket eating a sandwich. It's a very sad sandwich. It's mostly bread.  
> *show wren surprised*  
`wren:60` **Wren:** Oh. Hi. You found my secret place. I have a fifteen-minute break. I've had it for six minutes. I've spent four of them answering the radio.  

> **Choice**

`wren:63` **▸** Offer her half of the fancy pastry you grabbed from the tea bar.  
> *rapport +2 Wren*  
`wren:66` **Wren (surprised):** Is that the cardamom bun? There are only twelve of those. I've never gotten one. Not in six years.  
`wren:67` **Wren (happy):** Oh my god. Oh my god, it's so good. I'm going to cry. I'm not going to cry. I'm crew.  

`wren:69` **▸** Sit down on the floor next to her and say nothing.  
> *rapport +1 Wren*  
`wren:71` You sit. She eats her sad sandwich. The pool noises go on around the corner.  
`wren:72` **Wren (neutral):** This is nice. Nothing's on fire right now. It's like being underwater.  

`wren:74` **▸** "Want me to leave so you can actually have your break?"  
> *rapport +1 Wren*  
`wren:76` **Wren (neutral):** No. Stay. Actually, stay.  
`wren:77` **Wren:** It's nice to talk to someone who isn't telling me something's broken.  
> *(end of choice)*

> *show wren neutral*  
`wren:80` She turns the walkie down to its lowest setting. You can tell it costs her something.  
`wren:81` **Wren:** I'm on fire duty for the ark tomorrow. It comes down from the ballroom ceiling at 11:11 on a rig I built. Seven hundred people in the dark. If anything jams, I have about ninety seconds to fix it before anyone notices.  
`wren:82` **Wren:** Last year the fog machine caught on fire. Small fire. Supportive fire. But still.  

> **Choice**

`wren:85` **▸** "It'll go fine. And if it doesn't, it'll be a better story."  
> *rapport +2 Wren*  
`wren:87` **Wren (happy):** Ha. Okay. Yeah. The fire was a really good story, honestly.  
`wren:88` **Wren (neutral):** Thank you. I needed somebody to say that, and I've been saying it to everyone else.  

`wren:90` **▸** "Can I help? Running errands, carrying stuff, anything?"  
> *rapport +1 Wren*  
`wren:92` **Wren (neutral):** Guests aren't supposed to work. But I'll... keep that in mind. Seriously.  

`wren:94` **▸** "You should let someone else handle it."  
`wren:95` **Wren (neutral):** There isn't someone else. That's the whole job.  
> *(end of choice)*

`wren:97` **Walkie-talkie:** Wren, the Oracle robot is printing fortunes on the carpet. Just the carpet. It won't stop.  
`wren:98` **Wren (neutral):** Copy.  
`wren:99` **Wren (happy):** Thanks for the break. That was the best four minutes of my weekend.  

## wren_night_1

> *scene bg backstage*  
`wren:106` Behind a door marked BACKSTAGE: a forest of scaffolding, cables thick as pythons, road cases stenciled with names like PARTY HARDER and FRAGILE: FEELINGS. Through a gap in the curtain, the ballroom roars.  
`wren:107` Except the lasers have gone dark. The DJ is vamping. Seven hundred people are dancing under nothing but the exit signs, and it's starting to feel like a hotel ballroom again.  
> *show wren neutral*  
`wren:109` Halfway up a ladder, with a flashlight in her teeth and a screwdriver behind her ear, is Wren.  
`wren:110` **Wren:** Mmf. Oh, thank god, it's you. Don't touch anything red.  
`wren:111` **Wren:** The laser rig went down mid-set. I've got maybe two songs before people start noticing the carpet.  

> **Choice**

`wren:114` **▸** "What do you need?"  
> *rapport +2 Wren*  
`wren:116` She points at the flashlight in her mouth. You climb up and take it, and hold it exactly where she points, while she rewires something with the speed of a surgeon.  
`wren:117` **Wren (neutral):** Little left. Little more. Perfect. Don't breathe.  

`wren:118` **▸** "Have you tried turning it off and on again?"  
> *rapport +1 Wren*  
`wren:120` **Wren (neutral):** ...  
`wren:121` She stares at you. Then she reaches over and flips the master switch off and on again.  
`wren:122` Somewhere above you, the rig whirs back to life.  
`wren:123` **Wren (blush):** Do not tell anyone that worked.  

`wren:124` **▸** "Shouldn't someone with a real job be doing this?"  
`wren:125` **Wren (neutral):** I am someone with a real job. It's this. It's always this.  
> *(end of choice)*

`wren:127` The lasers blaze back on. Pink and cyan beams sweep the haze, the bass drops, and seven hundred people scream like it was all part of the show.  
`wren:128` None of them will ever know anything went wrong. Wren climbs down the ladder, sits on a road case, and watches them through the gap in the curtain.  
> *show wren happy*  
`wren:130` **Wren:** That. That's the job. Nobody's supposed to know. If they notice, the spell breaks.  
> *show wren neutral*  
`wren:132` **Wren:** Every year someone walks in here as one person and walks out as somebody else. I just keep the lights on while it happens.  

> **Choice**

`wren:135` **▸** "Who keeps the lights on for you?"  
> *rapport +2 Wren*  
`wren:137` Wren doesn't answer for a long time. The lasers sweep over her face, pink, then cyan, then pink.  
`wren:138` **Wren (blush):** ...Nobody's asked me that. I don't know. I don't know.  

`wren:139` **▸** "Come out there for one song."  
> *rapport +1 Wren*  
`wren:141` **Wren (neutral):** One song. If anything breaks, I'm—  
`wren:142` You pull her through the curtain. She stands at the very edge of the dance floor and doesn't dance, exactly, but she sways. For one song.  
`wren:143` **Wren (blush):** ...Okay. That was nice. Don't tell my crew.  

`wren:144` **▸** "You look exhausted."  
`wren:145` **Wren (neutral):** Thanks. I'm aware. I have a mirror. It's a crew mirror. It's black.  
> *(end of choice)*

`wren:147` **Walkie-talkie:** Wren, the Holy Skillet's spotlight just exploded. Small explosion. Supportive explosion.  
`wren:148` **Wren (neutral):** Copy. On my way.  
`wren:149` **Wren (happy):** Thanks for the flashlight. Or the moral support. Whichever it was.  

## wren_night_2

> *scene bg mission*  
`wren:156` STAFF ONLY. Inside, a linen closet has been turned into the crew's fire station. On one wall, a big hand-drawn map of the hotel, studded with little red magnets: one for everything that's currently broken. There are a lot of red magnets.  
`wren:157` Walkie-talkies charge in a row. Clean towels are stacked to the ceiling. A toolbox the size of a coffin sits open on the floor.  
> *show wren neutral*  
`wren:159` **Wren:** You found me. Don't tell anyone this room exists. I'll have to kill you. Gently. With towels.  
`wren:160` **Wren:** Actually, I could use a hand. The fog machine in Room 312 is stuck on. The forest is turning into soup.  
`wren:161` She points to a panel of big glowing buttons: FOG KILL. LASERS. ARK RIG. PANIC.  
`wren:162` **Wren:** The fog kill switch is flaky. It has to be held down for exactly three seconds while I reset the unit, or it reboots and floods the room. On my count. Three, two—  

> **Choice**

`wren:165` **▸** Hold FOG KILL down, perfectly steady, for exactly three seconds.  
> *rapport +2 Wren*  
`wren:168` You hold it. One. Two. Three. On the monitor, the fog in the forest room thins to a soft, pretty haze. Someone in there gasps, delighted.  
`wren:169` **Wren (happy):** Perfect. That was {i}perfect.{/i} You have no idea how rare steady hands are on this crew. You'd make good crew.  

`wren:170` **▸** Hold it down, panic, and let go a second early.  
`wren:171` The fog in the forest room surges, then settles. On the monitor, someone in there sneezes.  
`wren:172` **Wren (neutral):** That was early. It's fine. The forest got a little extra mood. Fog's very forgiving.  

`wren:173` **▸** Press PANIC, because how could you not.  
> *rapport +1 Wren*  
`wren:175` Somewhere in the walls, a single kazoo plays a long, sad note.  
`wren:176` **Wren (surprised):** Oh my god. Nobody's ever pressed that. In six years.  
`wren:177` **Wren (happy):** It's not connected to anything. It's just a kazoo. Somebody built it as a joke. You pressed the joke.  
> *(end of choice)*

> *show wren neutral*  
`wren:180` Between fires, the two of you sit on stacks of towels in the dark, lit by the monitors. It's very quiet in here. You can feel the bass through the floor like a heartbeat.  
`wren:181` Every so often she gets up and moves a red magnet to the other side of the map. Fixed.  
`wren:182` **Wren:** This is my favorite part of the whole weekend. Right here. Everybody out there having the best night of their life, and in here it's just quiet and the map, and the magnets going from red to done.  
`wren:183` **Walkie-talkie:** Wren, the Ice Machine Planetarium's star projector just went dark. Someone in there says the stars left them.  
`wren:184` **Wren (neutral):** Copy.  

> **Choice**
`wren:187` **Wren:** I have to go fix the sky. You should go enjoy the party. Or—I mean. You could come with me. You can hold the flashlight. You're good at it.  

`wren:189` **▸** "This is the party. I'm coming."  
> *rapport +2 Wren*  
`wren:191` **Wren (blush):** ...Okay. Yeah. Okay. Grab the flashlight.  
`wren:192` You walk the hallways side by side. She lets you carry the flashlight. Ten minutes later, the stars come back on in the planetarium, and a whole room of people says {i}oooh{/i} at once.  

`wren:193` **▸** "I'll hold down the fort here."  
> *rapport +1 Wren*  
`wren:195` **Wren (surprised):** You'd... yeah. Okay. Don't press anything. Except PANIC. You can press PANIC.  
`wren:196` She tosses you a spare walkie on her way out. For the next twenty minutes you're crew. You move two magnets. It feels incredible.  

`wren:197` **▸** "I'll see you later, then."  
`wren:198` **Wren (neutral):** Yeah. Later. Have fun.  
> *(end of choice)*

## wren_night_3

> *scene bg roof*  
`wren:206` The roof of the hotel tower. Above you, a sky full of stars. Far below, the black mirror of the lake and the glitter of the other casinos along the shore. Under your feet, the bass. Thick cables run down from the rigging into the ballroom skylight, where in a few minutes the ark will come down.  
> *show wren neutral*  
`wren:208` Wren is toolbox in hand, checking every knot. She looks up when the door clangs.  
`wren:209` **Wren:** Hey. I have seven minutes until I need to be under the stage. The rig's checked. Triple-checked.  
`wren:210` **Wren:** Seven minutes. What do people do with seven minutes?  

> **Choice**

`wren:213` **▸** "Sit down. Look at the stars. I'll watch the clock for you."  
> *rapport +2 Wren*  
`wren:215` You hold out your hand. After a long second, she gives you the walkie.  
`wren:216` She lies flat on her back on the gravel roof, arms out, and looks up. She doesn't say anything for three whole minutes.  
`wren:217` **Wren (blush):** I forgot there were stars here. Six years. I forgot.  

`wren:219` **▸** "Dance with me. No music."  
> *rapport +1 Wren*  
`wren:221` **Wren (surprised):** There's music. It's coming up through the roof. It's... actually, okay.  
`wren:222` You dance, badly, on the roof. She's stiff for a minute and then she isn't.  

`wren:224` **▸** "Shouldn't you be double-checking the rigging?"  
`wren:225` **Wren (neutral):** Triple. I said triple. ...You're right. I'll check it again.  
`wren:226` She spends the seven minutes checking knots.  
> *(end of choice)*

> *show wren neutral*  
`wren:229` **Wren:** Can I tell you something stupid? I've never seen the ark. Not once. Six years.  
`wren:230` **Wren:** During the ark I'm under the stage with a fire extinguisher and a roll of gaffer tape, watching it on a monitor the size of a sandwich. In case anything breaks. Ninety seconds, remember.  
`wren:231` **Wren:** Everyone says it's the best moment of the whole weekend. I wouldn't know.  

> **Choice**

`wren:234` **▸** "After the ark lands, come find me. Watch the end of it with me."  
> *rapport +2 Wren*  
`wren:236` **Wren (surprised):** I can't just—  
`wren:237` **Wren (blush):** ...After it lands. If nothing's broken. Maybe I could. Maybe I could, actually.  

`wren:239` **▸** "Next year, let someone else take fire duty. Come as a guest."  
> *rapport +1 Wren*  
`wren:241` **Wren (neutral):** Ha. Maybe. That's... maybe.  

`wren:243` **▸** "You'll see it someday."  
`wren:244` **Wren (neutral):** Yeah. Someday.  
> *(end of choice)*

`wren:246` **Walkie-talkie:** Wren, five minutes to ark. Rig's yours.  
`wren:247` **Wren (neutral):** Copy. On my way.  
> *if rapport["wren"] >= ROMANCE_THRESHOLD:*  
`wren:249` **Wren (blush):** My shift ends at 11:12. One minute after the ark. I've never once left on time. Tonight I'm going to.  
> *else:*  
`wren:251` **Wren (neutral):** Go get a spot near the front. Trust me. It's worth seeing in person.  

## wren_romance

> *scene bg ballroom*  
`wren:259` At 11:12, while the ballroom is still screaming and the confetti is still falling, someone taps you on the shoulder.  
> *show wren happy*  
`wren:261` Wren. No toolbox. The headset is around her neck instead of on her head, and she looks like someone who has just jumped off a high diving board.  
`wren:262` **Wren:** Nothing broke. Do you understand? Six years, and for the first time, nothing broke. Not one thing. I stood under that stage with a fire extinguisher and nothing caught fire.  
`wren:263` **Wren:** So I handed the toolbox to Pilar. Pilar's been begging for it for two years. And I just... walked out.  
`wren:264` **Wren:** I watched the duck come out of the ark from the back of the room. In person. With my actual eyes. It was so stupid. I cried so much.  
`wren:265` **Wren (surprised):** I don't know what to do with my hands. They keep reaching for a screwdriver.  

> **Choice**
`wren:267` **Wren:** What do guests do now? After the big moment? I've genuinely never known.  

`wren:269` **▸** "They dance. Badly. Come on."  
`wren:270` You pull her into the crowd. She dances like someone who has seen a thousand people dance and never once done it herself, stiff, then less stiff, then laughing.  

`wren:271` **▸** "They go find a quiet corner and talk until the sun comes up."  
`wren:272` **Wren (happy):** That sounds... incredible, honestly. I know every quiet corner in this building. I've fixed the lights in all of them.  
> *(end of choice)*

> *scene bg roof_dawn*  
> *show wren neutral*  
`wren:277` Hours later, you're both back on the roof, where you were before the ark. The rigging hangs slack. The sky is going gold over the mountains, and the lake below is turning from black to silver.  
`wren:278` Wren is sitting on the gravel with her back against the water tank, boots off, a stolen cardamom bun in each hand. She gives you one.  
> *if shared_bun:*  
`wren:280` **Wren:** You gave me half of one on Saturday. I've been waiting all weekend to pay you back. With interest.  
> *else:*  
`wren:282` **Wren:** There were twelve of these. Now there are zero. I have abused my position. I regret nothing.  
`wren:283` **Wren:** This is the first sunrise in six years I've watched without a radio on.  
`wren:284` She takes the headset off her neck and sets it on the gravel between you. It crackles once. She doesn't touch it.  

> **Choice**

`wren:287` **▸** "How does it feel?"  
`wren:288` **Wren (blush):** Terrifying. Amazing. Like I left the stove on, except the stove is a whole hotel.  
`wren:289` **Wren:** ...But it's fine. It's fine without me for one morning. Huh.  

`wren:290` **▸** Lean your shoulder against hers.  
`wren:291` She leans back. All of her, for once. You can feel how tired she is, and how much lighter.  
> *(end of choice)*

> *show wren neutral*  
`wren:294` **Wren:** Can I tell you what this weekend was supposed to be? For me? Toolbox, radio, eleven hours of sleep across three days, the lasers die, the fog machine catches fire, someone puts a disco ball in the pool.  
> *if called_fog_cue:*  
`wren:296` **Wren (happy):** And instead some guest walks into my linen closet and holds a kill switch steadier than half my crew. Do you know how annoying that is? I trained Pilar for a year.  
`wren:297` **Wren:** I keep thinking about my first year. The shower-curtain cape. The conga line. Saying things out loud I'd never said to anyone. I found out who I was in those hallways.  
`wren:298` **Wren:** Every year since, I've been building the place so other people get to find out too. And somewhere along the way I stopped thinking I was allowed to be one of them.  
`wren:299` **Wren (blush):** And then you just... kept pulling me back in. Over and over. A flashlight, a bun, a song. You kept asking if I needed anything.  

> **Choice**

`wren:302` **▸** "You always needed something. You just never got to ask."  
`wren:303` **Wren (blush):** ...  
`wren:304` **Wren:** Okay. That's... you can't just say that at sunrise. I'm going to think about that for a year.  

`wren:305` **▸** "I liked being near you. That's all it was."  
`wren:306` **Wren (blush):** That's all? That's everything. That's the whole reason I build any of this, actually. So people can just be near each other.  
> *(end of choice)*

`wren:308` The sun clears the mountains. Far below, in the parking lot, a crew member is coiling cables and singing to themselves. It isn't Wren's problem. For once, nothing is.  
> *if pool_seen["wren"] >= 1:*  
`wren:310` **Wren (blush):** I've been wanting to ask you something since the disco ball. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now.  
> *else:*  
`wren:312` **Wren (blush):** I've been wanting to ask you something all weekend. It's very unprofessional. I'm not on shift. I'm allowed to be unprofessional now.  
`wren:313` **Wren:** Is it okay if I kiss you?  

> **Choice**

`wren:316` **▸** "Yes. Very much yes."  
`wren:317` She kisses you like she's been planning it for three days, which it turns out she has. She's precise about it. Steady hands. Nothing breaks.  
`wren:318` **Wren (happy):** Fixed.  

`wren:319` **▸** "Only if I get to count it down. Three, two—"  
`wren:320` **Wren (happy):** Oh, you're—  
`wren:321` On one, she does.  
`wren:322` **Wren (happy):** Perfect timing. You really would make good crew.  
> *(end of choice)*

> *show wren happy*  
`wren:325` **Wren:** I have to go help strike the set in about an hour. That's the deal. Everyone helps strike.  
`wren:326` **Wren (blush):** But this hour's mine. I'm not giving it to anyone.  
> *scene bg roof_dawn*  
`wren:329` On the gravel between you, the walkie crackles: {i}Wren? Wren, where are the extra towels? Wren, the flamingo is back in the ice machine.{/i}  
`wren:330` She reaches over, very calmly, and turns it off. Then she lies back on the gravel next to you and watches the whole sky go from pink to blue over the lake.  
> *scene black*  
`wren:332` {i}A week later, an envelope arrives. Inside: a crew badge, laminated. It doesn't say CREW. It says GUEST.{/i}  
`wren:333` {i}On the back, in neat handwriting:{/i}  
`wren:334` **Wren:** Next year we both come as guests. I already asked. Pilar's on fire duty for the ark. I'm watching it with you, from the front, with my eyes. That's the whole plan.  
`wren:335` **Wren:** Also I'm free Saturday. Not a shift, not a fire. Just free. I had to look up what people do. Apparently it's brunch. — W  
> *→ jump ending_card*  

## wren_friend

> *scene bg exterior*  
> *show wren happy*  
`wren:345` Wren is coiling cables under the hotel's big neon sign on Monday morning, headset back on, already somewhere in the middle of tomorrow. She sees you and lifts one hand.  
`wren:346` **Wren:** Hey. You survived. Most people look worse than you on Monday. You look about forty percent worse. That's good.  
`wren:347` **Wren (neutral):** Thanks for this weekend. Seriously. You kept checking on me. Crew doesn't get checked on. It's... it was nice.  
`wren:348` **Walkie-talkie:** Wren, the moss in the forest room is smoking. Small smoke. Supportive smoke.  
`wren:349` **Wren:** Copy. Give me five.  
`wren:350` **Wren (happy):** You're on the list now. If you ever want to crew, I'll train you myself. You'd be good at it. You notice things right before they break.  
`wren:351` She hands you a spare walkie-talkie, switched off, as a souvenir. It has a strip of gaffer tape on the back that says FIX IT.  

---

# zyx.rpy

## zyx_pool_1

`zyx:5` Under a giant striped beach umbrella, set up indoors for reasons nobody has asked about, sits a silver alien with three eyes, two antennae and a sash that reads AMBASSADOR. They are wearing at least an inch of sunscreen anyway, and taking notes on a clipboard.  
> *show zyx neutral*  
`zyx:7` **Zyx:** Greetings, Earthling. This one is Zyx, Ambassador of the Outer Drift. You may approach. Slowly. The sun is very aggressive on this planet. Even through glass.  
`zyx:8` **Zyx:** Please explain the following ritual.  
`zyx:9` They point at the pool, where a dozen adults have their eyes closed, splashing around and screaming the same two words at each other.  
`zyx:10` **Zyx:** Why do humans close their eyes and shout the name of a dead Venetian explorer?  

> **Choice**

`zyx:13` **▸** Explain Marco Polo as seriously as possible.  
> *rapport +2 Zyx*  
`zyx:15` You explain the rules in full. The seeker. The call. The response. The fish-out-of-water rule, which you're not sure is real.  
`zyx:16` **Zyx (happy):** Fascinating. A game of trust and echolocation. Your species is part bat. We suspected.  
`zyx:17` They write {i}PART BAT{/i} in large letters on the clipboard and underline it twice.  

`zyx:19` **▸** "Just play it with me. You'll get it."  
> *rapport +1 Zyx*  
`zyx:21` You drag them into the shallow end. Zyx is the seeker. They close all three eyes.  
`zyx:22` **Zyx (surprised):** MARCO.  
`zyx:23` Everyone shouts POLO. Zyx's antennae go limp with delight.  
`zyx:24` **Zyx (happy):** Again. AGAIN.  

`zyx:26` **▸** "Are you... actually an alien?"  
`zyx:27` **Zyx (neutral):** Are you actually a human?  
`zyx:28` **Zyx:** Do not answer. It would ruin it. For both of us.  
> *(end of choice)*

> *show zyx neutral*  
`zyx:31` Zyx explains that they are here on a research mission: to determine whether Earth is ready for contact.  
`zyx:32` **Zyx:** Our current findings: Earth is not ready. Earth is very, very fun. These two findings are in tension. The report is going poorly.  

> **Choice**
`zyx:35` **Zyx:** Question for the report. Why do humans gather like this? In secret? Wearing other faces?  

`zyx:37` **▸** "Because sometimes the other face is the real one."  
> *rapport +2 Zyx*  
`zyx:39` All three of Zyx's eyes look at you at once.  
`zyx:40` **Zyx (blush):** ...That is the most accurate thing anyone has said for the report.  
`zyx:41` **Zyx:** This one is writing it down. With your name. No, without your name. Earth rules. No names in the report.  

`zyx:43` **▸** "To have fun. That's it. That's all."  
> *rapport +1 Zyx*  
`zyx:45` **Zyx (happy):** Simple. Elegant. This one respects it. Writing: FUN.  

`zyx:47` **▸** "I'm not sure. I came here to find out."  
> *rapport +1 Zyx*  
`zyx:49` **Zyx (neutral):** A fellow researcher. We will compare notes before the end.  
> *(end of choice)*

## zyx_pool_2

`zyx:56` Zyx is walking the pool deck with a mesh bag labeled EARTH ARTIFACTS. It contains nine mismatched flip-flops, a pair of sunglasses, a single swim fin, and a paperback novel swollen to twice its size from water.  
> *show zyx happy*  
`zyx:58` **Zyx:** Earthling! You are here! Good. The museum of the Outer Drift requires donations. Every visitor gives one artifact. It is the custom of our people. Just now. We invented it just now.  

> **Choice**
`zyx:61` **Zyx:** What do you donate to the Outer Drift?  

`zyx:63` **▸** Find a perfect smooth pebble by the planters, and explain that it's a 'nice rock.'  
> *rapport +2 Zyx*  
`zyx:66` **Zyx (surprised):** A nice rock.  
`zyx:67` They hold it up to the light from the atrium roof with all three eyes.  
`zyx:68` **Zyx (happy):** On the Outer Drift, there are no nice rocks. Every rock is jagged and furious. This changes everything. This is the centerpiece.  

`zyx:70` **▸** Your hotel key card.  
> *rapport +1 Zyx*  
`zyx:72` **Zyx (neutral):** A key to a door that already opens. Because everyone who enters is already checked in.  
`zyx:73` **Zyx (happy):** Profound. It goes in the philosophy wing.  

`zyx:75` **▸** "Nothing. Sorry. I need all my stuff."  
`zyx:76` **Zyx (neutral):** Understandable. Humans are very attached to stuff. We have noted it.  
> *(end of choice)*

> *show zyx neutral*  
`zyx:79` Zyx sits down on a lounger next to you and folds their silver hands.  
`zyx:80` **Zyx:** The Outer Drift is very quiet. Thirty-one of us, spread across a nebula. We communicate by changing color, very slowly. A conversation can take a year.  
`zyx:81` **Zyx:** No one has hugged on the Outer Drift since the third moon. We are not built for it. Too many antennae.  
`zyx:82` **Zyx:** But this one has observed many hugs here. Data suggests they are... good.  

> **Choice**
`zyx:85` **Zyx:** Earthling. For the report. Please demonstrate a hug. Consent is requested, in the Earth style.  

`zyx:87` **▸** "Yes. Come here."  
> *rapport +2 Zyx*  
`zyx:90` You hug. Zyx is very stiff at first, like a coat hanger. Then, slowly, their arms come up around you. Their antennae droop down over your shoulder.  
`zyx:91` **Zyx (blush):** Oh.  
`zyx:92` **Zyx:** Data confirmed. Data... very confirmed.  

`zyx:94` **▸** Offer a high five instead.  
> *rapport +1 Zyx*  
`zyx:96` Zyx studies your palm. Then, very carefully, presses their three-fingered glove against it.  
`zyx:97` **Zyx (happy):** A hug for hands. Efficient. We approve.  

`zyx:99` **▸** "Maybe later."  
`zyx:100` **Zyx (neutral):** Noted. Later. This one will hold you to the Earth word 'later.'  
> *(end of choice)*

## zyx_night_1

> *scene bg fortune*  
`zyx:108` THE ORACLE OF PING PONG, says the sign. A boxy robot with a glass dome on its head takes ping pong balls from a lottery machine and prints fortunes on them with a tiny buzzing arm.  
`zyx:109` People in capes and headsets queue in the purple light. At the front, Zyx is feeding the machine with great seriousness.  
> *show zyx neutral at slightright*  
`zyx:111` **Zyx:** Earthling! You are just in time. This machine is the most advanced intelligence on your planet. We have been consulting it for an hour.  
`zyx:112` The robot whirs. It spits out a ball. Zyx catches it and reads it aloud.  
`zyx:113` **THE ORACLE:** YOU ARE NOT THE ONLY ONE.  
> *show zyx surprised at slightright*  
`zyx:115` **Zyx:** Not the only one. Not the only one... what? This is troubling. Interpret it, please.  

> **Choice**

`zyx:118` **▸** "It means you're not alone. Here, at least."  
> *rapport +2 Zyx*  
`zyx:120` **Zyx (blush):** Not alone.  
`zyx:121` They turn the ball over and over in their gloved fingers.  
`zyx:122` **Zyx:** On the Outer Drift, the nearest Zyx is four light-years away. This one had forgotten that 'not alone' was a thing a person could be.  

`zyx:124` **▸** "It means there's another alien at this party."  
> *rapport +1 Zyx*  
`zyx:126` **Zyx (surprised):** !!!  
`zyx:127` Zyx spins around, scanning the crowd with all three eyes. A man in a cape waves at them. Zyx waves back, suspicious.  

`zyx:129` **▸** "It's a ping pong ball. It doesn't mean anything."  
`zyx:130` **Zyx (neutral):** Everything means something to the Oracle. But we will log your skepticism.  
> *(end of choice)*

> *show zyx neutral at slightright*  
`zyx:133` **Zyx:** Now you. Your turn. This one will read yours.  
`zyx:134` The robot whirs and prints a ball for you. Zyx reads it.  
`zyx:135` **THE ORACLE:** STAY UNTIL SUNRISE.  

> **Choice**
`zyx:137` **Zyx:** Will you follow the Oracle's guidance?  

`zyx:139` **▸** "Only if you stay too."  
> *rapport +2 Zyx*  
`zyx:141` **Zyx (blush):** Ah.  
`zyx:142` **Zyx:** Then it is decided. The Oracle has spoken. We both stay. For science.  

`zyx:144` **▸** "Probably. I'm not great at leaving things."  
> *rapport +1 Zyx*  
`zyx:146` **Zyx (happy):** Good. Neither is this one. This one came for a weekend nine years ago.  

`zyx:148` **▸** "I don't really believe in fortunes."  
`zyx:149` **Zyx (neutral):** The Oracle does not need your belief. It is a robot. It has a printer.  
> *(end of choice)*

## zyx_night_2

> *scene bg clinic*  
`zyx:157` The Clinic of Unnecessary Procedures smells like rubbing alcohol and bubblegum. An eye chart on the wall is made entirely of astrological symbols.  
`zyx:158` Two nurses in vintage uniforms are wheeling Zyx in on a gurney. Zyx is protesting in a language that sounds a lot like the noise a modem makes.  
> *show zyx surprised*  
`zyx:160` **Nurse Ratchet-and-Clank:** Are you the alien's next of kin?  

> **Choice**

`zyx:163` **▸** "Yes. I'm their emergency contact."  
> *rapport +2 Zyx*  
`zyx:166` **Zyx (blush):** You are?  
`zyx:167` **Zyx:** ...You are. Yes. Correct. This one's emergency contact. Please inform them of everything.  

`zyx:169` **▸** "I'm a friend."  
> *rapport +1 Zyx*  
`zyx:171` **Nurse Ratchet-and-Clank:** A friend may stay. Friends are encouraged. It says so on the chart.  

`zyx:173` **▸** "Never seen them before in my life."  
`zyx:174` **Zyx (surprised):** Betrayal! This one will be noting this in the report! In red!  
`zyx:175` The nurses let you stay anyway. They need a witness.  
> *(end of choice)*

> *show zyx neutral*  
`zyx:178` **Nurse Ratchet-and-Clank:** May I listen to your heart, Ambassador? The stethoscope is cold. I'm asking first.  
`zyx:179` **Zyx:** ...Permission granted.  
`zyx:180` The nurse listens for a long, long time. She frowns. She moves the stethoscope. She frowns harder.  
`zyx:181` **Nurse Ratchet-and-Clank:** Heart: one. Normal size. Slightly lonely.  
`zyx:182` **Zyx (surprised):** Slightly lonely!  
`zyx:183` **Nurse Ratchet-and-Clank:** It happens. Especially to travelers. Here's the prescription.  
`zyx:184` She writes on a pad and tears off the page with great ceremony: ONE (1) DANCE. TO BE TAKEN BEFORE SUNRISE. REPEAT AS NEEDED.  
> *show zyx neutral*  

> **Choice**
`zyx:187` **Zyx:** The prescription requires a partner. Are you... available? For medical purposes?  

`zyx:189` **▸** "Doctor's orders. I'm available."  
> *rapport +2 Zyx*  
`zyx:191` **Zyx (blush):** Medical purposes. Yes. Strictly medical.  
`zyx:192` Zyx dances like an alien who's watched a lot of dancing through a telescope: very precise, very wrong. You love it.  

`zyx:194` **▸** "I'll have to check my schedule."  
> *rapport +1 Zyx*  
`zyx:196` **Zyx (happy):** A tease. Your species is called 'a tease.' We have the data.  

`zyx:198` **▸** "You should ask someone else. I'm a terrible dancer."  
`zyx:199` **Zyx (neutral):** Understood. This one will dance alone. Doctor's orders.  
`zyx:200` They do, in the hallway, very precisely. It's a little sad.  
> *(end of choice)*

## zyx_night_3

> *scene bg planetarium*  
`zyx:208` Someone has turned the ice machine alcove into a planetarium. Stars cover every surface. Constellations are drawn between them in faint blue lines. The ice machine glows in the middle like a small, cold sun.  
> *show zyx neutral*  
`zyx:210` Zyx is sitting on the floor in front of it, antennae dimmed, looking up.  
`zyx:211` **Zyx:** Ah. Earthling. Sit. This is this one's favorite room. The ice machine dreams of the cold between stars. We understand each other.  

> **Choice**
`zyx:213` **Zyx:** That one, there. The faint one, near the Swan. That is home. Do you see it?  

`zyx:215` **▸** "I can't find it. Show me?"  
> *rapport +2 Zyx*  
`zyx:217` **Zyx (neutral):** May this one take your hand to point?  
`zyx:218` You say yes. Their gloved fingers wrap around yours and guide your arm up to a dim, blue star.  
`zyx:219` **Zyx (blush):** There. Home. Now two beings on this planet know where it is.  

`zyx:221` **▸** "I see it. It's beautiful."  
> *rapport +1 Zyx*  
`zyx:223` **Zyx (happy):** It is not, actually. It is very small and quite gray. But thank you.  

`zyx:225` **▸** "Is home even real?"  
`zyx:226` **Zyx (neutral):** Is anything? Is the ice machine? It makes ice. That seems real enough.  
> *(end of choice)*

> *show zyx neutral*  
`zyx:229` **Zyx:** After the ark, the mission ends. The Ambassadors carry the ark into the ballroom at 11:11. Then the report is complete. And then...  
`zyx:230` **Zyx:** Then this one is just Zyx. With no mission. On a strange planet. That is the part this one is afraid of.  

> **Choice**
`zyx:232` **Zyx:** Most Earthlings ask what is under the suit. Would you like to know?  

`zyx:234` **▸** "Only if you want to tell me. I like Zyx."  
> *rapport +2 Zyx*  
`zyx:236` Zyx's antennae light up, very slowly, pink.  
`zyx:237` **Zyx (blush):** You like Zyx.  
`zyx:238` **Zyx:** Then Zyx is what you get. Zyx is what is under the suit. All the way down.  

`zyx:240` **▸** "No. Keep the mystery. It's yours."  
> *rapport +1 Zyx*  
`zyx:242` **Zyx (happy):** A respecter of mysteries. Rare. Noted.  

`zyx:244` **▸** "Yes! Who are you, really?"  
`zyx:245` **Zyx (neutral):** This one is Zyx. That is the only answer this one has tonight.  
`zyx:246` The ice machine hums. It's a cold sound.  
> *(end of choice)*

> *if rapport["zyx"] >= ROMANCE_THRESHOLD:*  
`zyx:249` **Zyx (blush):** After the ark. When the mission is complete. Come to the roof. There is one more piece of research this one wishes to do. With you. Only with you.  
> *else:*  
`zyx:251` **Zyx (happy):** Watch for us at 11:11. We will be the ones carrying the gold box. Do not panic.  

## zyx_romance

> *scene bg roof_dawn*  
`zyx:259` After the ark, the Ambassadors of the Outer Drift vanish. One moment they're on stage in their silver suits, the next there's only the duck and the confetti.  
`zyx:260` You look for Zyx in the ballroom, in the hallways, by the ice machine. You find them on the roof, as the sky is going pink.  
`zyx:261` They're sitting on the bench with their sash folded in their lap, antennae glowing softly against the dawn.  
> *show zyx neutral*  
`zyx:263` **Zyx:** Earthling. You found this one. This one was hoping you would. This one did not leave a map. That was a test.  
`zyx:264` **Zyx (happy):** You passed. Obviously. Sit.  
> *if gave_rock:*  
`zyx:266` They're holding the nice rock from the pool. They turn it over and over in their gloved fingers, the way you'd worry a lucky coin.  
`zyx:267` **Zyx (neutral):** The ark has landed. The duck has been revealed. The war over the nature of water has ended in a hug. The report is filed.  
`zyx:268` **Zyx:** The mission is complete.  

> **Choice**
`zyx:271` **Zyx:** Do you want to hear the conclusion? This one wrote it during the ark. While crying. Which was not in the mission plan.  

`zyx:273` **▸** "Read it to me."  
`zyx:274` **Zyx (neutral):** Ahem.  

`zyx:275` **▸** "Only if it says nice things about me."  
`zyx:276` **Zyx (happy):** It says extremely specific things about you. You will be studied for generations.  
> *(end of choice)*

`zyx:278` **Zyx (neutral):** {i}Earth is not ready for contact. Earth is loud, and confusing, and keeps its feelings in rooms labeled LOST & FOUND.{/i}  
`zyx:279` **Zyx:** {i}Earth closes its eyes and shouts the names of dead explorers in swimming pools. Earth puts glitter on strangers. Earth gives its ice machines a planetarium.{/i}  
`zyx:280` **Zyx:** {i}But one Earthling is ready. Recommend further study. Recommend this one stays.{/i}  
> *show zyx blush*  
`zyx:282` **Zyx:** It was approved. By this one. This one is in charge of approvals.  

> **Choice**

`zyx:285` **▸** "So you're staying?"  
`zyx:286` **Zyx (blush):** For a while. On Earth, there is a thing called 'a while.' It is very elastic. We intend to stretch it.  

`zyx:287` **▸** Sit down next to them and take their gloved hand.  
`zyx:288` Three fingers fold around yours. Their antennae go from pink to a deep, warm red.  
> *(end of choice)*

> *show zyx neutral*  
`zyx:291` **Zyx:** Can this one confess something? For the report. The unofficial report.  
`zyx:292` **Zyx:** On the Outer Drift, we communicate by changing color. Slowly. A conversation can take a year. There are thirty-one of us and we are very, very far apart.  
> *if hugged_zyx:*  
`zyx:294` **Zyx:** When you hugged this one by the pool, this one's antennae went a color that does not have a name at home. This one has been trying to name it since Saturday.  
> *if zyx_emergency_contact:*  
`zyx:296` **Zyx:** And in the clinic, when you said you were this one's emergency contact. Nobody has ever been this one's anything.  
`zyx:297` **Zyx (blush):** This one would like to keep finding new colors. With you. If that is permitted under Earth law.  

> **Choice**

`zyx:300` **▸** "It's permitted. It's encouraged."  
`zyx:301` **Zyx (happy):** Excellent. This one will update the legal section of the report.  

`zyx:302` **▸** "What's the color now?"  
`zyx:303` Zyx's antennae are glowing a soft, warm gold, the exact color of the sun coming over the mountains.  
`zyx:304` **Zyx (blush):** This one is calling it... Monday.  
> *(end of choice)*

`zyx:306` **Zyx (blush):** There is one final experiment. On the Outer Drift, when two beings wish to be close, they touch foreheads. Third eye to third eye.  
`zyx:307` **Zyx:** You have only two eyes. This is a known limitation. We will adapt.  

> **Choice**

`zyx:309` **▸** Lean in and touch foreheads.  
`zyx:310` Their forehead is cool and smooth and smells faintly of sunscreen. The third eye closes.  
`zyx:311` For a long moment you just breathe like that, foreheads together, while the birds start up in the pines.  
> *(end of choice)*

`zyx:313` **Zyx (blush):** And now, for comparison. The Earth version. Consent is requested.  

> **Choice**

`zyx:316` **▸** "Granted. For science."  
`zyx:317` You kiss the Ambassador of the Outer Drift on the roof of the Hotel Paradiso at sunrise.  
`zyx:318` Their antennae spark. Actually spark. You're almost sure. It might have been the sun.  
`zyx:319` **Zyx (happy):** Data... very, very confirmed. Further study required. Extensive further study.  
`zyx:320` **Zyx:** This one will need to repeat the experiment. For reproducibility. Science is very strict about this.  
> *(end of choice)*

> *scene bg roof_dawn*  
`zyx:323` The sun clears the mountains and lights up the lake. Down below, cars are starting in the parking lot. Neither of you moves.  
`zyx:324` At some point Zyx takes off one glove and holds your hand properly. Their hand is warm. It has five fingers. You don't say anything about it, and they don't either.  
> *scene black*  
`zyx:326` {i}Two weeks later, a postcard arrives. The picture on the front is a gray, ordinary star.{/i}  
`zyx:327` {i}Return address: THE OUTER DRIFT (it's near Oakland).{/i}  
`zyx:328` **Zyx:** Earthling. Research continues. Thursday? This one has found a restaurant where you cook your own food on a hot rock. Gerald recommended it.  
> *if gave_rock:*  
`zyx:330` **Zyx:** Bring the nice rock. This one wants to introduce it to the hot rock. It is important that rocks have friends.  
> *else:*  
`zyx:332` **Zyx:** This one has found you a nice rock. It is waiting on this one's windowsill. It has been told about you.  
`zyx:333` **Zyx:** — Z. (The report now has a section about you. It is forty pages long and still in progress.)  
> *→ jump ending_card*  

## zyx_friend

> *scene bg exterior*  
> *show zyx happy*  
`zyx:343` On Monday morning, a silver figure is standing in the hotel parking lot, waving with all three fingers at every car as it pulls out.  
`zyx:344` **Zyx:** Earthling! You are leaving. This one has prepared a farewell ritual. It is called 'a wave.' This one has been practicing.  
`zyx:345` **Zyx (neutral):** The report is filed. Earth is not ready for contact. But Earth has friends in it. This one checked. You are one of them.  
`zyx:346` **Zyx:** On the Outer Drift, friendship is shown by changing to the same color as someone. This one cannot do that. This one is stuck being silver.  
`zyx:347` Zyx reaches into the bag of EARTH ARTIFACTS and hands you a single lost flip-flop, very solemnly.  
`zyx:348` **Zyx (happy):** This is the highest honor of our people. Do not lose it. We already lost the other one.  
`zyx:349` **Zyx:** Goodbye, Earthling! You are in the report! Section nine: Friends. You are the whole of section nine!  

---

# encounters.rpy

`encounters:14` enc_wedding  
`encounters:15` enc_gurus  
`encounters:16` enc_penguin_post  
`encounters:17` enc_speed_dating  
`encounters:27`   
> *if not left:*  
> *if getattr(store, "vn_testing", False):*  
> *else:*  

## random_encounter

> *if _enc is not None:*  
> *scene bg hallway*  
`encounters:44` On your way down the hall, something finds you first.  
> *→ call expression _enc*  

## enc_wedding

`encounters:50` Two mute clowns in bras and fishnets block the corridor. One is holding a bouquet of plastic forks. The other is weeping silently into a handkerchief that goes on forever.  
`encounters:51` They see you and gasp, enormously, without making a sound. One points at you. Then at a hand-lettered sign: WITNESS NEEDED.  
`encounters:52` It's a wedding. They need a witness. You are, apparently, it.  

> **Choice**
`encounters:54` What kind of witness are you?  

`encounters:56` **▸** A solemn one. Nod gravely at every vow they mime.  
`encounters:57` The vows go on for some time. One involves a juggling pin. You nod gravely through all of it.  
`encounters:58` At the end they kiss through their red noses, and the clown with the handkerchief hands you one end of it to keep. It is still going.  

`encounters:59` **▸** An emotional one. Weep openly.  
`encounters:60` You weep. They're delighted. Soon all three of you are weeping in perfect silence, and a passerby stops to weep too, just in case.  

`encounters:61` **▸** Object. Loudly.  
`encounters:62` Both clowns turn to you in slow-motion horror. Then they mime, very clearly: {i}speak now or forever hold your peace.{/i}  
`encounters:63` You hold your peace. They forgive you with a single shared honk of a bicycle horn, and the wedding resumes.  
> *(end of choice)*

`encounters:64` As they leave, one of them presses a plastic fork into your hand. It feels like an honor.  

## enc_vampire

`encounters:69` Halfway down the hall, a coffin is propped against the wall with its lid open. Inside, a vampire in full Victorian dress is lying very still with his arms crossed.  
`encounters:70` One eye opens.  
`encounters:71` He whispers: "Is it night yet? I can't tell in here. The fog machine is very confusing."  

> **Choice**

`encounters:73` **▸** "It's night. Rise."  
`encounters:74` He sits up in one smooth, theatrical motion, cape flaring. "At last." Then he notices his leg is asleep and has to lie back down.  

`encounters:75` **▸** "It's actually morning. Go back to sleep."  
`encounters:76` "Oh no," he whispers, and pulls the lid closed. From inside: "Wake me at the ark. Thank you, mortal."  

`encounters:77` **▸** "Is there room in there for two?"  
`encounters:78` He considers this seriously. "Ask before you touch," he says. "But yes. It's a double. The party thought of everything."  
`encounters:79` You lie in a vampire's coffin for exactly one minute. It's surprisingly comfortable. He smells like cloves.  
> *(end of choice)*

## enc_flu_shot

`encounters:84` Two nurses in vintage uniforms and very large paper hats roll a squeaking cart down the hallway. The cart has a sign: EMOTIONAL FLU SHOTS. NO NEEDLES. SOME FEELINGS.  
`encounters:85` "You there," says one. "When was your last emotional flu shot?"  

> **Choice**

`encounters:87` **▸** "Never. Give me the full dose."  
`encounters:88` They tap a jellybean gently against your arm and make you say one thing you're proud of out loud.  
`encounters:89` It's harder than it sounds. When you manage it, they clap and stick a gold star on your sleeve. It says BRAVE PATIENT.  

`encounters:90` **▸** "I'm afraid of feelings. Is there a smaller dose?"  
`encounters:91` "The pediatric dose," says the other nurse kindly, and hands you a lollipop. "For later. When you're ready."  

`encounters:92` **▸** Run.  
`encounters:93` You run. They don't chase you. They just call after you, very warmly: "We'll be here when you're ready!" It somehow feels worse.  
> *(end of choice)*

## enc_elder

> *scene bg livingroom*  
`encounters:99` You duck into the tea bar for a minute. At the counter, an old man in a rumpled white suit is rocking slowly back and forth, sweating, his eyes fixed on something you can't see.  
`encounters:100` He must be well past seventy. He looks like he's somewhere very far away.  

> **Choice**

`encounters:102` **▸** Gently check in: "Hey. Are you doing okay?"  
`encounters:103` He stops rocking. He turns and gives you a look that is compassionate and absolutely immovable, like a mountain being patient with a pebble.  
`encounters:104` "Friend," he says, "I have seen things in the last hour that you would not believe in a thousand years. But thank you for checking."  
`encounters:105` He pats your hand twice and goes back to wherever he was. You leave feeling oddly blessed, and slightly put in your place.  

`encounters:106` **▸** Let him be, but sit nearby with your tea.  
`encounters:107` You sit two stools down. After a while he starts humming. After a longer while you realize you're humming too. Neither of you says a word.  
`encounters:108` When you leave, he raises his teacup to you without looking. You raise yours back.  
> *(end of choice)*

## enc_gurus

> *scene bg ballroom*  
`encounters:114` At the edge of the ballroom, two gurus are holding competing seminars twenty feet apart, each with a small and devoted crowd.  
`encounters:115` One, in flowing white, is teaching that inner peace comes from surrender. The other, in a fleece vest with a headset mic, is teaching that it comes from a 5 AM routine and a cold plunge.  
`encounters:116` They both spot you at the same moment. "You," they say in unison. "Which way to inner peace?"  

> **Choice**

`encounters:118` **▸** "Both. Surrender to the cold plunge."  
`encounters:119` A long silence. Then the white-robed guru begins to weep, and the fleece-vest guru begins to weep, and they embrace across the gap.  
`encounters:120` Their followers merge into one confused, joyful seminar. Someone starts a guided meditation in an ice bath. You slip away while you can.  

`encounters:121` **▸** "Surrender. Obviously."  
`encounters:122` The white-robed guru bows to you. The fleece-vest guru adds you to an email list. You don't know how. You never gave an email.  

`encounters:123` **▸** "Cold plunge. Obviously."  
`encounters:124` You are handed a towel and a schedule. Your wake-up time tomorrow is listed as 4:45 AM. You quietly put the schedule in a plant.  
> *(end of choice)*

## enc_heist

> *scene bg exchange*  
`encounters:130` Someone has built a pawn shop entirely out of cardboard in the corner of the stock exchange. Cardboard guitars, cardboard watches, a cardboard taxidermied moose.  
`encounters:131` Three people in ski masks with cardboard guns burst in just as you arrive. "NOBODY MOVE," one of them shouts. "THIS IS A STICK-UP. THE STICKS ARE CARDBOARD."  

> **Choice**

`encounters:133` **▸** Join the heist. Grab the cardboard moose.  
`encounters:134` You flee with the moose under your arm. Ten minutes later, the robbers return in plain clothes and try to sell the moose back to the shop.  
`encounters:135` The shopkeeper offers forty dollars of cardboard money. You split it four ways. It's the most honest money you've ever made.  

`encounters:136` **▸** Be a brave customer. Refuse to put your hands up.  
`encounters:137` The robbers confer in whispers. One of them hands you a cardboard medal for valor and apologizes. Then they rob the shop anyway.  

`encounters:138` **▸** Offer to be the hostage.  
`encounters:139` "Oh, thank god," says a robber. "We forgot to plan for that." You're led out with great tenderness and released two doors down with a cardboard sandwich.  
> *(end of choice)*

## enc_alices

`encounters:144` A conga line of Alices comes around the corner. Alices of every age, every shape, every gender, in blue dresses and white pinafores, holding each other's waists.  
`encounters:145` At the end of the line, a six-foot caterpillar is smoking a bubble pipe. It points the pipe at you.  
`encounters:146` "WHO," it says, "ARE YOU?"  

> **Choice**

`encounters:148` **▸** "I'm not sure yet. That's sort of why I came."  
`encounters:149` The caterpillar blows a long, thoughtful stream of bubbles. "Good answer," it says. "Most people lie." It gestures, and the Alices open a space for you in the line.  
`encounters:150` You conga for one full lap of the second floor. It is better than you'd think.  

`encounters:151` **▸** "An Alice. Obviously."  
`encounters:152` Several Alices cheer. One gives you her headband. You are now an Alice. You conga for a full lap of the second floor.  

`encounters:153` **▸** "Just passing through."  
`encounters:154` "No one," says the caterpillar, "is just passing through." The Alices conga onward without you. You feel vaguely judged by an insect.  
> *(end of choice)*

## enc_note

`encounters:163` Someone in black jogs up to you, out of breath, headset askew. Not Wren. Someone newer, holding a folded slip of hotel stationery.  
> *if note_for is not None:*  
`encounters:165` "Hey, you're friends with [note_name], right? They left this at the tea bar. Can you get it to them? I'm drowning tonight."  

> **Choice**

`encounters:167` **▸** Take the note and promise to deliver it.  
`encounters:169` You find [note_name] an hour later and hand it over. They read it, laugh out loud, and fold it into a pocket.  
`encounters:170` "It's a list I made," they say, "of people I wanted to talk to this weekend. I forgot it. You were already on it."  

`encounters:171` **▸** Read it first. Just a peek.  
`encounters:172` You unfold it. It's a list, in [note_name]'s handwriting, of people they wanted to talk to this weekend. Your description is on it. Third line.  
`encounters:173` You fold it back up, feeling slightly guilty and extremely pleased, and deliver it without saying a word.  
> *(end of choice)*

> *else:*  
`encounters:175` "This is for... huh. It just says {i}for whoever you meet tonight.{/i} Can you take it?"  
`encounters:176` You unfold it. It says, in careful handwriting: {i}Go into one room you'd normally walk past.{/i}  
`encounters:177` You put it in your pocket. It feels like a dare.  
`encounters:193`   
> *if not met_list:*  

## enc_penguin_post

> *if "juni" in met:*  
> *→ jump enc_penguin_post_juni*  
> *scene bg penguinpost*  
`encounters:205` A line snakes out of a doorway and halfway down the hall. At the front, a sign glows in pink and blue neon: PENGUIN POST. PLEASE TAKE A NUMBER.  
`encounters:206` You take a number. It's 4,812. The display above the counter reads NOW SERVING: 3.  
`encounters:207` Inside it's a post office at the South Pole, sometime around the year 3000. Ice and snow everywhere, all of it sparkly and fake and freezing-looking under the neon. Behind the counter, three penguins in tiny postal caps are stamping things with enormous seriousness.  
`encounters:208` The line, it turns out, is the main event. A penguin with a clipboard walks up and down it running Line Activities: line trivia, line stretches, a line-wide game of telephone that starts as {i}I love you{/i} and ends as {i}iceberg lettuce{/i}.  
`encounters:209` Eventually a penguin waddles over, looks at your ticket, looks at you, and waves you straight to the front. Nobody ever finds out why.  

> **Choice**
`encounters:213` "How can Penguin Post serve you today?"  

`encounters:215` **▸** Write a postcard to [postcard_name].  
> *(shown if postcard_for is not None)*  
`encounters:216` The stationery has prompts printed on it. Yours reads: {i}Tell them one thing you noticed about them that they probably think nobody noticed.{/i}  
`encounters:217` You write it. It's harder than you expected, and then it isn't.  
`encounters:218` A penguin stamps it with a stamp shaped like a fish and slaps it into a mailbag. "Delivered within the hour," it honks. "Or your money back. You paid no money."  
`encounters:220` Later that night, across a hallway, you see [postcard_name] reading a postcard with a fish on it. They look up and find you. They don't say anything. They don't have to.  

`encounters:221` **▸** Ask to be mailed.  
`encounters:222` The penguins confer. One of them gets out the bubble wrap.  
`encounters:223` You are wrapped, stamped on the forehead (FRAGILE: CONTAINS FEELINGS), loaded onto a hand truck and wheeled at great speed down the hallway by two penguins who are clearly having the time of their lives.  
`encounters:224` You are delivered to the tea bar. Someone signs for you. You are unwrapped, handed a cup of tea, and released back into the wild.  

`encounters:225` **▸** Sign up for mail carrier orientation.  
`encounters:226` Orientation takes eleven minutes. You learn the Penguin Oath, the Penguin Waddle, and the correct way to hold a mailbag (with dignity, and both flippers).  
`encounters:227` You graduate with a paper postal cap and a bag of letters addressed to rooms you've never heard of. You deliver four of them. One of them is to yourself. It says: {i}Welcome to the flock.{/i}  
> *(end of choice)*

`encounters:228` On your way out, the NOW SERVING sign clicks over to 4. The line cheers.  

## enc_fanny_bar

> *if "gerald" in met:*  
> *→ jump enc_fanny_bar_gerald*  
> *scene bg ballroom*  
`encounters:236` The heat on the dance floor is unbearable. Somebody's glitter is melting. The bass is coming up through the carpet like it's trying to escape.  
`encounters:237` Then a cool breeze hits you. A woman in a blue hard hat and a hi-vis vest has set up an enormous box fan at the edge of the dance floor and is aiming it at the crowd like a firefighter.  
`encounters:238` She hands you a business card. It matches the sticker on her fan:  
`encounters:239` {i}FEELING HOTT? Come to Room 313 for a Blow Job at the OnlyFans Fanny Bar!!{/i}  
`encounters:240` She winks. "Fan Technician. I'm licensed."  
> *scene bg fanbar*  
`encounters:242` Room 313 is an oasis. Every surface has a fan on it: box fans, desk fans, ceiling fans, a fan that oscillates so dramatically it might be dancing. A basket of folding hand fans sits by the door under a sign: FOR SUBSCRIBERS ONLY!  
`encounters:243` Hand-lettered signs on every wall beg: PLEASE SUBSCRIBE!! SMASH THAT SUBSCRIBE!! WE ARE BEGGING YOU!!  
`encounters:244` A projector on the wall plays glitched-out clips of every movie scene that has ever had a fan in it, on loop.  

> **Choice**
`encounters:246` A clipboard by the door has a space for your name.  

`encounters:248` **▸** Subscribe.  
`encounters:249` You write your name. A bell rings. Somebody throws a little confetti at you, then fans it away.  
`encounters:250` As a subscriber, you are entitled to the Fanny Bar. It doesn't serve drinks. It serves mist. A bartender in a bow tie offers you a spray bottle fan: "Lemon or lilac?"  
`encounters:251` You choose lilac. It is the best thing that has happened to your face all night.  

`encounters:252` **▸** Refuse to subscribe, on principle.  
`encounters:253` You stand in the middle of the room, unsubscribed and sweating, as fans blow cool air on everyone except you.  
`encounters:254` It's a kind of protest. Nobody notices. One of the fans turns slowly toward you, almost apologetically, and then turns away again.  

`encounters:255` **▸** Check out the booth in the corner.  
`encounters:256` In the corner is an old-fashioned video booth with a blue-and-yellow sign: NUTBUSTER VIDEO. A rack of VHS tapes has titles like {i}Fan Girls Go Wild{/i} and {i}Hotties Cool Off{/i}.  
`encounters:257` You check out {i}Fan Girls Go Wild{/i} and put it in the VCR.  
`encounters:258` It is forty minutes of women holding fans. Just fans. Electric fans, paper fans, one very large fan made of ostrich feathers. Nobody ever does anything but fan.  
`encounters:259` You watch the whole thing. It's weirdly relaxing. A soft voice-over describes the sensation of moving air.  
> *(end of choice)*

`encounters:260` Then the power cuts out.  
`encounters:261` Every fan in the room winds down at once with a long, sad, descending whine, like a choir of tiny dying engines. In the silence, the heat rushes back in.  
`encounters:262` "NEVER FEAR!" shouts the Fan Technician from the doorway. "WE HAVE PALM FRONDS! FOR SUBSCRIBERS ONLY!"  
`encounters:263` The last few holdouts stampede toward the clipboard.  
`encounters:264` You leave fully cooled, with a folding hand fan and a pair of tiny propeller pasties you will explain to no one, ever.  

## enc_tentacletopia

> *if "solstice" in met:*  
> *→ jump enc_tentacletopia_solstice*  
> *scene bg tentacletopia*  
`encounters:272` A round hatch in the wall is marked AIRLOCK. A person in a full shrimp costume pokes their head out and beckons you in with a feeler.  
`encounters:273` "Adventurer! Thank the tides. The world is searching for the tech that'll save us all, and our sources say the answer lies in the Lost City of Miami."  
`encounters:274` "It sank into the ocean centuries ago. The jellyfish run it now. They have evolved. They have opinions."  
`encounters:275` "We, the crustaceans, will guide you. In exchange we only ask for one thing: an extended broadcast of our favorite program, {i}Shrimp Justice: A Crustacean Courtroom Show{/i}."  
`encounters:276` They hand you a snorkel, a pair of swim goggles and a flashlight that has been painted to look like a much better flashlight. You step through the airlock.  
`encounters:277` Beyond it is the bottom of the sea. A kelp forest sways under blue light. The sunken art-deco towers of Miami lean in the gloom, their neon signs still faintly glowing. Giant jellyfish drift overhead, trailing their tentacles.  

> **Choice**
`encounters:279` Where do you search for the savior tech?  

`encounters:281` **▸** Poke around the coral wall.  
`encounters:282` The coral wall is full of tiny hidden dioramas, each about the size of a shoebox. A shrimp wedding. A shrimp tax office. A shrimp lying on a tiny shrimp therapist's couch, describing its childhood.  
`encounters:283` Behind the last diorama, wedged in the coral, something glints.  

`encounters:284` **▸** Duck through the jellyfish.  
`encounters:285` You weave between the jellyfish, ducking tentacles. One brushes your shoulder. It's made of streamers and it smells faintly of fog machine.  
`encounters:286` At the heart of the swarm, the jellyfish part, as if they've been guarding something. Something glints.  

`encounters:287` **▸** Stop to watch an episode of Shrimp Justice.  
`encounters:288` A tiny TV half-buried in the sand is playing {i}Shrimp Justice{/i}. Today's case: a hermit crab is suing another hermit crab over a shell.  
`encounters:289` You are, apparently, the jury. You find for the plaintiff. The shrimp guides weep with joy. As a reward, one of them points a feeler at the kelp, where something glints.  
> *(end of choice)*

`encounters:290` You dig it out of the sand and hold it up. It's a disco ball.  
`encounters:291` Every shrimp in the room gasps. Somewhere a speaker kicks on and starts playing a 1977 disco hit. The jellyfish begin, very slowly, to dance.  
`encounters:292` "DISCO," says your shrimp guide, overcome. "Of course. It was always disco. The shrimp have always known."  

## enc_zany_optical

> *if "zyx" in met:*  
> *→ jump enc_zany_optical_zyx*  
> *scene bg optical*  
`encounters:300` A door is propped open by a giant inflatable eyeball. Inside, it's an optometrist's office from a strip mall, run through a vaporwave blender: neon pink and teal, palm-tree wallpaper, synth music that sounds like the 1980s imagining the future.  
`encounters:301` The receptionist is an iPad on a stand, with a cheerful AI face. Behind it, an enormous motorized googly eye rolls slowly around in its socket.  
`encounters:302` "Welcome to ZANY OPTICAL, a subsidiary of Manic Medical!" says the iPad. "Do you have vision insurance? Do you have a vision? Do you have insurance? Please don't answer, I'm an iPad."  
`encounters:303` A doctor in a lab coat and a pair of glasses with tiny windshield wipers on them waves you into the exam chair.  
`encounters:304` "Let's begin. Look through here and tell me: which is better, A or B?"  

> **Choice**
`encounters:306` Lens A: the world, but everyone is a little bit more of a golden retriever.\n\nLens B: the world, but every plant is softly whispering encouragement.  

`encounters:308` **▸** A is better.  
`encounters:309` "Interesting. Very interesting," says the doctor, writing {i}golden retriever{/i} on a clipboard and underlining it.  

`encounters:310` **▸** B is better.  
`encounters:311` "Mm-hm. Mm-hm," says the doctor, writing {i}plants{/i} on a clipboard and drawing a little heart next to it.  

`encounters:312` **▸** They're the same.  
`encounters:313` The doctor puts down the clipboard. "Nobody has ever said that," they whisper. "You may have perfect vision." They pick the clipboard back up. "Let's keep going anyway."  
> *(end of choice)*

`encounters:314` The doctor flips a switch. The room floods with a sodium-yellow light that drains every color into shades of grey. "Just checking your color vision. Now: what color is this flag?"  
`encounters:315` They hold up a flag. In the strange light, it could be anything.  

> **Choice**

`encounters:317` **▸** "Red."  
`encounters:318` "Correct! You can spot a red flag. That's rare in here."  

`encounters:319` **▸** "Green."  
`encounters:320` "Hm. You see green flags where others see red. Optimist. We have a lens for that, but we don't recommend it."  

`encounters:321` **▸** "It depends on the relationship."  
`encounters:322` The doctor nods slowly. "Diagnosis: wisdom. Extremely rare. Not covered by insurance."  
> *(end of choice)*

`encounters:323` Your prescription is a pair of glasses that bend your vision ninety degrees upward. You wear them for five minutes in the back of the clinic, staring at the ceiling, while a stranger in matching glasses lies down on the floor so you can talk face to face.  
`encounters:324` It's one of the best conversations you've had all weekend. You never see their face.  
`encounters:325` On your way out, the iPad flips around: HOW MUCH WOULD YOU LIKE TO TIP YOUR PROVIDER TODAY? The options are 18%, 20%, 25% and A Compliment. You choose A Compliment. The giant googly eye rolls happily.  

## enc_speed_dating

> *if speed_cast():*  
> *→ jump enc_speed_dating_cast*  
> *scene bg speeddating*  
`encounters:335` A sign on a door reads PLATONIC SPEED DATING: FIND YOUR SURVIVAL BUDDY. Inside, a crowd is standing in the middle of a ballroom side-room. Two volunteers stand at opposite walls holding small whiteboards.  
`encounters:336` The host, in a sequined blazer and a headset microphone, spots you. "A newcomer! Perfect. In you come. Every round, I ask a question. You pick a side. Everyone quietly judges each other. Then I loudly judge everyone. Ready?"  
`encounters:337` Round one. The host writes on a whiteboard paddle and holds it up: ONLY ONE CAN EXIST.  

> **Choice**
`encounters:339` Electric guitar, or electric synths?  

`encounters:341` **▸** Electric guitar.  
`encounters:342` You stand with the guitars. A man in a leather jacket nods at you with deep respect.  

`encounters:343` **▸** Electric synths.  
`encounters:344` You stand with the synths. Someone next to you hums an arpeggio, very quietly, to welcome you.  

`encounters:345` **▸** Stand exactly in the middle.  
`encounters:346` "A FENCE SITTER," booms the host. The whole room turns to look at you. "Bold. Wrong, but bold."  
> *(end of choice)*

`encounters:347` Round two. WOULD YOU RATHER.  

> **Choice**
`encounters:349` Know every language, or be able to talk to animals?  

`encounters:351` **▸** Every language.  
`encounters:352` You stand with the polyglots. The host asks your name and introduces you to a woman who says she's learning Klingon "for the love of the game."  

`encounters:353` **▸** Talk to animals.  
`encounters:354` You stand with the animal people. It's a bigger crowd than you'd think. A man in a duck costume gives you a solemn nod.  

`encounters:355` **▸** Talk to animals, but only pigeons.  
`encounters:356` The host stares at you. "That wasn't an option." Then, after a long pause: "I'll allow it." You stand alone in a third, newly drawn pigeon section.  
> *(end of choice)*

`encounters:359` After a few more rounds, the host walks the room, pairing people who chose the same side every single time.  
> *if dating_match is not None:*  
`encounters:361` And there, on your side for every single question, is [dating_match_name]. You hadn't even noticed them in the crowd.  
`encounters:362` "You two!" says the host. "Kindred spirits. Draw a mission." You pull a handwritten tag from a grab bag: {i}Go somewhere neither of you has been yet this weekend. Report back.{/i}  
`encounters:364` You and [dating_match_name] spend twenty minutes looking for a room neither of you has been in. You find a supply closet with a single disco light in it. You both agree it counts.  
> *else:*  
`encounters:366` You've ended up on the same side as a woman in a tinfoil cape every single time. The host introduces you. "Survival buddies! Draw a mission."  
`encounters:367` Your tag reads: {i}Find the strangest room on this floor and rate it out of ten.{/i} You do. It's a seven. She says eight. You agree to disagree, and part as friends forever.  

## enc_let_it_go

> *if "wren" in met:*  
> *→ jump enc_let_it_go_wren*  
> *scene bg letitgo*  
`encounters:375` Outside a door, a person with a clipboard and a calm, professional smile stops you. A sign beside them reads LET IT GO: A WORKSHOP.  
`encounters:376` "Before we begin, a few intake questions. On a typical day, how often do you look at your phone?"  

> **Choice**

`encounters:378` **▸** "A healthy amount."  
`encounters:379` "Mm," they say, writing {i}denial{/i} on the clipboard.  

`encounters:380` **▸** "Constantly. It's a problem."  
`encounters:381` "Thank you for your honesty," they say, writing {i}ready{/i} on the clipboard.  

`encounters:382` **▸** "I've used it as a flashlight all weekend."  
`encounters:383` They look up, impressed. "You're further along than most." They write {i}advanced{/i} on the clipboard.  
> *(end of choice)*

`encounters:384` Inside, folding chairs face a small stage. The presenter, in a turtleneck and a headset mic, clicks to the first slide of a presentation titled GOODBYE, MY BELOVED: LIFE AFTER THE PHONE.  
`encounters:385` Four slides in, the projector dies. Without missing a beat, the presenter pulls out a stack of hand-drawn posterboard slides and continues the presentation analog, flipping each one with a dramatic flourish.  
`encounters:386` There are exercises. You're asked to name the first app you open every morning, then to say goodbye to it out loud. Someone in the second row breaks down weeping while saying goodbye to a weather app.  
`encounters:387` At the end, the presenter gestures to a table at the side of the room. On it is a pile of blank wooden phone-shaped blocks, a hot-glue gun, and an overwhelming amount of glitter.  
`encounters:388` "Every graduate may adopt an Emotional Support Phone. It can't do anything. That's the point. It's just there for you."  

> **Choice**

`encounters:390` **▸** Decorate an Emotional Support Phone.  
`encounters:391` You give yours googly eyes, a glittery case and a little drawn-on screen that just says {i}you're doing great{/i}.  
`encounters:392` You put it in your pocket. Every so often for the rest of the weekend, you reach for your phone out of habit and find this one instead. It's always a good surprise.  

`encounters:393` **▸** Leave with nothing. You're ready.  
`encounters:394` The presenter places a hand over their heart. "That," they say quietly, "is the most advanced thing I have ever seen."  
`encounters:395` The room gives you a standing ovation as you leave. You feel incredibly, absurdly free.  
> *(end of choice)*

## enc_penguin_post_juni

> *scene bg penguinpost*  
`encounters:406` A line snakes out of a doorway and halfway down the hall. At the front, a sign glows in pink and blue neon: PENGUIN POST. PLEASE TAKE A NUMBER.  
`encounters:407` You take a number: 4,812. Directly in front of you, holding ticket 4,811 in both sleeves like a prize, is a pink axolotl.  
> *show juni happy*  
`encounters:409` **Juni:** Oh! Hi! You're in the line! Isn't the line great?  
`encounters:410` **Juni (neutral):** I've been here forty minutes. I love it. A line is a room you're allowed to stand outside of. Nobody expects you to go in yet.  
`encounters:411` A penguin with a clipboard waddles past, running Line Activities. Line trivia. Line stretches. A game of telephone that starts as {i}I love you{/i} and reaches you as {i}iceberg lettuce{/i}.  
`encounters:412` **Juni (happy):** Iceberg lettuce. Pass it on.  
`encounters:413` Eventually a penguin waves you both to the counter together. It slides two postcards across, with prompts printed on them.  
`encounters:414` Juni's says: {i}Write to the person standing behind you in line.{/i} Yours says: {i}Tell them one thing you noticed about them that they think nobody noticed.{/i}  
`encounters:415` **Juni (surprised):** Oh no. Oh, that's... okay. Okay. Don't look.  

> **Choice**
`encounters:417` What do you write?  

`encounters:419` **▸** "You laugh like it surprises you every time."  
> *rapport +1 Juni*  
`encounters:421` You hand it over. Juni reads it, and goes quiet, and then the hood goes very pink.  
`encounters:422` **Juni (blush):** ...Nobody's ever noticed that. I didn't know I did that.  

`encounters:423` **▸** "You hold your sleeves when you're nervous. It's very cute."  
> *rapport +1 Juni*  
`encounters:425` **Juni (blush):** I'm not nervous. I'm... okay, I'm holding my sleeves right now.  
`encounters:426` They don't let go of them. They hold the postcard against their chest instead.  

`encounters:427` **▸** "See you at the ark!"  
`encounters:428` **Juni (neutral):** Oh. Ha. Yeah! See you at the ark.  
`encounters:429` They look at the card a beat longer than a card that says {i}see you at the ark{/i} needs.  
> *(end of choice)*

`encounters:430` A penguin stamps Juni's postcard with a fish and tosses it into a mailbag.  
`encounters:431` **Juni (neutral):** You'll get it within the hour. Or your money back. You paid no money.  
`encounters:432` Forty minutes later, a penguin finds you in the hallway, salutes, and hands you a postcard. It's covered in tiny drawn axolotls. In the middle, in careful handwriting:  
`encounters:433` {i}You're the first person I didn't wait outside a door for. — J.{/i}  

## enc_fanny_bar_gerald

> *scene bg ballroom*  
`encounters:440` The heat on the dance floor is unbearable. A Fan Technician in a blue hard hat hands you a business card:  
`encounters:441` {i}FEELING HOTT? Come to Room 313 for a Blow Job at the OnlyFans Fanny Bar!!{/i}  
> *scene bg fanbar*  
`encounters:443` Room 313 is an oasis of fans: box fans, desk fans, a ceiling fan spinning so hard it might take off. Signs beg PLEASE SUBSCRIBE!!  
`encounters:444` Directly in front of the biggest box fan, eyes closed, fur streaming backward like a flag in a gale, sits a Sasquatch.  
> *show gerald happy*  
`encounters:446` **Gerald:** Oh. Oh, hello. Forgive me. I've been sitting here for half an hour. I may never move again.  
`encounters:447` **Gerald (neutral):** I have been wearing this coat since 1961. It does not come off. The dance floor was, if I may say, an ordeal.  
`encounters:448` **Gerald:** They tell me I must subscribe to stay. I tried. The clipboard wanted a name. I'm afraid I signed it with a footprint, out of habit. They seem unsure whether it counts.  

> **Choice**
`encounters:450` What do you do?  

`encounters:452` **▸** Drag a second fan over and aim it at him.  
> *rapport +1 Gerald*  
`encounters:454` You drag a pedestal fan across the room and point it at his other side. His fur now blows in two directions at once, like a dandelion.  
`encounters:455` **Gerald (happy):** Oh. Oh, that's... yes. Stereo. You've given me stereo.  

`encounters:456` **▸** Sign the clipboard for both of you.  
> *rapport +1 Gerald*  
`encounters:458` You write your name, and next to it: {i}+1 (Sasquatch).{/i} A bell rings. A volunteer throws confetti at you both and then, apologetically, fans it away.  
`encounters:459` **Gerald (happy):** Subscribed. How modern. I feel tremendously current.  

`encounters:460` **▸** Ask what he thinks of the Nutbuster booth.  
`encounters:461` **Gerald (surprised):** Ah. I... yes. I did investigate the booth. For research.  
`encounters:462` **Gerald (blush):** It's only fans. All of the tapes. Just people with fans. I watched {i}Hotties Cool Off{/i} three times. It was the most relaxing hour of my weekend. Please don't tell Margaret.  
> *(end of choice)*

`encounters:463` Then the power cuts out.  
`encounters:464` Every fan in the room winds down at once with a long, sad, descending whine. The heat rushes back in. People cry out. Someone shouts about palm fronds, for subscribers only.  
`encounters:465` Gerald doesn't move. He just sighs contentedly, reaches into his fur and produces a full-sized fern.  
`encounters:466` **Gerald (happy):** I'm from the woods. We've never had electricity. Allow me.  
`encounters:467` He stands up, all seven feet of him, and begins to fan the entire room with one slow, enormous sweep after another. The crowd turns toward him like sunflowers.  
`encounters:468` When the power comes back, the room gives him a standing ovation. The Fan Technician gives him an honorary blue hard hat. It's much too small. He wears it anyway.  

## enc_tentacletopia_solstice

> *scene bg tentacletopia*  
`encounters:475` A round hatch in the wall is marked AIRLOCK. Inside, a person in a full shrimp costume is briefing a raver who has put a snorkel on over her goggles.  
> *show solstice happy*  
`encounters:477` **Solstice:** Oh my god, hi! Get in here! We're going to the bottom of the sea! The shrimp say the world needs saving and the answer's in the Lost City of Miami!  
`encounters:478` The shrimp guide nods gravely. "The jellyfish run it now. They have evolved. They have opinions. We ask only one thing in return: an extended broadcast of {i}Shrimp Justice: A Crustacean Courtroom Show{/i}."  
`encounters:479` **Solstice:** I already said yes. I've seen four episodes. The hermit crab one is devastating.  
`encounters:480` Beyond the airlock: kelp swaying under blue light, sunken art-deco towers, neon signs still faintly glowing in the gloom. Giant jellyfish drift overhead. Solstice's LED top lights up the water around her like a little submarine.  
`encounters:481` **Solstice (neutral):** Okay. Savior tech. Where do we look?  
`encounters:482` You dig together through the coral dioramas: a shrimp wedding, a shrimp tax office, a shrimp on a tiny therapist's couch. Then Solstice shrieks and holds something up.  
`encounters:483` It's a disco ball.  
> *show solstice surprised*  
`encounters:485` **Solstice:** DISCO. It's DISCO. The savior tech is DISCO. I KNEW it! I've been saying this for YEARS!  
`encounters:486` A speaker kicks on. A 1977 disco track fills the sea. The shrimp weep with joy. The jellyfish, very slowly, begin to dance.  

> **Choice**
`encounters:488` **Solstice (happy):** Come on! The jellyfish are dancing! We have to dance with the jellyfish! It's literally the end of the world!  

`encounters:490` **▸** Dance with her and the jellyfish.  
> *rapport +1 Solstice*  
`encounters:492` You dance at the bottom of the sea with a raver and a swarm of evolved jellyfish. Solstice is laughing so hard her snorkel fills with air.  
`encounters:493` **Solstice (blush):** This is the best rave I've ever been to. And it's in a hotel room. And it's underwater. And it's with you.  

`encounters:494` **▸** Hold up the disco ball so it catches her lights.  
> *rapport +1 Solstice*  
`encounters:496` You hold the disco ball up over her head. Her LED top throws a thousand tiny colored lights across the whole ocean floor, the towers, the kelp, the jellyfish.  
`encounters:497` **Solstice (blush):** Oh. Oh wow. Look what we made.  

`encounters:498` **▸** Sit on the coral and watch.  
`encounters:499` You sit down on the reef. Solstice stops dancing and points at you, scandalized.  
`encounters:500` **Solstice (neutral):** Hey! No spectators! It's the rule! Even at the bottom of the sea!  
`encounters:501` She drags you up by both hands anyway. The jellyfish make room.  
> *(end of choice)*

`encounters:502` As you leave, the shrimp crown Solstice Disco Queen of the Lost City of Miami with a crown made of bottle caps. She wears it for the rest of the night.  

## enc_zany_optical_zyx

> *scene bg optical*  
`encounters:509` Through a door propped open by a giant inflatable eyeball: a vaporwave optometrist's office, pink and teal neon, synth music, an enormous googly eye rolling slowly on the wall.  
`encounters:510` At the reception desk, a silver alien is deep in an argument with an iPad.  
> *show zyx neutral*  
`encounters:512` **Zyx:** This one's insurance is from the Outer Drift. It is very comprehensive. It covers meteors.  
`encounters:513` "I'm sorry," chirps the iPad, "we don't accept Outer Drift. Have you considered paying with a compliment?"  
`encounters:514` **Zyx (happy):** Earthling! You are here. Good. This one requires an emergency contact for an eye exam. You have experience in this field.  
`encounters:515` A doctor in glasses with tiny windshield wipers leads you both into the exam room, sits Zyx in the chair, looks into their face, and drops the clipboard.  
`encounters:516` "That's three eyes," the doctor whispers. "I've only ever examined two at a time. This is the greatest day of my career."  
`encounters:517` The diagnosis comes quickly: third-eye astigmatism, mild. Then the doctor floods the room with a strange yellow light that drains all color away, and holds up a flag.  
`encounters:518` "Ambassador. What color is this flag?"  
`encounters:519` **Zyx (neutral):** Magenta.  
`encounters:520` "There's no magenta flag," says the doctor. "There's red, and there's green."  
`encounters:521` **Zyx:** There is magenta. It means: proceed, but with feelings. We use it constantly at home.  
`encounters:522` The doctor writes it down, reverently. Then they bring out a tray of frames, each with three lenses.  

> **Choice**
`encounters:524` **Zyx:** Earthling. You will choose this one's glasses. This one trusts your Earth taste.  

`encounters:526` **▸** The sparkly cat-eye ones.  
> *rapport +1 Zyx*  
`encounters:528` **Zyx (blush):** Fabulous. This one is fabulous. Write that down for the report.  

`encounters:529` **▸** The ones with tiny windshield wipers, like the doctor's.  
> *rapport +1 Zyx*  
`encounters:531` The wipers go back and forth across all three lenses. Zyx is delighted beyond words, which for Zyx is a lot of words.  
`encounters:532` **Zyx (happy):** For meteors. Practical. The insurance company will be thrilled.  

`encounters:533` **▸** "Honestly? You look perfect without them."  
> *rapport +1 Zyx*  
`encounters:535` Zyx goes very still. Their antennae glow, slowly, pink.  
`encounters:536` **Zyx (blush):** ...Then this one will wear them only for science.  
> *(end of choice)*

`encounters:537` On the way out, the iPad flips around: HOW MUCH WOULD YOU LIKE TO TIP YOUR PROVIDER TODAY? Zyx chooses A Compliment, leans in close to the giant googly eye and says, very formally:  
`encounters:538` **Zyx (neutral):** Your eye is extremely round. On behalf of the Outer Drift, well done.  
`encounters:539` The googly eye rolls with what can only be described as joy.  

## enc_let_it_go_wren

> *scene bg letitgo*  
`encounters:546` Outside a door, a sign reads LET IT GO: A WORKSHOP. Beside it, looking like someone who has been sentenced, stands Wren.  
> *show wren neutral*  
`encounters:548` **Wren:** Don't. Don't say anything. Pilar signed me up. She called it a {i}wellness intervention{/i}. In front of the whole crew.  
`encounters:549` **Wren:** It's about saying goodbye to your phone. I don't even have my phone on me. I have this.  
`encounters:550` She holds up her walkie-talkie like you've asked to see her ID.  
`encounters:551` Inside, folding chairs face a small stage. The presenter, in a turtleneck and headset mic, asks everyone to place their device in a wicker basket at the front. One by one, people do. Some of them are crying.  
`encounters:552` Wren doesn't move. Her hand is wrapped around the walkie so tightly her knuckles are white.  

> **Choice**
`encounters:554` What do you do?  

`encounters:556` **▸** "I'll keep an ear on it. If anything comes through, I'll get you."  
> *rapport +1 Wren*  
`encounters:558` You hold out your hand. She looks at it for a long time, then puts the walkie in it, like she's handing over something alive.  
`encounters:559` **Wren (blush):** Okay. Okay. If it says {i}fire{/i}, you come get me. It will say fire. If it says anything about a flamingo, ignore it.  

`encounters:560` **▸** Put your own phone in the basket, then look at her.  
> *rapport +1 Wren*  
`encounters:562` You walk to the front and drop your phone into the basket. Then you turn around and look at her.  
`encounters:563` **Wren (surprised):** Oh, that's... that's peer pressure. That's really effective peer pressure.  
`encounters:564` She walks up and lays the walkie gently on top of your phone, like tucking it into bed.  

`encounters:565` **▸** "You don't have to. It's okay."  
`encounters:566` **Wren (neutral):** ...Thanks. Yeah. I'll just... turn it down a little.  
`encounters:567` She turns the volume down one notch. It's something.  
> *(end of choice)*

`encounters:568` The presenter clicks to the first slide. Four slides in, the projector dies, and the talk continues on hand-drawn posterboard.  
`encounters:569` Wren lasts four minutes and thirty seconds before her hand starts drifting toward the basket. Then five minutes. Then, somewhere around minute eight, she stops reaching altogether, sits back, and actually listens.  
`encounters:570` At the end, there's a crafting table: blank wooden phones, googly eyes, glitter. Everyone gets to make an Emotional Support Phone.  
`encounters:571` Wren makes an Emotional Support Walkie instead. It's a block of wood with a pipe-cleaner antenna, two googly eyes, and a strip of gaffer tape on the back that says OFF DUTY. It doesn't do anything.  
`encounters:572` **Wren (happy):** It's perfect. Nobody can reach me on it. Not a single person.  
`encounters:573` When you walk out, the real walkie is back on her belt. But the wooden one is in her hand.  

## enc_speed_dating_cast

> *scene bg speeddating*  
`encounters:580` A sign on a door reads PLATONIC SPEED DATING: FIND YOUR SURVIVAL BUDDY. Inside, a crowd is milling around a side-room of the ballroom, with a strip of yellow tape down the middle of the floor.  
`encounters:581` And it's not just strangers. You spot familiar faces in the crowd: [speed_cast_names].  
`encounters:582` The host, in a sequined blazer and a headset microphone, claps. "Every round, I ask a question. You pick a side. Everyone quietly judges each other. Then I loudly judge everyone."  
`encounters:583` Round one. The host holds up a whiteboard paddle: ONLY ONE CAN EXIST.  

> **Choice**
`encounters:585` Electric guitar, or electric synths?  

`encounters:587` **▸** Electric guitar.  

`encounters:589` **▸** Electric synths.  

`encounters:591` **▸** Stand exactly in the middle.  
> *(end of choice)*

`encounters:594` Round two. WOULD YOU RATHER.  

> **Choice**
`encounters:596` Know every language, or be able to talk to animals?  

`encounters:598` **▸** Every language.  

`encounters:600` **▸** Talk to animals.  

`encounters:602` **▸** Talk to animals, but only pigeons.  
> *(end of choice)*

`encounters:605` Round three. THIS OR THAT.  

> **Choice**
`encounters:607` Sunrise, or sunset?  

`encounters:609` **▸** Sunrise.  

`encounters:611` **▸** Sunset.  

`encounters:613` **▸** "I've never stayed up to see either."  
> *(end of choice)*

`encounters:617` The host walks the room, matching people who kept ending up on the same side.  
`encounters:618` "You!" They point at you, then at [dating_match_name]. "Survival buddies. I've been watching. Draw a mission."  
`encounters:620` You pull a handwritten tag from the grab bag: {i}Go somewhere neither of you has been yet this weekend. Report back.{/i}  
> *→ call expression "speed_mission_" + dating_match*  
`encounters:629` juni  
`encounters:630` gerald  
`encounters:631` solstice  
`encounters:632` wren  
`encounters:633` zyx  

> **Platonic Speed Dating: what each guest says when they're on your side**

`encounters:638` **Juni (happy):** Synths! Synths are like... music that doesn't need you to be cool about it.  
`encounters:639` **Gerald (happy):** Guitar. My cousin Bernard played. Badly. Movingly.  
`encounters:640` **Solstice (happy):** SYNTHS. I'm going to hug everyone on this side. Brace.  
`encounters:641` **Wren (neutral):** Guitar. You can fix a guitar with tape. You can't fix a synth with tape. I've tried.  
`encounters:642` **Zyx (neutral):** The middle. This one is gathering data from both sides. Also, this one is a fence.  

`encounters:643` **Juni (happy):** Animals. They don't need you to make small talk. Lotl agrees.  
`encounters:644` **Gerald (neutral):** I already talk to animals. I thought everyone did. This is very upsetting news.  
`encounters:645` **Solstice (happy):** Every language! Imagine telling people they're doing great in like four hundred languages.  
`encounters:646` **Wren (neutral):** Every language. Then I could finally read the manuals for every fog machine. They're never in English.  
`encounters:647` **Zyx (happy):** Pigeons. Yes. This one already speaks pigeon. They are excellent diplomats.  

`encounters:648` **Juni (blush):** Neither. I've never stayed up. Maybe this weekend. If I'm with someone.  
`encounters:649` **Gerald (happy):** Sunrise. Always sunrise. It's the only time the forest is completely honest.  
`encounters:650` **Solstice (blush):** Neither! I'm always inside, dancing. That's... wow, that sounded sadder out loud.  
`encounters:651` **Wren (neutral):** Sunrise. Usually through a crack in a loading dock door, holding a toolbox. But still. Sunrise.  
`encounters:652` **Zyx (neutral):** Sunset. At home, sunset lasts four years. This one finds yours very brisk.  

> *if not same:*  
`encounters:665` You look around. Nobody you know is on your side this time. The host notices and nods at you, impressed: "A lone wolf."  

## speed_mission_juni

> *show juni happy*  
`encounters:686` You and Juni wander the halls looking for a room neither of you has been in. Juni stops at every door. Then, at a door marked SUPPLY, they take a breath and walk in first.  
`encounters:687` **Juni (blush):** I went in first. Did you see that? I went in first.  

## speed_mission_gerald

> *show gerald happy*  
`encounters:693` You and Gerald find a room neither of you has been in: the hotel's old boiler room, warm and humming. Gerald declares it the coziest cave he's been in since 1974. You report back: ten out of ten, would hibernate.  

## speed_mission_solstice

> *show solstice happy*  
`encounters:699` You and Solstice find a room neither of you has been in: a tiny closet with one disco light and nobody in it. She turns off her LED top. You stand there in the slow-turning light, not dancing, just talking. It's her favorite room of the weekend.  

## speed_mission_wren

> *show wren happy*  
`encounters:705` You and Wren try to find a room neither of you has been in. This is impossible: Wren has been in every room. Finally she leads you to a broom closet she's never opened, because it's labeled FOR WREN ONLY and she didn't make that sign. Inside is a single folding chair and a note: {i}Sit down. — Pilar.{/i} She does, for a full minute.  

## speed_mission_zyx

> *show zyx happy*  
`encounters:711` You and Zyx find a room neither of you has been in: the hotel laundry. Zyx stands in front of the dryers for a long time, watching the clothes go round. "Small planets," they whisper. "Warm, tumbling planets." They take extensive notes.  

---

# finale.rpy

## finale

> *→ call ceremony*  
> *scene bg ballroom*  
> *if candidates:*  
`finale:22` The party goes on around you, louder than ever. But your mind keeps drifting back to someone.  
> *if len(candidates) > 1:*  
`finale:24` More than one someone, actually. But you can only be in one place at sunrise.  

> **Choice**
`finale:27` Where do you go?  

`finale:29` **▸** Look for Juni. You have a feeling they'll be down by the pool.  
> *(shown if "juni" in candidates)*  

`finale:31` **▸** Climb to the roof. Gerald likes to be somewhere high when the sun comes up.  
> *(shown if "gerald" in candidates)*  

`finale:33` **▸** Find Solstice before the sun comes up.  
> *(shown if "solstice" in candidates)*  

`finale:35` **▸** Wait for Wren to get off shift.  
> *(shown if "wren" in candidates)*  

`finale:37` **▸** Go find Zyx. The mission's almost over.  
> *(shown if "zyx" in candidates)*  

`finale:39` **▸** Don't go to anyone. Some weekends are just yours.  
> *(end of choice)*

> *if who is not None:*  
> *→ jump expression "%s_romance" % who*  
> *if friend is not None:*  
> *→ jump friend_ending*  
> *→ jump solo_ending*  

## friend_ending

`finale:53` You dance until the windows go gray. You don't fall in love this weekend. That's okay. Not every story has to end the same way.  
`finale:54` But you made a friend. A real one. The kind you'll text in six months for no reason.  
> *→ call expression "%s_friend" % friend*  
> *scene black*  
`finale:57` {i}On the drive home, there's still glitter in your ears, a ping-pong ball in your pocket, and a laminated card that says you were never here.{/i}  
`finale:58` {i}You were, though.{/i}  
> *→ jump ending_card*  

## solo_ending

> *scene bg roof_dawn*  
`finale:66` You end up on the roof alone at sunrise. The rigging is slack. The string lights have burned out one by one, like the party is going to sleep a room at a time.  
`finale:67` You didn't find your person this weekend. Maybe you weren't looking. Maybe you were looking at everything else.  
`finale:68` And there was a lot of everything else. A hotel room that wasn't there. Mute clowns selling shares in people. A war over water, settled by a duck in a golden box.  
`finale:69` Seven hundred people in costumes being kind to each other on purpose, for three days, for no reason anyone could name.  
`finale:70` You sit on the bench and watch the light come over the mountains and across the lake. It's quiet up here. Somewhere below, a single kazoo plays one long note and stops.  
`finale:71` Down in the parking lot, Tamsin is waving both arms at you, covered in balloons, shouting something you can't hear.  
`finale:72` **Tamsin (text):** THERE you are!!! I looked for you for THREE DAYS. where WERE you  
`finale:73` Everywhere, you think. You were everywhere.  
`finale:74` **Tamsin (text):** ok come down I saved you a balloon. it's the good one. it says 'you were never here'  
> *scene black*  
`finale:76` {i}On the drive home you realize you never once took out your phone, except as a flashlight. You don't miss a single thing you didn't photograph.{/i}  
`finale:77` {i}A card arrives a month later, no return address. It says: NEXT TIME.{/i}  
`finale:78` {i}You put it on the fridge. Every morning, you look at it, and it makes you braver in some small way you can't quite explain.{/i}  
> *→ jump ending_card*  

## ending_card

> *scene black*  
> *if endings_found < endings_total:*  
`finale:94` {i}Thanks for checking in. Everyone who enters is already checked in. Come back anytime. The guests will remember you, even if the game doesn't.{/i}  
> *else:*  
`finale:96` {i}You've found every ending. Auntie Acid is very proud of you. Have a strawberry candy.{/i}  
