20. Valid Parentheses

# Stack
class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        left_stack = deque()
        n = len(s)

        for i in range(n):
            