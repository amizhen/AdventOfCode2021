from utility_functions.utilities import read_file

input = read_file('inputDay10.txt')


# def score_line(line):
#     scorer = {')': 3, ']': 57, '}': 1197, '>': 25137}
#     opened_closed = {'(':0, ')':0, '[':0, ']':0, '{':0, '}':0, '<':0, '>':0}
#     for i in line:
#         opened_closed[i] += 1
#         if i == ')' and opened_closed[')'] > opened_closed['(']:
#             return scorer[i]
#         if i == ']' and opened_closed[']'] > opened_closed['[']:
#             return scorer[i]
#         if i == '}' and opened_closed['}'] > opened_closed['{']:
#             return scorer[i]
#         if i == '>' and opened_closed['>'] > opened_closed['<']:
#             return scorer[i]
#     print(line)
#     return 0


def score_line(line):
    scorer = {')': 3, ']': 57, '}': 1197, '>': 25137}
    current = []
    for i in line:
        if i in {'(', '[', '{', '<'}:
            current.append(i)
        else:
            if i == ')' and current[-1] != '(':
                return scorer[i]
            if i == ']' and current[-1] != '[':
                return scorer[i]
            if i == '}' and current[-1] != '{':
                return scorer[i]
            if i == '>' and current[-1] != '<':
                return scorer[i]
            current.pop(-1)
    return 0


count = []
good_lines = []

for line in input:
    if score_line(line) == 0:
        good_lines.append(line)
    count.append(score_line(line))

print(sum(count))


def score_missing(line):
    scorer = {'(': 1, '[': 2, '{': 3, '<': 4}
    current = []
    score = 0
    for i in line:
        if i in {'(', '[', '{', '<'}:
            current.append(i)
        else:
            current.pop(-1)
    for i in current[::-1]:
        score *= 5
        score += scorer[i]
    return score

scores = []
for line in good_lines:
    scores.append(score_missing(line))

print(sorted(scores)[len(scores)//2])