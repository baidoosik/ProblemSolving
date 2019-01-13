# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import unittest
from typing import List


def solution(A: List[int])->int:
    A.sort()

    for idx, n in enumerate(A, 1):
        if idx != n:
            return idx
    return len(A) + 1


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [1, 4, 5, 2, 3, 7]
        expected = 6

        self.assertEqual(solution(input_a), expected)
