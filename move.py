import math, time

mm_per_step_0 = 1
mm_per_step_1 = 1
mm_per_step_2 = 1
mm_per_step_3 = 1

# a_motors = motors.Motor('A')
# b_motors = motors.Motor('B')

height = 100
width = 100
tension = True

def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def get_radii(pos):
    return [
    round(distance([0, 0], pos)/mm_per_step_0),
    round(distance([0, height], pos)/mm_per_step_1),
    round(distance([width, height], pos)/mm_per_step_2),
    round(distance([width, 0], pos)/mm_per_step_3)
    ]

def get_steps():
	step_file = open("steps.txt", "r")
	steps = ["", "", "", ""]
	index = 0

	for s in step_file.read():
		if s == "\n":
			index += 1
		else:
			steps[index] = steps[index] + s

	step_file.close()
	print(steps)
	for i in range(4):
		steps[i] = int(steps[i])

	return steps

def save_steps(steps):
	step_file = open("steps.txt", "w")
	for s in steps:
		step_file.write(str(s)+"\n")
	step_file.close()

def manual(motor, steps):
    if motor == 0:
        for i in range(abs(steps)):
            #a_motors.move_step0(abs(steps)/steps)
            time.sleep(.002)
    if motor == 1:
        for i in range(abs(steps)):
            #a_motors.move_step1(abs(steps)/steps)
            time.sleep(.002)
    if motor == 2:
        for i in range(abs(steps)):
            #b_motors.move_step0(abs(steps)/steps)   #was -abs
            time.sleep(.002)
    if motor == 3:
        for i in range(abs(steps)):
            #b_motors.move_step1(abs(steps)/steps)
            time.sleep(.002)

def off(motor):
    if motor == 0:
        a_motors.off0()
    if motor == 1:
        a_motors.off1()
    if motor == 2:
        b_motors.off0()
    if motor == 3:
        b_motors.off1()

def move(coords):
	steps = get_steps()
	print(steps)
	final = [
	round(distance([0, 0], coords)/mm_per_step_0), 
	round(distance([0, height], coords)/mm_per_step_1), 
	round(distance([width, height], coords)/mm_per_step_2), 
	round(distance([width, 0], coords)/mm_per_step_3), 
	]

	y0 = ((steps[0]**2)*mm_per_step_0-(steps[1]**2)*mm_per_step_1+height**2)/2/height
	x0 = math.sqrt(mm_per_step_0*steps[0]**2-y0**2)

	dx = coords[0]-x0
	dy = coords[1]-y0

	dsteps = [final[i]-steps[i] for i in range(4)]   #change in steps

	most_steps_motor = 0
	most_steps = 0
	for i in range(4):
		if dsteps[i] > most_steps:
			most_steps = dsteps[i]
			most_steps_motor = i

	num_targets = most_steps
	target_coords = []

	for i in range(num_targets):
		target_coords.append([
			round(x0+dx*i/num_targets, 2),
			round(y0+dy*i/num_targets, 2)
			])
	print(target_coords)
	print('\n\n\n')

	target_steps = []
	for t in target_coords:
		target_steps.append(get_radii(t))
	target_steps.append(final)

	print(target_steps)

	for t in target_steps:
		d0 = t[0]-steps[0]
		d1 = t[1]-steps[1]
		d2 = t[2]-steps[2]
		d3 = t[3]-steps[3]

		print(d0, d1, d2, d3)

		for i in range(abs(d0)):
			#a_motors.move_step0(abs(d0)/d0)
			steps[0] += int(abs(d0)/d0)
			time.sleep(.002)
		for i in range(abs(d1)):
			#a_motors.move_step1(abs(d1)/d1)
			steps[1] += int(abs(d1)/d1)
			time.sleep(.002)
		for i in range(abs(d2)):
			#b_motors.move_step0(abs(d2)/d2)
			steps[2] += int(abs(d2)/d2)
			time.sleep(.002)
		for i in range(abs(d3)):
			#b_motors.move_step1(abs(d3)/d3)
			steps[3] += int(abs(d3)/d3)
			time.sleep(.002)
	save_steps(steps)

save_steps(get_radii([100, 100]))
move([0, 0])