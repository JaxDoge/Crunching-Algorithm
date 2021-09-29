295. Find Median from Data Stream


class MedianFinder:
	from heapq import heappop, heappush, heapify

    def __init__(self):
    	# min heap queue
    	self.large = []
    	heapify(self.large)
    	# max heap queue
    	self.small = []
    	heapify(self.small)

    def addNum(self, num: int) -> None:
    	# 不仅要维护self.large和self.small的元素个数之差不超过 1，还要维护self.large堆的堆顶元素要大于等于self.small堆的堆顶元素
    	# 想要往self.large里添加元素，不能直接添加，而是要先往self.small里添加，然后再把self.small的堆顶元素加到self.large中；向self.small中添加元素同理。
    	if len(self.large) > len(self.small):
    		heappush(self.large, num)
    		heappush(self.small, (-1)*heappop(self.large))
    	else:
    		heappush(self.small, (-1)*num)
    		heappush(self.large, (-1)*heappop(self.small))

    def findMedian(self) -> float:
    	if len(self.large) > len(self.small):
    		return self.large[0]
    	elif len(self.large) < len(self.small):
    		return self.small[0]*(-1)
    	else:
    		return (self.large[0]+self.small[0]*(-1))/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()