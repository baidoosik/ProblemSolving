# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import unittest
from typing import List

def solution(N: int, A: List[int]):
    # write your code in Python 3.6
    highest_value, acc_value = 0, 0
    result={}

    for num in A:
        if num < N+1:
            if result.get(num) is None:
                result[num] =1
            else:
                result[num] +=1

            if result[num] > highest_value:
                highest_value = result[num]

        elif num == N+1:
            result = {}
            acc_value += highest_value
            highest_value = 0

    answer = [acc_value]*N
    for key, value in result.items():
        answer[key-1] += value
    return answer


class TestCase(unittest.TestCase):
    def test(self):
        input_a = [3, 4, 4, 6, 1, 4, 4]
        input_x = 5
        expected = [3, 2, 2, 4, 2]

        self.assertEqual(solution(input_x, input_a), expected)
