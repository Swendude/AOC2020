import copy
with open('input.txt', 'r') as inp:
    grid = [line.strip() for line in inp]

def neighbours(row, col):
    nbs = []
    for r_off in range(-1, 1):
        for c_off in range(-1, 1):
            if not(r_off == 0 and c_off==0):
                nbs.append((row+r_off, col + c_off))
    return nbs

while True:
    new_grid = copy.deepcopy(grid)
    for (row, rcell) in enumerate(grid):
        for (col, ccell) in enumerate(rcell):
            occupied = 0
            for c, r in neighbours(row, col):
                try:
                    print(grid[c][r])
                    if grid[c][r] == "#":
                        occupied += 1
                except IndexError:
                    continue
            if ccell == 'L':
                # print(occupied)
                if occupied == 0:
                    # print("SWITCH")
                    new_grid[col][row] == "#"
            if ccell == '#':
                if occupied >= 4:
                    new_grid[col][row] == "L"
    if grid == new_grid:
        break
    # for line in grid:
    #     print(line)
    # input(0)
    grid = new_grid

result = 0
for row in grid:
#     print(row)
    result += row.count("L")
print(result)