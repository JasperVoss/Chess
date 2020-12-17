import RPi.GPIO as gpio
import move, time, halifax

magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)

magnet_off()

while True:
	state = halifax.get_state()
	if state[5][4] != 1:
		while state[5][4] != 1:
			state = halifax.get_state()
			for i in range(len(state)):
				for j in range(len(state[i])):
					if state[i][j] == 1:
						move.move_square([i, j])


	# state = halifax.get_state()
	# departed = False
	# arrived = False
	# depart_square = [0, 0]
	# to_square = [0, 0]
	# for i in range(len(state)):
	# 	for j in range(len(i)):
	# 		difference[i][j] = state[i][j] - old_state[i][j]
	# 		if difference[i][j] == -1:
	# 			departed = True
	# 			depart_square = [i, j]
	# 		elif difference[i][j] == 1:
	# 			arrived = True
	# 			to_square = [i, j]



