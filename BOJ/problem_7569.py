# problem name: 토마토3
from collections import deque
import sys


m, n, h = map(int, sys.stdin.readline().split())

is_exist_zero = False
dataset = []
queue = deque([])
visited = [[[0]*m for _ in range(n)] for _ in range(h)]
directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

for x in range(h):
  i = []
  for y in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    i.append(data)
    for z, d in enumerate(data):
      if not is_exist_zero and d == 0:
        is_exist_zero = True
      if d == 1:
        queue.append([x, y, z])
        visited[x][y][z] = 1
  dataset.append(i)

if not is_exist_zero:
  print(0)
  sys.exit()

while queue:
  qx, qy, qz = queue.popleft()
  visited[qx][qy][qz] = 1
  day = dataset[qx][qy][qz]

  for dx, dy, dz in directions:
    nx, ny, nz = qx + dx, qy + dy, qz + dz

    if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
      if visited[nx][ny][nz] == 0 and dataset[nx][ny][nz] == 0:
        dataset[nx][ny][nz] = day + 1
        queue.append([nx, ny, nz])

result = 0
for x in range(h):
  for y in range(n):
    for z in range(m):
      if dataset[x][y][z] == 0:
        print(-1)
        sys.exit()
      if result < dataset[x][y][z]:
        result = dataset[x][y][z]

print(result-1)
