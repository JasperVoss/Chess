import RPi.GPIO as gpio
import move, time, halifax, bounceback
from random import randint
magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)


move.move_square(7.5, 0)
magnet_on()