90. Subsets II



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        cur_path = []

        def backtrack(start):
            nonlocal res, cur_path, nums
            # Preorder traverl
            res.append(cur_path.copy())
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                # Pruning tree
                if i > start and nums[i] == nums[i - 1]:
                    continue

                cur_path.append(nums[i])
                backtrack(i + 1)   # Caution !!
                cur_path.pop()

            return

        backtrack(0)
        return res