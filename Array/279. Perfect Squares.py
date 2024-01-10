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



# Dynamic Programming
class Solution2:
    def numSquares(self, n: int) -> int:
        perfect_max = int(n ** 0.5)
        dp_table = [[0] * (n + 1) for _ in range(perfect_max + 1)]

        for j in range(1, n + 1):
            dp_table[1][j] = j

        for i in range(2, perfect_max + 1):
            for j in range(1, n + 1):
                square_num = i**2
                max_choice = j // square_num
                dp_table[i][j] = dp_table[i - 1][j]

                for x in range(1, max_choice + 1):
                    dp_table[i][j] = min(dp_table[i][j], dp_table[i - 1][j - square_num * x] + x)

        return dp_table[perfect_max][n]