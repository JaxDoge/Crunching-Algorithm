1846. Maximum Element After Decreasing and Rearranging



# Amazon OA
# directly sort
# O(nlogn)
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        index = 0
        for i, num in enumerate(arr):
            if num > index:
                index += 1

        return index


# Mutation of counting sort
# Our goal is to cover the index [1,..,n] with the number in arr
# Larger number could cover the previous missed number
# any number larger than n could be treated as n
# if the indices are all covered, the answer is n
# otherwise, if several indices are missed, and those indices should be always located at the end of array
# the answer is n - missed count
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counter = [0] * (n + 1)

        for num in arr:
            if num > n:
                num = n

            counter[num] += 1

        miss = 0
        for i in range(1, n + 1):
            cnt = counter[i]
            if cnt == 0:
                miss += 1
            else:
                # Note that miss could not be negative number
                miss -= min(miss, cnt - 1)

        return n - miss

