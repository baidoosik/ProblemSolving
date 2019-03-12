n = int(input())

problems = [input() for i in range(n)]

for p in problems:
    criteria = 0
    for c in p:
        if c == '(':
            criteria += 1
        else:
            criteria -= 1
        if criteria < 0:
            print('NO')
            break
    if criteria == 0:
        print('YES')
    elif criteria < 0:
        pass
    else:
        print('NO')
