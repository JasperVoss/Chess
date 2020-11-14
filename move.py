import math, motors, time

mm_per_step_0 = .2652
mm_per_step_1 = .2643
mm_per_step_2 = .268
mm_per_step_3 = .267

a_motors = motors.Motor('A')
b_motors = motors.Motor('B')

height = 616
width = 492
tension = True

def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def get_radii(pos):
    return [
    round(move.distance([0, 0], pos)/move.mm_per_step_0),
    round(move.distance([0, height], pos)/move.mm_per_step_1),
    round(move.distance([width, height], pos)/move.mm_per_step_2),
    round(move.distance([width, 0], pos)/mm_per_step_3)
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
            a_motors.move_step0(abs(steps)/steps)
            time.sleep(.002)
    if motor == 1:
        for i in range(abs(steps)):
            a_motors.move_step1(abs(steps)/steps)
            time.sleep(.002)
    if motor == 2:
        for i in range(abs(steps)):
            b_motors.move_step0(abs(steps)/steps)   #was -abs
            time.sleep(.002)
    if motor == 3:
        for i in range(abs(steps)):
            b_motors.move_step1(abs(steps)/steps)
            time.sleep(.002)

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

	dx = x0-coords[0]
	dy = y0-coords[1]

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
			x0+dx*i/num_targets,
			y0+dy*i/num_targets
			])

	target_steps = []
	for t in target_coords:
		target_steps.append(get_radii(t))
	target_steps.append(final)

	for t in target_steps:
		d0 = abs(t[0]-steps[0])
		d1 = abs(t[1]-steps[1])
		d2 = abs(t[2]-steps[2])
		d3 = abs(t[3]-steps[3])

		print(d0, type(d0))
		for i in range(abs(d0)):
			a_motors.move_step0(abs(d0)/d0)
			steps[0] += abs(d0)/d0
			time.sleep(.002)
		for i in range(abs(d1)):
			a_motors.move_step1(abs(d1)/d1)
			steps[1] += abs(d1)/d1
			time.sleep(.002)
		for i in range(abs(d2)):
			b_motors.move_step0(abs(d2)/d2)
			steps[2] += abs(d2)/d2
			time.sleep(.002)
		for i in range(abs(d3)):
			b_motors.move_step1(abs(d3)/d3)
			steps[3] += abs(d3)/d3
			time.sleep(.002)
	save_steps(steps)


