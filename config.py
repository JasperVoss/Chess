import RPi.GPIO as gpio
import move, time

magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)

def get_radii(pos):
    return [
    round(distance([0, 0], pos)/move.mm_per_step_0),
    round(distance([0, boardHeight], pos)/move.mm_per_step_1),
    round(distance([boardWidth, boardHeight], pos)/move.mm_per_step_2),
    round(distance([boardWidth, 0], pos)/mm_per_step_3)
    ]

magnet_off()

r = [0, 0, 0, 0]
while True:
	inputtext = input("m = manual, move = move, enter to break")
	if inputtext == "m":
		move.manual(int(input("motor: ")), int(input("steps: ")))
	elif inputtext == "calibrate":
		for i in range(4):
			move.off(i)
		move.manual(0, -2000)
		r = move.move(move.get_radii([16, 16]), [100, 100])
		move.manual(0, 4)
		move.manual(1, -18)
		move.manual(2, 0)
		move.manual(3, 8)
	elif inputtext == "on":
		magnet_on()
	elif inputtext == "off":
		magnet_off()
	elif inputtext == "motors off":
		for i in range(4):
			move.off(i)
	elif inputtext == "move":
		if move.get_steps()[0] == "":
			move.save_steps(get_radii([input("current x: "), input("current y: ")]))

		move.move([round(input("final x: ")), round(input("final y: "))])
	elif inputtext == "":
		break