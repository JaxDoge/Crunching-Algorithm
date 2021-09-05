207. Course Schedule


# Determining whether there is a cycle, or is a DAG
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if numCourses == 0: return True
        
        # Build a course graph
        courseG = []
        for vertex in range(numCourses):
        	courseG.append([])

        for ele in prerequisites:
        	from_v = ele[1]
        	to_v = ele[0]
        	courseG[from_v].append(to_v)

        visited = [False for _ in range(numCourses)] # 记录遍历过的顶点，防止重复，不能用来判断是否成环，因为所有遍历路线共享同一组记录
        one_path = [False for _ in range(numCourses)]  # 记录当次遍历经过的节点
        res = True

        # 从 ver 节点出发的深度遍历
        def dfsTraverse(graph: List[List[int]], ver: int):
            nonlocal res
        	if one_path[ver]:  # 本次遍历已经访问过，出现环，结束递归
        	    res = False
        	    return
        	if visited[ver]:  # 该节点已经访问过，直接return
        	    return

        	one_path[ver] = True
        	visited[ver] = True
        	for next_v in graph[ver]:
        		dfsTraverse(graph, next_v)

            # 离开顶点 ver
            one_path[ver] = False
            return 
         
        # 图可能不联通, 因此每个点都要额外遍历一次
        for vertex in range(numCourses):
            dfsTraverse(courseG, vertex)

        return res

        	


