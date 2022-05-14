115. Distinct Subsequences


# DFS + memo
# memo[i][j] refer to the number of substrings of t[j:] in s[i:]
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            nonlocal s, t, m, n, memo
            # base case
            if j == n:  # target string all matched!
                return 1

            # bad case, rest target string is longer than rest source string
            if m - i < n - j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            res = 0
            if s[i] == t[j]:
                # There are two options, match s[i] or not
                res += dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                res += dfs(i + 1, j)

            memo[i][j] = res
            return res

        return dfs(0, 0)

