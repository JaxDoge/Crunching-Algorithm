LCP 07. 传递信息


# Bfs, 长度为K的路线多少条停留在了 n-1 上
import collections
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
    	# 构建图
    	relation_graph = collections.defaultdict(list)
    	for rela in relation:
    		src = rela[0]
    		dst = rela[1]
    		relation_graph[src].append(dst)

    	step = 0
    	helper_queue = collections.deque([0])
    	while helper_queue and step < k:
    		sub_size = len(helper_queue)
    		for _ in range(sub_size):
    			search_vector = helper_queue.popleft()
    			for next_vector in relation_graph[search_vector]:
    				helper_queue.append(next_vector)
    		step += 1

    	res = 0
    	if step == k:
    		while helper_queue:
    			if helper_queue.pop() == n-1:
    				res+=1
    	return res


