486. Predict the Winner

# Recursive
# The maxDiff represent the biggest difference of player who make the first pick can make, within the given range [left, right]
# initially the player 1 move first so the first maxDiff represent the larggest gap player one can make from palyer 2, range is [0, n-1]
class Solution:
	def predictTheWinner(self, nums: List[int]) -> bool:
		n = len(nums)

		def maxDiff(left, right):
			# base case, only one number left to choose
			if left == right:
				return nums[left]

			# if this player pick left number, this is the gap he can get
			pick_left = nums[left] - maxDiff(left + 1, right)
			pick_right = nums[right] - maxDiff(left, right - 1)

			return max(pick_left, pick_right)

		return maxDiff(0, n - 1) >= 0
	

# DP bottom-up
class Solution:
	def predictTheWinner(self, nums: List[int]) -> bool:
		n = len(nums)
		dp = [[0] * n for _ in range(n)]

		for i in range(n):
			dp[i][i] = nums[i]

		for diff in range(1, n):
			for left in range(n - diff):
				right = left + diff

				pick_left = nums[left] - dp[left + 1][right]
				pick_right = nums[right] - dp[left][right - 1]
				dp[left][right] = max(pick_left, pick_right)

		return dp[0][n - 1] >= 0