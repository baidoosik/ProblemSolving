'''
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.


'''

# 어떻게 풀지? 지도가 엄청 크지 않으니깐 모든 경우의수를 체크하는게 가능.
# combination 돌면서 안전 영역 크기의 최댓값을 구한다.

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

dataset = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
elements = []
targets = []
result = 0

for i in range(n):
    for j in range(m):
        if dataset[i][j] == 0:
            elements.append((i, j))
        elif dataset[i][j] == 2:
            targets.append((i, j))

combi = list(combinations(elements, 3))


def bfs(x, y):
    visited[x][y] = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        v = queue.popleft()
        for dx, dy in directions:
            nx, ny = v[0] + dx, v[1] + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and copied_dataset[nx][ny] == 0:
                    visited[nx][ny] = 1
                    copied_dataset[nx][ny] = 2
                    queue.append((nx, ny))


for i, j, k in combi:
    copied_dataset = copy.deepcopy(dataset)
    visited = [[0]*m for _ in range(n)]
    cnt = 0

    ix, iy = i
    jx, jy = j
    kx, ky = k

    copied_dataset[ix][iy] = 1
    copied_dataset[jx][jy] = 1
    copied_dataset[kx][ky] = 1

    for x, y in targets:
        if visited[x][y] == 0:
            bfs(x, y)

    for d in copied_dataset:
        cnt += d.count(0)

    result = max(result, cnt)

print(result)
