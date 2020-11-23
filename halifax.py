import RPi.GPIO as gpio
import time


outPins = [21, 20, 16, 12, 7, 8, 25, 25]
inPins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 23]

gpio.setmode(gpio.BCM)
for i in outPins:
    gpio.setup(i, gpio.IN)
for i in inPins:
    gpio.setup(i, gpio.IN)

status = []
template = []
for i in range(len(inPins)):
    template.append(0)
for i in range(len(outPins)):
    status.append(template)

while True:
    for i in range(len(outPins)):
        gpio.setup(outPins[i], gpio.OUT)
        gpio.output(outPins[i], 1)

        for j in range(len(inPins)):
            if gpio.input(inPins[j]) == gpio.LOW:
                status[i][j] = 0
            else:
                status[i][j] = 1
        gpio.output(outPins[i], 0)
        gpio.setup(outPins[i], gpio.IN)
        time.sleep(.01)
    for s in status:
        print(s)
    print('\n\n')
    time.sleep(3)
