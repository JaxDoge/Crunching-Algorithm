1743. Restore the Array From Adjacent Pairs


class Solution:
	def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
		n = len(adjacentPairs) + 1

		graph = defaultdict(list)
		visited = {}

		for u, v in adjacentPairs:
			graph[u].append(v)
			graph[v].append(u)
			visited[u] = False
			visited[v] = False

		
		res = deque()

		def dfs(number, head: bool):
			if visited[number]:
				return

			visited[number] = True

			if head:
				res.appendleft(number)
			else:
				res.append(number)

			for nghbr in graph[number]:
				dfs(nghbr, head)

		start_number = next(iter(graph))
		res.append(start_number)
		visited[start_number] = True

		left = graph[start_number][0]
		dfs(left, True)
			
		if len(graph[start_number]) == 2:
			right = graph[start_number][1]
			dfs(right, False)

		return list(res)