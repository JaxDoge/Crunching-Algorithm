239. Sliding Window Maximum

# heap queue 不合适，因为滑动窗口弹出的是某个特定的值，heap 无法快速定位
# 单调队列的实现
class MonotonicQueue:
    import collections
    def __init__(self):
        self.linked_list = collections.deque()

    # 队列插入 n 在队尾，保持非严格单调递增
    def push(self, n: int):
        while self.linked_list and self.linked_list[-1] < n:
            self.linked_list.pop()
        self.linked_list.append(n)

    def max(self) -> int:
        return self.linked_list[0]

    def pop(self, n: int):
        if n == self.linked_list[0]:
            self.linked_list.popleft()



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []

        for i in range(len(nums)):
            # 滑动窗口的技巧，先填满 k-1 的窗口，然后再增加一个元素，输出最大值，再删除第一个元素
            # 我觉得别的滑动方式也可以
            if i < k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res