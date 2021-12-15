import numpy as np

def part1(input):
    with open(input, 'r') as fp:
        data = fp.read()
    data = data.split('\n\n')
    points = data[0].split('\n')
    instructions = data[1].split('\n')

    points = [eval(i) for i in points]
    max_x = max(points, key=lambda points:points[0])[0]
    max_y = max(points, key=lambda points:points[1])[1]

    #array = np.zeros((11, 15))
    array = np.zeros((max_x+1,max_y+1))

    for point in points:
        array[point[0]][point[1]] = 1

    
    fold = instructions[0].split(' ')[-1].split('=')

    if fold[0] == 'y':
        flipped = array[:, int(fold[1])+1:]
        flipped = np.flip(flipped, 1)
        newarray = array[:, :int(fold[1])]
        array = np.add(flipped, newarray)
        
    elif fold[0] == 'x':
        flipped = array[int(fold[1])+1:, :]
        flipped = np.flip(flipped, 0)
        newarray = array[:int(fold[1]), :]
        array = np.add(flipped, newarray)
    
    sum = 0
    for x in array:
        for y in x:
            if y > 0:
                sum += 1

    print(sum)

def part2(input):
    with open(input, 'r') as fp:
        data = fp.read()

    data = data.split('\n\n')
    points = data[0].split('\n')
    instructions = data[1].split('\n')

    points = [eval(i) for i in points]
    max_x = max(points, key=lambda points:points[0])[0]
    max_y = max(points, key=lambda points:points[1])[1]
    array = np.zeros((max_x+1,max_y+1))

    for point in points:
        array[point[0]][point[1]] = 1

    for instruction in instructions:
        fold = instruction.split(' ')[-1].split('=')

        if fold[0] == 'y':
            flipped = array[:, int(fold[1])+1:]
            flipped = np.flip(flipped, 1)
            newarray = array[:, :int(fold[1])]
            array = np.add(flipped, newarray)
            
        elif fold[0] == 'x':
            flipped = array[int(fold[1])+1:, :]
            flipped = np.flip(flipped, 0)
            newarray = array[:int(fold[1]), :]
            array = np.add(flipped, newarray)
    
    array = np.transpose(array)

    for x in array:
        for y in x:
            if y > 0:
                print(f'█', end='')
            else:
                print(f' ', end='')
        print('')

part1('input')
part2('input')