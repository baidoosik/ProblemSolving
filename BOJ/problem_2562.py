import sys


max_val, max_idx = 0, 0
for i in range(9):
    m = int(sys.stdin.readline())
    if m > max_val:
        max_val = m
        max_idx = i + 1

print(max_val)
print(max_idx)
