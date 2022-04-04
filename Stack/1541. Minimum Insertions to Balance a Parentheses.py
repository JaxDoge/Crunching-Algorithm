1541. Minimum Insertions to Balance a Parentheses String

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        insertation = 0
        right_need = 0

        for i in range(n):
            if s[i] == '(':
                right_need += 2
                #  if the right_need is odd, we get a must-inserted right parenthese
                if right_need % 2 == 1:
                    insertation += 1
                    right_need -= 1

            if s[i] == ')':
                right_need -= 1
                # if there are too many right parenthese
                if right_need == -1:
                    insertation += 1
                    right_need = 1

        return insertation + right_need