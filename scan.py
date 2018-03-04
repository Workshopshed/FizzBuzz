# Gemma/Trinket IO demo - I2C scan
# I2C addresses found: ['0x3e']

 
import board
import busio
import time
 
# can also use board.SDA and board.SCL for neater looking code!
i2c = busio.I2C(board.D2, board.D0)
 
while not i2c.try_lock():
    pass
 
while True:
    print("I2C addresses found:", [hex(i) for i in i2c.scan()])
    time.sleep(2)