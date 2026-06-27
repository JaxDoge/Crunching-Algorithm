1895. Largest Magic Square


class Solution:
	def largestMagicSquare(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])

		row_prefix_sum_mat = [[0] * (n + 1) for _ in range(m + 1)]
		col_prefix_sum_mat = [[0] * (n + 1) for _ in range(m + 1)]

		# Construct row pre sum
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				row_prefix_sum_mat[i][j] = row_prefix_sum_mat[i][j - 1] + grid[i - 1][j - 1]

		# Construct col pre sum
		for j in range(1, n + 1):
			for i in range(1, m + 1):
				col_prefix_sum_mat[i][j] = col_prefix_sum_mat[i - 1][j] + grid[i - 1][j - 1]

		# Search the magic square from the largest possible one
		# The largest side length
		max_side = min(m, n)

		for l in range(max_side, 0, -1):
			# Move the top-left vertex
			for i in range(m):
				if i + l - 1 > m - 1:
					break

				for j in range(n):
					if j + l - 1 > n - 1:
						break

					# check if it is a magic square
					# check diagonals
					init_magic_sum = 0
					cur_magic_sum = 0
					for k in range(l):
						init_magic_sum += grid[i + k][j + k]
						cur_magic_sum += grid[i + k][j + l - 1 - k]

					if init_magic_sum != cur_magic_sum:
						continue

					# check row and col
					row_magic_sum = 0
					col_magic_sum = 0
					for k in range(l):
						row_magic_sum = row_prefix_sum_mat[i + 1 + k][j + 1 + l - 1] - row_prefix_sum_mat[i + 1 + k][j]
						col_magic_sum = col_prefix_sum_mat[i + 1 + l - 1][j + 1 + k] - col_prefix_sum_mat[i][j + 1 + k]
						if row_magic_sum != init_magic_sum or col_magic_sum != init_magic_sum:
							break

					if row_magic_sum != init_magic_sum or col_magic_sum != init_magic_sum:
						continue
					else:
						return l






