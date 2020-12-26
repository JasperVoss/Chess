import RPi.GPIO as gpio
import time


outpins = [21, 20, 16, 12, 7, 8, 25, 24]
inpins = [23, 22, 10, 9, 11, 5, 6, 13, 19, 26]

gpio.setmode(gpio.BCM)

for i in outpins:
    gpio.setup(i, gpio.OUT)
for i in inpins:
    gpio.setup(i, gpio.IN)

def get_square(i, j):
    for p in outpins:
        gpio.output(p, 0)
    gpio.setup(inpins[i], gpio.OUT)
    gpio.output(inpins[i], 0)
    time.sleep(.08)
    gpio.setup(inpins[i], gpio.IN)
    gpio.output(outpins[j], 1)
    time.sleep(.08)
    return gpio.input(inpins[i]) == 1

def get_state():
        
    pos = [[0 for _ in range(8)] for _ in range(10)]
        
    for p in outpins:
        gpio.output(p, 0)

    for i in range(len(outpins)):

        for p in inpins:
            gpio.setup(p, gpio.OUT)
            gpio.output(p, 0)

        time.sleep(.08)

        for p in inpins:
            gpio.setup(p, gpio.IN)

        gpio.output(outpins[i], 1)

        time.sleep(.08)

        for j in range(len(inpins)):
            if gpio.input(inpins[j]) == 0:
                pos[j][i] = 1
            else:
                pos[j][i] = 0

        gpio.output(outpins[i], 0)

    return pos

