import math
import unittest


def solution(X:int, Y:int, D:int)->int:
    # write your code in Python 3.6
    if X == Y:
        return 0
    else:
        return math.ceil((Y-X)/D)


class TestCase(unittest.TestCase):
    def test(self):
        input_x = 10
        input_y = 85
        input_d = 20
        expected = 4

        self.assertEqual(solution(input_x, input_y, input_d), expected)
