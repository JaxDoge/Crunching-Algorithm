279. Perfect Squares


# BFS，减去某个完全平方数类似开始遍历某个方向，求最短路线
import collections
class Solution:
    def numSquares(self, n: int) -> int:
    	# 所有候选完全平方树，倒序排列，因为考虑 queue 出数顺序，先出较小的left数提效
    	perfectS = [i**2 for i in range(int(n**0.5),0,-1)]
    	# Hashmap 快速判断差是否已经是完全平方数
    	perfectS_set = set(perfectS)
    	# bfs queue
    	helper_queue = collections.deque([n])
    	# distance dict
    	distance = {n:1}

    	while helper_queue:
    		popval = helper_queue.popleft()
    		# 如果已经是完全平方数，返回路线长度
    		if popval in perfectS_set:
    			return distance[popval]

    		for ps in perfectS:
    			# 如果差已经存在于 distance 中，那这条路线就没意义了，因为之前的路线肯定不差于这条路线（局部起点相同没必要算两条线路）
    			if popval-ps > 0 and popval-ps not in distance:
    				helper_queue.append(popval-ps)
    				distance[popval-ps] = distance[popval]+1

    	return 0