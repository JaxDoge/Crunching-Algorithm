3567. Minimum Absolute Difference in Sliding Submatrix

# Brutal Force
class Solution:
	def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
		m = len(grid)
		n = len(grid[0])

		res = [[-1] * (n - k + 1) for _ in range(m - k + 1)]

		for i in range(m - k + 1):
			for j in range(n - k + 1):
				value_in = []
				for x in range(i, i + k):
					for y in range(j, j + k):
						value_in.append(grid[x][y])

				sub_min = float('inf')
				value_in.sort()

				for p in range(1, len(value_in)):
					# We need to calculate the difference between two distinct values
					if value_in[p] == value_in[p - 1]:
						continue
					sub_min = min(sub_min, abs(value_in[p] - value_in[p - 1]))

				# If all values are the same, then the answer is 0
				if sub_min == float('inf'):
					sub_min = 0

				res[i][j] = sub_min

		return res



