# problem_name: 소수 찾기

import sys
import math

n = int(sys.stdin.readline())

dataset = list(map(int, sys.stdin.readline().split()))
try:
  dataset.remove(1)
except ValueError:
  pass
cnt = 0


def check_is_prime_number(num):
  end = int(math.sqrt(num))
  if end > 1:
    for i in range(2, end+1):
      if num % i == 0:
        return False
  return True


for d in dataset:
  if check_is_prime_number(d):
    cnt += 1

print(cnt)
