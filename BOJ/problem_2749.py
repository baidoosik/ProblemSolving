# problem_name: 피보나치 수 3
# link: https://www.acmicpc.net/problem/2749
# 피사노 주기는 피보나치 수를 K로 나눴을 때 그 나머지가 항상 주기
# -> (M = 10k 일 때, k > 2 )15 × 10**(k-1)

import sys

pisano_cycle = 15 * (10**(6-1))
n = int(sys.stdin.readline())

if n < pisano_cycle:
  d = [0] * (n+1)
  loop = n + 1
else:
  d = [0] * (pisano_cycle+1)
  loop = pisano_cycle + 1
d[1] = 1


for i in range(2, loop):
  d[i] = (d[i-1] % 1000000) + (d[i-2] % 1000000)

print(d[n % pisano_cycle] % 1000000)
