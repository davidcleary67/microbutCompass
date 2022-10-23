hands: List[Image] = []
dir2 = 0
idir = 0
def showCompass():
    global hands, dir2, idir
    hands = [images.create_image("""
            . . # . .
                    . . # . .
                    . . # . .
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . # . . .
                    . # . . .
                    . . # . .
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    # # . . .
                    . . # . .
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    # # # . .
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # . .
                    # # . . .
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # . .
                    . # . . .
                    . # . . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # . .
                    . . # . .
                    . . # . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # . .
                    . . . # .
                    . . . # .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # . .
                    . . . # #
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    . . . . .
                    . . # # #
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . . . . .
                    . . . # #
                    . . # . .
                    . . . . .
                    . . . . .
        """),
        images.create_image("""
            . . . # .
                    . . . # .
                    . . # . .
                    . . . . .
                    . . . . .
        """)]
    while True:
        dir2 = input.compass_heading() / 30
        idir = Math.floor(dir2)
        hands[idir].show_image(0)
        if input.button_is_pressed(Button.B):
            break
    basic.show_number(input.compass_heading())

def on_button_pressed_a():
    basic.show_leds("""
        # . # . #
                . # # # .
                # # . # #
                . # # # .
                # . # . #
    """)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    """)
    basic.clear_screen()
    basic.pause(1000)
    showCompass()
input.on_button_pressed(Button.B, on_button_pressed_b)
