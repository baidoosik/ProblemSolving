from typing import List


def merge_sort(a: List[int]):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                a[k] = right[j]
                j += 1
            else:
                a[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a


n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

second.sort(reverse=True)
result = 0
for a, b in zip(merge_sort(first), second):
    result += a * b

print(result)
