188. Best Time to Buy and Sell Stock IV

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
    	k_max = k
    	n = len(prices)
        if n == 0:
            return 0    	
    	dp = [[[0,0] for _ in range(k_max+1)] for _ in range(n)]  # k could be 0,1,2, and when k = 0, we got the base case
    	for i in range(n):
    		for k in range(1, k_max+1):
    			if i == 0:
    				dp[i][k][0] = 0
					dp[i][k][1] = -prices[i]
					continue
    			dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
    			dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
    	return dp[n-1][k][0]