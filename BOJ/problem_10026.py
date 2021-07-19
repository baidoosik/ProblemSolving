'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
  (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
'''
from collections import deque


def bfs(x, y, is_no_color=False):
    visited[x][y] = 1
    color = dataset[x][y]
    if is_no_color and color in ['R', 'G']:
        color = ['R', 'G']
    else:
        color = list(color)

    queue = deque([(x, y)])

    while queue:
        v = queue.popleft()
        for dx, dy in direction:
            nx, ny = v[0] + dx, v[1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if dataset[nx][ny] in color and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


n = int(input())

dataset = [
  [w for w in input()] for _ in range(n)
]
visited = [[0]*n for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

zone_number = 0
zone_number_with_no_color = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            zone_number += 1

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, True)
            zone_number_with_no_color += 1

print(zone_number, zone_number_with_no_color)
