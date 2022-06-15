321. Create Maximum Number


# Divide and Conquer
# Same as drop n - k element (keep k element) to get the max number
# use monotonic stack to find the max number of given nums and k in each array, record the answer
# loop for all possible k for each nums
# find the max result

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def subMax(nums, k):
            # note that k is no larger than len(num)
            stack = []
            drop = len(nums) - k
            for n in nums:
                while drop != 0 and stack and stack[-1] < n:
                    stack.pop()
                    drop -= 1
                stack.append(n)

            return stack[:k]

        # Note that there is a trick
        # If A[i] == B[j], we actually cannot decide which element should be picked
        # instead, we need compare the following element and pick the larger one
        # for instance, if A = [0,0,0], B = [0, 9, 9]
        # if we simply pick the first list element when A[i] == B[j], we will get
        # [0,0,0,0,9,9], which obviously is incorrect

        # Good news is that, in python, the comparation between lists is implement in this way
        # [0,0,0] < [0,9,9] return True

        # Or we could write a comparation udf
        def compare(list1, idx1, list2, idx2):
            len1 = len(list1)
            len2 = len(list2)

            while idx1 < len1 and idx2 < len2:
                if list1[idx1] ！= list2[idx2]:
                    return list1[idx1] - list2[idx2]
                idx1 += 1
                idx2 += 1
                
            # if one list is thoroughly checked, return the longer one
            return (len1 - idx1) - (len2 - idx2)


        def merge(A, B):
            i = j = 0
            lenA = len(A)
            lenB = len(B)
            mergeL = []

            while i < lenA or j < lenB:
                if i >= lenA:
                    mergeL.extend(B[j:lenB])
                    break
                elif j >= lenB:
                    mergeL.extend(A[i:lenA])
                    break

                if compare(A, i, B, j) > 0:
                    mergeL.append(A[i])
                    i += 1
                else:
                    mergeL.append(B[j])
                    j += 1

            return mergeL

        # In python max(list1, list2) will return the list with larger first different element from left
        res = []
        # loop through all possible distribution of k
        for ki in range(k+1):
            if ki <= len(nums1) and k - ki <= len(nums2):
                sub1 = subMax(nums1, ki)
                sub2 = subMax(nums2, k - ki)
                res.append(merge(sub1, sub2))

        return max(res)



