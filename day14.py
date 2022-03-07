from utility_functions.utilities import read_file
from collections import Counter

input = read_file("inputDay14.txt")

base = input[0]
patterns = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in input[2:]}


def transform(base, patterns):
    newBase = []
    char = 0
    while char < len(base) - 1:
        newBase.append(base[char])
        if base[char] + base[char + 1] in patterns:
            newBase.append(patterns[base[char] + base[char + 1]])
        char += 1
    newBase.append(base[-1])
    return newBase


current = list(base)
for i in range(10):
    # print(i)
    # print(current)
    current = transform(current, patterns)

counts = Counter(current)
print(sorted(counts.items(), key=lambda x: x[1]))


memory = {}
def transform2(char1, char2, patterns, times):
    pattern = char1 + char2
    if times == 0:
        return Counter([char1])
    if (char1, char2, times) in memory:
        return memory[(char1, char2, times)]
    if pattern in patterns:
        memory[(char1, char2, times)] = (transform2(char1, patterns[pattern], patterns, times-1) +
                                         transform2(patterns[pattern], char2, patterns, times-1)).copy()
        return transform2(char1, patterns[pattern], patterns, times-1) + \
               transform2(patterns[pattern], char2, patterns, times-1)

times = 40
result = Counter()
for char in range(len(base)-1):
    result += transform2(base[char], base[char+1], patterns, times)
result += Counter([base[-1]])

out = sorted(result.items(), key=lambda x: x[1])
print(out)
print(out[-1][1]-out[0][1])