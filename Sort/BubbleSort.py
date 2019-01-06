import unittest


def bubble_sort(a: list) -> list:
    for end in range(len(a)-1, -1, -1):
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1], = a[i+1], a[i]
    return a


class BubbleSortTestCase(unittest.TestCase):
    test_case = [34, 3, 4, 1, 4, 6, 8, 9, 0, -1]

    def test(self):
        result = sorted(self.test_case)
        self.assertEqual(bubble_sort(self.test_case), result)
