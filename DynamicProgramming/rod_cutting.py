import unittest
from typing import List


def divide_bar(n: int, p: List[int]) -> int:
    r = [0]
    for i in range(1, n + 1):
        temp = []
        for j in range(i):
            temp.append(p[i - j] + r[j])

        r.append(max(temp))
    return r[n]


class TestCase(unittest.TestCase):
    def test(self):
        input_p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        input_n = 4
        input_n2 = 7
        expected = 10
        expected2 = 18

        self.assertEqual(divide_bar(input_n, input_p), expected)
        self.assertEqual(divide_bar(input_n2, input_p), expected2)
