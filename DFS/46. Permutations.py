# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        :param nums: List[int]
        :return: res List[List[int]]
        """
        n = len(nums)
        res = []

        def backtrack(first=0):
            if first == n:
                res.append(nums.copy())
            for i in range(first, n):
                # make a choice
                nums[first], nums[i] = nums[i], nums[first]
                # backtrack
                backtrack(first+1)
                # revoke choice
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)

        return res

