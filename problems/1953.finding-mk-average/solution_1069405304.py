# 1953 - Finding MK Average
# Date: 2023-10-07
# Runtime: 1052 ms, Memory: 52 MB
# Submission Id: 1069405304


from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.deque = deque()
        self.sl = SortedList()
        self.total = self.first_k = self.last_k = 0
        self.size = 0

    def addElement(self, num: int) -> None:
        self.size += 1
        self.total += num
        self.deque.append(num)
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.first_k += num
            if self.size > self.k:
                self.first_k -= self.sl[self.k - 1]
        if index >= self.size - self.k:
            self.last_k += num
            if self.size > self.k:
                self.last_k -= self.sl[-self.k]
        self.sl.add(num)
        
        if self.size == self.m + 1:
            num = self.deque.popleft()
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.sl[self.k]
            elif index >= self.size - self.k:
                self.last_k -= num
                self.last_k += self.sl[-self.k - 1]
            self.sl.remove(num)
            self.size -= 1

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()