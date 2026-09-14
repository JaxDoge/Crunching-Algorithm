2906. Construct Product Matrix


# No need divide ops
# For any given cell i, j, we only need to know:
# By row, the product of all cells that row index < i and all cells that row index > i
# By col, in the same row, the prefix product and suffix product
# we can get all information in on iteration
MOD = 12345
class Solution:
	def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
		m, n = len(grid), len(grid[0])

		# [before i, after i]
		vertical_prod = [[1, 1] for _ in range(m)]

		prefix_prod = [[1] * n for _ in range(m)]
		suffix_prod = [[1] * n for _ in range(m)]

		for i in range(m):
			for j in range(n):
				# Using i, j to calculate prefix
				# Using r_i, r_j to calculate suffix
				r_i = m - 1 - i
				r_j = n - 1 - j

				# Calculate vertical products:
				if j == 0:
					if i == 0:
						vertical_prod[i][0] = 1
						vertical_prod[r_i][1] = 1
					else:
						vertical_prod[i][0] = ((prefix_prod[i - 1][n - 1] * vertical_prod[i - 1][0]) % MOD * grid[i - 1][n - 1] % MOD) % MOD
						vertical_prod[r_i][1] = ((suffix_prod[r_i + 1][0] * vertical_prod[r_i + 1][1]) % MOD * grid[r_i + 1][0] % MOD) % MOD

				# Calculate prefix and suffix product by each row
				elif j > 0:
					prefix_prod[i][j] = (prefix_prod[i][j - 1] * grid[i][j - 1] % MOD) % MOD
					suffix_prod[r_i][r_j] = (suffix_prod[r_i][r_j + 1] * grid[r_i][r_j + 1] % MOD) % MOD

		p = [[1] * n for _ in range(m)]

		for i in range(m):
			for j in range(n):
				p[i][j] = ((vertical_prod[i][0] * vertical_prod[i][1]) % MOD * (prefix_prod[i][j] * suffix_prod[i][j]) % MOD) % MOD

		return p


# p[i][j]=prefix[i][j]⋅suffix[i][j]
class Solution:
	def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
		MOD = 12345
		n, m = len(grid), len(grid[0])
		p = [[0] * m for _ in range(n)]

		suffix = 1
		for i in range(n - 1, -1, -1):
			for j in range(m - 1, -1, -1):
				p[i][j] = suffix
				suffix = (suffix * grid[i][j]) % MOD

		prefix = 1
		for i in range(n):
			for j in range(m):
				p[i][j] = (p[i][j] * prefix) % MOD
				prefix = (prefix * grid[i][j]) % MOD

		return p
		