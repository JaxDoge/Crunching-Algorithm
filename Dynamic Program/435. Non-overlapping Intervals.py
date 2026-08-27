435. Non-overlapping Intervals

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		# Badcase
		if len(intervals) == 0:
			return 0

		intervals = sorted(intervals, key=lambda x: x[1])
		res = 0

		end = intervals[0][1]
		for i in range(1, len(intervals)):
			if intervals[i][0] < end:
				res += 1
				continue
			end = intervals[i][1]

		return res


class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key = lambda intrvl: intrvl[1])

		res = 0
		last_end = float('-inf')

		for start, end in intervals:
			if start >= last_end:
				last_end = end
			else:
				res += 1
		return res