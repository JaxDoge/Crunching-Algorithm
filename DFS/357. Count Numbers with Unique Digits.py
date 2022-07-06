357. Count Numbers with Unique Digits


# recurtion
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        def dfs(num, cands):
            if num == 1:
                return cands

            # if the previous number is a leading zero
            if cands == 10:
                return dfs(num - 1, 10) + dfs(num - 1, 9) * 9
            else:
                return dfs(num - 1, cands - 1) * cands

        return dfs(n, 10)