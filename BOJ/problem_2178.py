# BFS Breath -> 최단거리
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dataset = [
    [int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)
]
visited = [[0]*m for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        v = queue.popleft()
        if v[0] == n - 1 and v[1] == m - 1:
            print(visited[v[0]][v[1]])
            return

        for dx, dy in directions:
            nx, ny = v[0] + dx, v[1] + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and dataset[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[v[0]][v[1]] + 1


bfs(0, 0)
