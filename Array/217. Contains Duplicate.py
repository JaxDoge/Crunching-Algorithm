217. Contains Duplicate



# bitewise operation
# 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))
