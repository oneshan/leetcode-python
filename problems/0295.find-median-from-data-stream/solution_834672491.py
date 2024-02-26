# 0295 - Find Median from Data Stream
# Date: 2022-11-01
# Runtime: 579 ms, Memory: 36.2 MB
# Submission Id: 834672491


import heapq

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.size & 1:
            heapq.heappush(self.min_heap, num)
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        else:
            heapq.heappush(self.max_heap, -num)
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            
        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()