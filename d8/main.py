import copy 

acc = 0
lines = []
pc = 0
seen = set()
last = None
with open('input.txt') as f:
    for i, line in enumerate(f):
        lines.append((i, line.split(" ")))



while True:
    ln, instarg = lines[pc]
    inst, arg = instarg 
    if not (ln, inst) in seen:
        seen.add((ln, inst))
    else:
        print('Part 1:',acc)
        break
    if inst == 'acc':
        acc += int(arg)
        pc += 1
    elif inst == 'jmp':
        pc += int(arg)
    else:
        pc += 1
    last = (ln, inst)

jmps = filter(lambda l: l[1][0] =='jmp', lines)
to_brute_force = []
for jmp in jmps:
    new_lines = copy.deepcopy(lines)
    new_lines[jmp[0]][1][0] = 'nop'
    to_brute_force.append(new_lines)

for bf in to_brute_force:
    pc = 0
    acc = 0
    seen = set()
    while True:
        if pc >= len(bf):
            print(print('Part 2:', acc))
            break
        ln, instarg = bf[pc]
        inst, arg = instarg 
        if not (ln, inst) in seen:
            seen.add((ln, inst))
        else:
            break
        if inst == 'acc':
            acc += int(arg)
            pc += 1
        elif inst == 'jmp':
            pc += int(arg)
        else:
            pc += 1



# print(to_brute_force)