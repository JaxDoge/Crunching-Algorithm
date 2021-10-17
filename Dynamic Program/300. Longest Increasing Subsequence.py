300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    	length = len(nums)
    	dp = [1] * length

    	for i in range(1, length):
    		for j in range(i-1, -1, -1):
    			# 找出 i 以前的索引中最大的 dp[j] + 1, 同时 num[i] 大于 nums[j]
    			if nums[i] > nums[j]:
    				dp[i] = max(dp[i], dp[j] + 1)

    	return max(dp)


# 二分查找，patience sorting

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    	# 牌堆数组，元素代表堆顶的牌
    	top = []
    	# 牌堆个数
    	piles = 0

    	for n in nums:
    		# binary search for the left boundary
    		left = 0
    		right = piles - 1 # right index inside

    		# find left boundary
    		while left <= right:
    			mid = left+(right-left)//2
    			if top[mid] >= n:
    				right = mid - 1
    			elif top[mid] < n:
    				left = mid + 1

            if left == piles: # 左指针越界，新建牌堆
                piles += 1
                top.append(n)
            else:
                top[left] = n
    	return piles
