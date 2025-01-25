def on_logo_pressed():
    global zoom
    if zoom:
        zoom = False
        music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        zoom = True
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    OLED12864_I2C.zoom(zoom)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global nr2
    OLED12864_I2C.clear()
    OLED12864_I2C.show_number(1, 0, nr2, 1)
    OLED12864_I2C.show_string(1, 3, "Hello!", 1)
    OLED12864_I2C.hline(0, 20, 50, 1)
    OLED12864_I2C.rect(0, 0, 63, 31, 1) # Rahmen
    nr2 += 1
    basic.show_number(nr2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global nr2
    nr2 += -1
    basic.show_number(nr2)
input.on_button_pressed(Button.B, on_button_pressed_b)

input2 = 0
temp_z = 0
nr2 = 0
time = 0
zoom = False
temp2 = 0
txt = ""
zoom = True
OLED12864_I2C.init(60)
basic.show_icon(IconNames.YES)

def on_forever():
    basic.pause(2000)
basic.forever(on_forever)
