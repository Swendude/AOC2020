# DEEL 1
# with open('input.txt','r') as inpf:
#     grid = list(map(lambda r: r.strip() ,list(inpf)))
#     cols = (len(grid[0]))
#     rows = len(grid)
#     pos = (0,0)
#     slope = (1,3) # 1 down, 3 right
#     trees = 0
#     while pos[0] < rows:
#         if grid[pos[0]][pos[1]] == "#":
#             trees += 1
#         pos = (pos[0] + slope[0], (pos[1] + slope[1]) % cols)
#     print(trees)

# DEEL 2
with open('input.txt','r') as inpf:
    grid = list(map(lambda r: r.strip() ,list(inpf)))
    cols = (len(grid[0]))
    rows = len(grid)
    pos = (0,0)
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)] 
    results = []
    for slope in slopes:
        trees = 0
        pos = (0,0)
        while pos[0] < rows:
            if grid[pos[0]][pos[1]] == "#":
                trees += 1
            pos = (pos[0] + slope[0], (pos[1] + slope[1]) % cols)
        results.append(trees)

    print(results)
    output = 1
    for result in results:
        output = output * result
    print(output)