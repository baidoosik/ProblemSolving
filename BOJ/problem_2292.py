num = int(input())

result, i = 1, 0
if num == 1:
    print(1)
else:
    while result < num:
        i += 1
        result += (6*i)
    print(i+1)
