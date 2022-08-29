994. Rotting Oranges


# BFS
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        minute = 0
        freshOranges = 0 

        # initial the BFS
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        def isValid(row, col):
            nonlocal m, n, grid
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        while queue:
            curSize = len(queue)
            for _ in range(curSize):
                curOrg = queue.popleft()
                curI, curJ = curOrg
                for dx, dy in directions:
                    newI, newJ = curI + dx, curJ + dy
                    if isValid(newI, newJ):
                        grid[newI][newJ] = 2
                        freshOranges -= 1
                        queue.append((newI, newJ))

            if queue:
                minute += 1

        return -1 if freshOranges else minute
