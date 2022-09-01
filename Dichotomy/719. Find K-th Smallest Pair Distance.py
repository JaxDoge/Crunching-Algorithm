719. Find K-th Smallest Pair Distance


# 1. sort the nums for sure, we are looking for the absolute difference
# 2. Note that kth smallest one in a sorted list must be larger or equal to k numbers (There are k numbers in the LHS, including itself).
# 3. The kth distance locates in interval [0, max - min]
# 4. we could check each one from the smallest to largest, the first distance that satisfying 2. is what we what
# 5. of course, we dont have to use linear search, instead, we need bisect here
# 6. next question is how to count the pair distances that smaller or equal to a given distance "mid" ?
# 7. we could iterate the right end j of all pairs, and find the left end i, note that nums[j] - nums[i] must smaller or equal to "mid"
# 8. so we could adapt bisect again here, we need to find the smallest i that nums[i] >= nums[j] - mid
# 9. j - i is the count of pair for this given "mid".
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            # For a given right end, caclulate how many pairs' distance smaller or equal to mid
            # Why including mid?
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)
