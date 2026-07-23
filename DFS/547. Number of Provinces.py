547. Number of Provinces

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		size = len(isConnected)
		res = 0
		visited = [False] * size

		def dfs(city):
			visited[city] = True
			# visit all neighbors
			# Cannot just scan the upper right trangle
			# Because the later node may connected to other node has smaller index
			# For example 1 -> 4 and 4 -> rest of world
			for c in range(size):
				if isConnected[city][c] and not visited[c]:
					dfs(c)

		for i in range(size):
			if not visited[i]:
				res += 1
				dfs(i)

		return res




