47. Permutations II



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        path = []
        memo = set([])
        self.backtrack(n, nums, memo, path, ans)

        return ans

    def backtrack(self, remain_slots, nums, pub_memo, cur_path, res):
        # base case
        if remain_slots == 0:
            return res.append(cur_path.copy())

        sub_memo = set([])

        for i in range(len(nums)):
            # pruning the tree
            if i in pub_memo or nums[i] in sub_memo:
                continue
            cur_path.append(nums[i])
            pub_memo.add(i)
            sub_memo.add(nums[i])
            self.backtrack(remain_slots-1, nums, pub_memo, cur_path, res)
            pub_memo.remove(i)
            cur_path.pop()

