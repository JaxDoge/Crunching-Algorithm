32. Longest Valid Parentheses


# Stack
# 具体做法是我们始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」，这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        from collections import deque

        n = len(s)
        ans = 0
        if not n:
            return ans

        stack_helper = deque()
        # There is always a right parenthese in the bottom of stack, so we put a dummy right one first
        stack_helper.append(-1)
        for i in range(n):
            # left paranthese enter the stack
            if s[i] == '(':
                stack_helper.append(i)
            # right paranthese try to match with the top element of the stack
            elif s[i] == ')':
                stack_helper.pop()
                if len(stack_helper) == 0:
                    stack_helper.append(i)
                else:
                    # update max ans
                    ans = max(ans, i-stack_helper[-1])
            else:
                print('impossible')

        return ans


