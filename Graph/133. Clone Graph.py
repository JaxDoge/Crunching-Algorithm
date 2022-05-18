133. Clone Graph


# BFS
# using dictionary to construct a map between original node and copycat node

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        queue = deque()
        queue.append(node)
        visited = {}
        visited[node] = Node(node.val)

        while queue:
            curNode = queue.popleft()
            # curNode is visited here
            for n in curNode.neighbors:
                # if n is not visited, we need create the corresponding copy
                # and continue search from this node
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                # update curNode's neighbor
                visited[curNode].neighbors.append(visited[n])

        return visited[node]



