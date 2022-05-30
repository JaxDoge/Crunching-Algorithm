912. Sort an Array



# Quick sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.shuffle(nums)

        def sort(nums, lo, hi):
            if lo >= hi:
                return

            # nums[p] is at the right place
            p = self.partition(nums, lo, hi)
            sort(nums, lo, p - 1)
            sort(nums, p + 1, hi)

        sort(nums, 0, n - 1)
        return nums

    def partition(self, nums, start, end):
        # # bad case
        # if start == end:
        #     return start

        pivot = nums[start]
        i = start
        j = end + 1

        while True:
            # Move i forward
            # check if i is invalid or nums[i] >= pivot
            # for each iteration, always move i firstly
            while True:
                i += 1
                if nums[i] >= pivot or i == end:
                    break

            # Same as j, and that's why j initialize as end + 1
            while True:
                j -= 1
                if nums[j] <= pivot or j == start:
                    break

            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[start] = nums[start], nums[j]
        return j

    def shuffle(self, nums):
        import random
        n = len(nums)
        for i in range(n):
            rd = random.randint(i, n - 1)
            nums[i], nums[rd] = nums[rd], nums[i]


