from utility_functions.utilities import read_file_digits

input = read_file_digits('inputDay15.txt')

memory = {}
max_path = 1000

def find_path(x, y, grid, path_sum):
    if (x, y) in memory:
        return memory[(x, y)]
    if x == 9 and y == 9:
        memory[(x, y)] = grid[y][x]
        return grid[y][x]
    if x > 9 or y > 9 or x < 0 or y < 0:
        return 1000000
    if path_sum > max_path:
        return 1000000

    out = []
    for i in [(x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)]:
        out.append(find_path(i[0], i[1], grid, path_sum+grid[y][x]))

    out = min(out) + grid[y][x]
    memory[(x, y)] = out
    return out


print(find_path(0, 0, input, 0) - input[0][0])
