97. Interleaving String


# DFS
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # notice when the recursion end, i and j are m and n
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            nonlocal s1, s2, s3, memo
            if i + j == len(s3):
                return True

            if memo[i][j] > -1:
                return True if memo[i][j] == 1 else False

            res = False
            # If s1[i] exists and equal to s3[i+j], match them
            if i < m and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)

            # If s2[j] exists and equal to s3[i+j], match them
            # the final res is True if either return true
            if j < n and s2[j] == s3[i + j]:
                res = res or dfs(i, j + 1)

            memo[i][j] = res

            return res

        return dfs(0, 0)