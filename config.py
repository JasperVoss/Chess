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
	inputtext = input("m = manual, move = move, enter to break")
	if inputtext == "m":
		move.manual(int(input("motor: ")), int(input("steps: ")))
	elif inputtext == "move":
		if r[0] == 0:
			r = move.get_steps([int(input("current x: ")), int(input("current y: "))])
		r = move.move(r, [int(input("final x: ")), int(input("final y: "))])[1]
	elif inputtext == "":
		break