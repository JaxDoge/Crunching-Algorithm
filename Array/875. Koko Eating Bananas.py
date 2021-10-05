875. Koko Eating Bananas


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    	import math
    	# 确定 x, f(x), target 分别是什么，并写出函数 f 的代码。
    	def finishHour(speed):
    		nonlocal piles
    		finish = 0
    		for pile in piles:
    			time = math.ceil(pile/speed)
    			finish += time
    		return finish

    	# 找到 x 的取值范围作为二分搜索的搜索区间，初始化 left 和 right 变量。
    	# 根据题意，speed 没有必要超过最大堆香蕉的数量
    	# 根据题目限制，一堆香蕉最大 10^9 个
    	left = 1
    	right = 10**9

    	# 注意 finishHour 是单调减函数
    	while left <= right:
    		mid = (left+right)//2
    		if finishHour(mid) > h:
    			left = mid+1
    		elif finishHour(mid) <= h:
    			right = mid - 1

    	return left

