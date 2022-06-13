剑指 Offer 29. 顺时针打印矩阵



# Same as https://leetcode-cn.com/problems/spiral-matrix/ 
class Solution(object):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        n = rows * cols

        memoMatrix = [[0] * cols for _ in range(rows)]
        res = []

        i, j = 0, 0
        di = 0
        while len(res) < n:
            res.append(matrix[i][j])
            memoMatrix[i][j] = 1
            
            newi, newj = i + self.directions[di][1], j + self.directions[di][0]
            if newi >= rows or newj >= cols or memoMatrix[newi][newj] > 0:
                di = (di + 1) % 4
                newi, newj = i + self.directions[di][1], j + self.directions[di][0]

        return res
