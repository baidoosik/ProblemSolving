import unittest
from typing import List


'''
문제 설명
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 

썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

'''


def solution(skill: str, skill_trees: List[str])->int:
    answer, a = 0, {}
    for index, c in enumerate(skill, 1):
        a[c] = index

    for tree in skill_trees:
        temp = 0
        for c in tree:
            if a.get(c) is not None:
                if temp != a[c]-1:
                    answer -= 1
                    break
                else:
                    temp = a[c]
        answer += 1
    return answer


class TestCase(unittest.TestCase):
    def test(self):
        input_skill = "CBD"
        input_skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
        expected = 2

        self.assertEqual(solution(input_skill, input_skill_trees), expected)
