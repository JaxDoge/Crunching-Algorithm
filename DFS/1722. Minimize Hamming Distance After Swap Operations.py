1722. Minimize Hamming Distance After Swap Operations


# Build the graph
# DFS visit the graph, and record the element of each group
class Solution:
	def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
		size = len(source)
		graph = defaultdict(list)
		visited = [False] * size
		res = 0

		for u, v in allowedSwaps:
			graph[u].append(v)
			graph[v].append(u)

		def dfs(index, group):
			visited[index] = True
			group.append(index)

			for neighbor in graph[index]:
				if not visited[neighbor]:
					dfs(neighbor, group)

		for i in range(size):
			if visited[i]:
				continue

			group = []
			
			dfs(i, group)

			# Count the values in the group
			source_cnt = Counter(source[idx] for idx in group)

			for idx in group:
				trgt = target[idx]

				if source_cnt[trgt] > 0:
					source_cnt[trgt] -= 1
				else:
					res += 1

		return res




