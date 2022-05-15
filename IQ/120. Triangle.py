120. Triangle


# Bottom up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        underSum = triangle[-1]
        if n == 1:
            return min(underSum)

        for i in range(n-2, -1, -1):
            thisSum = []
            m = len(triangle[i])
            for j in range(m):
                tmp = min(triangle[i][j] + underSum[j], triangle[i][j] + underSum[j + 1])
                thisSum.append(tmp)

            underSum = thisSum

        return min(underSum)