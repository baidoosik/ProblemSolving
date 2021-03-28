import random


def insertion_sort(array: list):
    array_length = len(array)
    for i in range(1, array_length):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break


def test_pass():
    test_set = [
        random.sample(range(1000), k=17) for _ in range(10)
    ]
    test_set.append([])
    for t in test_set:
        insertion_sort(t)
        assert sorted(t) == t
    print('All pass')


test_pass()