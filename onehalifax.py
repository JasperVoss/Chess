import RPi.GPIO as gpio
import time


outpin = 21
inpin = 26

gpio.setmode(gpio.BCM)
gpio.setup(outpin, gpio.OUT)
gpio.output(outpin, 0)
gpio.setup(inpin, gpio.IN)

while True:
    gpio.setup(inpin, gpio.OUT)
    gpio.output(inpin, 0)
    time.sleep(0)
    gpio.setup(inpin, gpio.IN)

    gpio.output(outpin, 1)
    time.sleep(0)
    print(chr(27) + "[2J")
    print(gpio.input(inpin))
    time.sleep(.2)
    gpio.output(outpin, 0)

