from utility_functions.utilities import read_file_int

depths = read_file_int("inputDay1.txt")


def count_increase(depths):
    count = 0
    for i in range(len(depths) - 1):
        if (depths[i] < depths[i + 1]):
            count += 1
    return count


def count_increase2(depths):
    count = 0
    for i in range(len(depths) - 3):
        a = depths[i] + depths[i + 1] + depths[i + 2]
        b = depths[i + 1] + depths[i + 2] + depths[i + 3]
        if a < b:
            count += 1
    return count


print(count_increase(depths))
print(count_increase2(depths))
