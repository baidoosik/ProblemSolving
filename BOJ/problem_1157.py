from collections import Counter
word = input()

word = word.upper()
c = Counter(word)

if len(c.most_common()) ==0:
    pass
elif len(c.most_common()) > 1:
    print(c.most_common()[0][0]) \
        if c.most_common()[0][1] != \
        c.most_common()[1][1] else print("?")
else:
    print(c.most_common()[0][0])
