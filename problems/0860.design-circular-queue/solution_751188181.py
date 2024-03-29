# 0860 - Design Circular Queue
# Date: 2022-07-19
# Runtime: 125 ms, Memory: 14.5 MB
# Submission Id: 751188181


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.array = [0] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[(self.head + self.count) % self.size] = value
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
        return self.array[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[(self.head + self.count - 1) % self.size]

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