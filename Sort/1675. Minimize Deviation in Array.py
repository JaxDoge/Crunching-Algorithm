1675. Minimize Deviation in Array



from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        queue = SortedList()
        for num in nums:
            if nums % 2 == 1:
                queue.add(num * 2)
            else:
                queue.add(num)

        ans = float("inf")
        while True:
            ans = min(ans, queue[-1] - queue[0])
            cur = queue.pop()
            # Try to shrink the maximum
            if cur % 2 == 1:
                return ans 
            queue.add(cur // 2)