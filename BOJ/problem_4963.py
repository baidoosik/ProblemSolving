'''
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.

지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.
'''

import sys
sys.setrecursionlimit(100000)


directions = [(0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
results = []


def is_finished(a, b):
    return True if a == 0 and b == 0 else False


def dfs(x, y):
    visited[x][y] = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if dataset[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)


while 1:
    island_cnt = 0
    w, h = map(int, input().split())
    if is_finished(w, h):
        break
    visited = [[0] * w for _ in range(h)]
    dataset = []
    for _ in range(h):
        dataset.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if dataset[x][y] == 1 and visited[x][y] == 0:
                island_cnt += 1
                dfs(x, y)
    results.append(island_cnt)

for r in results:
    print(r)
