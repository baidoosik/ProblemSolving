results = [i for i in range(1, 10001)]


def d(i: int) -> int:
    div = 1
    result = i
    while i >= div:
        result += i % (10*div) // div
        div *= 10
    return result


for i in range(1, 10001):
    n = d(i)
    try:
        results.remove(n)
    except ValueError:
        pass

for i in results:
    print(i)
