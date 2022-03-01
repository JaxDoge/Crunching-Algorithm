class Solution:
    def __init__(self):
        self.res = list()

    def solveNQueens(self, n: int) -> List[List[str]]:
        one_solution = [['.' for x in range(n)] for x in range(n)]
        self.backtrack(one_solution, 0)
        return self.res

    def backtrack(self, current_board: List[str], row: int):
        # base case. Find an acceptable solution
        if row == len(current_board):
            # join list to string
            tmp_board = list()
            for i in range(len(current_board)):
                tmp_board.append("".join(current_board[i]))
            self.res.append(tmp_board.copy())
            return

        for col in range(len(current_board[0])):
            # validate the acceptable position for queen pawn
            if not self.is_valid(current_board, row, col):
                continue

            current_board[row][col] = 'Q'
            self.backtrack(current_board, row+1)
            current_board[row][col] = '.'

    def is_valid(self, board, row, col):
        num = len(board)

        # check above
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # check upper-right
        for i in range(row-1, -1, -1):
            j = col + row - i
            if i < 0 or j >= num:
                break
            if board[i][j] == 'Q':
                return False
        # check upper-left
        for i in range(row-1, -1, -1):
            j = col - (row - i)
            if i < 0 or j < 0:
                break
            if board[i][j] == 'Q':
                return False

        return True







