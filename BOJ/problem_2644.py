# problem_name: 촌수계산
# link: https://www.acmicpc.net/problem/2644
# x, y -> x는 y의 부모 번호
from collections import deque
import sys


n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

relations = list(map(int, sys.stdin.readline().split()) for _ in range(m))
relation_data = [[] for _ in range(n+1)]

for x, y in relations:
    relation_data[x].append(y)
    relation_data[y].append(x)

visited = [False] * (n+1)


def bfs(data, a, target):
    count = 0
    q = deque([[a, count]])

    while q:
        v, count = q.popleft()
        visited[v] = True
        if v == target:
            return count

        count += 1
        for i in data[v]:
            if not visited[i]:
                q.append([i, count])

    return -1


result = bfs(relation_data, a, b)

print(result)
