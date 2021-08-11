# problem_name: 숫자 카드 1
# link: https://www.acmicpc.net/problem/10815

import sys

n = int(sys.stdin.readline())
n_information = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_information = list(map(int, sys.stdin.readline().split()))


n_information_map = {}

for i in n_information:
  previous = n_information_map.get(i)
  n_information_map[i] = previous + 1 if previous else 1

for t in m_information:
  print(1 if n_information_map.get(t) else 0, end=' ')
