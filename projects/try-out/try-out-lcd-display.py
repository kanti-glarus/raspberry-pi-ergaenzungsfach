# Grove Pi Plus on top of raspberry
# Connect LCD with *I2C-1*

from grove_rgb_lcd import *

setText("Hello world\nLCD test")
setRGB(0,128,64)

# Slowly change the colors every 0.01 seconds.
for c in range(0, 255):
    setRGB(c, 255-c, 0)
    time.sleep(0.01)

for c in range(0, 255):
    setRGB(255-c, c, 0)
    time.sleep(0.01)

for c in range(0, 255):
    setRGB(c, c, c)
    time.sleep(0.01)

for c in range(0, 255):
    setRGB(255-c, 255-c, 255-c)
    time.sleep(0.01)

setRGB(0,255,0)
setText("Good Bye...")