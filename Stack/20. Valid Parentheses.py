20. Valid Parentheses

# Stack
class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        left_stack = deque()
        n = len(s)

        for i in range(n):
            if s[i] in {'{','[','('}:
                left_stack.appendleft(s[i])
            elif len(left_stack) != 0 and self.leftPa(s[i]) == left_stack[0]:
                left_stack.popleft()
            else:
                return False

        # All left parentheses are matched, then return true, otherwise return false
        return len(left_stack) == 0


    def leftPa(self, right_pa):
        if right_pa == '}':
            return '{'
        elif right_pa == ']':
            return '['
        return '('