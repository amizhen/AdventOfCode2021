from utility_functions.utilities import read_file

input = read_file('inputDay8.txt')

input1 = [i.split(' | ')[1] for i in input]


input1 = [i.split() for i in input1]


count = 0
for i in input1:
    for j in i:
        if len(j) in {2, 4, 3, 7}:
            count += 1

print(count)


def get_sum(line):
    newline = []
    for digit in line:
        if len(digit) == 2:
            cf = digit
        elif len(digit) == 3:
            acf = digit
        elif len(digit) == 4:
            bdcf = digit
        elif len(digit) == 7:
            abcdefg = digit

    cf = set(cf)
    acf = set(acf)
    bdcf = set(bdcf)
    abcdefg = set(abcdefg)
    a = acf-cf
    bd = bdcf - cf
    eg = abcdefg - bdcf - a
    count = 0
    for digit in line[-4:]:
        if len(digit) == 2:
            newline.append(1)
        elif len(digit) == 3:
            newline.append(7)
        elif len(digit) == 4:
            newline.append(4)
        elif len(digit) == 7:
            newline.append(8)
        elif len(digit) == 6:
            if (abcdefg - set(digit)).issubset(bd):
                newline.append(0)
            elif (abcdefg - set(digit)).issubset(eg):
                newline.append(9)
            else:
                newline.append(6)
        elif len(digit) == 5:
            if len((abcdefg - set(digit)).intersection(cf))>0 and len((abcdefg - set(digit)).intersection(bd))>0:
                newline.append(2)
            elif len((abcdefg - set(digit)).intersection(cf))>0 and len((abcdefg - set(digit)).intersection(eg))>0:
                newline.append(5)
            else:
                newline.append(3)
    out = ''
    for i in newline:
        out+=f'{i}'
    return int(out)

print(get_sum(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab', 'cdfeb', 'fcadb', 'cdfeb', 'cdbaf']))

input2 = [[n for n in i.split() if n != '|'] for i in input]


sum = 0
for line in input2:
    sum += get_sum(line)

print(sum)


