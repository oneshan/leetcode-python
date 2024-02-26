# 0295 - Find Median from Data Stream
# Date: 2022-10-09
# Runtime: 2358 ms, Memory: 36.1 MB
# Submission Id: 818641399


class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        index = bisect_left(self.arr, num)
        self.arr.insert(index, num)
        self.size += 1

    def findMedian(self) -> float:
        mid = self.size // 2
        if self.size & 1:
            return self.arr[mid]
        return (self.arr[mid-1] + self.arr[mid]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()