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

move.calibrate()
time.sleep(.5)
move.move([100, 100])
time.sleep(.5)
move.move([100, 390])
time.sleep(.5)
move.move([500, 100])

# magnet_off()
# move.move_square(7, 0)
# magnet_on()
# time.sleep(.3)
# move.move_square(6.5, .5)
# time.sleep(.3)
# move.move_piece(6.5, 1.5)
# time.sleep(.3)
# move.move_piece(6, 2)
# magnet_off()
# move.move_square(4, 0)
# magnet_on()
# move.move_piece(0, 4)
# time.sleep(.3)
# move.move_piece(0, 7)
# time.sleep(.3)
# move.move_piece(0, 0)
# time.sleep(.3)
# move.move_piece(4, 0)
# magnet_off()
# move.move_square(6, 2)
# magnet_on()
# move.move_square(6.5, 1.5)
# time.sleep(.3)
# move.move_piece(6.5, .5)
# time.sleep(.3)
# move.move_piece(7, 0)
# magnet_off()

# bounceback.bounceback()