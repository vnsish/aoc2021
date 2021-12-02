def part1(input):
    with open(input, "r") as fp:
        lines = [int(n) for n in fp.read().splitlines()]
        prev = lines[0]
        count = 0
        for line in lines[1:]:
            if line > prev:
                count += 1
            prev = line
    print(count)

def part2(input):
    with open(input, "r") as fp:
        lines = [int(n) for n in fp.read().splitlines()]

        prev = lines[0]+lines[1]+lines[2]
        count = 0
        i = 3

        for line in lines[3:]:
            sum = line + lines[i-1] + lines[i-2]

            if sum > prev:
                count += 1
            prev = sum
            i += 1
    print(count)

if __name__ == "__main__":
    part1("input")
    part2("input")




