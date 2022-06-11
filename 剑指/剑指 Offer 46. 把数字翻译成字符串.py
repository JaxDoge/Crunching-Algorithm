剑指 Offer 46. 把数字翻译成字符串


# DFS
# DP, dp[i] is the number of valid decodes in num[0:i], dp[0] = 0, dp[i] = dp[i-1] + dp[i - 2] if dp[i-1:i+1] is a valid number
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # note that there is no leading zero
        numStr = str(num)
        n = len(numStr)
        if num == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, n):
            if int(numStr[i-1]) * 10 + int(numStr[i]) < 26 and numStr[i-1] != "0":
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]

        return dp[n]