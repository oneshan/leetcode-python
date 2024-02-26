# 0295 - Find Median from Data Stream
# Date: 2023-09-16
# Runtime: 431 ms, Memory: 38.2 MB
# Submission Id: 1051026261


import heapq

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.size & 1:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            
        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()