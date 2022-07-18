4. Median of Two Sorted Arrays



# Dichotomy
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        we wanna find the the kth number in these two arrays
        Note that we could find the (k//2 - 1)th element in both arrays as two pivots
        so regularly, there are [0 .. k//2 - 2] k//2 - 2 elements at LHS in both arrays
        therefore, the smaller pivots would be only larger or equal to k - 2 elements
        then, the larger one could be only larger or equal to k - 1 elements
        So, once k diwindle to 1, we got the orginal kth element we want
        """
        m, n = len(nums1), len(nums2)

        def findTheKth(k):
            nonlocal nums1, nums2, m, n

            startIdx1, startIdx2 = 0, 0

            while True:
                # base case 1, nums1 is running out
                if startIdx1 == m:
                    return nums2[startIdx2 + k - 1]
                # base case 2
                elif startIdx2 == n:
                    return nums1[startIdx1 + k - 1]
                # base case 3, k == 1
                elif k == 1:
                    return min(nums1[startIdx1], nums2[startIdx2])

                # regular iteration
                nextIdx1 = min(startIdx1 + k // 2 - 1, m - 1)
                nextIdx2 = min(startIdx2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[nextIdx1], nums2[nextIdx2]

                # throw [start1 .. next1]
                if pivot1 <= pivot2:
                    k -= nextIdx1 - startIdx1 + 1
                    startIdx1 = nextIdx1 + 1
                # throw [start2 .. next2]
                elif pivot1 > pivot2:
                    k -= nextIdx2 - startIdx2 + 1
                    startIdx2 = nextIdx2 + 1


        # Odd or even?
        total = m + n
        # if the total elements is odd
        if total % 2 == 1:
            return findTheKth(total // 2 + 1)
        # if the total elements is even, the median is the mean of two numbers in the middle
        else:
            return (findTheKth(total // 2) + findTheKth(total // 2 + 1)) / 2



