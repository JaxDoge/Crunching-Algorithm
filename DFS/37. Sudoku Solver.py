class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = 9
        cols = 9

        def backtrack(board_, i, j):
            if j == cols:
                # enumerate one row
                return backtrack(board_, i + 1, 0)

            if i == rows:
                # base case
                return True

            if board_[i][j] != '.':
                # encounter a preset number
                return backtrack(board_, i, j + 1)

            # enumerate all possible characters
            for char in range(1, 10):
                # validation
                if not isvalid(board_, i, j, str(char)):
                    continue

                board_[i][j] = str(char)
                # backtrack and exit condition
                if backtrack(board_, i, j + 1):
                    return True
                board_[i][j] = '.'

            # There is no solution
            return False

        def isvalid(p_board, row, col, char: str):
            for i in range(9):
                if p_board[row][i] == char:
                    return False
                if p_board[i][col] == char:
                    return False
                # How to iterate a 3x3 sub-square:
                if p_board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == char:
                    return False

            return True

        backtrack(board, 0, 0)
