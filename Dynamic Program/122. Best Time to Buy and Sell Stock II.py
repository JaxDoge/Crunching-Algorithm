122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	n = len(prices)
    	dp_i_0 = 0
    	dp_i_1 = float('-inf')

    	for i in range(n):
    		tmp = dp_i_0
    		dp_i_0 = max(dp_i_1+prices[i], dp_i_0)
    		dp_i_1 = max(dp_i_1, tmp - prices[i])

    	return dp_i_0