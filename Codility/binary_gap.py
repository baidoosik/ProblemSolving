import unittest
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N: int)->int:
    # write your code in Python 3.6
    binary = change_binary(N)
    temp, hightest = 0, 0
    for idx, i in enumerate(binary, 1):
        if i == '1':
            if temp > hightest:
                hightest = temp
            temp =0
        else:
            temp +=1
    return hightest


def change_binary(a: int)->str:
    result = ''
    while a >= 1:
        remainder = a % 2
        a = a//2
        result = str(remainder)+result
    return result


class TestCase(unittest.TestCase):
    def test(self):
        input_value = 32
        input_value2 = 1042

        expected = 0
        expected2 = 5

        self.assertEqual(solution(input_value), expected)
        self.assertEqual(solution(input_value2), expected2)
