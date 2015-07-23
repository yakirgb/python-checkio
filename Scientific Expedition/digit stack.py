def digit_stack(commands):
    total, queue = 0, []
    for c in commands:
        if 'PUSH' in c:
            queue.append(int(c[5:]))
        elif queue and c =='POP':
            total += queue.pop()
        elif queue and c == 'PEEK':
            total += queue[-1]
    return total


digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8