707. Design Linked List

class Node(object):
    def __init__(self, item = 0):
        self.item = item
        self.pre = None
        self.next = None

class MyLinkedList:


    def __init__(self):
        self.sentinel = Node(None)
        self.size = 0
        self.sentinel.pre = self.sentinel
        self.sentinel.next = self.sentinel

    def insert(self, first, middle, last):
        first.next = middle
        middle.next = last
        last.pre = middle
        middle.pre = first
        self.size += 1


    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del node
        self.size -= 1

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 

        p = self.sentinel.next
        while index > 0:
            p = p.next
            index -= 1

        return p.item


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        self.insert(self.sentinel, node, self.sentinel.next)

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        self.insert(self.sentinel.pre, node, self.sentinel)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        node = Node(val)
        p = self.sentinel.next
        while index > 0:
            p = p.next
            index -= 1

        self.insert(p.pre, node, p)



    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        p = self.sentinel.next
        while index > 0:
            p = p.next
            index -= 1

        self.delete(p)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)