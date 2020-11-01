# Grove Temperature & Humidity Sensor

[Wiki-Eintrag](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/)

## Anschluss
Diesen Sensor musst du über einen Digitalen Anschluss am [Grove Pi+-Board](./grove-pi-plus-board.md) anschliessen.
In unserem Beispiel haben wir `D4` gewählt.

## Software
```python
import grovepi
import time
grovepi.set_bus('RPI_1')

run = True

while run:
    try:
        # Pin: D4, Color: 0
        [temp, humidity] = grovepi.dht(4, 0)
        print('Temperatur:', temp)
        print('Luftfeuchtigkeit:', humidity)
        time.sleep(5)

    except IOError as e:
        run = False
        print('IOError')
        
    except KeyboardInterrupt:
        run = False
        print('good bye')
```
