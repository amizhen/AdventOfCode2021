def read_file(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]

def read_file_int(file_name):
    with open(file_name, "r") as file:
        return [int(line) for line in file]

def make_number(string):
    numb = ""
    for i in string:
        if i.isdigit():
            numb = numb + i
    return int(numb)

def count_frequency(string, char):
    count = 0
    for i in string:
        if i == char:
            count = count + 1
    return count