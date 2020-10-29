import grovepi
import time

grovepi.set_bus('RPI_1')

print(grovepi.version())

pin = 4
color = 0
run = True

while run:
    try:
        [temp, humidity] = grovepi.dht(pin, color)
        print(temp)
        print(humidity)
        time.sleep(2)

    except IOError as e:
        print('IOError')
        print(e)
        
    except KeyboardInterrupt:
        run = False
        print('good bye')
