import unittest
from typing import List


def solution(A: List[int]) -> int:
    temp_dict = {}
    for i in A:
        if temp_dict.get(i) is None:
            temp_dict[i] = 0
        else:
            temp_dict.pop(i)

    return list(temp_dict.keys())[0]


class TestCase(unittest.TestCase):
    def test(self):
        input_list = [3, 5, 9, 7, 3, 9, 5]
        expected = 7

        self.assertEqual(solution(input_list), expected)
