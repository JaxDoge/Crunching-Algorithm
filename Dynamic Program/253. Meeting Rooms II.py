253. Meeting Rooms II


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    	n = len(intervals)
    	starts = []
    	ends = []
    	for i in range(n):
    		starts.append(intervals[i][0])
    		ends.append(intervals[i][1])

    	starts.sort()
    	ends.sort()

    	count, res, i, j = (0, 0, 0, 0)

    	while j < n and i < n:  # if i = n, count stops adding, so the max result is already known
    		# find a start point
    		if starts[i] < ends[j]:
    			count += 1
    			i += 1
    		else:
    			count -= 1
    			j += 1
    		res = max(res, count)
    	return res

