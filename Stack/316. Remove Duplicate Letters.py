316. Remove Duplicate Letters


# Monotonic Stack - increasing
# The element in Stack only appear once
# we use an extra hashset to record the elements that already in the stack
# we use an counter to record the remain number of each letter
# if the remaining number of certain number is zero, it cannot be poped in any case

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter

        stack = []
        memo = set()
        remain = Counter(s)

        for c in s:
            # the remain number of c is subtract by one
            remain[c] -= 1

            # if c is already in the stack, skip it
            if c in memo:
                continue

            # Should we pop up the top element in the stack?
            # if stack is empty, no
            # if c >= stack[-1], no
            # if remain(stack[-1]) == 0, no
            while stack and stack[-1] > c and remain[stack[-1]] > 0:
                memo.remove(stack.pop())

            # add c into stack and memo
            stack.append(c)
            memo.add(c)

        return "".join(stack)