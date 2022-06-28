350. Intersection of Two Arrays II



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.intersect(nums2, nums1)

        # record the frequency of each number in the short array
        from collections import Counter
        counter = Counter(nums1)

        res = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                res.append(num)
                counter[num] -= 1

        return res






# What if the given array is already sorted? How would you optimize your algorithm?
If these array is sorted, I could use two pointers, and the time complexity is O(min(n, m)),
and the space complexity if O(1)
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
first one obviously
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
first one, since all we need to do with nums2 is go through it once for all.
