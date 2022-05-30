剑指 Offer 09. 用两个栈实现队列



# Note that we do not have to pour back elements to addStack from deleteStack
# Only if the delete stack is empty and the current order is delete, we need to transfer all element
class CQueue:

    def __init__(self):
        self.addStack = []
        self.deleteStack = []
        self.size = 0


    def appendTail(self, value: int) -> None:
        self.addStack.append(value)
        self.size += 1
        return

    def deleteHead(self) -> int:
        if self.size == 0:
            return -1

        if len(self.deleteStack) == 0:
            while len(self.addStack):
                self.deleteStack.append(self.addStack.pop())

        val = self.deleteStack.pop()
        self.size -= 1
        return val


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()