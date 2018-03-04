#http://blog.boochow.com/article/453758697.html
#Place in LIB folder

from micropython import const
import time

CLEAR_DISPLAY       = const(0x01)
RETURN_HOME         = const(0x02)
SET_ENTRY_MODE      = const(0x04)
DISPLAY_ON          = const(0x0C)
FUNCTION_SET        = const(0x20)
OSC_FREQUENCY       = const(0x10)
POW_ICON_CONTRAST   = const(0x50)
FOLLOWER            = const(0x60)
SET_CONTRAST        = const(0x70)

class ST7032i(object):

    def __init__(self, i2c, addr=0x3e):
        self.i2c = i2c
        self.addr = addr
        self.buf = bytearray(2)
        self.init_display()

    def write_cmd(self, cmd):
        self.buf[0] = 0x00
        self.buf[1] = cmd
        self.i2c.writeto(self.addr, self.buf)

    def write_data(self, char):
        self.buf[0] = 0x40
        self.buf[1] = char
        self.i2c.writeto(self.addr, self.buf)

    def init_display(self):
        while not self.i2c.try_lock():
            pass
        for cmd in (
            # data is 8 bits | 2 lines mode
            FUNCTION_SET | 0x10 | 0x08,
            # select Instruction table 1
            FUNCTION_SET | 0x10 | 0x08 | 0x01,
            # BS=1 (1/4 bias), OSC frequency=183Hz
            OSC_FREQUENCY | 0x08 | 0x04,
            # ICON on, Booster on, Contrast(upper 2bits) = 10
            POW_ICON_CONTRAST | 0x08 | 0x04 | 0x02,
            # Contrast(lower 4bits) = 1000
            SET_CONTRAST | 0x08,
            # Follower on, amplify ratio = 4/8
            FOLLOWER | 0x08 | 0x04
            ):
            self.write_cmd(cmd)
        time.sleep(0.2)
        for cmd in (
            DISPLAY_ON,
            CLEAR_DISPLAY,
            # Left to right, no shift
            SET_ENTRY_MODE | 0x02
            ):
            self.write_cmd(cmd)
