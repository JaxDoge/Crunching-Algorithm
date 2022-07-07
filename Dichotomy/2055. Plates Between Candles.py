2055. Plates Between Candles


# Using a list cList to record the indices of each candle in the s
# note that the index of cList tell us the number of candles between two candles
# and the value of cList tell us the number of candles plus plates between two candles

# the question is how to find the endpoint candles of each query interval less than O(n) time complexity
# and the answer is dichotomy

# we could use the library bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        from bisect import bisect_left, bisect_right
        n = len(s)
        cList = []

        for idx, c in enumerate(s):
            if c == "|":
                cList.append(idx)

        ans = []
        for left, right in queries:

            # find the first candle index in cList
            fIdx = bisect_left(cList, left)
            # find the last one
            lIdx = bisect_right(cList, right) - 1

            if lIdx <= fIdx:
                ans.append(0)
                continue
            else:
                plates = cList[lIdx] - cList[fIdx] - 1 - (lIdx - fIdx - 1)
                ans.append(plates)
                continue

        return ans

        




