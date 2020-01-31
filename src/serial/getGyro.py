import time
from arduino import Arduino


arduino = Arduino('/dev/ttyUSB3')
for _ in range(10000):
    while True:
        arduino.write(b'1')
        time.sleep(1)
        arduino.write(b'0')
        time.sleep(1)

