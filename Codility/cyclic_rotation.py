import unittest
from typing import List


def solution(A:List[int], K: int)->List[int]:
    a_length = len(A)
    if K > a_length and a_length != 0:
        K = K % len(A)
    return A[a_length-K:] + A[:a_length-K]


class TestCase(unittest.TestCase):
    def test(self):
        input_list = [1, 2, 3, 4, 5]
        input_k =3
        expected = [3, 4, 5, 1, 2]

        self.assertEqual(solution(input_list, input_k), expected)
