import RPi.GPIO as gpio
import time


outpins = [21, 20, 16, 12, 7, 8, 25, 24]
inpins = [26, 19, 13, 6, 5, 11, 9, 10, 22, 23]

gpio.setmode(gpio.BCM)

for i in outpins:
    gpio.setup(i, gpio.OUT)
for i in inpins:
    gpio.setup(i, gpio.IN)


def get_piece_pos():

    status = []
    for i in range(8):
        status.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in range(len(outpins)):

        for p in inpins:
            gpio.setup(p, gpio.OUT)
            gpio.output(p, 0)

        time.sleep(.01)

        for p in inpins:
            gpio.setup(p, gpio.IN)

        gpio.output(outpins[i], 1)

        time.sleep(.01)

        for j in range(len(inpins)):
            if gpio.input(inpins[j]) == gpio.LOW:
                status[i][j] == 1
            else:
                status[i][j] == 0

        gpio.output(outpins[i], 0)

    return status


while True:
    print(chr(27) + "[2J")
    state = get_piece_pos()
    for i in state:
        for j in i:
            print(j, end = " ")
        print("\n")
    time.sleep(.5)