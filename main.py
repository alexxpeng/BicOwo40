print("BicOwo Starting...")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers

import busio as io
import adafruit_ssd1306                                                                     
from digitalio import DigitalInOut
import adafruit_framebuf

i2c = io.I2C(board.GP17, board.GP16)#set to sda and scl
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
reset_pin = DigitalInOut(board.GP15) # any pin!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
TH = bytearray()
fb = adafruit_framebuf.FrameBuffer(TH, 64, 32)

print("Syncing OLED Display...")
#OLED STUFF
oled.fill(0)
oled.rect(0, 0, 128, 32, 1)

oled.show()
#END OF OLED STUFF


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.col_pins = (board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0,)  
keyboard.row_pins = (board.GP21, board.GP20, board.GP19, board.GP18,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [  #QWERTY
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,\
        KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENT, KC.NO,\
        KC.LSFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.SLASH, KC.RSFT, KC.NO,\
        KC.LCTL, KC.LGUI, KC.MO(2), KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.MO(1), KC.MO(3)
    ],
    [  #NumKeys
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.DELETE,\
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,\
        KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.RSFT, KC.NO,\
        KC.TRNS, KC.LALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ],
    [  #Function Keys
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,\
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,\
        KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.RSFT, KC.NO,\
        KC.TRNS, KC.LALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ],
    [  #Extras
        KC.NO, KC.NO, KC.UP, KC.NO, KC.NO, KC.NO, KC.NO, KC.MINUS, KC.EQUAL, KC.LBRACKET, KC.RBRACKET, KC.BSLASH,\
        KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.SCOLON, KC.QUOTE, KC.NO, KC.NO,\
        KC.LSFT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.COMMA, KC.DOT, KC.RSFT, KC.NO,\
        KC.TRNS, KC.LALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ],
]
print("Keymap Configured...")
print("Startup Successful!")
print("=====================")
if __name__ == '__main__':
    keyboard.go()