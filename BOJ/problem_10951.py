import sys


while True:
    try:
        a = sys.stdin.readline()
        c, d = map(int, a.split())
        print(c+d)
    except Exception:
        break