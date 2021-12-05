def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
        drawings = data[0]
        drawings = drawings.split(',')

        games = []
        game = []
        for line in data[2:]:
            print(line)
            if line != '':
                game.append([n for n in line.split()])
            else:
                games.append(game)
                game = []
                
        games.append(game)
        
        for game in games:
            print(game)

        #for drawing in drawings:


            
part1('test')