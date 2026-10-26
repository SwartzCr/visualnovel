## core.rpy — characters, images, rapport tracking, and the guest book.

################################################################################
## Characters
################################################################################

define narrator = Character(None, what_italic=False)

define j = Character("Juni", image="juni", color="#ff9ccc")
define g = Character("Gerald", image="gerald", color="#e0a878")
define s = Character("Solstice", image="solstice", color="#ffd36b")
define w = Character("Wren", image="wren", color="#c8b8ff")
define z = Character("Zyx", image="zyx", color="#7affd0")

define oz = Character("Grandma Ozone", color="#ffb07a")
define tam = Character("Tamsin (text)", color="#9fe6ff", what_italic=True)
define herald = Character("The Herald", color="#ffe14d")
define clown = Character("A Mute Clown", color="#ff7a7a")
define nurse = Character("Nurse Ratchet-and-Clank", color="#7ad8a8")
define robot = Character("THE ORACLE", color="#c8a0ff", what_font="DejaVuSansMono.ttf")
define beige = Character("Man in a Beige Suit", color="#d8c8a8")
define priest = Character("Deacon of Cast Iron", color="#b0b0b0")
define priestess = Character("High Priestess of Teflon", color="#ff8080")
define moth = Character("Mothman", color="#ff6060")
define walkie = Character("Walkie-talkie", color="#a0a0a0", what_italic=True)
define pj = Character("Man in Pajamas", color="#a8c8ff")

################################################################################
## Images
################################################################################

image bg exterior = "images/bg/exterior.png"
image bg exterior_night = "images/bg/exterior_night.png"
image bg lobby = "images/bg/lobby.png"
image bg pool = "images/bg/pool.png"
image bg hallway = "images/bg/hallway.png"
image bg bedroom = "images/bg/bedroom.png"
image bg room404 = "images/bg/room404.png"
image bg lostfound = "images/bg/lostfound.png"
image bg regen = "images/bg/regen.png"
image bg breakfast = "images/bg/breakfast.png"
image bg forest = "images/bg/forest.png"
image bg cryptid = "images/bg/cryptid.png"
image bg exchange = "images/bg/exchange.png"
image bg karaoke = "images/bg/karaoke.png"
image bg ballroom = "images/bg/ballroom.png"
image bg ballroom_ark = "images/bg/ballroom_ark.png"
image bg livingroom = "images/bg/livingroom.png"
image bg mission = "images/bg/mission.png"
image bg roof = "images/bg/roof.png"
image bg roof_dawn = "images/bg/roof_dawn.png"
image bg fortune = "images/bg/fortune.png"
image bg clinic = "images/bg/clinic.png"
image bg planetarium = "images/bg/planetarium.png"

init python:
    for _who in ("juni", "gerald", "solstice", "wren", "zyx"):
        for _expr in ("neutral", "happy", "surprised", "blush"):
            renpy.image((_who, _expr), "images/sprites/%s_%s.png" % (_who, _expr))

image black = Solid("#000000")
image white = Solid("#ffffff")

transform slightleft:
    xalign 0.25 yalign 1.0

transform slightright:
    xalign 0.75 yalign 1.0

define flash = Fade(0.1, 0.0, 0.4, color="#ffffff")
define slowfade = Fade(0.8, 0.4, 0.8)

################################################################################
## Rapport
################################################################################

define ROMANCE_THRESHOLD = 10
define FRIEND_THRESHOLD = 5

define GUESTS = ["juni", "gerald", "solstice", "wren", "zyx"]

define GUEST_INFO = {
    "juni": ("Juni", "#ff9ccc", "A person in a pink axolotl kigurumi. Hood stays up."),
    "gerald": ("Gerald", "#e0a878", "A Sasquatch. Drinks tea. Possibly not a costume."),
    "solstice": ("Solstice", "#ffd36b", "A raver in fur leg warmers and an LED top. Gives gifts."),
    "wren": ("Wren", "#c8b8ff", "Crew. Dressed in black. Has a headset and a clipboard and a lot to do."),
    "zyx": ("Zyx", "#7affd0", "Ambassador from the Outer Drift. Studying Earth parties."),
}

default rapport = {"juni": 0, "gerald": 0, "solstice": 0, "wren": 0, "zyx": 0}
default pool_seen = {"juni": 0, "gerald": 0, "solstice": 0, "wren": 0, "zyx": 0}
default night_seen = {"juni": 0, "gerald": 0, "solstice": 0, "wren": 0, "zyx": 0}
default met = set()
default day = 1
default met_tonight = []
default wanders = 0
default chosen = None

init python:

    def gain(who, n=1):
        """Add rapport. Big moments get a little notification."""
        store.rapport[who] += n
        store.met.add(who)
        name = GUEST_INFO[who][0]
        if n >= 2:
            renpy.notify("%s will remember that." % name)
        elif n < 0:
            renpy.notify("%s seems a little further away." % name)

    def hearts(who):
        v = max(0, store.rapport[who])
        full = min(5, v // 2)
        return "♥" * full + "♡" * (5 - full)

    def romanceable():
        return [g for g in GUESTS if store.rapport[g] >= ROMANCE_THRESHOLD]

    def closest():
        best = max(GUESTS, key=lambda g: store.rapport[g])
        return best if store.rapport[best] >= FRIEND_THRESHOLD else None

## Shown in the top-right corner by the time_tag screen (ui.rpy).
default time_label = ""

init python:
    config.overlay_screens.append("time_tag")
