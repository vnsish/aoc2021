def part1(input):
    with open(input, 'r') as fp:

        lines = fp.read().splitlines()
        length = len(lines[0])
        count_zero = [0] * length

        for line in lines:
            for i, char in enumerate(line):
                if char == '0':
                    count_zero[i] += 1
        
        gamma = ''
        epsilon = ''

        nvalues = len(lines)

        for i in range(length):
            zeroes = count_zero[i]
            ones = nvalues - count_zero[i]
            if zeroes > ones:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'

        gammai = int(gamma, 2)
        epsiloni = int(epsilon, 2)
    
    print(gammai * epsiloni)

def part2(input):
    with open(input, 'r') as fp:
        lines = fp.read().splitlines()
        
        length = len(lines[0])
        

        for i in range(length):
            nvalues = len(lines)
            count_zero = 0
            for line in lines:
                if line[i] == '0':
                    count_zero += 1

            if count_zero > (nvalues - count_zero):
                most_common = '0'
            else:
                most_common = '1'

            oxygen = lines.copy()

            for line in lines:
                if line[i] != most_common:
                    oxygen.remove(line)
                    
            lines = oxygen
            if len(lines) == 1:
                break
        
        # refactor?
        fp.seek(0)
        lines = fp.read().splitlines()
        for i in range(length):
            nvalues = len(lines)
            count_zero = 0
            for line in lines:
                if line[i] == '0':
                    count_zero += 1
            
            if count_zero > (nvalues - count_zero):
                least_common = '1'
            else:
                least_common = '0'

            co2 = lines.copy()

            for line in lines:
                if line[i] != least_common:
                    co2.remove(line)
            lines = co2
            if len(lines) == 1:
                break

        print(int(oxygen[0], 2) * int(co2[0], 2))

part1("input")
part2("input")
