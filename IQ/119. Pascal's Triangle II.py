119. Pascal's Triangle II


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        lastRow = [1, 1]
        for i in range(2, rowIndex + 1):
            thisRow = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    thisRow.append(1)
                    continue
                tmp = lastRow[j-1] + lastRow[j]
                thisRow.append(tmp)
            lastRow = thisRow

        return thisRow
