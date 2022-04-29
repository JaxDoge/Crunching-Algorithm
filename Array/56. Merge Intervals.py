56. Merge Intervals



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        import functools
        def udcmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return b[1] - a[1]

        intervals.sort(key = functools.cmp_to_key(udcmp))

        res = []
        left = intervals[0][0]
        right = intervals[0][1]

        n = len(intervals)
        for i in range(1, n):
            l = intervals[i][0]
            r = intervals[i][1]

            if l > right:
                res.append([left, right])
                left = l
                right = r
                continue
            elif l <= right:
                right = max(right, r)
                continue

        res.append([left, right])
        
        return res



