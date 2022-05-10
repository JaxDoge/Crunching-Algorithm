84. Largest Rectangle in Histogram


# Monotonous stack
# Sentinel
# Fine the left and right boundary of a rectangle, which has the height of current bar
from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = []  # left boundary of each bar
        right = deque()  # right boundary of each bar

        mono_stack = []
        for i in range(n):
            while len(mono_stack) and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            leftB = mono_stack[-1] if len(mono_stack) else -1  # -1 is sentinel
            left.append(leftB)
            mono_stack.append(i)

        mono_stack = []
        for i in range(n-1,-1,-1):
            while len(mono_stack) and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            rightB = mono_stack[-1] if len(mono_stack) else n  # n is sentinel
            right.appendleft(rightB)
            mono_stack.append(i)

        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))

        return res