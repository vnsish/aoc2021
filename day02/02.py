def part1(input):
    with open(input, 'r') as fp:
        lines = fp.read().splitlines()

        pos = 0
        dep = 0

        for line in lines:
            instruction = line.split(' ')
            command = instruction[0]
            value = int(instruction[1])

            if command == 'forward':
                pos += value
            elif command == 'down':
                dep += value
            elif command == 'up':
                dep -= value

    print(dep*pos)

def part2(input):
    with open(input, 'r') as fp:
        lines = fp.read().splitlines()

        pos = 0
        dep = 0
        aim = 0

        for line in lines:
            instruction = line.split(' ')
            command = instruction[0]
            value = int(instruction[1])

            if command == 'forward':
                pos += value
                dep += aim*value
            elif command == 'down':
                aim += value
            elif command == 'up':
                aim -= value
        
    print(dep*pos)

if __name__ == "__main__":
    part1("input")
    part2("input")