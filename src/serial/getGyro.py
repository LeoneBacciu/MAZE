from arduino import Arduino

datap = 0.0
for _ in range(10000):
    data = Arduino.read()
    if data < datap-1.0 or data > datap+1.0:
        print(data)
        datap = data
