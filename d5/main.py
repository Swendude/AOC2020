def partition_walk(syms, rows, upper, lower):
    
    try:
        current_sym = syms[0]
    except IndexError:
        return rows[0]

    if current_sym == upper:
        if len(rows) != 1:
            return partition_walk(syms[1:], rows[:len(rows)//2], upper, lower)
    elif current_sym == lower:
        if len(rows) != 1:
            return partition_walk(syms[1:], rows[len(rows)//2:], upper, lower)

max_row = 128
max_col = 8
ids = []
with open('input.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    for inp in inputs:
        row_syms = inp[:7]
        col_syms = inp[7:]
        row = partition_walk(row_syms, list(range(max_row)), 'F', 'B')
        seat = partition_walk(col_syms, list(range(max_col)), 'L', 'R')
        ids.append(row * 8 + seat)

print('Part 1:', max(ids))

for i in range(max(ids)):
    if i not in ids:
        if (i - 1) in ids:
            if (i +1) in ids:
                print(i)




