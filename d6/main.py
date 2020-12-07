with open('input.txt') as f:
    inputs = [
        line
        for line in f.read().split('\n\n')
    ]

total = 0
for inp in inputs:
    answers = set(inp.replace("\n", ""))
    total += len(answers)

print('part 1:', total)

total_2 = 0
for inp in inputs:
    answers = list(map(set, inp.split("\n")))
    total_2 += len(answers[0].intersection(*answers[1:]))

print('part 2:', total_2)
