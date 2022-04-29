67. Add Binary


# Not that easy actually
# 
from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = deque()
        n = max(len(b), len(a))
        carry = 0

        for i in range(n):
            carry += int(a[len(a)-1-i]) if i < len(a) else 0
            carry += int(b[len(b)-1-i]) if i < len(b) else 0
            ans.appendleft(str(carry % 2))
            carry = carry >> 1

        if carry > 0:
            ans.appendleft(str(carry))

        return ''.join(ans)






