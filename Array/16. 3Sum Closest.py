16. 3Sum Closest

# You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for i in range(n):
            # [-100,-98,-2,-1]
            # -101
            # No early stop here
            # if nums[i] >= target:
            #     if i < n - 2:
            #         three_sum = nums[i]+nums[i+1]+nums[i+2] 
            #         ans = self.udcmp(three_sum, target, ans)
            #         break
            #     else:
            #         break

            L = i + 1
            R = n - 1

            while L < R:
                three_sum = nums[i] + nums[L] + nums[R]
                if three_sum == target:
                    return three_sum
                elif three_sum > target:
                    R -= 1
                elif three_sum < target:
                    L += 1
                ans = self.udcmp(three_sum, target, ans)

        return ans

    def udcmp(self, three_sum, target, ans):
        if abs(three_sum - target) < abs(ans - target):
            return three_sum
        else:
            return ans

