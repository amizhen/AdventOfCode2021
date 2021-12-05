from utility_functions.utilities import read_file

input = read_file('inputDay5.txt')
lines = []
for line in input:
    import re
    x1, y1, x2, y2 = [int(i) for i in re.split(r'\D+', line)]
    lines.append(((x1, y1), (x2, y2)))


grid = [[0 for n in range(1000)] for i in range(1000)]


part2 = True


for segment in lines:
    (x1, y1), (x2, y2) = segment

    if y1 == y2:
        for i in range(min(x1, x2), max(x2, x1) + 1):
            grid[y1][i] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y2, y1) + 1):
            grid[i][x1] += 1
    elif part2:
        x_change = (x2 - x1) // abs(y2 - y1)
        y_change = (y2 - y1) // abs(x2 - x1)
        for i in range(abs(x1 - x2) + 1):
            grid[y1 + i*y_change][x1 + i*x_change] += 1

count = 0
for row in grid:
    for point in row:
        if point >= 2:
            count += 1

print(count)