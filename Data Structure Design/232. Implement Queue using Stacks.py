232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
    	self.s1, self.s2 = list(), list()

    def push(self, x: int) -> None:
    	self.s2.append(x)

    def pop(self) -> int:
    	self.peek()
    	return self.s1.pop()

    def peek(self) -> int:
    	# s1 非空直接返回
    	if not self.s1:
	    	# 把 s2 中的元素按顺序压入 s1
	    	while self.s2:
	    		self.s1.append(self.s2.pop())
	    return self.s1[-1]    	


    def empty(self) -> bool:
    	return not self.s1 and not self.s2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()