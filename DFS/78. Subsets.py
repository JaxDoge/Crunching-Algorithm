class Solution:
    def __init__(self):
        self.res = list()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        one_subset = list()
        self.backtrack(nums, one_subset, 0)
        return self.res

    def backtrack(self, nums, one_subset, start):
        # Pre-order of a tree
        self.res.append(one_subset.copy())

        # i start from current start point and end at the length of nums
        for i in range(start, len(nums)):
            # choose a branch
            one_subset.append(nums[i])
            # recursive travel
            self.backtrack(nums, one_subset, i+1)
            one_subset.pop()

