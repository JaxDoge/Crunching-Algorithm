565. Array Nesting


# Easy
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] in visited:
                continue

            curPath = set()
            curNum = nums[i]
            while curNum not in curPath:
                curPath.add(curNum)
                visited.add(curNum)
                ans = max(ans, len(curPath))
                curNum = nums[curNum]

        return ans
            
