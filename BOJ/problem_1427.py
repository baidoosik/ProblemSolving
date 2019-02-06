def _quick_sort(a: list, start: int, end: int) -> list:
    if start < end:
        pivot = end
        wall = start

        for i in range(start, end):
            if a[i] > a[pivot]:
                a[i], a[wall] = a[wall], a[i]
                wall += 1
        a[wall], a[pivot] = a[pivot], a[wall]

        _quick_sort(a, start, wall - 1)
        _quick_sort(a, wall + 1, end)
    return a


def quick_sort(a: list):
    return _quick_sort(a, 0, len(a) - 1)


n = input()

result = []
for i in n:
    result.append(int(i))

answer = quick_sort(result)

for i in answer:
    print(i, end="")