import RPi.GPIO as gpio
import move, time

magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)

magnet_off()

r = [0, 0, 0, 0]
while True:
	inputtext = input(">> ")
	if inputtext == "m":
		move.manual(int(input("motor: ")), int(input("steps: ")))
	elif inputtext == "on":
		magnet_on()
	elif inputtext == "off":
		magnet_off()
	elif inputtext == "motors off":
		for i in range(4):
			move.off(i)
	elif inputtext == "move":
		if move.get_steps()[0] == 0:
			move.save_steps(move.get_radii([int(input("current x: ")), int(input("current y: "))]))

		move.move([int(input("final x: ")), int(input("final y: "))])
	elif inputtext == "tension":
		move.tension()
	elif inputtext == "release":
		move.release_tension()
	elif inputtext == "reset pos":
		move.save_steps([0, 0, 0, 0])
	elif inputtext == "":
		break