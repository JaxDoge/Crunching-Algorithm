518. Coin Change 2


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    	length = len(coins)

    	dp = [[0 for _ in range(amount+1)] for _ in range(length+1)]

    	# base case
    	for row in range(length+1):
    		dp[row][0] = 1

    	for row in range(1, length+1):
    		for col in range(1, amount+1):
    			if col < coins[row-1]:
    				dp[row][col] = dp[row-1][col]
    			else:
    				dp[row][col] = dp[row-1][col] + dp[row][col-coins[row-1]]
    	return dp[-1][-1]



# compress dp table
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    	length = len(coins)

    	dp = [0 for _ in range(amount+1)]
    	# base case
    	dp[0] = 1

    	for row in range(1, length+1):
    		for col in range(1, amount+1):
    			if col < coins[row-1]:
    				continue
    			else:
    				dp[col] = dp[col] + dp[col - coins[row-1]]
    	return dp[-1]
