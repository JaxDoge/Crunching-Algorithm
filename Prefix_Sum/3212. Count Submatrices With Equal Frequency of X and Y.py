3212. Count Submatrices With Equal Frequency of X and Y

# Convert X, Y, `.` to 1, -1, 0. Then use presum to quickly get the submatrix result
class Solution:
	def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
		m, n = len(grid), len(grid[0])
		has_x = [[False] * n for _ in range(m)]
		presum = [[0] * n for _ in range(m)]
		res = 0

		def converter(val):
			if val == 'X':
				return 1
			elif val == 'Y':
				return -1
			else:
				return 0

		# Construct has X matrix
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					if grid[i][j] == 'X':
						has_x[i][j] = True

					continue

				if grid[i][j] == 'X':
					has_x[i][j] = True
				else:
					if i > 0:
						has_x[i][j] = has_x[i][j] or has_x[i - 1][j]
					if j > 0:
						has_x[i][j] = has_x[i][j] or has_x[i][j - 1]

		for i in range(m):
			for j in range(n):
				if j == 0:
					presum[i][j] = converter(grid[i][j])
					continue
				presum[i][j] = converter(grid[i][j]) + presum[i][j - 1]

		# Reuse presum to calculate submatrix sum
		for i in range(m):
			for j in range(n):
				if i > 0:
					presum[i][j] = presum[i][j] + presum[i - 1][j]
				if presum[i][j] == 0 and has_x[i][j]:
					res += 1

		return res


