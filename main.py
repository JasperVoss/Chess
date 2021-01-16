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

magnet_off()
move.move_square(7, 8)
magnet_on()
move.move_square(1, 1)
time.sleep(.1)
move.move_square(2, 9)
time.sleep(.1)
move.move_square(7, 0)
time.sleep(1)
move.move_square(7, 9)
magnet_off()
move.calibrate()
