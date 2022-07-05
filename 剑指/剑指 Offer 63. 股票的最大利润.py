剑指 Offer 63. 股票的最大利润


# Classic Dynamic Programming Queation
# Note that the limitation of transaction time is one (k = 1)
# so the dimension k could be removed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0        
        dp = [[0, 0] for _ in range(n)]
        # base case
        dp[0][0] = 0
        dp[0][1] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], - prices[i])

        return dp[n-1][0]


