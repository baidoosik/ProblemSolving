import random


def quick_sort(array: list, start: int, end: int):
    if start < end:
        pivot = array[end]
        wall_idx = start

        for i in range(start, end):
            if array[i] < pivot:
                array[i], array[wall_idx] = array[wall_idx], array[i]
                wall_idx += 1
        array[wall_idx], array[end] = array[end], array[wall_idx]

        quick_sort(array, start, wall_idx - 1)
        quick_sort(array, wall_idx+1, end)


def test_pass():
    test_set = [
        random.sample(range(1000), k=17) for _ in range(10)
    ]
    test_set.append([])
    for t in test_set:
        quick_sort(t, 0, len(t) - 1)
        assert sorted(t) == t
    print('All pass')


test_pass()
