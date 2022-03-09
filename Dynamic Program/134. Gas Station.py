134. Gas Station


# 图像法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    	n = len(gas)
    	start = 0
    	sum_ = 0
    	min_sum = 0

    	for i in range(n):
    		sum_ += gas[i] - cost[i]
    		if sum_ < min_sum:
    			min_sum = sum_
    			start = i + 1

    	if sum_ < 0:
    		return -1

    	return start % n
