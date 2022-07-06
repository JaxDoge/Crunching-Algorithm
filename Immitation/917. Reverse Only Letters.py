917. Reverse Only Letters



# double pointers
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        l = 0
        r = n - 1

        sList = list(s)

        while l < r:
            if not sList[l].isalpha():
                l += 1
                continue

            if not sList[r].isalpha():
                r -= 1
                continue

            sList[l], sList[r] = sList[r], sList[l]
            l += 1
            r -= 1

        return "".join(sList)
