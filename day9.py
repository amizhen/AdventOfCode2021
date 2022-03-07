from utility_functions.utilities import read_file

input = read_file('inputDay9.txt')

data = [[10]+[int(i) for i in line]+[10] for line in input]
data.insert(0, [10]*(len(input[0])+2))
data.append([10]*(len(input[0])+2))




count = 0
lows = []
for y in range(1, len(data) - 1):
    for x in range(1, len(data) - 1):
        if data[y][x] < data[y + 1][x] and \
            data[y][x] < data[y - 1][x] and \
            data[y][x] < data[y][x - 1] and \
            data[y][x] < data[y][x + 1]:
            # count += data[y][x] + 1
            lows.append((x, y))

# print(count)

def check_point(current, target, data):
    x1, y1 = current
    x2, y2 = target
    return data[y1][x1] < data[y2][x2]

def count_basin(x, y, checked):
    if(data[y][x] >= 9):
        return 0
    out = 1
    checked.append((x, y))
    for cords in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
        if cords not in checked and check_point((x, y), cords, data):
            out += count_basin(cords[0], cords[1], checked)
    return out


basins = []

for low in lows:
    basins.append(count_basin(low[0], low[1], []))


print(sorted(basins)[-3]*sorted(basins)[-2]*sorted(basins)[-1])

