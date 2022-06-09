1044. Longest Duplicate Substring


# Approach #1, dichotomy + string hash
# Last 2 unit tests TLE!!
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)   # the longest dupsubstr has length n - 1
        l = 1
        r = n
        if n < 2:
            return ""

        def check(subLen):
            nonlocal n, s
            memo = set()
            strHash = 0
            base = 1
            prime = 31

            for i in range(subLen):
                strHash = strHash * prime + (ord(s[i]) - ord("a") + 1)
                base *= prime

            memo.add(strHash)
            # Slide window
            # kick out the head character and move in the tail one
            for i in range(subLen, n):
                strHash = strHash * prime - (ord(s[i - subLen]) - ord("a") + 1) * base + (ord(s[i]) - ord("a") + 1)
                if strHash in memo:
                    return i - subLen + 1
                memo.add(strHash)

            return -1 

        pos = -1
        subLen = 0
        while l < r:
            mid = l + (r - l) // 2
            start = check(mid)
            if start != -1:
                subLen = mid
                pos = start
                l = mid + 1
            else:
                r = mid 

        if pos == -1:
            return ""
        return s[pos:pos + subLen]

# 
