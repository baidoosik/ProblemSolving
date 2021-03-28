import random


def selection_sort(array: list) -> list:
    array_length = len(array)
    for start_idx in range(0, array_length - 1):
        min_idx = start_idx
        for idx in range(start_idx, array_length):
            if array[min_idx] > array[idx]:
                min_idx = idx
        array[start_idx], array[min_idx] = array[min_idx], array[start_idx]
    return array


def test_pass():
    test_set = [
        random.sample(range(10000000), k=17) for _ in range(10)
    ]
    test_set.append([])
    for t in test_set:
        assert sorted(t) == selection_sort(t)
    print('All pass')


test_pass()
