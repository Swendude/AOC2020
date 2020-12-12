import copy
with open('input.txt', 'r') as inp:
    grid = [list(line.strip()) for line in inp]


def neighbours(row, col):
    nbs = []
    for r_off in range(-1, 2):
        for c_off in range(-1, 2):
            if not(r_off == 0 and c_off == 0):
                new_r = row+r_off
                new_c = col + c_off
                if new_r >= 0 and new_c >= 0:
                    nbs.append((new_r, new_c))
    return nbs


while True:
    new_grid = copy.deepcopy(grid)
    for (row, rcell) in enumerate(grid):
        for (col, ccell) in enumerate(rcell):
            occupied = 0
            for r, c in neighbours(row, col):
                try:
                    if grid[r][c] == "#":
                        occupied += 1
                except IndexError:
                    pass
            if ccell == 'L':
                if occupied == 0:
                    new_grid[row][col] = "#"

            if ccell == '#':
                if occupied >= 4:
                    new_grid[row][col] = "L"

    if grid == new_grid:
        break
    else:
        grid = new_grid


result = 0
for row in new_grid:
    result += row.count("#")
print('Part 1: ', result)


with open('input.txt', 'r') as inp:
    grid = [list(line.strip()) for line in inp]


def directions(row, col):
    dirs = []
    for r_off in range(-1, 2):
        for c_off in range(-1, 2):
            if not(r_off == 0 and c_off == 0):
                dirs.append((r_off, c_off))
    return dirs


while True:
    new_grid = copy.deepcopy(grid)
    for (row, rcell) in enumerate(grid):
        for (col, ccell) in enumerate(rcell):
            occupied = 0
            for r, c in directions(row, col):
                edge_or_found = False
                new_r = row + r
                new_c = col + c
                while not edge_or_found:
                    if new_r < 0:
                        edge_or_found = True
                    if new_c < 0:
                        edge_or_found = True
                    if not edge_or_found:
                        try:
                            if grid[new_r][new_c] == "#":
                                occupied += 1
                                edge_or_found = True
                            if grid[new_r][new_c] == "L":
                                edge_or_found = True
                        except IndexError:
                            edge_or_found = True
                    new_r += r
                    new_c += c

            if ccell == 'L':
                if occupied == 0:
                    new_grid[row][col] = "#"

            if ccell == '#':
                # print(row, col, ':', occupied)
                if occupied >= 5:
                    new_grid[row][col] = "L"


    if grid == new_grid:
        break
    else:
        grid = new_grid

result = 0
for row in new_grid:
    result += row.count("#")
print('Part 2: ', result)