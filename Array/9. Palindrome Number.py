9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        from collections import deque
        divisor = 10
        tmp = x
        help_stack = deque()
        while True:
            help_stack.append(tmp % divisor)
            tmp = tmp // divisor
            if tmp == 0:
                break

        y = 0
        while len(help_stack):
            y = y * 10 + help_stack.popleft()

        return x == y



