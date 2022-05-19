135. Candy


# The rules could be catagoried into two cases
# 1. if Ri > Ri-1 Ci is Ci-1 + 1 
# 2. if Ri > Ri+1 Ci is Ci+1 + 1
# Scan the ratings from left to right, get the left rules candy list
# Then Scanning from right to left
class Solution:
    def candy(self, ratings: List[int]) -> int:
        r = ratings
        n = len(ratings)
        left = [1] * n

        for i in range(n):
            if i > 0 and r[i] > r[i - 1]:
                left[i] = left[i - 1] + 1

        # right list is unnecessary
        # collect the real candy numbers while scanning
        res = 0
        right = 0

        for i in range(n - 1, -1, -1):
            if i < n - 1 and r[i] > r[i + 1]:
                right = right + 1
            else:
                right = 1
            res = max(left[i], right) + res

        return res
