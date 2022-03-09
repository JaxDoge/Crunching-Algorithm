452. Minimum Number of Arrows to Burst Balloons


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    	n = len(points)
    	if n == 0:
    		return 0

    	points = sorted(points, key=lambda x: x[1])
    	count = 1

    	end = points[0][1]
    	for i in range(1, n):
    		if points[i][0] <= end:
    			continue
    		end = points[i][1]
    		count += 1

    	return count