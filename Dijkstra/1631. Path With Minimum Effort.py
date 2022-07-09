1631. Path With Minimum Effort




# Dijkstra
class SState:
    def __init__(self, coor, effortFStart):
        self.coor = coor
        self.effortFStart = effortFStart


from heapq import heappop, heappush, heapify, heappushpop
class Myheap:
    def __init__(self, initial = None, key = lambda x: x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapify(self._data)
        else:
            self._data = []

    def __len__(self):
        return len(self._data)

    def getTop(self):
        return self._data[0][2]

    def push(self, item):
        heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        return heappop(self._data)[2]

    def pushpop(self, item):
        outcast = heappushpop(self._data, (self.key(item), self.index, item))
        self.index += 1
        return outcast

    def getHeap(self):
        return self._data  


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(heights)
        n = len(heights[0])
        
        # graph function: input current coordinate and return the list of valid adjacent cells
        def adjF(curCoor):
            nonlocal heights, m, n
            neighbors = []
            for d in dirs:
                nx = curCoor[0] + d[0]
                ny = curCoor[1] + d[1]

                # check validity
                if nx >= m or ny >= n or nx < 0 or ny < 0:
                    continue

                neighbors.append((nx, ny))

            return neighbors

        # dijkstra
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = 0

        pq = Myheap(key = lambda x: x.effortFStart)
        pq.push(SState((0, 0), 0))

        while pq.getHeap():
            curState = pq.pop()
            curCoor = curState.coor
            curX, curY = curCoor
            curEffort = curState.effortFStart

            # if we have arrived the bottom-right corner
            if curCoor == (m - 1, n - 1):
                return curEffort

            # if we find a shorter path to current cell
            # skip this state
            if dp[curX][curY] < curEffort:
                continue

            for nbhX, nbhY in adjF(curCoor):
                # calculate the effort from start cell to this neighbor
                nextEffort = max(curEffort, abs(heights[curX][curY] - heights[nbhX][nbhY]))

                # check if the dp table need be updated
                if dp[nbhX][nbhY] > nextEffort:
                    dp[nbhX][nbhY] = nextEffort
                    # the neighbors of nbh need be updated later
                    pq.push(SState((nbhX, nbhY), nextEffort))

        # program should not get here
        return -1