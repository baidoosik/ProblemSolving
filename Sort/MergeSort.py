import unittest
import random


def merge_sort(a: list) -> list:
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                a[k] = right[j]
                j += 1
            else:
                a[k] = left[i]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a


class MergeSortTest(unittest.TestCase):
    testcase1 = random.choices([i for i in range(10)], k=10)
    testcase2 = random.choices([i for i in range(10)], k=10)

    def test(self):
        print(merge_sort(self.testcase1), sorted(self.testcase1))
        print(merge_sort(self.testcase2), sorted(self.testcase2))
        self.assertEqual(merge_sort(self.testcase1), sorted(self.testcase1))
        self.assertEqual(merge_sort(self.testcase2), sorted(self.testcase2))
