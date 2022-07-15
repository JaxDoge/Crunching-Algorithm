310. Minimum Height Trees



# https://leetcode.cn/problems/minimum-height-trees/solution/zui-xiao-gao-du-shu-by-leetcode-solution-6v6f/
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]

        # indirection graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # We need to build a parent list to record a path
        # Parent[i] is the parent node of i
        parent = [-1] * n

        from collections import deque
        def bfs(node):
            nonlocal n, parent, graph
            visited = [False] * n
            visited[node] = True
            queue = deque([node])
            while queue:
                cur = queue.popleft()
                for nbh in graph[cur]:
                    if not visited[nbh]:
                        visited[nbh] = True
                        # maintain tree relationship
                        parent[nbh] = cur
                        queue.append(nbh)
            # return the last node reached by bfs procedure
            return cur

        endI = bfs(0)
        endJ = bfs(endI)

        # construct the path from I to J
        path = []
        # parent of end I did not update in the second bfs
        parent[endI] = -1
        while endJ != -1:
            path.append(endJ)
            endJ = parent[endJ]

        m = len(path)

        if m % 2 == 1:
            return [path[m // 2]]

        return [path[m // 2 - 1], path[m // 2]] 
