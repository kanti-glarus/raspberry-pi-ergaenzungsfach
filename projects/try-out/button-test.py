import grovepi
import time

grovepi.set_bus('RPI_1')

buttonPort = 3
run = True

print(grovepi.version())

grovepi.pinMode(buttonPort, "INPUT")

while run:
    try:
        digitalInput = grovepi.digitalRead(buttonPort)
        print(digitalInput)
        time.sleep(1)
    except IOError:
        print('IOError')
        run = False
    except KeyboardInterrupt:
        print('good bye')
        run = False
