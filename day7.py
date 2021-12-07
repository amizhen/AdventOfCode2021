from utility_functions.utilities import read_file

input = [int(i) for i in read_file("inputDay7.txt")[0].split(',')]


def calc_dist(target, input):
    dist = 0
    for i in input:
        dist += abs(target - i)
    return dist


def part1(input):
    out = []
    for i in range(max(input)):
        out.append(calc_dist(i, input))
    return min(out)


print(part1(input))


def calc_dist2(target, input):
    dist = 0
    for i in input:
        dist += abs(target - i) * (abs(target - i) + 1) // 2
    return dist


def part2(input):
    out = []
    for i in range(max(input)):
        out.append(calc_dist2(i, input))
    return min(out)


print(part2(input))
