73. Set Matrix Zeroes


# O(1) extra space complexity
# Using the first row and first column to mark if the whole row or column shuold be set to zero
# Using another two varible to mark if the first row and first column should be set to zero originally.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_col0 = any(matrix[i][0] == 0 for i in range(m))
        first_row0 = any(matrix[0][i] == 0 for i in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col0:
            for i in range(m):
                matrix[i][0] = 0

        if first_row0:
            for j in range(n):
                matrix[0][j] = 0

        return


