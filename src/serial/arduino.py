from serial import Serial
from time import sleep


class Arduino:

    def __init__(self, port):
        self.arduino = Serial(port, 115200)

    def read(self):
        while self.arduino.in_waiting > 0:
            sleep(.1)
        return self.arduino.readline().decode("utf-8")[:-2]

    def write(self, s):
        self.arduino.write(s)

    def ping(self):
        self.write(b'0')
        print(self.read() == '48')

    def __del__(self):
        self.arduino.close()
