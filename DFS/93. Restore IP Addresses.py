93. Restore IP Addresses


# Backtrack
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        if n < 4:
            return res
        # curPath = []  # 0 ~ 255
        # curIP = []  # length == 4

        def backtrack(idx, choice, curPath, curIP):
            nonlocal n, res
            curNum = "".join(curPath)
            if not self.isValid(curNum) and idx > 0:
                return
            if choice:
                # add the number to curIP
                curIP.append(curNum)
                curPath.clear()
                if len(curIP) == 4 and idx != n: # invalid IP length
                    return
            if idx == n:
                if choice and len(curIP) == 4:  # the ending period
                    res.append(".".join(curIP))
                return

            curPath.append(s[idx])
            backtrack(idx + 1, True, curPath[:], curIP[:])
            backtrack(idx + 1, False, curPath[:], curIP[:])

            return

        backtrack(0, False, [], [])
        return res



    def isValid(self, s):
        if len(s) == 0:
            return True
        if len(s) > 1 and s[0] == "0":
            return False
        if int(s) < 0:
            return False
        if int(s) > 255:
            return False
        return True