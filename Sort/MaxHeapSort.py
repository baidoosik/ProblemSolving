import unittest
import random
from typing import List


def heapsort(a: List[int]) -> List[int]:
    def swap(a: List[int], x: int, y: int) -> None:
        a[x], a[y] = a[y], a[x]

    def shift_down(a: List[int], i: int, size: int) -> None:
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i

        if l < size and a[l] > a[largest]:
            largest = l

        if r < size and a[r] > a[largest]:
            largest = r

        if largest != i:
            swap(a, largest, i)
            shift_down(a, largest, size)

    def heapify(a: List[int], size: int) -> None:
        mid = size // 2 - 1

        while mid >= 0:
            shift_down(a, mid, size)
            mid -= 1

    end = len(a)

    while end > 0:
        heapify(a, end)
        end -= 1
        swap(a, 0, end)

    return a


class TestCase(unittest.TestCase):
    random_box = [i for i in range(100)]

    def test(self):
        input_list = [random.choice(self.random_box) for i in range(100)]
        input_list2 = [random.choice(self.random_box) for i in range(100)]
        self.assertEqual(sorted(input_list), heapsort(input_list))
        self.assertEqual(sorted(input_list2), heapsort(input_list2))
