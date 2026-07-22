2858. Minimum Edge Reversals So Every Node Is Reachable

# Using DFS to find the answer for one node, which is easy
# The answers of its neighbors can be derived by DP

# Remember the graph is a tree-like.
# Between any two vertices, there is only one path
# So during searching on a path, current vertex only have one parent that need to avoid repeat visit

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        # Build the graph table
        # Treat as bidirectional graph except there is a cost
        for u, v in edges:
            # Original direction: u -> v
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        answer = [0] * n

        # First DFS:
        # Calculate the reversals required when starting from node 0.
        def count_reversals(node: int, parent: int) -> int:
            total = 0

            for neighbor, cost in graph[node]:
                if neighbor == parent:
                    continue

                total += cost
                total += count_reversals(neighbor, node)

            return total

        answer[0] = count_reversals(0, -1)

        # Second DFS:
        # Calculate answers for neighboring roots.
        def reroot(node: int, parent: int) -> None:
            for neighbor, cost in graph[node]:
                if neighbor == parent:
                    continue

                # if cost = 0, answer[neighbor] = answer[node] + 1, since we need to reverse on more edge
                # if cost = 1, answer[neighbor] = answer[node] - 1, there is one less edge to reverse
                answer[neighbor] = answer[node] + 1 - 2 * cost
                reroot(neighbor, node)

        reroot(0, -1)

        return answer