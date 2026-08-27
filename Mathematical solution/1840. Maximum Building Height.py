1840. Maximum Building Height


# Because n is quite large, we cannot compute the hight limit of each building
# Note that if we know the building i and building j are explictly restricted in the list, and there is no other building in-between also be explictly restricted
# Then we have (best(i,j) − limit_i) + (best(i,j) − limit_j) ≤ j−i. That's how we find the largest limitation.

class Solution:
	def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
		restrictions.append([1, 0])
		restrictions.sort(key = itemgetter(0))

		if restrictions[-1][0] != n:
			restrictions.append([n, n-1])

		m = len(restrictions)

		# Note any explict restriction will impact rest buildings
		# The height of building i−1 cannot exceed hi+1.
		# The height of building i+1 cannot exceed hi+1.
		# The height of building j cannot exceed hi+∣i−j∣
		# So we need to propagade each restriction to others

		# From left to right. Check if need a tighter limitation
		for i in range(1, m):
			restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]))

		# From right to left
		for i in range(m - 2, -1, -1):
			restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]))


		res = 0
		for i in range(m - 1):
			best = ((restrictions[i + 1][0] - restrictions[i][0]) + restrictions[i + 1][1] + restrictions[i][1]) // 2
			res = max(res, best)

		return res

														