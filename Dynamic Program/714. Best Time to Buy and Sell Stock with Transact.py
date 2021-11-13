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