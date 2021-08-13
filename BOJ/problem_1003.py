# problem_name: 피보나치 함수
# link: https://www.acmicpc.net/problem/1003

import sys


d = [(0, 0) for i in range(41)]

for i in range(41):
  if i > 1:
    d[i] = (d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1])
  elif i == 0:
    d[i] = (1, 0)
  elif i == 1:
    d[i] = (0, 1)

n = int(sys.stdin.readline())

for _ in range(n):
  a, b = d[int(sys.stdin.readline())]
  print(f'{a} {b}')
