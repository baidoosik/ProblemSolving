import sys
import unittest
from typing import List


def solution(A: List[int])-> int:
    sum_right = sum(A)
    sum_left = 0
    result = sys.maxsize

    for i in range(len(A) - 1):
        sum_right -= A[i]
        sum_left += A[i]
        result = min(result, abs(sum_right - sum_left))
    return result


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [10, -4, 5, 6, 8, 9]
        expected = 0
        self.assertEqual(solution(input_a), expected)
