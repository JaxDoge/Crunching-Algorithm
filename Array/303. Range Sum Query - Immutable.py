303. Range Sum Query - Immutable


class NumArray:

    def __init__(self, nums: List[int]):
    	self.presum = [0] * (len(nums)+1)
    	for i in range(1, len(self.presum)):
    		self.presum[i] = self.presum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
    	return self.presum[right+1] - self.presum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)