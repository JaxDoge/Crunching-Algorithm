2571. Minimum Operations to Reduce an Integer to 0

# BFS
# n < 10^5 then i <= 17 (easy to prove)
# Thus we have at most 18 different step range

class Solution:
	def minOperations(self, n: int) -> int:
		max_value = 2**17
		max_steps = 18
		queue = deque()
		queue.append((0, 0))
		visited = {0}


		while queue:
			cur_idx, step = queue.popleft()
			# loop 17 steps
			for i in range(max_steps):
				# two direction
				for sign in [-1, 1]:
					cand_idx = cur_idx + sign * 2**i
					if 0 <= cand_idx <= max_value and cand_idx not in visited:
						if cand_idx == n:
							return step + 1
						queue.append((cand_idx, step + 1))
						visited.add(cand_idx)
					


		