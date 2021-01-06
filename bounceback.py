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

# squarex = int(input("x: "))
# squarey = int(input("y:"))
# counter = 0
# while True:
# 	state = halifax.get_state()
# 	for i in range(len(state)):
# 		for j in range(len(state[i])):
# 			if state[i][j] == 1:
# 				if i != squarex or j != squarey:
# 					move.move_square(i, j)
# 					magnet_on()
# 					move.move_piece(squarey, squarex)
# 					magnet_off()
# 					counter += 1
# 					if counter >= 5:
# 						move.calibrate()
# 						counter = 0

original_state = halifax.get_state()
while True:
	while True:
		difference = [[0 for _ in range(8)] for _ in range(10)]
		new_state = halifax.get_state()
		for i in range(len(original_state)):
			for j in range(8):
				difference[i][j] = new_state[i][j]-original_state[i][j]
		movedto = [-1, -1]
		movedfrom = [-1, -1]
		for i in range(len(original_state)):
			for j in range(8):
				if difference[i][j] == 1:
					movedto[0], movedto[1] = i, j
				elif difference[i][j] == -1:
					movedfrom[0], movedfrom[1] = i, j
		if movedto[0] != -1 and movedfrom[0] != -1:
			break
	move.move_square(movedto[0], movedto[1])
	time.sleep(.1)
	magnet_on()
	move.move_square(movedfrom[0], movedfrom[1])
	magnet_off()
