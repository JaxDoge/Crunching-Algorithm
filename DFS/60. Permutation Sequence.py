60. Permutation Sequence


#  Decomposition the original question
#  for each given leading digit, it represents a certain range of permutations
#  maybe I could implement bisect from improve speed, but later
import math
from sortedcontainers import SortedSet
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        candSet = SortedSet(range(1, n+1))
        self.helper(n, k, res, 1, candSet)
        return ''.join(res)


    def helper(self, n, k, res, start, candSet):
        if n == len(res):
            return

        seachWin = math.factorial(n - len(res) - 1)
        # try to find the leading digit
        # linear search, could be improved
        for i in range(n-len(res)):
            left = start + i * seachWin
            right = left + seachWin - 1
            if k >= left and k <= right:
                # choose this one
                cand = candSet[i]
                res.append(str(cand))
                candSet.remove(cand)
                break

        return self.helper(n, k, res, left, candSet)
