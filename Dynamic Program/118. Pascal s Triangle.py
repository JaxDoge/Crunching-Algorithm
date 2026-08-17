118. Pascal s Triangle

# Simulation + DP
# similar to pouring wine problem

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		tri = [[0] * col for col in range(1, numRows + 2)]
		tri[0][0] = 1

		# calculate next level based on this level
		for row in range(0, numRows):
			for col in range(row + 1):
				cur_val = tri[row][col]
				tri[row + 1][col] += cur_val
				tri[row + 1][col + 1] += cur_val

		return tri[:numRows]