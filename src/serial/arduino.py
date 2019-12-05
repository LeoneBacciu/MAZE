from serial import Serial


class Arduino:
    arduino = Serial('/dev/ttyACM0', 115200)

    @staticmethod
    def read():
        try:
            return float(Arduino.arduino.readline()[:-2])
        except ValueError:
            return 0.0

    def __del__(self):
        Arduino.arduino.close()

