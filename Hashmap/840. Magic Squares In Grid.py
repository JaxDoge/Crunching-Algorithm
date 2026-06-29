840. Magic Squares In Grid


# Note that each row, col, and diagonal sum is 45 / 3 = 15
# Then we can seach from the top-left magic square
# We need to check:
# 1. If the 3 col sums are 15.
# 2. the rows
# 3. the diagonals
# 4. the 1-9 distinction
# Then move the square to the right

class Solution:
	# Check if the square (top-left corner is (row, col))
	def _isMagicSquare(self, grid, row, col):
		unique_set = set()
		row_sums = [0, 0, 0]
		col_sums = [0, 0, 0]
		diag_sums = [0, 0]

		for i in range(3):
			for j in range(3):
				num = grid[row + i][col + j]
				# Check range
				if num < 1 or num > 9:
					return False
				# Check unique
				if num in unique_set:
					return False
				unique_set.add(num)

				row_sums[i] += num
				col_sums[j] += num
				if i == j:
					diag_sums[0] += num
				if i + j == 2:
					diag_sums[1] += num
		# Check row and col sums
		for i in range(3):
			if row_sums[i] != 15 or col_sums[i] != 15:
				return False
		# Check diagonals' sums
		if diag_sums[0] != 15 or diag_sums[1] != 15:
			return False

		return True



	def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])

		if m < 3 or n < 3:
			return 0

		res = 0

		for i in range(m - 2):
			for j in range(n - 2):
				if self._isMagicSquare(grid, i, j):
					res += 1

		return res





