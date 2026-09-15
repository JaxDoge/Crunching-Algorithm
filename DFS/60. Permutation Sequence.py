60. Permutation Sequence


#  Decomposition the original question
#  for each given leading digit, it represents a certain range of permutations
#  maybe I could implement bisect from improve speed, but later
import math
from sortedcontainers import SortedSet
class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		res = []
		# the rest candidate digits should be reindexed each time, and SortedSet could do that automatically
		candSet = SortedSet(range(1, n+1))
		self.helper(n, k, res, 1, candSet)
		return ''.join(res)


	# Parameter start is the lower bound of k, so it initialize as 1
	def helper(self, n, k, res, start, candSet):
		if n == len(res):
			return

		seachWin = math.factorial(n - len(res) - 1)
		# try to find the leading digit. If k is located in a certain window, then left is the new start
		# then the scale of question shrink.
		# linear search, could be improved
		for i in range(n-len(res)):
			# For each loop, the left is increasing from the lower bound of k, which is start
			left = start + i * seachWin
			# the right is increasing based on left
			right = left + seachWin - 1
			if k >= left and k <= right:
				# choose this one
				cand = candSet[i]
				res.append(str(cand))
				candSet.remove(cand)
				break

		return self.helper(n, k, res, left, candSet)



class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		# The possible permutation for a given n
		# Note that if n = 0, the result is 1 (as no position is available), same as n = 1.
		factorial = [1] * (n + 1)
		for i in range(1, n + 1):
			factorial[i] = factorial[i-1] * i

		available = SortedSet([str(i) for i in range(1, n + 1)]) 
		result = []
		# 0-indexed array
		k -= 1

		for remaining in range(n, 0, -1):
			# the group size for this undefined digit
			group_size = factorial[remaining - 1]
			idx, k = divmod(k, group_size)
			result.append(available.pop(idx))

		return ''.join(result)