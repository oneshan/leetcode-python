# 1953 - Finding MK Average
# Date: 2024-06-09
# Runtime: 6834 ms, Memory: 52.2 MB
# Submission Id: 1282643148


from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.sl = SortedList()
        self.queue = deque()
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.sl.add(num)
        self.queue.append(num)
        if len(self.queue) > self.m:
            num = self.queue.popleft()
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        return sum(self.sl[self.k:-self.k]) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()