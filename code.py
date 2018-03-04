import board
import digitalio
import time
import busio
from st7032i import ST7032i

i2c = busio.I2C(board.SCL, board.SDA)

cols = 16
rows = 2
lcd = ST7032i(i2c)

#Write ABC
for c in "Hi Workshopshed":
    lcd.write_data (ord(c))

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
 
while True:
    led.value = True
    time.sleep(0.8)
    led.value = False
    time.sleep(0.2)# Write your code here :-)