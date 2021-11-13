213. House Robber II


class Solution:
    def rob(self, nums: List[int]) -> int:
    	n = len(nums)
    	# bad case, considering n-2
    	if n <= 2:
    		return max(nums)
    	dp_1 = [0] * (n+1)  # 0 to n-2
    	dp_2 = [0] * (n+1)  # 1 to n-1

    	for i in range(n-2,-1,-1):
    		dp_1[i] = max(dp_1[i+1], nums[i]+dp_1[i+2])
    		dp_2[i] = max(dp_2[i+1], nums[i+1]+dp_2[i+2])
    	return max(dp_1[0], dp_2[0])

