# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List
import unittest


def solution(A: List[int]) -> int:
    # nlogn
    A.sort()
    for idx, num in enumerate(A, 1):
        if idx != num:
            return 0
    return 1


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [1, 4, 2, 3]
        expected = 1
        input_a2 = [1, 5, 2, 6, 3]
        expected2 = 0

        self.assertEqual(solution(input_a), expected)
        self.assertEqual(solution(input_a2), expected2)
