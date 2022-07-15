454. 4Sum II



# Brutal Force
# A + B = -(C + D)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        counterAB = Counter(a + b for a in nums1 for b in nums2)

        ans = 0
        for c in nums3:
            for d in nums4:
                if -(c + d) in counterAB:
                    ans += counterAB[-(c + d)]

        return ans