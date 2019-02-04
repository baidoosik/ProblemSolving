from typing import List

result = []


def perm(a: List[int], i):
    if i == len(a) - 1:
        result.append(a.copy())
    else:
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            perm(a, i + 1)
            a[i], a[j] = a[j], a[i]


n = int(input())

perm([i for i in range(1, n + 1)], 0)
result.sort()

for r in result:
    for i in r:
        print(i, end=" ")
    print("")
