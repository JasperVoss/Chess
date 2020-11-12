import RPi.GPIO as gpio

magnet_pin = 4

gpio.setmode(gpio.BCM)
gpio.setup(magnet_pin, gpio.OUT)

def magnet_on():
    gpio.output(magnet_pin, 1)
    
def magnet_off():
    gpio.output(magnet_pin, 0)

magnet_off()

r = move.get_radii([300, 200])

for i in range(5):
	magnet_on()
	r = move.move(r, [300, 300])
	magnet_off()
	r = move.move(r, [250, 250])
	magnet_on()
	r = move.move(r, [350, 250])
	magnet_off()
	r = move.move(r, [300, 300])
	magnet_on()
	r = move.move(r, [300, 200])
	magnet_off()
	r = move.move(r, [350, 250])
	magnet_on()
	r = move.move(r, [250, 250])
	magnet_off()
	r = move.move(r, [300, 200])