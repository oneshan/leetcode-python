# 0295 - Find Median from Data Stream
# Date: 2024-06-12
# Runtime: 392 ms, Memory: 38.3 MB
# Submission Id: 1285639172


class MedianFinder:

    def __init__(self):
        self.min_heap = []  # larger
        self.max_heap = []  # smaller
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size & 1:  # len(self.max_heap) > len(self.min_heap)
            heapq.heappush(self.max_heap, -num)
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.min_heap, num)
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return -self.max_heap[0]

        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()