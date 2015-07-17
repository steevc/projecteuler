__author__ = 'steve'
with open('pe11.txt','r') as f:
    content = f.readlines()

grid = [[int(i) for i in l.split()] for l in content]

max = 0
for x in range(20):
    for y in range(20):
        if x < 17:
            p = grid[y][x] * grid[y][x+1]* grid[y][x+2] * grid[y][x+3]
            if p > max:
                max = p
        if x < 17 and y < 17:
            p = grid[y][x] * grid[y+1][x+1]* grid[y+2][x+2] * grid[y+3][x+3]
            if p > max:
                max = p
        if y <17:
            p = grid[y][x] * grid[y+1][x]* grid[y+2][x] * grid[y+3][x]
            if p > max:
                max = p
        if x >2 and y < 17:
            p = grid[y][x] * grid[y+1][x-1]* grid[y+2][x-2] * grid[y+3][x-3]
            if p > max:
                max = p
    print(max)