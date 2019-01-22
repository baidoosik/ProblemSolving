input_list = []
for i in range(4):
    input_list.append(list(map(int, input().split())))

highest, result = 0, 0
for a, b in input_list:
    result += (b-a)
    if highest < result:
        highest = result

print(highest)
