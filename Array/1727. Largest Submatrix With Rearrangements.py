1727. Largest Submatrix With Rearrangements

# Very similar to regular maximum rectangle problem.
# Deal the matrix row by row
# O(M*N*log(N))
class Solution:
	def largestSubmatrix(self, matrix: List[List[int]]) -> int:
		m = len(matrix)
		n = len(matrix[0])
		ans = 0

		for row in range(m):
			for col in range(n):
				if matrix[row][col] and row > 0:
					matrix[row][col] += matrix[row - 1][col]

			# For a given i, we know the hieght of rectangle is h, and the width is equal to the number of other cells in this row with height >= h
			# Thus we need to sort this row so all index to the left has larger or equal heights.
			sort_row = sorted(matrix[row], reverse=True)
			for i in range(n):
				area = (i + 1) * sort_row[i]
				ans = max(ans, area)

		return ans



# Note that if previous row is sorted, we can construct this row that is also sorted without extra sort operation
# Because all column height can only 1. add one 2. ruled out because of 0
# Only special treatment is the new 1 in this row need to be append to the last

class Solution:
	def largestSubmatrix(self, matrix: List[List[int]]) -> int:
		m, n = len(matrix), len(matrix[0])

		# (height, column), descending by height
		prev = []
		ans = 0

		for r in range(m):
			curr = []
			# Need a flag to track if this cell starts a new run
			seen = [False] * n

			# Columns that already had positive height.
			# Their relative ordering stays unchanged.
			for height, col in prev:
				if matrix[r][col] == 1:
					curr.append((height + 1, col))
					seen[col] = True

			# Columns starting a new run of 1s have height = 1.
			# They can safely be appended at the end.
			for col in range(n):
				if matrix[r][col] == 1 and not seen[col]:
					curr.append((1, col))

			# curr is already sorted by descending height
			for width, (height, col) in enumerate(curr, 1):
				ans = max(ans, height * width)

			prev = curr

		return ans