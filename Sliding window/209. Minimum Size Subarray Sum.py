209. Minimum Size Subarray Sum


# Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        window_sum = 0
        res = float("inf")
        left = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                # Update res
                res = min(res, right - left + 1)

                window_sum -= nums[left]
                left += 1

        return res if res != float("inf") else 0






# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).