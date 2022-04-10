15. 3Sum


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 3:
            return res

        # sort the nums
        nums.sort()

        # Double pointers, and i is the first number
        for i in range(n):
            if nums[i] > 0:  # No way to find a result if nums[i] is a positive integer
                return res
            # the next i should map to a different nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = n - 1

            while L < R:
                if sum([nums[i], nums[L], nums[R]]) == 0:
                    res.append([nums[i], nums[L], nums[R]])

                    # avoids duplicate
                    while L < R and nums[L+1] == nums[L]:
                        L += 1
                    while L < R and nums[R-1] == nums[R]:
                        R -= 1

                    L += 1
                    R -= 1

                elif sum([nums[i], nums[L], nums[R]]) > 0:
                    R -= 1
                elif sum([nums[i], nums[L], nums[R]]) < 0:
                    L += 1

        return res