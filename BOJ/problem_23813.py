import sys

n = int(sys.stdin.readline())

total, origin = n, n
digit = len(str(n)) -1

for _ in range(digit):
    n = (n % 10)*(10**digit) + n // 10
    total += n

print(total)
