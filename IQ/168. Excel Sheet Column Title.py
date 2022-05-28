168. Excel Sheet Column Title



# 26 decimal number system
# Note that we need recode the number of each letter by subtract one
# A - 0
# B - 1
# Z - 25
from collections import deque
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = deque()
        target = columnNumber - 1

        def covert(n):
            if n == 0:
                return "Z"
            upperL = n + ord("A") - 1
            return chr(upperL)

        while True:
            quotient = target // 26

            # append the code of letter at this target number
            # which is the remainder
            res.append(target % 26)
            
            if quotient == 0:
                break
            # subtract one for next iteration
            target = quotient - 1

        ans = []
        while len(res):
            ans.append(covert(res.pop()))

        return "".join(ans)
