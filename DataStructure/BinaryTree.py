import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        # test purpose lists
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            self._add(self.head, value)

    def _add(self, cur, value):
        if cur.value < value:
            if cur.right is None:
                cur.right = Node(value)
            else:
                self._add(cur.right, value)
        else:
            if cur.left is None:
                cur.left = Node(value)
            else:
                self._add(cur.left, value)

    def search(self, value):
        if self.head.value is None:
            return False
        else:
            return self._search(self.head, value)

    def _search(self, cur, value):
        if cur.value == value:
            return True
        else:
            if cur.value < value:
                if cur.right is None:
                    return False
                else:
                    return self._search(cur.right, value)
            else:
                if cur.left is None:
                    return False
                else:
                    return self._search(cur.left, value)

    def remove(self, value):
        if self.head.value is None:
            return print("there is no value in this binary tree")
        else:
            if self.head.value == value:
                if self.head.left is None and self.head.right is None:
                    self.head = Node(None)
                elif self.head.left is None and self.head.right is not None:
                    self.head = self.head.right
                elif self.head.left is not None and self.head.right is None:
                    self.head = self.head.left
                else:
                    self.head.value = self._most_left_val_from_right_node(self.head.right).value
                    self._remove_item(self.head, self.head.right)
                    return True
            else:
                if self.head.value < value:
                    self._remove(self.head, self.head.right, value)
                else:
                    self._remove(self.head, self.head.left, value)

    def _remove(self, prev, cur, value):
        if cur is None:
            return print("not found value")

        if cur.value < value:
            self._remove(cur, cur.right, value)
        elif cur.value > value:
            self._remove(cur, cur.left, value)
        else:
            if cur.left is None and cur.right is None:
                if prev.left.value == value:
                    prev.left = None
                else:
                    prev.right = None
            elif cur.left is None and cur.right is not None:
                if prev.left.value == value:
                    prev.left = cur.right
                else:
                    prev.right = cur.right
            elif cur.left is not None and cur.right is None:
                if prev.left.value == value:
                    prev.left = cur.left
                else:
                    prev.right = cur.left
            else:
                cur.value = self._most_left_val_from_right_node(cur.right).value
                self._remove_item(cur, cur.right)
                return True

    def _most_left_val_from_right_node(self, cur):
        if cur.left is not None:
            return self._most_left_val_from_right_node(cur.left)
        else:
            return cur

    def _remove_item(self, prev, cur):
        if cur.left is None:
            prev.right = cur.right
        else:
            while cur.left is not None:
                prev = cur
                cur = cur.left
            if cur.right is not None:
                prev.left = cur.right
            else:
                prev.left = None

    def preorder_traverse(self):
        if self.head is not None:
            self._preorder_traverse(self.head)

    def _preorder_traverse(self, cur):
        self.preorder_list.append(cur.value)
        if cur.left is not None:
            self._preorder_traverse(cur.left)
        if cur.right is not None:
            self._preorder_traverse(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self._inorder_traverse(self.head)

    def _inorder_traverse(self, cur):
        if cur.left is not None:
            self._inorder_traverse(cur.left)

        self.inorder_list.append(cur.value)

        if cur.right is not None:
            self._inorder_traverse(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self._postorder_traverse(self.head)

    def _postorder_traverse(self, cur):
        if cur.left is not None:
            self._postorder_traverse(cur.left)
        if cur.right is not None:
            self._postorder_traverse(cur.right)
        self.postorder_list.append(cur.value)


class BinaryTreeTest(unittest.TestCase):
    def test(self):
        bt = BinaryTree()
        bt.add(6)
        bt.add(3)
        bt.add(4)
        bt.add(1)
        bt.add(7)
        print("pre order")
        bt.preorder_traverse()
        self.assertEqual(bt.preorder_list, [6, 3, 1, 4, 7])

        print("in order")
        bt.inorder_traverse()
        self.assertEqual(bt.inorder_list, [1, 3, 4, 6, 7])

        print("post order")
        bt.postorder_traverse()
        self.assertEqual(bt.postorder_list, [1, 4, 3, 7, 6])

        print("bt root remove")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(50)
        bt_root_remove_test.add(70)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [70, 50])

        print("bt root remove2")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(50)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [50])

        print("bt root remove3")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(70)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [70])

        print("bt left remove 1")
        bt_left_remove_test_1 = BinaryTree()
        bt_left_remove_test_1.add(60)
        bt_left_remove_test_1.add(50)
        bt_left_remove_test_1.add(70)
        bt_left_remove_test_1.remove(50)
        bt_left_remove_test_1.preorder_traverse()
        self.assertEqual(bt_left_remove_test_1.preorder_list, [60, 70])

        print("bt left remove 2")
        bt_left_remove_test_2_left = BinaryTree()
        bt_left_remove_test_2_left.add(60)
        bt_left_remove_test_2_left.add(50)
        bt_left_remove_test_2_left.add(70)
        bt_left_remove_test_2_left.add(40)
        bt_left_remove_test_2_left.remove(50)
        bt_left_remove_test_2_left.preorder_traverse()
        self.assertEqual(bt_left_remove_test_2_left.preorder_list, [60, 40, 70])

        print("bt right remove 2")
        bt_left_remove_test_2_right = BinaryTree()
        bt_left_remove_test_2_right.add(60)
        bt_left_remove_test_2_right.add(50)
        bt_left_remove_test_2_right.add(70)
        bt_left_remove_test_2_right.add(55)
        bt_left_remove_test_2_right.remove(50)
        bt_left_remove_test_2_right.preorder_traverse()
        self.assertEqual(bt_left_remove_test_2_right.preorder_list, [60, 55, 70])

        print("bt right remove 1")
        bt_right_remove_test_1 = BinaryTree()
        bt_right_remove_test_1.add(60)
        bt_right_remove_test_1.add(50)
        bt_right_remove_test_1.add(70)
        bt_right_remove_test_1.remove(70)
        bt_right_remove_test_1.preorder_traverse()
        self.assertEqual(bt_right_remove_test_1.preorder_list, [60, 50])

        print("bt right remove 2")
        bt_right_remove_test_2_left = BinaryTree()
        bt_right_remove_test_2_left.add(60)
        bt_right_remove_test_2_left.add(50)
        bt_right_remove_test_2_left.add(70)
        bt_right_remove_test_2_left.add(65)
        bt_right_remove_test_2_left.remove(70)
        bt_right_remove_test_2_left.preorder_traverse()
        self.assertEqual(bt_right_remove_test_2_left.preorder_list, [60, 50, 65])

        print("bt right remove 3")
        bt_right_remove_test_1 = BinaryTree()
        bt_right_remove_test_1.add(60)
        bt_right_remove_test_1.add(78)
        bt_right_remove_test_1.add(70)
        bt_right_remove_test_1.add(50)
        bt_right_remove_test_1.add(55)
        bt_right_remove_test_1.add(65)
        bt_right_remove_test_1.add(67)
        bt_right_remove_test_1.add(69)
        bt_right_remove_test_1.add(79)
        bt_right_remove_test_1.remove(70)
        bt_right_remove_test_1.preorder_traverse()
        self.assertEqual(bt_right_remove_test_1.preorder_list, [60, 50, 55, 78, 65, 67, 69, 79])

        print("bt right remove 2")
        bt_right_remove_test_2_right = BinaryTree()
        bt_right_remove_test_2_right.add(60)
        bt_right_remove_test_2_right.add(50)
        bt_right_remove_test_2_right.add(70)
        bt_right_remove_test_2_right.add(75)
        bt_right_remove_test_2_right.remove(70)
        bt_right_remove_test_2_right.preorder_traverse()
        self.assertEqual(bt_right_remove_test_2_right.preorder_list, [60, 50, 75])

        print("bt left remove 3")
        bt_left_remove_test_3 = BinaryTree()
        bt_left_remove_test_3.add(60)
        bt_left_remove_test_3.add(50)
        bt_left_remove_test_3.add(70)
        bt_left_remove_test_3.add(40)
        bt_left_remove_test_3.add(55)
        bt_left_remove_test_3.add(52)
        bt_left_remove_test_3.remove(50)
        bt_left_remove_test_3.preorder_traverse()
        self.assertEqual(bt_left_remove_test_3.preorder_list, [60, 52, 40, 55, 70])

        print("BST search test")
        bt_search_test = BinaryTree()
        bt_search_test.add(60)
        bt_search_test.add(50)
        bt_search_test.add(70)
        bt_search_test.add(40)
        bt_search_test.add(55)
        bt_search_test.add(52)
        self.assertTrue(bt_search_test.search(60))
        self.assertTrue(bt_search_test.search(50))
        self.assertTrue(bt_search_test.search(70))
        self.assertTrue(bt_search_test.search(40))
        self.assertTrue(bt_search_test.search(55))
        self.assertTrue(bt_search_test.search(52))
        self.assertFalse(bt_search_test.search(61))
        self.assertFalse(bt_search_test.search(81))
