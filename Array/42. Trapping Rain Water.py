42. Trapping Rain Water

# Memo + brutal search

class Solution:
    def trap(self, height: List[int]) -> int:
    	# Badcase
    	if len(height) == 0:
    		return 0 

    	# Using l_Max and r_Max to record the highest pillars of index i to both sides
    	