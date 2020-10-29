import grovepi
import grove_rgb_lcd
import time
import math

grovepi.set_bus('RPI_1')

print('running on grovepi', grovepi.version())
grove_rgb_lcd.setText('Meteostation v3')
grove_rgb_lcd.setRGB(255, 128, 0)

pin = 4
color = 0
running = True

while running:
    try:
        [temp, humidity] = grovepi.dht(pin, color)

        if not math.isnan(temp):
            print('Temperatur:', temp, '°C')
            grove_rgb_lcd.setText('Meteostation v3\n' + 'inside: ' + str(temp) + 'C')
        else:
            print('no input')
        time.sleep(2)

    except IOError as e:
        print('IOError')
        print(e)
        
    except KeyboardInterrupt:
        running = False
        grove_rgb_lcd.setText('')
        grove_rgb_lcd.setRGB(0, 0, 0)
        print('...good bye...')
