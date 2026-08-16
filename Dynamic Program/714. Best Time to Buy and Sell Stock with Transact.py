714. Best Time to Buy and Sell Stock with Transaction Fee


class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		n = len(prices)
		dp_i_0 = 0
		dp_i_1 = float('-inf')
		for i in range(n):
			tmp = dp_i_0
			dp_i_0 = max(dp_i_0, dp_i_1+price[i])
			dp_i_1 = max(dp_i_1, dp_i_0-price[i]-fee)

		return dp_i_0


class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		n = len(prices)
		hold_dp = [0] * n
		free_dp = [0] * n

		hold_dp[0] = -prices[0]

		for i in range(1, n):
			hold_dp[i] = max(hold_dp[i-1], free_dp[i-1]-prices[i])
			free_dp[i] = max(free_dp[i-1], hold_dp[i-1]+prices[i]-fee)

		return free_dp[-1]