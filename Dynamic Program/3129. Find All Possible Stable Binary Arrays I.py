3129. Find All Possible Stable Binary Arrays I
3130. Find All Possible Stable Binary Arrays II



# Can't believe this one is just a midium
# Dynamic Programming
# Note that the `limit` means: there is no subarray with limit + 1 consecutive 1s or 0s
# Check the solution for DP transit equation
# The most important idea is that how to subtract the number of illegit schema while calculating the new state

class Solution:
	def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
		mod = 10**9 + 7
		dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

		# Initial base cases
		for i in range(1, min(zero, limit) + 1):
			dp[i][0][0] = 1
		for j in range(1, min(one, limit) + 1):
			dp[0][j][1] = 1

		for i in range(1, zero + 1):
			for j in range(1, one + 1):
				# calculate 0 ending schemas
				# if i > limit, we need to subtract the invalid schema number
				if i > limit:
					dp[i][j][0] = dp[i - 1][j][1] + dp[i - 1][j][0] - dp[i - 1 - limit][j][1]
				else:
					dp[i][j][0] = dp[i - 1][j][1] + dp[i - 1][j][0]
				# mod the result then store
				dp[i][j][0] = dp[i][j][0] % mod

				# Similar for 1 ending schemas
				if j > limit:
					dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0] - dp[i][j - 1 - limit][0]
				else:
					dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0]
				dp[i][j][1] = dp[i][j][1] % mod

		return (dp[zero][one][0] + dp[zero][one][1]) % mod