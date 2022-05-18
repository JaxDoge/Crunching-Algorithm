131. Palindrome Partitioning


# DP table record s[i:j+1] if it is palindrome
# Middle-out construct DP table
# Backtrack search the possible split

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = []

        def middleOut(i, j):
            nonlocal s, dp, n
            while i >= 0 and j < n and s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1


        def backtrack(start, curPath):
            nonlocal res, dp, n, s
            # base case
            if start == n:
                res.append(curPath[:])
                return

            for i in range(start, n):
                if not dp[start][i]:
                    continue

                curPath.append(s[start:i+1])
                backtrack(i + 1, curPath)
                curPath.pop()

        for i in range(n):
            # single middle character
            middleOut(i, i)
            # Double middle character
            middleOut(i, i + 1)

        backtrack(0, [])
        return res