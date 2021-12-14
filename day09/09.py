import numpy as np

def checklowpoint(i, j, array):

    if i > 0:
        if array[i-1][j] <= array[i][j]:
            return False
    if i+1 < len(array):
        if array[i+1][j] <= array[i][j]:
            return False
    if j > 0:
        if array[i][j-1] <= array[i][j]:
            return False
    if j+1 < len(array[0]):
        if array[i][j+1] <= array[i][j]:
            return False

    return True


def findbasin(i, j, array, size):
    if i > 0 and array[i-1][j] < 9:
        array[i-1][j] = 9
        size = findbasin(i-1, j, array, size)
    if i+1 < len(array) and array[i+1][j] < 9:
        array[i+1][j] = 9
        size = findbasin(i+1, j, array, size)
    if j > 0 and array[i][j-1] < 9:
        array[i][j-1] = 9
        size = findbasin(i, j-1, array, size)
    if j+1 < len(array[0]) and array[i][j+1] < 9:
        array[i][j+1] = 9
        size = findbasin(i, j+1, array, size)

    return size+1

def part2(input):
    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    columns = len(data)
    rows = len(data[0])

    
    basins = []

    for j in range(rows):
        for i in range(columns):
            if checklowpoint(i, j, data):
                size = findbasin(i, j, data, -1)
                basins.append(size)

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])
    
def part1(input):
    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    columns = len(data)
    rows = len(data[0])

    risk = 0

    for j in range(rows):
        for i in range(columns):
            if checklowpoint(i, j, data):
                risk += data[i][j] + 1
    print(risk)

part1('input')
part2('input')
