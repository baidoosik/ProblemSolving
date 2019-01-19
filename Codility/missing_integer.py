import unittest
from typing import List


def solution(A: List[int])->int:
    # write your code in Python 3.6
    # nlogn + n
    result = 0
    A.sort()
    for num in A:
        if num > 0:
            if num > result+1:
                return result + 1
            else:
                result = num
    return result+1


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [1, 3, 6, 4, 1, 2]
        expected = 5

        self.assertEqual(solution(input_a), expected)
