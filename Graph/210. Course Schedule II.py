210. Course Schedule II

# topological sort 拓扑排序
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


# 拓扑排序，广度搜索优先
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        import collections

        # Store the graph
        graphC = collections.defaultdict(list)
        # Store the in-degree of every node
        in_degree_list = [0] * numCourses
        # Store the result
        study_plan = list()

        # Build the graph and initial the in-degree
        for ele in prerequisites:
            graphC[ele[1]].append(ele[0])
            in_degree_list[ele[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        helper_queue = collections.deque()
        for i in range(numCourses):
            if in_degree_list[i] == 0:
                helper_queue.append(i)

        while helper_queue:
            # 取出队首节点，放入答案列表中
            pre_course = helper_queue.popleft()
            study_plan.append(pre_course)
            # 所有相邻节点入读 -1
            for next_c in graphC[pre_course]:
                in_degree_list[next_c] -= 1
                if in_degree_list[next_c] == 0:
                    # 该课程可以选修了
                    helper_queue.append(next_c)

        # 有环存在的情况下，会有若干节点入度永远不为0
        if len(study_plan) != numCourses:
            return []

        return study_plan


