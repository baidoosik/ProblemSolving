command_n = int(input())

commands = [input() for i in range(command_n)]

part1, part2 = "", None
queue = []
case = {
    "push": lambda x: queue.append(int(x)),
    "pop": lambda x: queue.pop() if len(queue) != 0 else -1,
    "size": lambda x: len(queue),
    "empty": lambda x: 1 if len(queue) == 0 else 0,
    "top": lambda x: queue[-1] if len(queue) != 0 else -1
}

for w in commands:
    try:
        part1, part2 = w.split()
        case[part1](part2)
    except ValueError:
        part1 = w
        print(case[part1](0))
