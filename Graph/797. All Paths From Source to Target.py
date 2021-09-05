797. All Paths From Source to Target

# DAG

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    	res = list()
    	one_path = [0]
        # 之所以这个题目没有 visited 数组，纯粹是因为这题的要求是寻找路径，而不是遍历图，所以即便是重复访问的 vertex，也是属于不同的 path，不需要 return 而是继续递归
    	def findaPath(node):
    		if node == len(graph) - 1:
    			res.append(one_path)  
    			# 这条路径已经抵达目标点  # 这里很奇怪，明明逻辑没问题，在leetcode 提交会导致[[0],[0]]，完全不合理啊
    		    # 这是因为直接 append 是追加了 one_path reference 在res里面，而不是一个新的变量地址，后续对 one_path 的修改会影响 res 中已添加的结果
    		    # [:]可以copy生成新的列表存入
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