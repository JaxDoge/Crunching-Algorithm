210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    	import collections

    	# Store the graph
    	graphC = collections.defaultdict(list)
    	# Store the search status 0 = untouched, 1 = in-search, 2 = searched
    	visited = [0] * numCourses
    	# result stack
    	study_plan = list()
    	# Cycle flag
    	valid_plan = True 

    	# Build the course graph
    	for ele in prerequisites:
    		graphC[ele[1]].append(ele[0])

    	# DFS function
    	def dfsTraverse(graph, v):

    		nonlocal valid_plan
    		visited[v] = 1
    		for ver in graph[v]:
    		    if visited[ver] == 2:
    			    continue
    			if visited[ver] == 1:
    				valid_plan = False
    				return
    			if visited[ver] == 0:
    				dfsTraverse(graph, ver)
    		# v is totally searched
    		visited[v] = 2
    		study_plan.append(v)
    		return

    	for course in range(numCourses):
    		# 只用遍历还没搜索过的 vertex
    		if not visited[course]:
    		    dfsTraverse(graphC, course)
    		# if there is a cycle, break the loop
    		if not valid_plan: return []

    	return study_plan[::-1]

