392. Is Subsequence

class Solution:
    # doulbe pointers scan the two string
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)



Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, 
and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?


class Solution:
    # bisection
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        # preprocess t
        from collections import defaultdict
        index = defaultdict(list)
        for i in range(n):
            c = t[i]
            index[c].append(i)

        j = 0
        for i in range(m):
            c = s[i]
            if c not in index:
                return False
            # bisect the c in all c indices for index j, or the index just larger than j
            position = leftbound(index[c], j)
            # invalid position
            if position >= len(index[c]):
                return False
            # find one, move j
            j = index[c][position] + 1

        return True


    def leftbound(self, search_r, target):
        low = 0
        high = len(search_r)
        while low < high:
            mid = low + (high - low) // 2
            if target > search_r[mid]:
                low = mid + 1
            else:
                high = mid

        return low

