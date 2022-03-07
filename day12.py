from utility_functions.utilities import read_file

input = read_file("inputDay12.txt")
paths = [i for line in input for i in line.split('-')]
# print(paths)

adjacents = {i: [] for i in set(paths)}
for i in range(len(paths) // 2):
    adjacents[paths[i * 2]].append(paths[i * 2 + 1])
    adjacents[paths[i * 2 + 1]].append(paths[i * 2])
print(adjacents)


def find_paths(current, vistited):
    if current == 'end':
        return 1
    if current in vistited:
        return 0

    if current.islower():
        # print(current)
        vistited.add(current)

    return sum(find_paths(adjacent, vistited.copy()) for adjacent in adjacents[current])


print(find_paths('start', set()))

def find_paths2(current, vistited, visited_twice):
    if current == 'end':
        return 1
    if current in vistited:
        if not visited_twice:
            visited_twice = True
        else:
            return 0

    if current.islower():
        vistited.add(current)

    return sum(find_paths2(adjacent, vistited.copy(), visited_twice)
               for adjacent in adjacents[current] if adjacent != 'start')

print(find_paths2('start', set(), False))
