# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import unittest
from typing import List


def solution(X: int, A: List[int]) -> int:
    # write your code in Python 3.6
    a_dict, a_sum = {}, 0
    expected = sum([i for i in range(X + 1)])

    for idx, num in enumerate(A):
        if X >= num and a_dict.get(num) is None:
            a_dict[num] = num
            a_sum += num
            if a_sum == expected:
                return idx
    return -1


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [1, 3, 1, 4, 2, 3, 5, 4]
        input_x = 5
        expected = 6

        self.assertEqual(solution(input_x, input_a), expected)
