3418. Maximum Amount of Money Robot Can Earn

# DFS
# Update res to find the maximum profit
# Track the minimum two negative cells
# TLE. PUUUUUUr
class Solution:
	def maximumAmount(self, coins: List[List[int]]) -> int:
		m = len(coins)
		n = len(coins[0])
		res = float('-inf')

		def dfs(row, col, sub_sum, min_1, min_2):
			nonlocal res
			# Processing current cell
			val = coins[row][col]
			sub_sum += val

			if val < 0:
				if val < min_2:
					min_1 = min_2
					min_2 = val
				elif val < min_1:
					min_1 = val

			# Base case
			if row == m - 1 and col == n - 1:
				if min_2 < 0:
					sub_sum += -min_2
				if min_1 < 0:
					sub_sum += -min_1

				res = max(res, sub_sum)
				return

			# Choose branches
			for nrow, ncol in [[row + 1, col], [row, col + 1]]:
				if nrow >= m or ncol >= n:
					continue
				dfs(nrow, ncol, sub_sum, min_1, min_2)

			return

		dfs(0, 0, 0, 0, 0)
		return res


# DP
# Buttom up

class Solution:
	def maximumAmount(self, coins: List[List[int]]) -> int:
		m, n = len(coins), len(coins[0])
		NEG_INF = float('-inf')

		# dp[i][j][k]:
		# max profit reaching (i, j) using exactly k neutralizations
		dp = [
			[[NEG_INF] * 3 for _ in range(n)]
			for _ in range(m)
		]

		for i in range(m):
			for j in range(n):
				val = coins[i][j]

				# Special initialization for (0, 0)
				if i == 0 and j == 0:
					dp[i][j][0] = val

					if val < 0:
						dp[i][j][1] = 0

					continue

				for k in range(3):
					# Best profit before entering current cell
					prev = NEG_INF

					# Option 1: don't neutralize current cell
					if i > 0:
						prev = max(prev, dp[i - 1][j][k])

					if j > 0:
						prev = max(prev, dp[i][j - 1][k])

					
					dp[i][j][k] = prev + val

					# Option 2: neutralize current robber
					# So the previous status must be k - 1
					if val < 0 and k > 0:
						prev_neutralize = NEG_INF

						if i > 0:
							prev_neutralize = max(
								prev_neutralize,
								dp[i - 1][j][k - 1]
							)

						if j > 0:
							prev_neutralize = max(
								prev_neutralize,
								dp[i][j - 1][k - 1]
							)

						dp[i][j][k] = max(
							dp[i][j][k],
							prev_neutralize
						)

		return max(dp[m - 1][n - 1])