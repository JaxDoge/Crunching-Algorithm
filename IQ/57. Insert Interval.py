57. Insert Interval


# relocated every interval in res[] from left to right; each time compare current interval with new one
# there are three cases
# 1. current one is at the left of the new one, no over lap, e.g. r < left: append current one
# 2. current one is at the right of the new one, no over lap, e.g. l > right, if new one still unsettled, append new one
# append current one
# 3. they are overlapped, merge them as a new "new interval"
# if the new interval still unsettled after the loop, place it at the end of the new list
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        is_placed = False
        res = []


        for l, r in intervals:
            # first condition
            if r < left:
                res.append([l, r])
            # second
            elif l > right:
                if not is_placed:
                    res.append([left, right])
                    is_placed = True
                res.append([l, r])
            # third
            else:
                left = min(left, l)
                right = max(right, r)

        if not is_placed:
            res.append([left, right])

        return res