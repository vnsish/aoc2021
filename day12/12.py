paths = []

def dfs(graph, current, visited):
    if not current.isupper():
        visited.append(current)
    if current != 'end':
        for vert in graph[current]:
            if vert not in visited:
                dfs(graph, vert, visited.copy())
    if current == 'end':
        paths.append(visited)

def dfs2(graph, current, visited, path, visitedtwice):
    
    if not current.isupper() and current != 'start':
        
        visited.append(current)
        if current in path:
            visitedtwice = True

    path.append(current)

    if current != 'end':
        for vert in graph[current]:
            if vert not in visited:
                dfs2(graph, vert, visited.copy(), path.copy(), visitedtwice)
            elif not visitedtwice and vert != 'start':
                dfs2(graph, vert, visited.copy(), path.copy(), visitedtwice)
    else:
        paths.append(path)



def part1(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
    
    graph = {}

    for line in data:
        verts = line.split('-')
        if verts[0] not in graph:
            graph[verts[0]] = [verts[1]]
        else:
            graph[verts[0]].append(verts[1])

        if verts[1] not in graph:
            graph[verts[1]] = [verts[0]]
        else:
            graph[verts[1]].append(verts[0])
    
    print(graph)

    dfs(graph, 'start', ['start'])


    print(len(paths))

def part2(input):
    with open(input, 'r') as fp:
        data = fp.read().splitlines()
    
    graph = {}

    for line in data:
        verts = line.split('-')
        if verts[0] not in graph:
            graph[verts[0]] = [verts[1]]
        else:
            graph[verts[0]].append(verts[1])

        if verts[1] not in graph:
            graph[verts[1]] = [verts[0]]
        else:
            graph[verts[1]].append(verts[0])
    
    print(graph)

    dfs2(graph, 'start', ['start'], [], False)


    print(len(paths))
    
#part1('input')
part2('input')
