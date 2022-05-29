171. Excel Sheet Column Number



# convert to 26 digits number system
# A - 0
# B - 1
# Add an one in every iteration
from collections import deque
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0

        for i in range(n):
            ans = ans * 26 + (ord(columnTitle[i]) - ord("A") + 1)

        return ans
