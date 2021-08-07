# problem name: 토마토2
import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())

queue = deque([])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False]*m for _ in range(n)]
dataset = []
is_exist_zero = False
for i in range(n):
  row = list(map(int, sys.stdin.readline().split()))
  dataset.append(row)
  for j, d in enumerate(row):
    if not is_exist_zero and d == 0:
      is_exist_zero = True

    if d == 1:
      queue.append((i, j))
      visited[i][j] = True

if not is_exist_zero:
  print(0)
  sys.exit()

while queue:
  x, y = queue.popleft()
  for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
      if not visited[nx][ny] and dataset[nx][ny] == 0:
        visited[nx][ny] = True
        dataset[nx][ny] = dataset[x][y] + 1
        queue.append((nx, ny))

days = 1

for x in range(n):
  for y in range(m):
    if dataset[x][y] == 0:
      print(-1)
      exit()
    if days < dataset[x][y]:
      days = dataset[x][y]

print(days-1)
