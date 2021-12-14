import numpy as np

def part1(input):
    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    totalflashes = 0

    for step in range(100):
        flash = []

        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1 
                if data[i][j] > 9:
                    flash.append((i, j))    

        flashed = [[0]*10 for i in range(10)]

        while flash:
            point = flash.pop()
            x = point[0]
            y = point[1]

            data[x][y] = 0
            flashed[x][y] = 1
            totalflashes += 1

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i==0 and j==0: continue
                    elif 0 <= x+i < 10 and 0 <= y+j < 10 and flashed[x+i][y+j] == 0:
                        data[x+i][y+j] += 1
                        if data[x+i][y+j] > 9 and (x+i, y+j) not in flash and flashed[x+i][y+j] == 0:
                            flash.append((x+i, y+j))

    print(totalflashes)

def part2(input):
    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    totalflashes = 0
    allflashed = False
    step = 0
    while not allflashed:
        flash = []

        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1 
                if data[i][j] > 9:
                    flash.append((i, j))    

        flashed = [[0]*10 for i in range(10)]

        while flash:
            point = flash.pop()
            x = point[0]
            y = point[1]

            data[x][y] = 0
            flashed[x][y] = 1
            totalflashes += 1

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i==0 and j==0: continue
                    elif 0 <= x+i < 10 and 0 <= y+j < 10 and flashed[x+i][y+j] == 0:
                        data[x+i][y+j] += 1
                        if data[x+i][y+j] > 9 and (x+i, y+j) not in flash and flashed[x+i][y+j] == 0:
                            flash.append((x+i, y+j))
        
        step += 1
        array = np.array(data)

        if np.all(array==0):
            allflashed = True
            print(f'all flashed on step: {step}')
 


part1('input')
part2('input')
