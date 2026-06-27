3721. Longest Balanced Subarray II

# This one derive from basic update value
class LazyTag:
	def __init__(self):
		self.to_add = 0
	def add(self, other: LazyTag):
		self.to_add += other.to_add
	def has_tag(self):
		return self.to_add != 0
	def clear(self):
		self.to_add = 0

# This one derive from basic segment critical value (like sum)
# Combined with basic lazy array
class SegmentTreeNode:
	def __init__(self):
		self.min_value = 0
		self.max_value = 0
		self.lazy_tag = LazyTag()



class SegmentTree:
	def __init__(self, data):
		self.n = len(data)
		self.tree = [SegmentTreeNode() for _ in range(4 * self.n + 1)]
		self._build(data, 1, self.n, 1)

	def _push_up(self, i):
		self.tree[i].min_value = min(
			self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
			)
		self.tree[i].max_value = max(
			self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
			)

	def _build(self, data, l, r, i):
		# base case: the leaf node value is equal to data[l -1]
		if l == r:
			self.tree[i].min_value = data[l - 1]
			self.tree[i].max_value = data[l - 1]
			return
		# Otherwise, bisect the range
		mid = l + ((r - l) >> 1)
		self._build(data, l, mid, i << 1)
		self._build(data, mid + 1, r, (i << 1) | 1)

		# Children nodes are built, now merge to this parent node
		self._push_up(i)

	def _apply_lazytag(self, tag, i):
		self.tree[i].min_value += tag.to_add
		self.tree[i].max_value += tag.to_add
		self.tree[i].lazy_tag.add(tag)

	def _pushdown(self, i):
		if self.tree[i].lazy_tag.has_tag():
			tag = self.tree[i].lazy_tag

			self._apply_lazytag(tag, i << 1)
			self._apply_lazytag(tag, (i << 1) | 1)
			self.tree[i].lazy_tag.clear()


	def _update(self, tag: LazyTag, tl, tr, l, r, i):
		# base case, the node range is encompassed by the target range
		# Update the min, max and lazy tag
		if tl <= l and r <= tr:
			self._apply_lazytag(tag, i)
			return

		# Otherwise we need to update the child nodes first
		# Check if there is previous lazy tag already in the parent node, push it to children
		self._pushdown(i)

		mid = l + ((r - l) >> 1)
		# update left child if needed
		if tl <= mid:
			self._update(tag, tl, tr, l, mid, i << 1)
		# update right child if needed
		if mid + 1 <= tr:
			self._update(tag, tl, tr, mid + 1, r, (i << 1) | 1)

		# For now at least one child is update, we need to push up the update to parent noded
		self._push_up(i)

	# Given a range, find the rightmost `value` position
	def _find(self, val, tl, tr, l, r, i):
		# base case 1, value is not in the range
		if val < self.tree[i].min_value or self.tree[i].max_value < val:
			return -1

		# base case 2, find the value
		if l == r:
			return l

		# not leaf node, search child nodes
		self._pushdown(i)

		mid = l + ((r - l) >> 1)
		# we need rightmost position, so start from right child, return if found
		# search range overlap with right child
		if mid + 1 <= tr and r >= tl:
			res = self._find(val, tl, tr, mid + 1, r, (i << 1) | 1)
			if res != -1:
				return res

		# else check left child
		if l <= tr and mid >= tl:
			return self._find(val, tl, tr, l, mid, i << 1)

		# Only for defensive, shouldn't be touched
		return -1

	def add(self, val, tl, tr):
		tag = LazyTag()
		tag.to_add = val
		if tl <= tr:
			self._update(tag, tl, tr, 1, self.n, 1)

    # Find the rightmost val position in range [start, n]
	def find_last(self, start, val):
		if start > self.n:
			return -1
		return self._find(val, start, self.n, 1, self.n, 1)



class Solution:
	def longestBalanced(self, nums: List[int]) -> int:

		n = len(nums)

		# Need a dict to record the occurrence position of each number
		occur_map = defaultdict(deque)
		res = 0

		def sign(x):
			return 1 if x % 2 == 0 else -1

		pre_sum = [0] * n
		# Initial first element in presum array and occurrence map
		pre_sum[0] = sign(nums[0])
		occur_map[nums[0]].append(1)

		for i in range(1, n):
			pre_sum[i] = pre_sum[i - 1]

			occ = occur_map[nums[i]]
			# if the number never appear before
			if not occ:
				pre_sum[i] += sign(nums[i])

			occ.append(i + 1)

		# build the tree
		seg_tree = SegmentTree(pre_sum)

		# Search the rightmost zero presum for each given left start point
		# Note we can pruning the start point since we are looking for the longest subarray
		for i in range(n):
			# the .find_last() return the outbound end position, which gives us presum[i, j) == 0, so j - i is the length
			res = max(res, seg_tree.find_last(i + res, 0) - i)

			occur_map[nums[i]].popleft()
			if occur_map[nums[i]]:
				next_pos = occur_map[nums[i]][0]
			else:
				next_pos = n + 1

			# move out the nums[i] will affect the presum range [i + 1, next nums[i] position - 1]
			# Or [i + 1, n]
			seg_tree.add(-sign(nums[i]), i + 1, next_pos - 1)

		return res






