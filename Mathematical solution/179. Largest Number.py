179. Largest Number




# Greedy Algorithm
# If ab < ba, then ... b a ... should always larger than ... a b ...
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        str_nums = map(str, nums)

        def cmp(a: str, b: str):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        from functools import cmp_to_key
        str_nums = sorted(str_nums, key = cmp_to_key(cmp))
        return "".join(str_nums) if str_nums[0] != "0" else "0"