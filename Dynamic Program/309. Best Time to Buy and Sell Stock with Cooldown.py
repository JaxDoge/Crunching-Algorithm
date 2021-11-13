309. Best Time to Buy and Sell Stock with Cooldown


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	n = len(prices)
    	d_i_0 = 0
    	d_i_1 = float('-inf')
    	d_i_pre = 0

    	for i in range(n):
    		tmp = d_i_0
    		d_i_0 = max(d_i_0, d_i_1+prices[i])
    		d_i_1 = max(d_i_1, d_i_pre-prices[i])
    		d_i_pre = tmp

    	return d_i_0