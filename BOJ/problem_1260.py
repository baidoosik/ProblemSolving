vertex_num, edge_num, start = map(int, input().split())

edge_list = [tuple(map(int, input().split())) for i in range(edge_num)]
vertext_list = [i for i in range(1, vertex_num + 1)]


def dfs(vertext_list, edge_list, start):
    stack = [start]
    adjacency_list = [[] for i in vertext_list]
    visited_list = []
    edge_list = list(set(edge_list))
    for edge in edge_list:
        adjacency_list[edge[0] - 1].append(edge[1])
        adjacency_list[edge[1] - 1].append(edge[0])

    for ad in adjacency_list:
        ad.sort(reverse=True)

    while stack:
        current = stack.pop()
        if not current in visited_list:
            visited_list.append(current)

        for neighbor in adjacency_list[current - 1]:
            if not neighbor in visited_list:
                stack.append(neighbor)
    return visited_list


for i in dfs(vertext_list, edge_list, start):
    print(i, end=" ")
print("")


def bfs(vertext_list, edge_list, start):
    queue = [start]
    adjacency_list = [[] for i in vertext_list]
    visited_list = []
    edge_list = list(set(edge_list))

    for edge in edge_list:
        adjacency_list[edge[0] - 1].append(edge[1])
        adjacency_list[edge[1] - 1].append(edge[0])

    for ad in adjacency_list:
        ad.sort()

    while queue:
        current = queue.pop()
        if not current in visited_list:
            visited_list.append(current)
        for neighbor in adjacency_list[current - 1]:
            if not neighbor in visited_list:
                queue.insert(0, neighbor)
    return visited_list


for i in bfs(vertext_list, edge_list, start):
    print(i, end=" ")
