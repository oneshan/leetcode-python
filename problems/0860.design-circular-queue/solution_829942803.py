# 0860 - Design Circular Queue
# Date: 2022-10-25
# Runtime: 162 ms, Memory: 14.7 MB
# Submission Id: 829942803


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.count == 0:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
            
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.count == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()