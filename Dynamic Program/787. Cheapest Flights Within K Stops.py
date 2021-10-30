787. Cheapest Flights Within K Stops


# dp table
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    	# the largest edge number the path takes is k + 1
    	k = k+1

    	# dp[i][j] 的含义：恰好搭乘 i 次航班，从 src 到达 j city 的最小花费
    	dp = [[float('inf')]*n for _ in range(k+1)]
    	# base case
    	dp[0][src] = 0

    	for row in range(1, k+1):
    		for from_, col, cost in flights:
    			dp[row][col] = min(dp[row][col], dp[row-1][from_]+cost)

    	res = min([dp[row][dst] for row in range(1, k+1)])
    	return res


# DFS

class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
		k = k+1

		from collections import defaultdict
		indegree_hashmap = defaultdict(list)
		for ele in flights:
			from_ = ele[0]
			to_ = ele[1]
			price_ = ele[2]
			indegree_hashmap[to_].extend([from_, price_])

		memo = [[-2]*n for _ in range(k+1)]

		def dp(k, j):   # k 次航班内从 src 到达 j city 最小花费
			nonlocal src, dst, indegree_hashmap
			if j == src:  # 
				return 0
			if k <= 0:
				return- -1  # 不可能的路线
			if memo[k][j] != -2:
				return memo[k][j]

			res = float('inf')
			# if there is last destination of j city
			if j in indegree_hashmap:
				for route in indegree_hashmap[j]:					
					sub_problem = dp(k-1, route[0])
					if sub_problem != -1:
						res = min(res, sub_problem+route[1])

			memo[k][j] = res if res != float('inf') else -1
			return memo[k][j]

		return dp(k, dst)
