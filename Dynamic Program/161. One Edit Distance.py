161. One Edit Distance


# consider all possible situation
# assume len(s) <= len(t)
# otherwise just call isOneEditDistance(t, s)

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # bad case
        if s == t:
            return False

        m = len(s)
        n = len(t)

        if abs(m - n) > 1:
            return False
        if m > n:
            return self.isOneEditDistance(t, s)

        for i in range(m):
            # check if the difference exists in [0, m - 1]
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]

        return True



# DP? 
# note that dp table has m + 1 rows and n + 1 columns 
# because the base case dp[0][0] should always be zero
# so we reserve a row and a column for empty strings

# time limitation exceeded

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # bad case
        if s == t:
            return False

        m = len(s)
        n = len(t)

        if abs(m - n) > 1:
            return False

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Delete s[i-1]
                    # Add at s[i]
                    # substitute s[i-1]                   
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,      
                        dp[i][j - 1] + 1,      
                        dp[i - 1][j - 1] + 1   
                        )

        return dp[m][n] == 1

