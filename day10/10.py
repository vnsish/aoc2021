def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
    
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    stack = []
    totalpoints = 0

    for line in data:
        for char in line:
            if char in chunks:
                stack.append(char)
            elif char == chunks[stack[-1]]:
                stack.pop()
            else:
                #print(f'error found in line {line} char {char}')
                totalpoints += points[char]
                break
    
    print(totalpoints)

def part2(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
    
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}

    stack = []
    strings = []

    for line in data:
        stack = []
        corrupted = False
        for char in line:
            if char in chunks:
                stack.append(char)
            elif char == chunks[stack[-1]]:
                stack.pop()
            else:
                corrupted = True
                break
        
        if stack and not corrupted:
            totalscore = 0
            while len(stack) > 0:
                totalscore *= 5
                totalscore += points[stack.pop()]
            strings.append(totalscore)

    strings.sort()
    print(strings[len(strings)//2])

part1('input')
part2('input')
