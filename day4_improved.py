from utility_functions.utilities import read_file

input = read_file('inputDay4.txt')
bingo_stream = [int(num) for num in input[0].split(',')]
boards = [[[int(num) for num in row.split()]
           for row in input[i * 6 + 2:i * 6 + 7]]
          for i in range(len(input) // 6)]


# Boards is now a list of boards, which is a list of rows, which is a list of values.
class Board:
    def __init__(self, rows):
        self.rows = rows
        self.winner = False

    def mark_number(self, new_number):
        for row in self.rows:
            for index, n in enumerate(row):
                if n == new_number:
                    row[index] = 0

    def is_complete(self):
        for row in self.rows:
            if sum(row) == 0:
                return True

        for i in range(5):
            col_sum = 0
            for row in self.rows:
                col_sum += row[i]

            if col_sum == 0:
                return True

        return False

    def score(self, winning_number):
        return sum(i
                   for row in self.rows
                   for i in row) * winning_number

    def mark_winner(self):
        self.winner = True

    def is_winner(self):
        return self.winner


def play_bingo(boards, bingo_stream):
    for value in bingo_stream:
        for board in boards:
            if not board.is_winner():
                board.mark_number(value)
                if board.is_complete():
                    board.mark_winner()
                    yield board.score(value)


boards2 = [Board(board) for board in boards]
game = list(play_bingo(boards2, bingo_stream))
print(game[0], game[-1])
