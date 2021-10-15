322. Coin Change

# 备忘录递归
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    	import collections
    	memo = collections.defaultdict(int)

    	def dp(amount):
    		nonlocal coins, memo
    		if amount == 0:
    			return 0
    		# 负数无解
    		if amount < 0:
    			return -1
    		if amount in memo:
    			return memo[amount]

    		res = float('inf')
    		for coin in coins:
    			sub_problem = dp(amount-coin)
    			if sub_problem == -1:
    				continue
    			res = min(res, sub_problem+1)
    		# 穷举完所有子问题都无解的情况
    		if res == float('inf'):
    			memo[amount] = -1
    		else:
    			memo[amount] = res
    		
    		return memo[amount]

    	return dp(amount)


# dp 状态转移数组，自底向上
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    	# 由于有 base case amount=0，所以数组长度是 amount +1
    	# 由于硬币取值不可能超过 amount 所以 amount + 1 是最小上界
    	dp = [amount+1] * (amount+1)
    	# base case
    	dp[0] = 0

    	for index in range(amount+1):
    		for coin in coins:
    			if index - coin < 0:
    				continue
    			dp[index] = min(dp[index], dp[index-coin]+1)
    	if dp[-1] == amount+1:
    		return -1  # 无解
    	return dp[-1]
