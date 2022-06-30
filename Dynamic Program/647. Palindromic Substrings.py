647. Palindromic Substrings



# DP table
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = n
        
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = 1
                        ans += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j] == 1:
                            ans += 1

        return ans



