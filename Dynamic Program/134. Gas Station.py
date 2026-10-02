134. Gas Station


# 图像法
# The key is that the accumulation function image is always the same. Change the start point will only change the origin position
# So our goal is to find a start point (origin) that keeyp the function always above the x-axis, if possible
# Which is the lowest point of the function, so the start point should be right next to it.
class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		n = len(gas)
		start = 0
		sum_ = 0
		min_sum = 0

		for i in range(n):
			sum_ += gas[i] - cost[i]
			if sum_ < min_sum:
				min_sum = sum_
				start = i + 1

		if sum_ < 0:
			return -1

		return start % n
