1878. Get Biggest Three Rhombus Sums in a Grid


# Simulation
# Prefix Sum for the O(1) Rhombus Sums calculation
# down_right[i + 1][j + 1] be the sum along the \ diagonal ending at grid[i][j].
# down_left[i + 1][j] be the sum along the / diagonal ending at grid[i][j].

class Solution:
	def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
		res = []
		seen = set()

		# Note the heap alone cannot secure the distinct result
		def addRes(cand):
			if cand in seen:
				return

			seen.add(cand)
			heapq.heappush(res, cand)

			if len(res) > 3:
				heapq.heappop(res)

		m = len(grid)
		n = len(grid[0])

		# diag "\"
		diag_1 = [[0] * (n + 1) for _ in range(m + 1)]

		# diag "/"
		diag_2 = [[0] * (n + 1) for _ in range(m + 1)]

		for i in range(m):
			for j in range(n):
				diag_1[i + 1][j + 1] = diag_1[i][j] + grid[i][j]

		for i in range(m):
			for j in range(n - 1, -1, -1):
				diag_2[i + 1][j] = diag_2[i][j + 1] + grid[i][j]

		for top_r in range(m):
			for top_c in range(n):
				addRes(grid[top_r][top_c])

				max_k = min(top_c, n - 1 - top_c, (m - 1 - top_r) // 2)

				for k in range(1, max_k + 1):
					top = (top_r, top_c)
					left = (top_r + k, top_c - k)
					right = (top_r + k, top_c + k)
					bottom = (top_r + 2*k, top_c)

					# top -> right ('\')
					edge_1 = diag_1[right[0] + 1][right[1] + 1] - diag_1[top[0]][top[1]]
					# right -> bottom ('/')
					edge_2 = diag_2[bottom[0] + 1][bottom[1]] - diag_2[right[0]][right[1] + 1]
					# left -> bottom ('\')
					edge_3 = diag_1[bottom[0] + 1][bottom[1] + 1] - diag_1[left[0]][left[1]]
					# top -> left ('/')
					edge_4 = diag_2[left[0] + 1][left[1]] - diag_2[top[0]][top[1] + 1]	

					rhombus_sum = edge_1 + edge_2 + edge_3 + edge_4
					rhombus_sum -= grid[top[0]][top[1]] + grid[left[0]][left[1]] + grid[right[0]][right[1]] + grid[bottom[0]][bottom[1]]

					addRes(rhombus_sum)

		res.sort(reverse = True)
		return [x for x in res if x != 0]
