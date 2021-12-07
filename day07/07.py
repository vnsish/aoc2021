import math

def part1(input):

    with open(input, 'r') as fp:
        data = fp.read()
        data = [int(n) for n in data.split(',')]

    data.sort()
    median = data[math.floor(len(data)/2)]

    totalfuel = 0
    for value in data:
        totalfuel += abs(value-median)
    
    print(totalfuel)

def part2(input):

    with open(input, 'r') as fp:
        data = fp.read()
        data = [int(n) for n in data.split(',')]
    
    higher = max(data)

    data.sort()

    totalfuel = 0      

    for value in data:
        distance = abs(1-value)
        fuel = (distance*(distance+1))/2 
        totalfuel += fuel
    
    lastsolution = totalfuel

    for i in range(2, higher+1):
        totalfuel = 0

        for value in data:
            distance = abs(i-value)
            fuel = (distance*(distance+1))/2
            totalfuel += fuel
        

        if lastsolution < totalfuel:
            break
        lastsolution = totalfuel

    print(f'position {i-1} - fuel cost: {lastsolution}')

def part2mean(input):
    with open(input, 'r') as fp:
        data = fp.read()
        data = [int(n) for n in data.split(',')]
    
    mean = sum(data)/len(data)
    
    floor = math.floor(mean)
    fuelfloor = 0
    for value in data:
        distance = abs(floor-value)
        fuel = (distance*(distance+1))/2
        fuelfloor += fuel
    
    ceil = math.ceil(mean)
    fuelceil = 0
    for value in data:
        distance = abs(ceil-value)
        fuel = (distance*(distance+1))/2
        fuelceil += fuel
    
    totalfuel = fuelfloor if fuelfloor < fuelceil else fuelceil
    position = floor if fuelfloor < fuelceil else ceil
    
    print(f'position {position} - fuel cost: {totalfuel}')
    
#part1('input')

part2('input')
part2mean('input')