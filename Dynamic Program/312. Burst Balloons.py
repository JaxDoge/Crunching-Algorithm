312. Burst Balloons

# 从戳气球改为放气球, dfs + lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
    	# according to the problem description, introduce new list nums_dummy with two addtional dummy ballons
    	nums_dummy = [1] + nums + [1]

    	# 填满开区间 (left, right) 得到的最大分数
    	@lru_cache(None)
    	def dp(left, right):
    		if left >= right - 1:
    			# 已经填满
    			return 0

    		ans = 0
    		for i in range(left+1, right):
    			ans = max((nums_dummy[left]*nums_dummy[i]*nums_dummy[right]+dp(i,right)+dp(left,i)), ans)
    		return ans

    	return dp(0, len(nums_dummy)-1)
