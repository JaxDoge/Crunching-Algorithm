315. Count of Smaller Numbers After Self


# Count the reverse pair
# Merge sort

class node:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos

class Solution:

    def __init__(self):
        self.tmp = []
        self.ans = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return [0]
        # maintain a new nums
        numsN = []
        for idx, num in enumerate(nums):
            numsN.append(node(num, idx))

        self.ans = [0] * n
        self.tmp = [0] * n
        self.mergeSort(numsN, 0, n - 1)
        return self.ans

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 

        mid = left + (right - left) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        return

    def merge(self, nums, l, mid, r):
        for i in range(l, r + 1):
            self.tmp[i] = nums[i]

        lP = l
        rP = mid + 1

        for k in range(l, r + 1):
            if lP == mid + 1:
                nums[k] = self.tmp[rP]
                rP += 1
            elif rP == r + 1:
                nums[k] = self.tmp[lP]
                self.ans[nums[k].pos] += rP - 1 - mid
                lP += 1

            elif self.tmp[lP].val <= self.tmp[rP].val:
                nums[k] = self.tmp[lP]
                self.ans[nums[k].pos] += rP - 1 - mid
                lP += 1
            else:
                nums[k] = self.tmp[rP]
                rP += 1

        return


