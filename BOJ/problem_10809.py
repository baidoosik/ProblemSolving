from typing import List

a = [int(input()) for i in range(9)]


diff = sum(a)-100


def search(a: List[int], n: int):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]+a[j] == diff:
                return a[i], a[j]


x, y = search(a, diff)
a.remove(x)
a.remove(y)
a.sort()
for i in a:
    print(i)
