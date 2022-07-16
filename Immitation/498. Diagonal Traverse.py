498. Diagonal Traverse



# immitation
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        directions = [[-1, 1], [1, -1]]

        m = len(mat)
        n = len(mat[0])

        ans = []
        target = m * n
        i = j = 0
        d = 0

        while len(ans) < target:
            ans.append(mat[i][j])

            dr, dc = directions[d]
            ni, nj = i + dr, j + dc

            if not (0 <= ni < m) or not (0 <= nj < n):
                d = (d + 1) % 2

            if ni < 0 and (0 <= nj < n):
                ni, nj = i, j + 1
            elif (0 <= ni < m) and nj < 0:
                ni, nj = i + 1, j
            elif ni >= m:
                ni, nj = i, j + 1
            elif nj >= n:
                ni, nj = i + 1, j

            i = ni
            j = nj


        return ans