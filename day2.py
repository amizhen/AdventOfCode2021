from utility_functions.utilities import read_file

moves = read_file('inputDay2.txt')


def find_pos(moves):
    depth = 0
    forward = 0
    for move in moves:
        if move[0] == 'u':
            depth -= int(move[-1])
        elif move[0] == 'd':
            depth += int(move[-1])
        elif move[0] == 'f':
            forward += int(move[-1])
    return depth * forward

def find_pos2(moves):
    depth = 0
    forward = 0
    aim = 0
    for move in moves:
        if move[0] == 'u':
            aim -= int(move[-1])
        elif move[0] == 'd':
            aim += int(move[-1])
        elif move[0] == 'f':
            forward += int(move[-1])
            depth += aim * int(move[-1])
    return depth * forward


print(find_pos(moves))
print(find_pos2(moves))
