import RPi.GPIO as gpio
import move, time
from random import randint
magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)

magnet_off()
	
while True:
	move.move([300, 250])
	time.sleep(2)
	move.release_tension()
	time.sleep(.2)
	move.tension()
	move.move([randint(50, 566), randint(50, 442)])
	move.release_tension()
	time.sleep(.2)
	move.tension()
	move.move([randint(50, 566), randint(50, 442)])
	move.release_tension()
	time.sleep(.2)
	move.tension()
# d = int(input("distance?: "))
# move.move([300, 250-d])

# for i in range(4):
# 	magnet_on()
# 	move.move([300, 250+d])
# 	magnet_off()
# 	move.move([300-d, 250])
# 	magnet_on()
# 	move.move([300+d, 250])
# 	magnet_off()
# 	move.move([300, 250+d])
# 	magnet_on()
# 	move.move([300, 250-d])
# 	magnet_off()
# 	move.move([300+d, 250])
# 	magnet_on()
# 	move.move([300-d, 250])
# 	magnet_off()
# 	move.move([300, 250-d])

# move.move([300, 250])

# for i in range(4):
# 	move.manual(i, 5)