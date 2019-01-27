# N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.

n = int(input())

elements = list(map(int, input().split()))
sum_list, result = [None]*n, 0

sum_list[0] = sum(elements)-elements[0]
for i in range(1, n):
    sum_list[i] = sum_list[i-1]-elements[i]

for i in range(n):
    result += sum_list[i] * elements[i]

print(result)
