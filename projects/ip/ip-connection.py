# Grove Pi Plus on top of raspberry
# Connect LCD with *I2C-1*

import grove_rgb_lcd
import socket
import time
from datetime import datetime

print('start:', datetime.now())
wait = 3

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def call_for_ip():
    # Output current ip
    ip = get_ip()

    print('result:', datetime.now())
    print('ip:', ip)
    grove_rgb_lcd.setText("IP: " + ip)
    grove_rgb_lcd.setRGB(0,128,64)

    if ip != '127.0.0.1':
        return True

    for i in range(0, wait):
        grove_rgb_lcd.setText("IP: " + ip + "\n ... " + str(wait-i))
        time.sleep(1)
        print('sleep', i)

    grove_rgb_lcd.setText("IP: " + ip)

    return False

ip_check = False

while not ip_check:
    ip_check = call_for_ip()



    
