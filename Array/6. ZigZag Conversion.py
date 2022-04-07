6. ZigZag Conversion

# Using flag parameter to implement zigzag scanning
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        res = ["" for _ in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag

        return "".join(res)