def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for i in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current = queue.pop()
        if not current in visitedList:
            visitedList.append(current)

        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0, neighbor)
    return visitedList
