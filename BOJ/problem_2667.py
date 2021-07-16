# input 처리
n = int(input())
dataset = [[int(j) for j in input()] for _ in range(n)]

# 필요한 데이터
visited = [[0]*n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


# dfs 함수 정의
def dfs(x, y):
    global number
    number += 1
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if dataset[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)


number = 0
numbers = []
cnt = 0
for i in range(n):
    for j in range(n):
        if dataset[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            numbers.append(number)
            cnt += 1
            number = 0

print(cnt)
for i in sorted(numbers):
    print(i)
