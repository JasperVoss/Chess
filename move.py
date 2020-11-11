import math, motors, time

mm_per_step_0 = .263
mm_per_step_1 = .265
mm_per_step_2 = .26
mm_per_step_3 = .262

w = 616   #boardWidth
h = 493   #boardHeight

a_motors = motors.Motor('A')
b_motors = motors.Motor('B')

def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def get_steps(pos):
    return [
    round(distance([0, 0], pos)/mm_per_step_0),
    round(distance([0, h], pos)/mm_per_step_1),
    round(distance([w, h], pos)/mm_per_step_2),
    round(distance([w, 0], pos)/mm_per_step_3)
]

def off(motor):
    if motor == 0:
        a_motors.off0()
    if motor == 1:
        a_motors.off1()
    if motor == 2:
        b_motors.off0()
    if motor == 3:
        b_motors.off1()
def manual(motor, steps):
    print(motor, steps)
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
            b_motors.move_step0(abs(steps)/steps)
            time.sleep(.002)
    if motor == 3:
        for i in range(abs(steps)):
            b_motors.move_step1(abs(steps)/steps)
            time.sleep(.002)
    
def move(radii, end):
    current = 0
    steps = plotSteps(radii, end, 1000)
    for s in steps[0]:
        if s[0] == 'A0':
            a_motors.move_step0(s[1])
        elif s[0] == 'A1':
            a_motors.move_step1(s[1])
        elif s[0] == 'B0':
            b_motors.move_step0(s[1])
        elif s[0] == 'B1':
            b_motors.move_step1(s[1])
    for i in range(0, 4):
        off(i)
    return steps[1]

def plotSteps(steps, endCoords, numBreaks):
    plot = []
    targets = []

    s0 = steps[0]
    s1 = steps[1]
    s2 = steps[2]
    s3 = steps[3]

    r0 = s0*mm_per_step_0
    r1 = s1*mm_per_step_1
    r2 = s2*mm_per_step_2
    r3 = s3*mm_per_step_3

    startCoords = [(r2**2-r1**2-w**2)/(-2*w), 0]
    startCoords[1] = math.sqrt(r0**2-startCoords[0]**2)

    stops = []

    x0 = startCoords[0]
    xf = endCoords[0]
    y0 = startCoords[1]
    yf = endCoords[1]

    if x0-xf != 0:
        m = (y0-yf)/(x0-xf)
    else:
        m = "vertical"

    if m != "vertical":
        if m != -h/w:
            intersection1 = (h+m*x0-y0)/(m+h/w)
        else:
            intersection1 = -1

        if m != h/w:
            intersection2 = (m*startCoords[0]-startCoords[1])/(m-h/w)
        else:
            intersection2 = -1


        if intersection1 < x0 and intersection1 > xf or intersection1 > x0 and intersection1 < xf:
            stops.append([intersection1, m*(intersection1-x0)+y0])

        if intersection2 < x0 and intersection2 > xf or intersection2 > x0 and intersection2 < xf:
            stops.append([intersection2, m*(intersection2-x0)+y0])
    else:
        y1 = x0*h/w
        y2 = h-x0*h/w

        if y0 < y1 and yf > y1 or y0 > y1 and yf < y1:
            stops.append([x0, y1])
        if y0 < y2 and yf > y2 or y0 > y2 and yf < y2:
            stops.append([x0, y2])

    step_targets = []
    step_targets.append(steps)
    for t in stops:
        step_targets.append(get_steps(t))
    step_targets.append(get_steps(endCoords))

    counter=0
    for i in range(len(step_targets)-1):
        dr0 = step_targets[i+1][0]-step_targets[i][0]
        dr1 = step_targets[i+1][1]-step_targets[i][1]
        dr2 = step_targets[i+1][2]-step_targets[i][2]
        dr3 = step_targets[i+1][3]-step_targets[i][3]

        most_steps = dr0
        most_steps_motor = 0
        if dr1 > most_steps:
            most_steps = dr1
            most_steps_motor = 1
        if dr2 > most_steps:
            most_steps = dr2
            most_steps_motor = 2
        if dr3 > most_steps:
            most_steps = dr3
            most_steps_motor = 3

        for j in range(0, most_steps):
            plot.append([0, 0, 0, 0])
        for j in range(dr0):
            difference = math.copysign(1, dr0)
            plot[counter+round(most_steps*j/dr0)][0] = difference
            s0 += difference
        for j in range(dr1):
            difference = math.copysign(1, dr1)
            plot[counter+round(most_steps*j/dr1)][1] = difference
            s1 += difference
        for j in range(dr2):
            difference = math.copysign(1, dr2)  
            plot[counter+round(most_steps*j/dr2)][2] = difference
            s2 += difference
        for j in range(dr3):
            difference = math.copysign(1, dr3)  
            plot[counter+round(most_steps*j/dr3)][3] = difference
            s3 += difference

        counter += most_steps

    return plot, [s0, s1, s2, s3]
