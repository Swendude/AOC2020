import copy

with open('input.txt') as inp:
    lines= [int(line) for line in inp]

last = max(lines) + 3
current = 0
chain = []
one_jumps = 0
three_jumps = 1 # for the last adapter

while True:
    possible = range(current + 1, current + 4)
    for pos in possible:
        if pos in lines:
            if pos - current == 1:
                one_jumps += 1
            if pos - current == 3:
                three_jumps += 1
            chain.append(pos)
            current = pos
    if last - current == 3:
        chain.append(last)
        break   
    
print('Part 1: ', one_jumps * three_jumps)

with open('input.txt') as inp:
    lines= [int(line) for line in inp]

lines= lines + [0, max(lines)]
last = max(lines)
possibilities = [0] * (last + 1)
possibilities[0] = 1

for adapter in range(1, last + 1):
    for offset in range(1, 4):
        if (adapter - offset) in lines:
            possibilities[adapter] += possibilities[adapter - offset]

print('part 2: ', possibilities[-1] )
