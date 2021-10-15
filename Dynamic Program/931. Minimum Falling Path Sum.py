931. Minimum Falling Path Sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = float('inf')
        memo = [[9999999 for _ in range(n)] for _ in range(n)]

        def dp_table(row, col):
            nonlocal matrix, n
            # check if out of bound
            if row < 0 or col < 0 or row >= n or col >= n:
                return float('inf')

            # base case
            if row == 0:
                # print(matrix[row][col])
                return matrix[row][col]

            # check memo
            if memo[row][col] != 9999999:
                return memo[row][col]

            memo[row][col] = matrix[row][col] + min(dp_table(row-1,col-1),dp_table(row-1,col),dp_table(row-1,col+1))
            return memo[row][col]


        # 最后落在 n - 1 行某一列，所以要遍历所有结果，返回最小值
        for j in range(n):
            res = min(res, dp_table(n-1,j))

        return res


