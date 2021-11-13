651. 4 Keys Keyboard


class Solution:
    def maxA(self, n: int) -> int:
    	# base case is n = 0
    	dp = [0]*(n+1)
    	for i in range(1:n+1):
    		dp[i] = dp[i-1]+1   # press 'A'
    		# OR press Ctrl+V, search all possible Ctrl+A
    		for j in range(2:i):
    			# select all and copy dp[j-2]
    			# paste dp[j-2] i-j times, the final result is dp[j-2]* (i-j+1)
    			dp[i] = max(dp[i], dp[j-2]*(i-j+1))
    	return dp[n]