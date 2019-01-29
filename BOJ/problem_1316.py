n = int(input())

words = [input() for i in range(n)]
total = 0
for word in words:
    total += 1
    my_dict, temp = {}, ''
    for w in word:
        if temp == w:
            pass
        else:
            if my_dict.get(w) is None:
                my_dict[w] = 1
                temp = w
            else:
                total -= 1
                break

print(total)
