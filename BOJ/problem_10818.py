'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

min, max 이용 안하기.
'''
import sys


n = int(input())

dataset = list(map(int, sys.stdin.readline().split()))
min_val, max_val = dataset[0], dataset[0]


for i in dataset:
    if min_val > i:
        min_val = i
        continue
    if max_val < i:
        max_val = i

print(min_val, max_val)
