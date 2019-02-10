def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacenyList = [[] for vertext in vertexList]

    for edge in edgeList:
        adjacenyList[edge[0]].append(edge[1])
    while stack:
        current = stack.pop()
        if not current in visitedVertex:
            visitedVertex.append(current)

        for neighbor in adjacenyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
    return visitedVertex
