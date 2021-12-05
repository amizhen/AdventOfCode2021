from utility_functions.utilities import read_file

input = read_file('inputDay4.txt')
bingo_stream = [int(num) for num in input[0].split(',')]

# Boards is now a list of boards, which is a list of rows, which is a list of values.
boards = [[[int(num) for num in row.split()]
           for row in input[i * 6 + 2:i * 6 + 7]]
          for i in range(len(input) // 6)]


def score(board, called_values):
    sum = 0
    for row in board:
        for val in row:
            if val not in called_values:
                sum += val
    return sum * called_values[-1]


def check_row(board, called_values):
    for row in board:
        count = 0
        for val in row:
            if val in called_values:
                count += 1
        if count == 5:
            return True
    return False


def check_column(board, called_values):
    for column in range(5):
        count = 0
        for row in board:
            if row[column] in called_values:
                count += 1
        if count == 5:
            return True
    return False


def find_winner(boards, bingo_stream):
    called_values = []
    for value in bingo_stream:
        called_values.append(value)
        for board in boards:
            if check_row(board, called_values) or \
                    check_column(board, called_values):
                return score(board, called_values)


def find_looser(boards, bingo_stream):
    called_values = []
    winners = []
    for value in bingo_stream:
        if len(winners) == len(boards):
            return score(boards[winners[-1]], called_values)
        called_values.append(value)

        for board_index in range(len(boards)):
            if board_index not in winners:
                if check_row(boards[board_index], called_values) or \
                        check_column(boards[board_index], called_values):
                    winners.append(board_index)


print(find_winner(boards, bingo_stream))
print(find_looser(boards, bingo_stream))
