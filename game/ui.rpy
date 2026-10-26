## ui.rpy — custom screens: the time tag and the guest book.

################################################################################
## Screens
################################################################################

## Little day/time tag in the top-right corner.
screen time_tag():
    zorder 50
    if time_label:
        frame:
            xalign 1.0 xoffset -16 ypos 12
            background Frame("gui/tag.png", 18, 10)
            padding (20, 9)
            text time_label size 16 color "#ffe6f4" bold True

## The guest book: who you've met and how close you are.
screen guest_book():
    tag menu
    modal True
    add Solid("#0a0614e6")

    frame:
        xalign 0.5 yalign 0.5
        xsize 900
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        padding (40, 30)

        vbox:
            spacing 18
            text "GUEST BOOK" size 34 color gui.accent_color xalign 0.5
            text "Hotel Marisol — please do not photograph this page." size 14 color "#a99cc8" xalign 0.5

            for gid in GUESTS:
                if gid in met:
                    $ nm, colr, blurb = GUEST_INFO[gid]
                    hbox:
                        spacing 20
                        text nm size 26 color colr min_width 160
                        text hearts(gid) size 26 color "#ff5fb8" min_width 180
                        text blurb size 16 color "#e8e0ff" yalign 0.5 xmaximum 420
                else:
                    hbox:
                        spacing 20
                        text "???" size 26 color "#5a4a78" min_width 160
                        text "♡♡♡♡♡" size 26 color "#3a2a50" min_width 180
                        text "You haven't met this guest yet." size 16 color "#6f6488" yalign 0.5

            null height 6
            text "Rumor has it that on the last night, the guests you're closest to might want a moment alone." size 15 color "#a99cc8" xalign 0.5 text_align 0.5
            textbutton "Close" action Return() xalign 0.5


## Soft shadows so dialogue and names stay readable over the glow.
style say_dialogue:
    outlines [ (2, "#0a041466", 0, 1) ]
    line_spacing 4

style say_label:
    outlines [ (2, "#0a0414cc", 0, 0) ]

style choice_button_text:
    outlines [ (2, "#0a041488", 0, 1) ]
