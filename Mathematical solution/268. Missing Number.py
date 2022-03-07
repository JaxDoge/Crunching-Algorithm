# XRO operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # dummy index and value
        res = n ^ 0
        # Bitwise XOR
        for i in range(n):
            res ^= nums[i] ^ i
        return res



# array sum operation; avoiding integer overflow
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # dummy index and value
        res = n - 0
        # sum up the rest diff of indices and values
        for i in range(n):
            res += i - nums[i]
        return res

