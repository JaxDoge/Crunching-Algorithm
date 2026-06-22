253. Meeting Rooms II

# The end time sorted list has the most info
# Any start time that smaller that current end time need a separated meeting room
# If start time is larger or equal to current end time, one meeting room can be release

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        start_time = []
        end_time = []

        for i in range(n):
            start_time.append(intervals[i][0])
            end_time.append(intervals[i][1])

        start_time.sort()
        end_time.sort()

        booked_cnt = 0
        ps, pe = 0, 0
        res = 0

        while ps < n and pe < n:
            if start_time[ps] < end_time[pe]:
                booked_cnt += 1
                ps += 1
            else:
                booked_cnt -= 1
                pe += 1
            
            res = max(res, booked_cnt)

        return res

