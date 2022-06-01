440. K-th Smallest in Lexicographical Order




# Classic Problem
# lexical tree
# 1
# |  \  \      \
# 10  11 12 ...  19
# | \
# 100  101
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1   # Search start from the smallest number, 1
        prefix = 1   # when ans == k, we got the kth smallest number, so ans is refer to the order of curren prefix
        while ans < k:
            count = self.getCount(prefix, n)
            # case 1, k exists in current prefix tree
            # note that ans + count is the order of next prefix
            if ans + count > k:
                # search inside the tree
                prefix *= 10
                ans += 1
            # case 2, k exists in rest prefix trees
            # so we move the ans to the next prefix position, and next prefix is current one plus 1
            elif ans + count <= k:
                prefix += 1
                ans += count

        return prefix

    # return the number of elements with current prefix
    # calculate the count from the root node to the child tree
    # subtract the next prefix at this layer by current one, we can get the number of elements with current prefix
    # there are two corner case
    # 1. current prefix overrun the n, then stop further calculation and return
    # 2. next prefix overrun the n, then the number at this layer should be n+1 - cur 
    def getCount(self, prefix, n):
        count = 0
        cur = prefix
        nex = prefix + 1

        while cur <= n:
            count += min(n+1, nex) - cur
            cur *= 10
            nex *= 10

        return count
