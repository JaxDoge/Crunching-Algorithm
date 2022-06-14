402. Remove K Digits



# Monotonic stack
# we scan from the first number
# if there is a RHS adjacent number, we compare there size
# if the RHS number is larger, drop it, and k = k - 1
# if the k is zero, stop dropping and put rest numbers into stack
# what we need is keep n - k element remain
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k

        # badcase
        if remain <= 0:
            return "0"

        for n in num:
            while k != 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        # strip leading zeros
        # but if the rest numbers are all zeros, the stripping will return "", which should be "0"
        return "".join(stack[:remain]).lstrip("0") or "0"