'''
기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다.
사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
'''

# 왼쪽 부터 가능한한 가장 먼거리에 있는 햄버거를 먹는다.
import sys


n, k = map(int, sys.stdin.readline().split())

array = sys.stdin.readline().rstrip()
array_length = len(array)

eaten = [0] * array_length

result = 0

for idx, w in enumerate(array):
    if w == 'P':
        start = idx - k if idx - k >= 0 else 0
        end = idx + k + 1 if idx + k + 1 <= array_length else array_length

        for i in range(start, end):
            if array[i] == 'H' and eaten[i] == 0:
                eaten[i] = 1
                result += 1
                break

print(result)
