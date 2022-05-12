87. Scramble String


# Simple elegant pythonic recursion
# time limit exceeded!
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # bad cases
        if s1 ==  s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True

        return False


# DP
# dp[i][j][len] represents if the s1[i:i+len-1] and s2[j,j+len-1] is mutual scrambled
# Note that zero len is meaningless, so the range of len is larger than the range of i or j plus one
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        dp = [[[False] * (m + 1) for _ in range(m)] for _ in range(m)]

        # When len is 1, it is base case
        for i in range(m):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True


        for length in range(2, m + 1):
            for i in range(m - length + 1):  #  preserve the last len positions
                for j in range(m - length + 1):
                    for k in range(1, length):
                        # First case
                        if dp[i][j][k] and dp[i+k][j+k][length-k]:
                            dp[i][j][length] = True
                            break

                        if dp[i][j+length-k][k] and dp[i+k][j][length-k]:
                            dp[i][j][length] = True
                            break

        return dp[0][0][m]

