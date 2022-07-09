1514. Path with Maximum Probability



# Dijkstra is designed to calculate the smaller weight, not the larger one
# So we could convert the question into find the smallest failure rate.


class SState:
    def __init__(self, _id, failureRate):
        self.id = _id
        self.failureRate = failureRate

from heapq import heappop, heappush, heapify, heappushpop
class Myheap:
    def __init__(self, initial = None, key = lambda x: x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self.data)
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
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # build the graph
        m = len(succProb)
        graph = [[] for _ in range(n)]
        for i in range(m):
            a, b = edges[i]
            succ = succProb[i]
            graph[a].append((b, succ))
            graph[b].append((a, succ))

        dp = [float("inf")] * n
        dp[start] = 0

        pq = Myheap(key = lambda x: x.failureRate)
        pq.push(SState(start, 0))

        while pq.getHeap():
            curState = pq.pop()
            curId = curState.id
            curFR = curState.failureRate

            # Because of heapq, the first time we pop out end id, curFR is the answer we want
            if curId == end:
                return 1 - curFR

            if dp[curId] < curFR:
                continue

            for nbhId, nbhSP in graph[curId]:
                nextFR = 1 - (1 - curFR) * nbhSP

                if dp[nbhId] > nextFR:
                    dp[nbhId] = nextFR
                    pq.push(SState(nbhId, nextFR))

        # or it is impossible to find a valid path
        return 0
