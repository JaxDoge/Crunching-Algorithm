305. Number of Islands II

# Union Find

class Solution:
	def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
		parent = {} # array or hashmap. Both OK
		size = {}
		count = 0
		res = []

		# 2d array code to 1d array
		def get_id(r, c):
			return r * n + c

		# find node parent
		def find(i: int):
			# path compression
			if i != parent[i]:
				parent[i] = find(parent[i])

			return parent[i]

		# balanced union (small tree append to big one)
		def union(i, j) -> bool:
			root_i = find(i)
			root_j = find(j)

			if root_i == root_j:
				# Already union, do nothing
				return False

			if size[i] < size[j]:
				root_i, root_j = root_j, root_i

			parent[root_j] = root_i
			size[root_i] += size[root_j]

			return True


		directions = [(1,0), (0,1), (-1,0), (0,-1)]

		for r, c in positions:
			curr = get_id(r, c)

			# if curr is already an island
			if curr in parent:
				res.append(count)
				continue

			# Firstly, build an independent island
			parent[curr] = curr
			size[curr] = 1
			count += 1

			# Start merging. Try each direction and decrease the count for each success merge
			for d in directions:
				nr, nc = r + d[0], c + d[1]

				# Check inbound
				if 0 <= nr < m and 0 <= nc < n:
					# if this neighbor is an island
					if get_id(nr, nc) in parent:
						if union(curr, get_id(nr, nc)):
							count -= 1

			res.append(count)

		return res









