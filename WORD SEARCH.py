def exist(board, word):
    if not board:
        return False

    def backtrack(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        tmp, board[i][j] = board[i][j], "#"
        res = (backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or
               backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1))
        board[i][j] = tmp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(exist(board, word))  
