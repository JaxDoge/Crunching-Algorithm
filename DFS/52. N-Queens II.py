52. N-Queens II


# DFS
# Notice:
# for main diagonal, the cell has i - j = constant
# for sub-diagonal, the cell has i + j = constant
# So those specific constants could identify diagonals
class Solution:
    def totalNQueens(self, n: int) -> int:

                    
        col_memo = set()
        diag1_memo = set()
        diag2_memo = set()

        return self.backtrack(n, col_memo, diag1_memo, diag2_memo, 0)



    def backtrack(self, n, columns, diagonal1, diagonal2, row) -> int:
        # base case, find a solution
        if row == n:
            return 1

        count = 0
        for i in range(n):
            if i in columns or row - i in diagonal1 or row + i in diagonal2:
                continue
            columns.add(i)
            diagonal1.add(row - i)
            diagonal2.add(row + i)
            count += self.backtrack(n, columns, diagonal1, diagonal2, row+1)
            columns.remove(i)
            diagonal1.remove(row - i)
            diagonal2.remove(row + i)
        return count