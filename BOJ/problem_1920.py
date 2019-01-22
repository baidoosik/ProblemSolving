n = input()

search_list = input().split()

m = input()

element_list = input().split()

memo = {}
for i in search_list:
    memo[i] = 1

for i in element_list:
    if memo.get(i) is None:
        print(0)
    else:
        print(1)
