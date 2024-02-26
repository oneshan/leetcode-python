# 0860 - Design Circular Queue
# Date: 2022-10-25
# Runtime: 150 ms, Memory: 14.4 MB
# Submission Id: 829938585


class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.size = k
        self.head = self.tail = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.size
        self.arr[self.tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.head + 1) % self.size]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail]

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