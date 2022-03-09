1024. Video Stitching


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
    	if time == 0:
    		return 0

    	# Sort the clips by start time ascending, and the same start time sort by end time descending
    	# we could use user defined cmp functools cmp_to_key
    	# or use the Sort Stability of sort function

    	clips.sort(key = lambda k: k[1], reverse=True)
    	clips.sort(key = lambda k: k[0])

    	res = 0
    	currend = 0
    	nextend = 0
    	i = 0
    	n = len(clips)

    	while i < n:
    		if clips[i][0] > currend:  # There is a gap
    			break
    		while i < n and clips[i][0] <= currend:
    			nextend = max(nextend, clips[i][1])
    			i += 1

    		res += 1
    		currend = nextend
    		if currend >= time:
    			return res

    	return -1