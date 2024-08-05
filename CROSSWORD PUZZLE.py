def print_crossword(board):
    for row in board:
        print("".join(row))
    print()

def is_valid_move(board, word, x, y, direction):
    if direction == 'H':
        if y + len(word) > len(board[0]):
            return False
        for j in range(len(word)):
            if board[x][y + j] not in ('-', word[j]):
                return False
    else:
        if x + len(word) > len(board):
            return False
        for i in range(len(word)):
            if board[x + i][y] not in ('-', word[i]):
                return False
    return True

def place_word(board, word, x, y, direction):
    positions = []
    if direction == 'H':
        for j in range(len(word)):
            if board[x][y + j] == '-':
                positions.append((x, y + j))
                board[x][y + j] = word[j]
    else:
        for i in range(len(word)):
            if board[x + i][y] == '-':
                positions.append((x + i, y))
                board[x + i][y] = word[i]
    return positions

def remove_word(board, positions):
    for x, y in positions:
        board[x][y] = '-'

def solve_crossword(board, words, index):
    if index == len(words):
        print_crossword(board)
        return True
    word = words[index]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_valid_move(board, word, i, j, 'H'):
                positions = place_word(board, word, i, j, 'H')
                if solve_crossword(board, words, index + 1):
                    return True
                remove_word(board, positions)
            if is_valid_move(board, word, i, j, 'V'):
                positions = place_word(board, word, i, j, 'V')
                if solve_crossword(board, words, index + 1):
                    return True
                remove_word(board, positions)
    return False
board = [
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-'],
    ['-', '-', '-', '#', '-', '-', '-', '#', '-']
]
words = ["HELLO", "WORLD", "PYTHON", "CROSSWORD"]
solve_crossword(board, words, 0)
