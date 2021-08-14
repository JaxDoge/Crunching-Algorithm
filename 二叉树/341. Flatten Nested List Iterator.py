341. Flatten Nested List Iterator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """



# 紫金解法
# 调用hasNext时，如果nestedList的第一个元素是列表类型，则不断展开这个元素，直到第一个元素是整数类型。
# 由于调用next方法之前一定会调用hasNext方法，这就可以保证每次调用next方法的时候第一个元素是整数型，直接返回并删除第一个元素即可。

class NestedIterator:
	import collections
    def __init__(self, nestedList: [NestedInteger]):
    	# change the original list to deque for the head operations
    	self.helper = collections.deque(nestedList)
        
    def next(self) -> int:
    	# The hasNext function guarantees the first element in helper is an integer
    	return self.helper.popleft().getInteger()
        
    
    def hasNext(self) -> bool:
    	# if the first element of helper is not an integer, unpack the first list element
    	while len(self.helper)>0 and not self.helper[0].isInteger():
    		tmp = self.helper.popleft().getList()  # tmp is a list not a deque
    		for i in range(len(tmp)-1,-1,-1):
    			self.helper.appendleft(tmp[i])

        return len(self.helper)>0

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.size = len(nestedList) if nestedList else 0
        self.iterator = None
        self.i = 0
    
    def next(self) -> int:
        cur = self.nestedList[self.i]
        if cur.isInteger():
            self.i += 1
            return cur.getInteger()
        else: return self.iterator.next()
    
    def hasNext(self) -> bool:
        while self.i < self.size:
            cur = self.nestedList[self.i]
            if cur.isInteger(): return True
            else:
                if self.iterator == None:
                    self.iterator = NestedIterator(cur.getList())
                if self.iterator.hasNext(): return True
                else: 
                    self.iterator = None
                    self.i += 1
        return False