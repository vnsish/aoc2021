def checkwinner(game):
    for i in range(len(game)):
        if game[i] == [-1, -1, -1 , -1, -1]:
            return True
        column = [line[i] for line in game]
        if column == [-1, -1, -1, -1, -1]:
            return True

    return False

def printgame(game):
    for line in game:
        for number in line:
            print(str(number) + ' ', end="")
        print('\n')

def calcpoints(game, drawing):
    sum = 0
    for line in game:
        for number in line:
            if number != -1:
                sum += int(number)
    print(f'{sum} * {drawing}')
    return sum*int(drawing)

def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
        drawings = data[0]
        drawings = drawings.split(',')

        games = []
        game = []
        for line in data[2:]:
            if line != '':
                game.append([n for n in line.split()])
            else:
                games.append(game)
                game = []
                
        games.append(game)

        found = False
        
        for drawing in drawings:
            if found:
                break
            for game in games:
                for line in game:
                    if drawing in line:
                        line[line.index(drawing)] = -1
                        break
                if checkwinner(game):
                    found = True
                    print(calcpoints(game, drawing))

def part2(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
        drawings = data[0]
        drawings = drawings.split(',')

        games = []
        game = []
        for line in data[2:]:
            if line != '':
                game.append([n for n in line.split()])
            else:
                games.append(game)
                game = []
                
        games.append(game)

        for drawing in drawings:
            if len(games) == 0:
                break
            for game in games[:]:
                for line in game:
                    if drawing in line:
                        line[line.index(drawing)] = -1
                        break

                if checkwinner(game):
                    games.remove(game)
                    if len(games) == 0:
                        print(calcpoints(game, drawing))
                

part1('input')

part2('input')