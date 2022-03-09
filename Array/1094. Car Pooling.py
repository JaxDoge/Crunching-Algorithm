1094. Car Pooling


class Difference:
    def __init__(self, nums):
        n = len(nums)
        self.diff = []
        self.diff.append(nums[0])
        for i in range(1, n):
            self.diff.append(nums[i]-nums[i-1])

    def increment(self, i, j, val):
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val

    def returnOrigin(self):
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res.append(res[i-1]+self.diff[i])
        return res


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    	input_nums = [0] * 1001
    	df = Difference(input_nums)

    	for trip in trips:
    		numpassengers = trip[0]
    		i = trip[1]
    		j = trip[2] - 1  # the passengers are dropped off in stop j, so the increment interval is [i, j)
    		df.increment(i, j, numpassengers)

    	res = df.returnOrigin()

    	if max(res) > capacity:
    		return False
    	return True
