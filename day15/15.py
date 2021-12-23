from queue import PriorityQueue

class Vertex:
    
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return f'{self.name} - {self.edges}'

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dijkstra(graph, start, destination):
    cost = {}
    sum = 0
    for vertex in graph:
        cost[graph[vertex].name] = float('inf')

    cost[start] = 0

    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        sum += 1
        (totaldistance, current) = q.get()
        if current == destination: 
            break
        for edge in graph[current].edges:
            olddist = cost[edge[0]]
            newdist = totaldistance + edge[1]
            if newdist < olddist:
                q.put((newdist, edge[0]))
                cost[edge[0]] = newdist

    return cost[destination]



def part1(input):
    graph = {}

    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    #generate graph
    for i in range(len(data)):
        for j in range(len(data)):
            newvertex = Vertex(f'{i},{j}')
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx==0 and dy==0: continue
                    #not moving diagonally
                    elif dx==0 or dy==0:
                        if 0 <= i+dx < len(data) and 0 <= j+dy < len(data):
                            newvertex.edges.append((f'{i+dx},{j+dy}', data[i+dx][j+dy]))
            graph[f'{i},{j}'] = newvertex
    

    totalcost = dijkstra(graph, '0,0', f'{len(data)-1},{len(data)-1}')

    print(totalcost)

def part2(input):
    graph = {}

    with open(input, 'r') as fp:
        data = [j for j in fp.read().splitlines()]
        for i, line in enumerate(data):
            data[i] = [int(j) for j in line]

    newdata = []
    for line in data:
        newline = line.copy()
        for i in range(1,5):
            for j in range(0, len(line)):
                newnumber = line[j]+i if line[j]+i < 10 else line[j]+i-9
                newline.append(newnumber)
        newdata.append(newline)

    reps = len(newdata)
    sum = 0
    for i in range(1,5):
        for k in range(reps):
            sum += 1
            line = newdata[k]
            newline = []
            for j in range(len(line)):
                newnumber = line[j]+i if line[j]+i < 10 else line[j]+i-9
                newline.append(newnumber)
            newdata.append(newline)

    data = newdata

    
    for i in range(len(data)):
        for j in range(len(data)):
            newvertex = Vertex(f'{i},{j}')
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx==0 and dy==0: continue
                    #not moving diagonally
                    elif dx==0 or dy==0:
                        if 0 <= i+dx < len(data) and 0 <= j+dy < len(data):
                            newvertex.edges.append((f'{i+dx},{j+dy}', data[i+dx][j+dy]))
            graph[f'{i},{j}'] = newvertex
    

    totalcost = dijkstra(graph, '0,0', f'{len(data)-1},{len(data)-1}')

    print(totalcost)
    
part1('input')
part2('input')