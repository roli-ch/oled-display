input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (zoom) {
        zoom = false
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    } else {
        zoom = true
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    
    OLED12864_I2C.zoom(zoom)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    OLED12864_I2C.clear()
    OLED12864_I2C.showNumber(1, 0, nr2, 1)
    OLED12864_I2C.showString(1, 3, "Hello!", 1)
    OLED12864_I2C.hline(0, 20, 50, 1)
    OLED12864_I2C.rect(0, 0, 63, 31, 1)
    //  Rahmen
    nr2 += 1
    basic.showNumber(nr2)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    nr2 += -1
    basic.showNumber(nr2)
})
let input2 = 0
let temp_z = 0
let nr2 = 0
let time = 0
let zoom = false
let temp2 = 0
let txt = ""
zoom = true
OLED12864_I2C.init(60)
basic.showIcon(IconNames.Yes)
basic.forever(function on_forever() {
    basic.pause(2000)
})
