370. Range Addition


# Partial difference array
class Difference:
	def __init__(self, nums):
		assert len(nums) > 0
        self.diff = []
        self.diff.append(nums[0])
		for i in range(1, len(nums)):
			self.diff.append(nums[i]-nums[i-1])

	def increment(self, i, j, val):
		self.diff[i] += val
		if j+1 < len(self.diff):
			self.diff[j+1] -= val

	def returnResult(self):
		res = [self.diff[0]]
		for i in range(1, len(self.diff)):
			res.append(res[i-1]+self.diff[i])
		return res




class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    	input_nums = [0]*length
    	df = Difference(input_nums)
    	for update in updates:
    		i = update[0]
    		j = update[1]
    		val = update[2]

    		df.increment(i,j,val)

    	return df.returnResult()