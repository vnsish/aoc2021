def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()

    outvalues = [n[1] for n in (m.split(" | ") for m in data)]

    digsegments = {1: 2, 4: 4, 7: 3, 8: 7}

    sum = 0

    for value in outvalues:        
        for digit in value.split():
            if len(digit) in digsegments.values():
                sum += 1
    print(sum)

def part2(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()

    outvalues = [(n, e) for n, e in (m.split(" | ") for m in data)]

    numbers = [set([1, 2, 3, 4, 5, 6]), 
               set([2, 3]), 
               set([1, 2, 7, 5, 4]), 
               set([1, 2, 7, 3, 4]), 
               set([2, 3, 6, 7]), 
               set([1, 6, 7, 3, 4]), 
               set([1, 6, 7, 3, 4, 5]), 
               set([1, 2, 3]), 
               set([1, 2, 3, 4, 5, 6, 7]), 
               set([1, 2, 3, 4, 6, 7])]

    sum = 0

    for mapping, value in outvalues:
        mapdic = {}
        realmap = {}
        for number in mapping.split():
            if len(number) == 4:
                mapdic[4] = set([n for n in number])
            elif len(number) == 2:
                mapdic[1] = set([n for n in number])
            elif len(number) == 7:
                mapdic[8] = set([n for n in number])
            elif len(number) == 3:
                mapdic[7] = set([n for n in number])
            
        for number in mapping.split():
            if len(number) == 6:
                intersect = set(number) & mapdic[1]
                if len(intersect) == 1:
                    realmap[3] = list(intersect)[0]
                    mapdic[6] = set(number)
            elif len(number) == 5:
                intersect = set(number) & mapdic[4]
                if len(intersect) == 2:
                    mapdic[2] = set(number)
                intersect = set(number) & mapdic[1]
                if len(intersect) == 2:
                    mapdic[3] = set(number)
            
        for number in mapping.split():
            if len(number) == 6 and set(number) not in mapdic.values():
                intersect = set(number) & mapdic[4]
                if len(intersect) == 4:
                    mapdic[9] = set(number)
                else:
                    mapdic[0] = set(number)
            elif len(number) == 5:
                intersect = set(number) & mapdic[6]
                if len(intersect) == 5:
                    mapdic[5] = set(number)
                    

        realmap[1] = list(mapdic[7] - mapdic[1])[0]
        realmap[2] = list(mapdic[8] - mapdic[6])[0]
        realmap[7] = list(mapdic[8] - mapdic[0])[0]
        realmap[4] = list(mapdic[3] - set(realmap.values()))[0]
        realmap[6] = list(mapdic[9] - set(realmap.values()))[0]
        realmap[5] = list(mapdic[0] - mapdic[9])[0]

        realmap = {v: k for k, v in realmap.items()}

        numstring = ''

        for number in value.split():
            digits = set()
            for digit in number:
                digits.add(realmap[digit])
            numstring += str(numbers.index(digits))
            
        sum += int(numstring)

        #print(realmap)
        #print(numstring)

    print(sum)

part1('input')
part2('input')