494. Target Sum


# 时间复杂度 O(2^n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    	length = len(nums)
    	if length == 0:
    		return 0
    	result = 0
    	def backtrack(index, rest):
    		nonlocal nums, length, result
    		# base case
    		if index == length:
				if rest == 0:
    				result += 1
    			return

    		# ADD minus before nums[index]
    		rest += nums[index]
    		backtrack(index+1, rest)
    		rest -= nums[index]

    		# Add plus before nums[index]
    		rest -= nums[index]
    		backtrack(index+1, rest)
    		rest += nums[index]
    	backtrack(0, target)
    	return result

# 增加 memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        result = 0
        memo = dict()
        def backtrack(index, rest):
            nonlocal nums, length, result
            # base case
            if index == length:
                if rest == 0:
                    return 1
                return 0
            key = (index, rest)
            if key in memo:
                return memo[key]
            result = backtrack(index+1, rest+nums[index]) + backtrack(index+1, rest-nums[index])
            memo[key] = result
            return result

        backtrack(0, target)
        return result


# 动态规划
# sum(A) - sum(B) = target
# sum(A) = target + sum(B)
# sum(A) + sum(A) = target + sum(B) + sum(A)
# 2 * sum(A) = target + sum(nums)
# sum(A) = (target + sum(nums)) / 2
# 问题变为有 sum 多少种组合 A 满足上式，背包问题

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = 0
        for n in nums:
            total_sum += n
        # bad cases
        if (target > total_sum or (target+total_sum) % 2 != 0 or target < -total_sum):
            return 0

        def allSubsetA(sums):
            nonlocal nums
            length = len(nums)
            # dp 表的行数表示 前 i 个物品, 列数表示目标重量是 j，因此索引要多加一
            dp = [[0 for _ in range(sums+1)] for _ in range(length+1)]
            # 如果没有目标重量，没有物品，则组合方法只有一个，A 为空集
            dp[0][0] = 1

            # 遍历更新‘内表’
            for i in range(1, length+1):
                for j in range(0, sums+1):
                    # 如果 j 容量的背包能装下第 i 个物品, 注意对应 nums 索引是 i-1
                    if j >= nums[i-1]:
                        dp[i][j] = dp[i-1][j]+dp[i-1][j-nums[i-1]]
                    else: #没有空间，只能不装 i
                        dp[i][j] = dp[i-1][j]
            return dp[length][sums]
        return allSubsetA(int((target+total_sum)/2))
