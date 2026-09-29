120. Triangle


# Bottom up DP
class Solution:
	def minimumTotal(self, triangle: list[list[int]]) -> int:
		m = len(triangle)
		buttom_up_sum = triangle[-1]
		if m == 1:
			return buttom_up_sum[0]

		for i in range(m - 2, -1, -1):
			next_sum = []
			for j in range(i + 1):
				tmp = min(triangle[i][j] + buttom_up_sum[j], triangle[i][j] + buttom_up_sum[j + 1])
				next_sum.append(tmp)
			buttom_up_sum = next_sum
		
		return buttom_up_sum[0]