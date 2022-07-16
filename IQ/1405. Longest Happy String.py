1405. Longest Happy String



# Greedy algorithm
# always try to choose the character with the largest remains
# there are only three choices, so we could check which one is the chosen one with if-else statement

from ast import literal_eval
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        while a + b + c > 0:
            choose = '-'
            maxNum = 0
            n = len(ans)
            # check if a could be chosen
            if a > maxNum and (n < 2 or ans[-1] != "a" or ans[-2] != "a"):
                choose = "a"
                maxNum = a

            # check if b could be chosen
            if b > maxNum and (n < 2 or ans[-1] != "b" or ans[-2] != "b"):
                choose = "b"
                maxNum = b

            # check if a could be chosen
            if c > maxNum and (n < 2 or ans[-1] != "c" or ans[-2] != "c"):
                choose = "c"
                maxNum = c                                

            # if there is no chosen one
            if choose == '-':
                break

            ans.append(choose)
            if choose == "a": a -= 1
            elif choose == "b": b -= 1
            elif choose == "c": c -= 1

        return "".join(ans)
                

