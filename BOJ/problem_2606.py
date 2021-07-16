node_number = int(input())
edge_number = int(input())

edge_list = [list(map(int, input().split())) for _ in range(edge_number)]

visited = [0 for _ in range(node_number+1)]
graph = [
    [] for _ in range(node_number+1)
]

for i, j in edge_list:
    graph[i].append(j)
    graph[j].append(i)


def dfs(v):
    if not visited[v]:
        global num
        num += 1
        visited[v] = 1

        for i in graph[v]:
            dfs(i)


# exclude no.1 computer
num = -1
dfs(1)

print(num)
