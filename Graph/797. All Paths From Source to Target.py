797. All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    	res = list()
    	one_path = [0]

    	def findaPath(node):
    		if node == len(graph) - 1:
    			res.append(one_path)  # 这条路径已经抵达目标点  # 这里很奇怪，明明逻辑没问题，在leetcode 提交会导致[[0],[0]]，完全不合理啊
    		    return

    		for ele in graph[node]:
    			one_path.append(ele)
    			# dfs
    			findaPatho(ele)
    			# Complete ele search, pop it
    			one_path.pop()
    		return
    	findaPath(0)
    	return res