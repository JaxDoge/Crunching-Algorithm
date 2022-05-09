80. Remove Duplicates from Sorted Array II


# Double pointer
# general solution
# milk the non-descending list special attribution
# compare current num with the num k positions leads to the current insert position
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def generalSolution(k):
            nonlocal nums
            insert_p = 0
            for x in nums:
                if insert_p < k or x != nums[insert_p - k]:
                    nums[insert_p] = x
                    insert_p += 1
            return insert_p

        return generalSolution(2)


