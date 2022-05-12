88. Merge Sorted Array



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ans = []
        p1 = p2 = 0

        while p1 < m or p2 < n:
            if p1 == m:
                ans.extend(nums2[p2:])
                break

            if p2 == n:
                ans.extend(nums1[p1:m])  # Caution !! nums1 has extra elements
                break

            if nums1[p1] <= nums2[p2]: 
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1

        for i in range(len(ans)):
            nums1[i] = ans[i]

