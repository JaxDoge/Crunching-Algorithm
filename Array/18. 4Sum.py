18. 4Sum


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        res = []
        nums.sort()

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                L = j + 1
                R = n - 1

                while L < R:
                    quad_sum = nums[i] + nums[j] + nums[L] + nums[R]

                    # move the two pointers in different scenarios
                    if quad_sum == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        # find the next one;
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1

                        L += 1
                        R -= 1

                    elif quad_sum < target:
                        L += 1
                    elif quad_sum > target:
                        R -= 1

        return res
