# problem_name: 설탕 배달
# https://www.acmicpc.net/problem/2839
# 5a + 3b -> a + b
import sys


n = int(sys.stdin.readline())

d = [-1] * (n+1)

if n >= 3:
  d[3] = 1
if n >= 5:
  d[5] = 1

for i in range(5, n+1):
  a = i // 5
  while a >= 0:
    b = (i - (5*a)) % 3
    if b == 0:
      d[i] = a*d[5] + ((i - (5*a)) // 3)*d[3]
      break
    else:
      a -= 1

print(d[n])
