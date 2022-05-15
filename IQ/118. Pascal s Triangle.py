118. Pascal s Triangle



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            thisRow = []
            for j in range(i+1):
                if j == 0 or j == i:
                    #  Critical step, compatible for every row and handle the special case at the very first two rows.
                    thisRow.append(1)
                else:
                    tmp = res[i-1][j] + res[i-1][j-1]
                    thisRow.append(tmp)
            res.append(thisRow)

        return res

