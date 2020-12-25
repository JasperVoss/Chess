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

squarex = int(input("x: "))
squarey = int(input("y:"))
while True:
	state = halifax.get_state()
	for i in range(len(state)):
		for j in range(len(state[i])):
			if state[i][j] == 1:
				move.move_square(i, j)
				magnet_on()
				move.move_piece(squarey, squarex)
				magnet_off()

