while 1:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break
    total, highest_val = 0, 0
    for i in [a, b, c]:
        if i > highest_val:
            highest_val = i
        total += i**2

    if total - 2*(highest_val**2) == 0:
        print('right')
    else:
        print('wrong')
