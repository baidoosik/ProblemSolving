a, b, c = (int(input()) for i in range(3))

result = a*b*c

result_list = [0]*10
while result >= 1:
    result_list[result % 10] += 1
    result = result // 10

for i in result_list:
    print(i)
