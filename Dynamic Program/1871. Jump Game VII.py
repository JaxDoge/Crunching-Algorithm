1871. Jump Game VII

# DP + Prefix sum
# The current dp[i] depends on the state of s[i] and dp[i - maxJump] ... dp[i - minJump]
# We need the presum to determine for a given range in the dp array, if there is any True in O(1) time
class Solution:
	def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
		n = len(s)

		# construct the prefix sum array
		# Note the first minJump dp presum need to be precomputed
		presum = [0] * n
		for i in range(minJump):
			presum[i] = 1

		# first minJump state is base case
		dp = [0] * n
		dp[0] = 1
		
		# We start from minJump.
		for i in range(minJump, n):
			left = i - maxJump
			right = i - minJump
			if s[i] == '0':
				total_sum = presum[right] - (0 if left <= 0 else presum[left - 1])
				dp[i] = int(total_sum > 0)
			# Update presum on fly
			presum[i] = presum[i - 1] + dp[i]

		return bool(dp[-1])





