# 0295 - Find Median from Data Stream
# Date: 2024-05-22
# Runtime: 372 ms, Memory: 38.4 MB
# Submission Id: 1264659012


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size & 1:
            heapq.heappush(self.max_heap, -num)
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, num)
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return -self.max_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()