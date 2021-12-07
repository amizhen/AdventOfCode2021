from utility_functions.utilities import read_file

input = [int(i) for i in read_file("inputDay6.txt")[0].split(',')]


def count_fish(input, length):
    values = [input.count(i) for i in range(9)]
    for i in range(length):
        new = values[0]
        for i in range(8):
            values[i] = values[i + 1]
        values[6] += new
        values[8] = new
    return sum(values)


print(count_fish(input, 80))
print(count_fish(input, 256))
