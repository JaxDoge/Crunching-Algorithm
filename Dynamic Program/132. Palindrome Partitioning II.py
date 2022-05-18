132. Palindrome Partitioning II


# DP1  dp1[i][j] refer to if the s[i:j+1] is palindrome
# middle out
# DP2 dp2[i] refer to the minimium cut of s[0:i+1]
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp1 = [[False] * n for _ in range(n)]
        dp2 = [2000] * n

        def middleOut(i, j):
            nonlocal n, s, dp1
            while i >= 0 and j < n and s[i] == s[j]:
                dp1[i][j] = True
                i -= 1
                j += 1

        for i in range(n):
            middleOut(i, i)
            middleOut(i, i + 1)

        for i in range(n):
            # base case dp2[0] is covered
            if dp1[0][i]:
                dp2[i] = 0
                continue

            for j in range(i):
                if dp1[j+1][i]:
                    dp2[i] = min(dp2[i], dp2[j] + 1)

        return dp2[n-1]
