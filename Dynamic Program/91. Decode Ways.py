91. Decode Ways


# Backtrack
# Time limitation exceeded !!
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set([str(x) for x in range(1,27)])
        # curCode = []  # Must constrain to 1 ~ 26
        res = 0

        def backtrack(idx, curCode, choice):
            nonlocal n, validSet, res, s
            if "".join(curCode) not in validSet and idx > 0:
                return
            if len(curCode) > 2:
                return
            if idx == n:
                if choice:
                    res += 1
                return


            if choice:
                curCode = []
            
            curCode.append(s[idx])
            # Choice one: add separator 
            backtrack(idx + 1, curCode, True)
            # Choice two: no separator
            backtrack(idx + 1, curCode, False)
            curCode.pop()

            return

        backtrack(0, [], False)  # True is still OK
        return res



# DP
# dp[i] is the number of decode approches for s[0:i+1]
# if s[i] is a standalone code, there is dp[i-1] decode ways
# if s[i] could combine with s[i-1], there is dp[i-2] decode ways
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set([str(x) for x in range(1,27)])
        dp = [0] * n
        if s[0] in validSet:
            dp[0] = 1
        else:
            return 0

        for i in range(1, n):
            if i == 1:
                if "".join(s[:2]) in validSet: 
                    if s[1] != "0":
                        dp[i] = 2
                    else:
                        dp[i] = 1
                else:
                    if s[1] != "0":
                        dp[i] = 1
                    else:
                        dp[i] = 0
                continue

            if "".join(s[i-1:i+1]) in validSet: 
                if s[i] != "0":
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = dp[i-2]
            else:
                if s[i] != "0":
                    dp[i] = dp[i-1]
                else:
                    dp[i] = 0
                    break

        return dp[n-1]







