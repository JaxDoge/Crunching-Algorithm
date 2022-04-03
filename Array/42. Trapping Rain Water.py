42. Trapping Rain Water

# Memo + brutal search

class Solution:
    def trap(self, height: List[int]) -> int:
    	n = len(height)
    	# Badcase
    	if len(height) == 0:
    		return 0 
    	res = 0

    	# Using l_Max and r_Max to record the highest pillars of index i to both sides
    	from collections import deque
		l_Max = deque([height[0]])
		r_Max = deque([height[n-1]])

		for i in range(1,n):
			if height[i] >= l_Max[i-1]:
				l_Max.append(height[i])
			else:
				l_Max.append(l_Max[i-1])
		for j in range(n-2,-1,-1):
			if height[j] >= r_Max[0]:
				r_Max.appendleft(height[j])
			else:
				r_Max.appendleft(r_Max[0])

		# calculate the water volumn in each index
		for i in range(n):
			res += min(l_Max[i], r_Max[i]) - height[i]

		return res


# Double pointers
# The key point is for each time, move and calculate the lower side
# Remember the water volumn decided by the shortest bar.
# Space compexity is O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Badcase
        if len(height) == 0:
            return 0 
        res = 0

        left = 0
        right = n - 1
        l_Max, r_Max = 0, 0

        while left < right:
            l_Max = max(l_Max, height[left])
            r_Max = max(r_Max, height[right])

            if l_Max < r_Max:
                res += l_Max - height[left]
                left += 1
            else:
                res += r_Max - height[right]
                right -= 1

        return res