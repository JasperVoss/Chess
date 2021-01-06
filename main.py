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
move.move_square(7, 0)
magnet_on()
time.sleep(.1)
move.move_square(6.5, .5)
time.sleep(.1)
move.move_square(6.5, 1.5)
time.sleep(.1)
move.move_square(6, 2)
magnet_off()
move.move_square(4, 0)
magnet_on()
move.move_piece(4, 5)
time.sleep(.1)
move.move_piece(9, 5)
time.sleep(.1)
move.move_piece(0, 5)
time.sleep(.1)
move.move_piece(4, 0)
