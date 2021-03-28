import random


def bubble_sort(array: list):
    for end in range(len(array) - 1, -1, -1):
        for i in range(end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1], = array[i + 1], array[i]


def test_pass():
    test_set = [
        random.sample(range(1000), k=17) for _ in range(10)
    ]
    test_set.append([])
    for t in test_set:
        bubble_sort(t)
        assert sorted(t) == t
    print('All pass')


test_pass()
