121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	length = len(prices)
    	dp = [[0,0] for _ in range(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
    	for i in range(1,length):
    		dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    		dp[i][1] = max(dp[i-1][1], -prices[i])
    	return dp[n-1][0]

