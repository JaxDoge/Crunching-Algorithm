3510. Minimum Pair Removal to Sort Array II


# Use heapq to find the min_sum_pair entry
# Note the variants for a piar [i,j]:
# 1. The value of val[i] become the sum
# 2. The index j is dead
# 3. Two new sums pair [i-1, i] and [i, j-1]. If they exist (stale sum problem)
# 4. The index relative position. i and j-1 (if exists) are adjacent

class Solution:
	def _isDescPair(self, i, j, val: List) -> int:
		if i == -1 or j == -1:
			return 0
		return 1 if val[i] > val[j] else 0


	def minimumPairRemoval(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1:
			return 0

		# Don't change nums directly
		val = nums[:]

		# Use two extra lists to help us find the current previous and next index of a given i
		# -1 represent not exist
		prev = [i - 1 for i in range(n)]
		nxt = [i + 1 for i in range(n)]
		nxt[-1] = -1

		# Record if an index is still alive (not been merged)
		alive = [True] * n

		# Record current decrease count
		desc_cnt = 0

		res = 0

		# initial decrease count
		for i in range(n - 1):
			if nums[i + 1] < nums[i]:
				desc_cnt += 1

		# Read the min heap
		# The heap entry is (pair_sum, original_i)
		# Note we need the leftmost minimum pair sum
		heap = []
		for i in range(n - 1):
			heap.append((nums[i] + nums[i + 1], i))
			
		heapq.heapify(heap)

		while desc_cnt > 0:
			# Find current min pair sum entry
			while True:
				pair_sum, i = heapq.heappop(heap)

				# Check if i is dead
				if not alive[i]:
					continue

				j = nxt[i]
				# Check if j is dead if i has j
				if j == -1 or not alive[j]:
					continue

				# Check if the pair sum is staled
				if val[i] + val[j] != pair_sum:
					continue

				break

			# Start merging.
			# The neighbors may be affected
			left = prev[i]
			right = nxt[j]

			# Remove current decrease count contribution in [left, i, j, right]. Will add new count later
			desc_cnt -= self._isDescPair(left, i, val)
			desc_cnt -= self._isDescPair(i, j, val)			
			desc_cnt -= self._isDescPair(j, right, val)

			# val[i] store the merged sum
			val[i] += val[j]
			alive[j] = False

			# The next index of i will be changed
			nxt[i] = right
			if right != -1:
				prev[right] = i

			# Add back the decrease count contribution
			desc_cnt += self._isDescPair(left, i, val)
			desc_cnt += self._isDescPair(i, right, val)			

			# Push back two new pair sum entries (if there is)
			if left != -1:
				heapq.heappush(heap, (val[left] + val[i], left))
			if right != -1:
				heapq.heappush(heap, (val[i] + val[right], i))

			# Operation + 1
			res += 1

		return res




















