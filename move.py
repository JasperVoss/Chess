import math, motors, time

mm_per_step_0 = .2663
mm_per_step_1 = .2665
mm_per_step_2 = .267
mm_per_step_3 = .2665

boardWidth = 616
boardHeight = 493

a_motors = motors.Motor('A')
b_motors = motors.Motor('B')

def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def get_radii(pos):
    return [distance([0, 0], pos), distance([0, boardHeight], pos), distance([boardWidth, boardHeight], pos), distance([boardWidth, 0], pos)]

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
    
def move(radii, end):
    current = 0
    steps = plotSteps(radii, end, 1000)
    for s in steps[0]:
        if s[0] == 'A0':
            a_motors.move_step0(s[1])
        elif s[0] == 'A1':
            a_motors.move_step1(s[1])
        elif s[0] == 'B0':
            b_motors.move_step0(s[1])           #was -s[1]
        elif s[0] == 'B1':
            b_motors.move_step1(s[1])
        #time.sleep(.0002)
    for i in range(4):
        off(i)
    return steps[1]

def plotSteps(radii, endCoords, numBreaks):
    plot = []
    targets = []

    r0 = radii[0]
    r1 = radii[1]
    r2 = radii[2]
    r3 = radii[3]

    startCoords = [(radii[2]**2-radii[1]**2-boardWidth**2)/(-2*boardWidth), 0]
    startCoords[1] = math.sqrt(r0**2-startCoords[0]**2)
    for i in range(0, numBreaks):
        targets.append([startCoords[0]+(i+1)*(endCoords[0]-startCoords[0])/numBreaks,
                        startCoords[1]+(i+1)*(endCoords[1]-startCoords[1])/numBreaks])

    for t in targets:
        dr0 = distance([0, 0], t) - r0
        dr1 = distance([0, boardHeight], t) - r1
        dr2 = distance([boardWidth, boardHeight], t) - r2
        dr3 = distance([boardWidth, 0], t) - r3

        steps0 = int(dr0/mm_per_step_0)
        steps1 = int(dr1/mm_per_step_1)
        steps2 = int(dr2/mm_per_step_2)
        steps3 = int(dr3/mm_per_step_3)

        for i in range(abs(steps0)):
            plot.append(['A0', math.copysign(1, steps0)])
        for i in range(abs(steps1)):
            plot.append(['A1', math.copysign(1, steps1)])
        for i in range(abs(steps2)):
            plot.append(['B0', math.copysign(1, steps2)])
        for i in range(abs(steps3)):
            plot.append(['B1', math.copysign(1, steps3)])

        r0 += steps0*mm_per_step_0
        r1 += steps1*mm_per_step_1
        r2 += steps2*mm_per_step_2
        r3 += steps3*mm_per_step_3

    return plot, [r0, r1, r2, r3]
