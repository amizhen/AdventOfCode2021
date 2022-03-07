from utility_functions.utilities import read_file_digits

input = read_file_digits('inputDay15.txt')

memory = {}

minimum = 1000000


def find_path(x, y, grid, visited, visited_sum):
    global minimum
    if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0:
        return 1000000

    if (x, y) in visited:
        return 1000000

    if (x, y) in memory:
        return memory[(x, y)]

    visited.add((x, y))
    visited_sum += grid[y][x]

    if visited_sum > minimum:
        return 1000000

    if x == len(grid[0]) - 1 and y == len(grid) - 1:
        print(sorted(visited), visited_sum, minimum)
        memory[(x, y)] = grid[y][x]
        visited.remove((x, y))
        if visited_sum < minimum:
            minimum = visited_sum
        return grid[y][x]

    out = []
    for i in [(x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)]:
        out.append(find_path(i[0], i[1], grid, visited, visited_sum))

    out = min(out) + grid[y][x]
    memory[(x, y)] = out
    visited.remove((x, y))
    return out


print(find_path(0, 0, input, set(), 0) - input[0][0])
