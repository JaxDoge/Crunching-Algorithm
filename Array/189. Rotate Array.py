189. Rotate Array

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


# Extra O(n) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        extra = []
        start = (n - k % n) % n
        while len(extra) != n:
            extra.append(nums[start])
            start = (start + 1) % n

        for i in range(n):
            nums[i] = extra[i]

        return


# rotation k times
# time limitation exceed!
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        for i in range(k):
            tmp = nums[0]
            for j in range(n):
                nums[(j + 1) % n], tmp = tmp, nums[(j + 1) % n]

        return


# Auxiliary varibale for exchange element
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # Note that when i go back to the start point, there could be several elements unvisited
        # At this circumstance, the start point need move forward one position and start the next iteration
        # The total number of iteration is gcd(k, n), which could be proved
        # Or we could count the visited elements until it is n
        count = self.gcd(k, n)
        for start in range(count): 
            tmp = nums[start]
            i = start
            while True:
                i = (i + k) % n
                nums[i], tmp = tmp, nums[i]
                if i == start:
                    break

        return

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)


# reverse list:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def rev(i, j):
            nonlocal nums
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
            return

        nums.reverse()
        rev(0, k-1)
        rev(k, n-1)

        return