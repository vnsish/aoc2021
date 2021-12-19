def insertchar(string, char, index):
    return string[:index] + char + string[index:]

#naive solution manipulating the whole sequence
def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().split('\n\n')
    
    sequence = data[0]
    rulestring = data[1].splitlines()
    rules ={}

    for rule in rulestring:
        condition = rule.split(' -> ')[0]
        toinsert = rule.split(' -> ')[1]
        rules[condition] = toinsert
    
    for i in range(10):
        
        insertions = []
        for j, char in enumerate(sequence):
            if j < len(sequence)-1:
                if rules[sequence[j] + sequence[j+1]]:
                    insertions.append(rules[sequence[j] + sequence[j+1]])
        

        for k, insertion in enumerate(insertions, 1):
            sequence = insertchar(sequence, insertion, 2*k-1)

        
    charcount = {}
    for character in sequence:
        if character in charcount.keys():
            charcount[character] += 1
        else:
            charcount[character] = 1

    max_char = max(charcount, key=charcount.get)
    min_char = min(charcount, key=charcount.get)

    print(charcount)

    print(f'{charcount[max_char]} - {charcount[min_char]} = {charcount[max_char] - charcount[min_char]}')

#faster solution, the sequence itself doesn't matter so I'm using a map and counting only the substitutions every step
def part2(input):
    with open(input, 'r') as fp:
        data = fp.read().split('\n\n')
    
    sequence = data[0]
    rulestring = data[1].splitlines()
    rules ={}

    for rule in rulestring:
        condition = rule.split(' -> ')[0]
        toinsert = rule.split(' -> ')[1]
        rules[condition] = toinsert

    solmap = {}
    inserted = {}
    for key in rules:
        if rules[key] not in inserted:
            inserted[rules[key]] = 0

    for char in sequence:
        inserted[char] += 1


    for j, char in enumerate(sequence):
        if j < len(sequence)-1:
            if sequence[j] + rules[sequence[j] + sequence[j+1]] in solmap:
                solmap[sequence[j] + rules[sequence[j] + sequence[j+1]]] += 1
            else:
                solmap[sequence[j] + rules[sequence[j] + sequence[j+1]]] = 1
            
            if rules[sequence[j] + sequence[j+1]] + sequence[j+1] in solmap:
                solmap[rules[sequence[j] + sequence[j+1]] + sequence[j+1]] += 1
            else:
                solmap[rules[sequence[j] + sequence[j+1]] + sequence[j+1]] = 1

            inserted[rules[sequence[j] + sequence[j+1]]] += 1
    
    for step in range(39):
        newmap = {}
        for key in solmap:
            if key[0] + rules[key] in newmap:
                newmap[key[0] + rules[key]] += solmap[key]
            else:
                newmap[key[0] + rules[key]] = solmap[key]
            if rules[key] + key[1] in newmap:
                newmap[rules[key] + key[1]] += solmap[key]
            else:
                newmap[rules[key] + key[1]] = solmap[key]
            
            inserted[rules[key]] += solmap[key]

        solmap = newmap.copy()

    print(inserted)
    print(f'{max(inserted.values())} - {min(inserted.values())} = {max(inserted.values()) - min(inserted.values())}')

part1('input')
part2('input')