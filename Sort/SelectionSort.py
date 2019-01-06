import unittest


def selection_sort(a: list) -> list:
    min_idx = 0
    for start in range(0, len(a)-1):
        min_idx = start
        for idx in range(start+1, len(a)):
            if a[idx] < a[min_idx]:
                min_idx = idx
        a[start], a[min_idx] = a[min_idx], a[start]
    return a


class SelectionSortTest(unittest.TestCase):
    testcase1 = [1, 4, 4, 3, 1, 49, 8, 7, 6, 80]
    testcase2 = [77, 6, 4, 3, 2, 21, 2198]

    def test(self):
        self.assertEqual(sorted(self.testcase1), selection_sort(self.testcase1))
        self.assertEqual(sorted(self.testcase2), selection_sort(self.testcase2))
