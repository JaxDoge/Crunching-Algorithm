921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_need = 0
        right_need = 0
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                right_need += 1
            elif s[i] == ')':
                right_need -= 1
                # if right_need smaller than zero, then we need a left parenthese
                if right_need == -1:
                    left_need += 1
                    right_need = 0

        return left_need + right_need