import unittest
from typing import List


def binary_search(target: int, a: List[int]) -> int:
    start, end = 0, len(a)
    mid = (start + end) // 2
    while mid != 0 and mid != len(a):
        if target > a[mid]:
            start = mid + 1
            mid = (start + end) // 2
        elif target < a[mid]:
            end = mid - 1
            mid = (start + end) // 2
        else:
            return mid

    return -1


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [i for i in range(100)]
        target = 55
        expected = 55

        input_a2 = [i ** 2 for i in range(10)]
        target2 = 81
        expected2 = 9

        input_a3 = [i ** 2 for i in range(10)]
        target3 = -81
        expected3 = -1

        self.assertEqual(binary_search(target, input_a), expected)
        self.assertEqual(binary_search(target2, input_a2), expected2)
        self.assertEqual(binary_search(target3, input_a3), expected3)
