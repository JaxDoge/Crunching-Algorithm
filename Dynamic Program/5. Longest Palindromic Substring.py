5. Longest Palindromic Substring

# Dynamic Program
# status transform formula Dij = Di+1j-1 and Di == Dj
# There are two exceptions, i = i and i + 1 = j
# Zigzag Scanning
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # bad case
        if n < 2:
            return s

        start_p = end_p = 0

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-2,-1,-1): 
            for j in range(i+1,n):
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False

                elif s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                # if dp[i][j] is true, update the start and end points
                if dp[i][j] and (j-i+1) > (end_p-start_p+1):
                    start_p = i
                    end_p = j

        return s[start_p:end_p]