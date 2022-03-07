def make_page(width_x, height_y, old_page):
    new_page = [['.'] * width_x for _ in range(height_y)]

    if old_page:
        for y in range(height_y):
            for x in range(width_x):
                new_page[y][x] = old_page[y][x]

    return new_page


def fold(old_page, line, fold_vertical=True):
    def reflect_x(x):
        if fold_vertical:
            return line - (x - line)
        else:
            return x

    def reflect_y(y):
        if not fold_vertical:
            return line - (y - line)
        else:
            return y

    def combine(v1, v2):
        if v1 == '#' or v2 == '#':
            return '#'
        else:
            return '.'

    width_x = len(old_page[0])
    height_y = len(old_page)

    if fold_vertical:
        new_page = make_page(line, height_y, old_page)
    else:
        new_page = make_page(width_x, line, old_page)

    start_y = 0 if fold_vertical else line + 1
    start_x = 0 if not fold_vertical else line + 1

    y_range = range(start_y, height_y)
    x_range = range(start_x, width_x)

    for y in y_range:
        for x in x_range:
            new_page[reflect_y(y)][reflect_x(x)] = \
                combine(old_page[y][x], new_page[reflect_y(y)][reflect_x(x)])

    return new_page


def print_page(page):
    for line in page:
        print(' '.join(line))
    print()



from utility_functions.utilities import read_file

input = read_file("inputDay13.txt")

cords = input[:input.index('')]
folds = input[input.index('') + 1:]

cords = [int(i) for line in cords for i in line.split(',')]
# print(cords)
folds = [(line.split()[2].split('=')[0], int(line.split()[2].split('=')[1]))
         for line in folds]
# print(folds)

maxX = 0
for i in range(len(cords) // 2):
    maxX = max(maxX, cords[2 * i])

maxY = 1
for i in range(len(cords) // 2):
    maxY = max(maxY, cords[2 * i + 1])

page = [['.' for x in range(maxX + 1)] for y in range(maxY + 1)]

for i in range(len(cords) // 2):
    x = cords[2 * i]
    y = cords[2 * i + 1]
    page[y][x] = '#'

for f in folds:
    if f[0] == 'x':
        page = fold(page, f[1], fold_vertical=True)
    else:
        page = fold(page, f[1], fold_vertical=False)

for line in page:
    out = ''
    for char in line:
        out += char + ' '

    print(out)