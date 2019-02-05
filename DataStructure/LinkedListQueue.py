class Node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


class MyQueue:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)

    def append(self, val):
        cur = self.head.next
        self.size += 1
        if cur is None:
            self.head.next = Node(val)
            self.tail.next = self.head.next
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val)
            self.tail.next = cur.next

    def pop(self):
        if self.head.next is None:
            print(-1)
        else:
            self.size -= 1
            print(self.head.next.val)
            self.head.next = self.head.next.next
            if self.head.next is None:
                self.tail.next = None

    @property
    def empty(self):
        if self.head.next is None:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head.next is None:
            print(-1)
        else:
            print(self.head.next.val)

    def back(self):
        if self.tail.next is None:
            print(-1)
        else:
            print(self.tail.next.val)


command_n = int(input())

commands = [input() for i in range(command_n)]

part1, part2 = "", None
queue = MyQueue()
case = {
    "push": lambda x: queue.append(int(x)),
    "pop": lambda x: queue.pop(),
    "size": lambda x: print(queue.size),
    "empty": lambda x: queue.empty,
    "front": lambda x: queue.front(),
    "back": lambda x: queue.back()
}

for w in commands:
    try:
        part1, part2 = w.split()
        case[part1](part2)
    except ValueError:
        part1 = w
        case[part1](0)
