155. Min Stack






class MinStack:

    def __init__(self):
        self.items = []
        # record the minimum item in items[0:i+1]
        self.minitems = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minitems:
            self.minitems.append(val)
        else:
            self.minitems.append(min(val, self.minitems[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.minitems.pop()


    def top(self) -> int:
        return self.items[-1]


    def getMin(self) -> int:
        return self.minitems[-1]