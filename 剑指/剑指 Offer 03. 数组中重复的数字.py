剑指 Offer 03. 数组中重复的数字



# Hashmap

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        memo = defaultdict(int)

        for n in nums:
            memo[n] += 1
            if memo [n] == 2:
                return n