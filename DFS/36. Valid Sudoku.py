36. Valid Sudoku


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Using Three high dimension list to record the count of each number in each row, column and subsquare
        row_counter = [[0] * 9 for _ in range(9)]
        col_counter = [[0] * 9 for _ in range(9)]
        sq_counter = [[[0] * 9 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1
                if row_counter[i][num] > 0:
                    return False
                else:
                    row_counter[i][num] += 1

                if col_counter[j][num] > 0:
                    return False
                else:
                    col_counter[j][num] += 1  

                if sq_counter[i//3][j//3][num] > 0:
                    return False
                else:
                    sq_counter[i//3][j//3][num] += 1

        return True