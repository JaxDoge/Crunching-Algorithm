class Solution:
    def __init__(self):
        self.res = list()

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        one_comb = list()
        self.backtrack(nums, one_comb, 0, k)
        return self.res

    def backtrack(self, nums, one_comb, start, k):
        if len(one_comb) == k:
            self.res.append(one_comb.copy())
            return

        for i in range(start, len(nums)):
            one_comb.append(nums[i])
            self.backtrack(nums, one_comb, i+1, k)
            one_comb.pop()

