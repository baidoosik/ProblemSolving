'''
지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때,
이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
'''

import sys
from copy import deepcopy

n, m, x, y, k = map(int, sys.stdin.readline().split())

dataset = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
movement = list(map(int, sys.stdin.readline().split()))
dice = [0]*7

directions = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}


def update_dice(dice, v):
    new_dice = deepcopy(dice)
    if v == 1:
        new_dice[1] = dice[4]
        new_dice[3] = dice[1]
        new_dice[4] = dice[6]
        new_dice[6] = dice[3]
    elif v == 2:
        new_dice[4] = dice[1]
        new_dice[1] = dice[3]
        new_dice[6] = dice[4]
        new_dice[3] = dice[6]
    elif v == 3:
        new_dice[2] = dice[1]
        new_dice[1] = dice[5]
        new_dice[5] = dice[6]
        new_dice[6] = dice[2]
    else:
        new_dice[1] = dice[2]
        new_dice[5] = dice[1]
        new_dice[6] = dice[5]
        new_dice[2] = dice[6]
    return new_dice


for v in movement:
    nx, ny = directions[v]

    dx, dy = x + nx, y + ny
    if 0 <= dx < n and 0 <= dy < m:
        dice = update_dice(dice, v)
        if dataset[dx][dy] == 0:
            dataset[dx][dy] = dice[6]
        else:
            dice[6] = dataset[dx][dy]
            dataset[dx][dy] = 0
        x, y = dx, dy
        print(dice[1])
