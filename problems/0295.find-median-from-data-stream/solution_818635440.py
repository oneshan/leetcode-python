# 0295 - Find Median from Data Stream
# Date: 2022-10-09
# Runtime: 1375 ms, Memory: 35.7 MB
# Submission Id: 818635440


import heapq

class MedianFinder:

    def __init__(self):
        self.large = []  # min-heap
        self.small = []  # max-heap

    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            val = heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, -val)
        else:
            val = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            median = (self.large[0] - self.small[0]) / 2
        else:
            median = self.large[0]
        return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()