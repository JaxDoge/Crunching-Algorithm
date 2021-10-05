1011. Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    	def finishDay(capacity):
    		nonlocal weights
    		finish = 0
    		load = 0

    		# 注意最后一趟运输时间是没有在这个循环里加入的
    		for ele in weights:
    			if load+ele > capacity:
    				finish += 1
    				load = 0
    				load += ele  # 别忘了也要上船
    			else:
    				load += ele

    		return finish+1

    	left = max(weights)
    	right = sum(weights)

    	while left <= right:
    		mid = left+(right-left)//2
    		if finishDay(mid) <= days:
    			right = mid - 1
    		elif finishDay(mid) > days:
    			left = mid + 1

    	return left 




