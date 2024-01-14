import sys
import array

n = int(sys.stdin.readline())

relations = []
for _ in range(n):
    relations.append(int(sys.stdin.readline(), 2))

question_number = int(sys.stdin.readline())
for _ in range(question_number):
    x, y = map(int, sys.stdin.readline().split())
    first = relations[x - 1]
    second = relations[y - 1]
    print((first & second).bit_count())
