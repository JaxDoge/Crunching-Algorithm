LCP 09. 最小跳跃次数


# 建图 + bfs
# 由于题目数组最大可能是 10^6 长度，不能构图
# 优化时间复杂度，直接 bfs 是 n^2
# 由于我们是 BFS，一个位置只要被更新了，就一定不需要再次被更新。
# 所以，我们维护一个变量 preidx，表示当前 [1,preidx−1] 之间的所有位置都已经被更新过了。

# 超时解法
import collections
class Solution:
    def minJump(self, jump: List[int]) -> int:
        if not jump: return 0

        max_distance = len(jump)
        # Build graph
        
        visited = set()

        # 不应该建图，这样往前回溯和往后跳混在一起了，然而这两个过程是不一样的

        edge_graph = collections.defaultdict(list)
        for index in range(max_distance):
            edge_graph[index].extend(list(range(index)))
            edge_graph[index].append(jump[index]+index)

        jump_cnt = 1
        helper_queue = collections.deque([0])
        while helper_queue:
            sub_size = len(helper_queue)
            for _ in range(sub_size):
                pop_ind = helper_queue.popleft()
                visited.add(pop_ind)
                for next_one in edge_graph[pop_ind]:
                    # if jump out
                    if next_one >= max_distance:
                        return jump_cnt
                    if not next_one in visited:
                        helper_queue.append(next_one)
            jump_cnt += 1

        return jump_cnt




# BFS+ 优化
import collections
class Solution:
    def minJump(self, jump: List[int]) -> int:
        if not jump: return -1

        max_distance = len(jump)
        visited = set([0])
		# pre_far 以前的索引不需要在左跳阶段遍历了，以前的索引自身也不需要左跳过程
        pre_far = 1
        jump_path_queue = collections.deque()  # 记录到某个 index 最短跳跃次数
        jump_path_queue.append([0,0])
        # bfs 遍历 queue
        while jump_path_queue:
        	index, step = jump_path_queue.popleft()
        	right_index = index+jump[index]
        	if right_index >= max_distance:
        		return step+1
        	# 右跳阶段
        	if not right_index in visited:
        		jump_path_queue.append([right_index,step+1])
        		visited.add(right_index)

        	# 回溯阶段，利用 pre_far 缩短回溯范围
        	for ind in range(pre_far, index):
        		if not ind in visited:
        			jump_path_queue.append([ind, step+1])
        			visited.add(ind)
        	# 回溯完毕，更新 pre_far
        	pre_far = max(pre_far, index+1)
        return -1



# Dynamic Programming
# https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/solution/zui-xiao-tiao-yue-ci-shu-by-leetcode-solution/

class Solution:
    def minJump(self, jump: List[int]) -> int:
        res = n = len(jump)
        f = [n] * (n + 1)
        f[0] = 0
        max_dis = [0] * (n + 1) 
        w = 0
        for i in range(0,n):
            if i >= max_dis[w]:
                w += 1
            f[i] = min(f[i], w + 1)
            
            jump_tmp = i + jump[i]
            if jump_tmp >= n:
                res = min(res,f[i] + 1)
            else:
                f[jump_tmp] = min(f[jump_tmp],f[i]+1)
                max_dis[f[jump_tmp]] = max(max_dis[f[jump_tmp]],jump_tmp)
        return res

