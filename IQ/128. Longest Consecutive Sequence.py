128. Longest Consecutive Sequence


# Utilize the feature of set to skip non-start point numbers
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestQ = 0
        nums = set(nums)

        for n in nums:
            if n - 1 not in nums: # n is the start point of a queue
                curQ = 1
                curNum = n

                while curNum + 1 in nums:
                    curQ += 1
                    curNum += 1
                longestQ = max(longestQ, curQ)
                
        return longestQ    