11. Container With Most Water


# Double pointers
# find the max area of rectange between two pillars
# the width of rectange is shrinking
# the area depend on the shorter pillar.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right  = len(height) - 1
        res = 0

        while left < right:
            cur_rec_area = min(height[left], height[right]) * (right - left)
            res = max(res, cur_rec_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
