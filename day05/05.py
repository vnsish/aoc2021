import numpy as np

def getdiffp1(p1, p2):
    if p1[0] != p2[0] and p1[1] != p2[1]:
        return False
    return p2[0]-p1[0], p2[1]-p1[1]

def getdiffp2(p1, p2):
    return p2[0]-p1[0], p2[1]-p1[1]

def part1(input):
    chart = np.zeros((1000,1000))
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
        points = []
        for line in data:
            points.append((line.split(' -> ')[0], line.split(' -> ')[1]))
    
    for element in points:
        p1 = (int(element[0].split(',')[0]), int(element[0].split(',')[1]))
        p2 = (int(element[1].split(',')[0]), int(element[1].split(',')[1]))
        diff = getdiffp2(p1,p2)
        if diff[0] == 0:
            stepx = 0 
        else:
            stepx = diff[0]/abs(diff[0])

        if diff[1] == 0:
            stepy = 0
        else:
            stepy = diff[1]/abs(diff[1])

        if diff[0] == 0 or diff[1] == 0: 
            steps = abs(diff[0] + diff[1])
            for i in range(steps+1):
                chart[p1[1]+int(0+i*stepy)][p1[0]+int(0+i*stepx)] += 1

    sum = 0
    for line in chart:
        for value in line:
            if value > 1:
                sum += 1
    #print(chart)
    print(f'Points with overlap: {sum}')

def part2(input):
    chart = np.zeros((1000,1000))
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
        points = []
        for line in data:
            points.append((line.split(' -> ')[0], line.split(' -> ')[1]))
    
    for element in points:
        p1 = (int(element[0].split(',')[0]), int(element[0].split(',')[1]))
        p2 = (int(element[1].split(',')[0]), int(element[1].split(',')[1]))
        diff = getdiffp2(p1,p2)
        if diff[0] == 0:
            stepx = 0 
        else:
            stepx = diff[0]/abs(diff[0])

        if diff[1] == 0:
            stepy = 0
        else:
            stepy = diff[1]/abs(diff[1])

        if diff[0] != 0 and diff[1] != 0: 
            steps = abs(diff[0])
        else:
            steps = abs(diff[0] - diff[1])

        for i in range(steps+1):
            chart[p1[1]+int(0+i*stepy)][p1[0]+int(0+i*stepx)] += 1


    sum = 0
    for line in chart:
        for value in line:
            if value > 1:
                sum += 1
    #print(chart)
    print(f'Points with overlap: {sum}')

part1('input')
part2('input')