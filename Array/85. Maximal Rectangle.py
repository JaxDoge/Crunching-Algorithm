85. Maximal Rectangle


# Downgrade to find the largest rectangle in multiple histogram
from collections import deque
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # Construct a new matrix to record the number of consecutive ones left hand side of this cell
        leftMatrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    leftMatrix[i][j] = 1 if j == 0 else leftMatrix[i][j-1] + 1

        res = 0 
        # Each column could be regarded as a histogram
        for j in range(n):
            left = [-1] * m
            right = [m] * m

            monoStack = []
            for i in range(m):
                while len(monoStack) and leftMatrix[monoStack[-1]][j] >= leftMatrix[i][j]:
                    i0 = monoStack.pop()
                    right[i0] = i
                if len(monoStack):
                    left[i] = monoStack[-1]
                monoStack.append(i)

            resT = max((right[i] - left[i] - 1) * leftMatrix[i][j] for i in range(m))
            res = max(res, resT)

        return res