import unittest


class Node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = Node(None)

    def add(self, val):
        self.length += 1
        if self.head.next is None:
            self.head.next = Node(val)
        else:
            self.head.next = Node(val, self.head.next)

    def show(self):
        cur = self.head.next
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def search(self, val):
        cur = self.head.next
        while cur is not None:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def remove(self, val):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == val:
                self._remove(cur, cur.next)
                self.length -= 1
                return True
            cur = cur.next
        return False

    def _remove(self, prev, cur):
        if cur.next is None:
            prev.next = None
        else:
            prev.next = cur.next

    def get_last_kth_element(self, k: int):
        if self.length < k:
            raise IndexError
        cur = self.head.next
        index, i = self.length - k, 0
        while i != index:
            cur = cur.next
            i += 1
        return cur.val

    def remove_duplicate_word(self):
        temp_buffer = {}
        cur = self.head

        while cur.next is not None:
            if temp_buffer.get(cur.next.val) is not None:
                self._remove(cur, cur.next)
                self.length -= 1
            else:
                temp_buffer[cur.next.val] = 0
                cur = cur.next


class TestCase(unittest.TestCase):
    test_linked_list = LinkedList()

    for i in range(1, 10):
        test_linked_list.add(i)

    def test_get_last_kth_word(self):
        for i in range(9, 0, -1):
            self.assertEqual(i, self.test_linked_list.get_last_kth_element(i))
