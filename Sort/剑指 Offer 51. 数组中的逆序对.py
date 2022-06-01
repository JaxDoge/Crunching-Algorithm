剑指 Offer 51. 数组中的逆序对



# Merge sort
# count the inversion number at merge function
# only if the pointer of last subarray move to the next one, the count need be increased
# Classic Question, recite it!
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Can I modify the original nums
        copyNums = nums[:]

        tmp = [0] * n
        return self.mergeSort(copyNums, 0, n - 1, tmp)

    # Calculate the inversion number
    # Sort the invterval [left...right] in nums
    '''
    nums:
    left:
    right:
    tmp: for storing the left and right subarray
    '''
    def mergeSort(self, nums, left, right, tmp):
        if left == right:
            return 0
        # Dividend and Conquer
        # left part is [left...mid], right part is [mid + 1...right]
        mid = left + (right - left) // 2

        # Count and sort
        leftPairs = self.mergeSort(nums, left, mid, tmp)
        rightPairs = self.mergeSort(nums, mid + 1, right, tmp)

        # if left and right array do not need further merge
        if nums[mid] <= nums[mid + 1]:
            return leftPairs + rightPairs

        # Count the inversion pairs in the merge step
        crossPairs = self.mergeCount(nums, left, mid, right, tmp)
        return leftPairs + rightPairs + crossPairs

    # core code
    def mergeCount(self, nums, left, mid, right, tmp):
        # Store left and right array in tmp
        for i in range(left, right + 1):
            tmp[i] = nums[i]

        # two points
        i = left
        j = mid + 1

        count = 0
        # When j need move forward and left array is not empty(i <= mid), it indicated that there are mid - i + 1 
        # inversion paris for tmp[j], before sorted
        # When i need move forward, all related inversion pairs is cacluated in the above step, so count is untouched
        for k in range(left, right + 1):
            # base case, i overflow
            if i == mid + 1:
                nums[k] = tmp[j]
                j += 1
            elif j > right:
                nums[k] = tmp[i]
                i += 1
            # note that it's not < since merge sort has to be stable sort
            # and same value pairs do not be deemed as inversion pairs
            elif tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1
                count += mid - i + 1

        return count
