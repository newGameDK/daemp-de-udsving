datalogningStatus = 0

def on_button_pressed_a():
    global datalogningStatus
    datalogningStatus = 1
    basic.show_leds("""
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    datalogger.delete_log()
    basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global datalogningStatus
    if datalogningStatus:
        datalogningStatus = 0
        basic.show_leds("""
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            """)
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval():
    if datalogningStatus == 1:
        datalogger.log(datalogger.create_cv("Acceleration", input.acceleration(Dimension.STRENGTH)))
loops.every_interval(100, on_every_interval)