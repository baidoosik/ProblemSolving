'''
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다.
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면,
그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.
'''
# 직사각형의 좌표들을 0으로 채우고 1인 곳만 search
from collections import deque
m, n, k = map(int, input().split())

dataset = [[1]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]
squares = [list(map(int, input().split())) for _ in range(k)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


for x1, y1, x2, y2 in squares:
    for x in range(x1, x2):
        for y in range(m-y2, m-y1):
            dataset[y][x] = 0


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    global cnt

    while queue:
        x1, y1 = queue.popleft()
        cnt += 1

        for dx, dy in directions:
            nx, ny = x1 + dx, y1 + dy
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and dataset[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1


cnt = 0
results = []

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and dataset[i][j] == 1:
            bfs(i, j)
            results.append(cnt)
            cnt = 0

print(len(results))
for i in sorted(results):
    print(i, end=' ')
