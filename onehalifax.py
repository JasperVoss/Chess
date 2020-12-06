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
    time.sleep(1)
    gpio.setup(inpin, gpio.IN)

    gpio.output(outpin, 0)
    time.sleep(.1)
    gpio.output(outpin, 0)
    print(gpio.input(inpin))

    print(status)