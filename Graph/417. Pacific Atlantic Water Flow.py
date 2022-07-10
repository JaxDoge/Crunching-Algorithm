417. Pacific Atlantic Water Flow



# reverse thinking, we could go through every edge cell, and check all reachable cells
# the rule is, only those adjacent cells are flush with or higher than current cell are reachable
# thus the time complexity is O((n+m)^2)
# BFS and DFS are both OK

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = heights.__len__()
        n = len(heights[0])

        # return a list of reachable cells of a cell
        def reachableNbh(curCell = (0, 0)):
            nonlocal dirs, heights
            neighbors = []

            curX, curY = curCell
            for dx, dy in dirs:
                nX = curX + dx
                nY = curY + dy

                # Check validity
                if not (0 <= nX < m) or not (0 <= nY < n):
                    continue
                if heights[curX][curY] > heights[nX][nY]:
                    continue

                neighbors.append((nX, nY))

            return neighbors

        # using an extra m*n matrix to record the state of each cell
        accessM = [[0] * n for _ in range(m)]
        from collections import deque

        def bfs(startCell):
            nonlocal heights, accessM, m, n

            queue = deque()
            visited = set()

            startX, startY = startCell
            # connect to Pacific Ocean
            if startX == 0 or startY == 0:
                accessM[startX][startY] |= 1
            # connect to Atlantic Ocean
            if startX == m - 1 or startY == n - 1:
                accessM[startX][startY] |= 2

            queue.append(startCell)
            visited.add(startCell)

            while queue:
                curCell = queue.popleft()

                nbhList = reachableNbh(curCell)
                for nbh in nbhList:
                    if nbh in visited:
                        continue
                    nbhX, nbhY = nbh
                    # update this neighbor
                    accessM[nbhX][nbhY] |= accessM[startX][startY]
                    visited.add(nbh)
                    queue.append(nbh)

        # run bfs for every edge cell
        for j in range(n):
            bfs((0, j))
            bfs((m - 1, j))

        for i in range(1, m - 1):
            bfs((i, 0))
            bfs((i, n - 1))

        ans = []
        for i in range(m):
            for j in range(n):
                if accessM[i][j] == 3:
                    ans.append([i, j])

        return ans




