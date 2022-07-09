743. Network Delay Time




# Dijkstra
# firstly, construct the adjacency list of the graph
# calculate the shortest distance from k to every vertex
# find the longest one
class VertexState:
    def __init__(self, id, disFStart):
        self.id = id
        self.disFStart = disFStart

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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)

        for s, t, w in times:
            graph[s].append((t, w))

        distList = self.dijkstra(k, graph, n)

        return -1 if max(distList) == float("inf") else max(distList)    

    def dijkstra(self, start, graph, n):
        # Dp table, the algorithm will try to update the list based on the search state
        distList = [float("inf")] * (n + 1)
        # base case
        distList[start], distList[0] = 0, 0

        # Core data structure, the priority queue
        pq = Myheap(key = lambda x: x.disFStart)

        pq.push(VertexState(start, 0))

        # BFS code frame
        while pq.getHeap():
            cVS = pq.pop()
            # the length of current path (until current vertex)
            curDistFStart = cVS.disFStart

            # if there is a shorter path to current vertex, the current path is useless
            # Note that distList[cVS.id] will never be infinite
            if (distList[cVS.id] < curDistFStart):
                continue

            # else, if distList[cVS.id] == curDistFStart
            # note that there is no distList[cVS.id] > curDistFStart
            for nextID, weight in graph[cVS.id]:
                # calculate the distance to the next vertex
                disTNext = curDistFStart + weight

                # if it is a shorter path to next vertex, update the dp table
                # and add the next vertex into pq queue
                if disTNext < distList[nextID]:
                    distList[nextID] = disTNext
                    pq.push(VertexState(nextID, disTNext))

        return distList



