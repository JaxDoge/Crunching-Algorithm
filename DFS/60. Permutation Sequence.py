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
