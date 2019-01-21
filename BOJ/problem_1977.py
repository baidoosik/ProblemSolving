from typing import List

m = int(input())
n = int(input())


def solution(m: int, n: int) -> List[int]:
    i, result1, result2 = 1, 0, 0
    while m > (i ** 2):
        i += 1
    result1 = (i ** 2)

    while n >= (i ** 2):
        result2 += (i ** 2)
        i += 1

    if result2 == 0:
        return [-1]
    return [result2, result1]


for i in solution(m, n):
    print(i)
