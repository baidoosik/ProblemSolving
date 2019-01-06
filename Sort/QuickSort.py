import unittest


def _quick_sort(a: list, start: int, end: int) -> list:
    if start < end:
        pivot = a[end]
        wall = start

        for i in range(start, end):
            if a[i] < pivot:
                a[i], a[wall] = a[wall], a[i]
                wall += 1
        a[wall], a[end] = a[end], a[wall]

        _quick_sort(a, start, wall - 1)
        _quick_sort(a, wall + 1, end)
    return a


def quick_sort(a: list):
    return _quick_sort(a, 0, len(a) - 1)


class QuickSortTest(unittest.TestCase):
    test_case1 = [324, 5, 1, 4, 454, 45]
    test_case2 = [4, 6, 4, 98, 2, 1, 3, 5, 5, 6]

    def test(self):
        self.assertEqual(sorted(self.test_case1), quick_sort(self.test_case1))
        self.assertEqual(sorted(self.test_case2), quick_sort(self.test_case2))
