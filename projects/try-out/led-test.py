import grovepi
import time

grovepi.set_bus('RPI_1')

ledPort = 2
run = True

print(grovepi.version())

grovepi.pinMode(ledPort, "OUTPUT")


while run:
    try:
        grovepi.digitalWrite(ledPort, 1)
        time.sleep(1)
        grovepi.digitalWrite(ledPort, 0)
        time.sleep(1)
    except IOError:
        print('IOError')
        grovepi.digitalWrite(ledPort, 0)
        run = False
    except KeyboardInterrupt:
        print('good bye')
        grovepi.digitalWrite(ledPort, 0)
        run = False
