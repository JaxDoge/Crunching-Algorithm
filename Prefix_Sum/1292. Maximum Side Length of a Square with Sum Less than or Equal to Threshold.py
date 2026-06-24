1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# 2D presum question
# We need a presum_mat which presunm_mat[i][j] is the sum of the rectangle that top-left corner is mat[0][0], and right-botton corner is mat[i][j]
# The presum_mat can be constructed from lef to right and top to down
# Thus we can get any rec area sum in O(1)

# Note that similar to array presum, the presum list or matrix index represent `How many elements added up`, so it will larger than the original array (matrix) by 1

class Solution:
	def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
		m = len(mat)
		n = len(mat[0])

		# Construct the presum_mat
		presum_mat = [[0] * (n + 1) for _ in range(m + 1)]

		# Start construction from [1, 1]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				presum_mat[i][j] = mat[i - 1][j - 1] + presum_mat[i - 1][j] + presum_mat[i][j - 1] - presum_mat[i - 1][j - 1]

		# x2 > x1, y2 > y1
		def getRectSum(x1, y1, x2, y2):
			return presum_mat[x2][y2] - presum_mat[x1 - 1][y2] - presum_mat[x2][y1 - 1] + presum_mat[x1 - 1][y1 - 1]

		max_side, res = min(m, n), 0

		for i in range(1, m + 1):
			for j in range(1, n + 1):
				# The side loop can start from current res + 1 cause we don't care smaller side for a new corner point
				# if current side is too large, then we can break directly cause all number are positive (monotonicity)
				for side in range(res + 1, max_side + 1):
					if (
						i + side - 1 <= m and
						j + side - 1 <= n and
						getRectSum(i, j, i + side - 1, j + side -1) <= threshold
					):
						res += 1
					else:
						break

		return res
