from utility_functions.utilities import read_file_digits

input = read_file_digits('inputDay11.txt')

input = [[100]+i+[100] for i in input]

input.insert(0, [100]*12)
input.append([100]*12)


def count_glows(octi, glowing, glowed):
    for y in range(1, len(octi)-1):
        for x in range(1, len(octi[0])-1):
            if octi[y][x] > 9 and (x, y) not in glowed:
                glowing.add((x, y))
    return glowing


def inc_surrounding(cord, octi):
    x = cord[0]
    y = cord[1]
    octi[y-1][x-1] += 1
    octi[y-1][x] += 1
    octi[y-1][x+1] += 1
    octi[y][x-1] += 1
    octi[y][x+1] += 1
    octi[y+1][x-1] += 1
    octi[y+1][x] += 1
    octi[y+1][x+1] += 1


def inc_all(octi):
    for y in range(1, len(octi)-1):
        for x in range(1, len(octi[0])-1):
            octi[y][x] += 1


def step(octi):
    inc_all(octi)

    glowed = set()
    glowing = count_glows(octi, set(), glowed)
    while len(glowing) > 0:
        for cord in glowing:
            inc_surrounding(cord, octi)
        glowed = glowed.union(glowing)
        glowing = count_glows(octi, set(), glowed)

    for y in range(1, len(octi)-1):
        for x in range(1, len(octi[0])-1):
            if octi[y][x] > 9:
                octi[y][x] = 0

    return len(glowed)



count = 0
for i in range(100):
    count += step(input)

print(count)


input = read_file_digits('inputDay11.txt')

input = [[100]+i+[100] for i in input]

input.insert(0, [100]*12)
input.append([100]*12)

i = 0
while True:
    i+=1
    value = step(input)
    if value == 100:
        print(f'100 at {i}')
        break



for line in input:
    print(line)
