first = input().split()
second = input().split()
third = input().split()

game_dict = {0: "E", 1: "A", 2: "B", 3: "C", 4: "D"}
first_solution, second_solution, third_solution = 0, 0, 0
for i in first:
    if i == '0':
        first_solution += 1
print(game_dict[first_solution])

for i in second:
    if i == '0':
        second_solution += 1
print(game_dict[second_solution])

for i in third:
    if i == '0':
        third_solution += 1
print(game_dict[third_solution])
