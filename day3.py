from utility_functions.utilities import read_file

power = read_file('inputDay3.txt')


def find_power(inputs):
    powers = [0] * 12
    out = ''
    for num in inputs:
        for i in range(12):
            powers[i] += int(num[i])
    for i in powers:
        if i > 500:
            out += '1'
        else:
            out += '0'
    return int(out, 2) * (2 ** 12 - 1 - int(out, 2))


def count_frequency(inputs, pos):
    frequency = 0
    for command in inputs:
        frequency += int(command[pos])

    return frequency


def scrub(inputs, pos, bit):
    out = []
    for command in inputs:
        if command[pos] == bit:
            out.append(command)
    return out


def oxygen_rating(inputs):
    commands = inputs.copy()
    for i in range(12):
        frequency = count_frequency(commands, i)
        if frequency >= len(commands) / 2:
            commands = scrub(commands, i, '1')
        else:
            commands = scrub(commands, i, '0')

    return int(commands[0],2)


def carbon_rating(inputs):
    commands = inputs.copy()
    for i in range(12):
        if(len(commands)==1):
            return int(commands[0],2)
        frequency = count_frequency(commands, i)
        if frequency >= len(commands) / 2:
            commands = scrub(commands, i, '0')
        else:
            commands = scrub(commands, i, '1')

    return int(commands[0], 2)




print(find_power(power))
print(oxygen_rating(power))
print(carbon_rating(power))
