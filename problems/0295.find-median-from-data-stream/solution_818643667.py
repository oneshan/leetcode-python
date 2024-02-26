# 0295 - Find Median from Data Stream
# Date: 2022-10-09
# Runtime: 1737 ms, Memory: 36.6 MB
# Submission Id: 818643667


class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        # index = bisect_left(self.arr, num)
        index = self.search_insert_index(num)
        self.arr.insert(index, num)
        self.size += 1

    def findMedian(self) -> float:
        mid = self.size // 2
        if self.size & 1:
            return self.arr[mid]
        return (self.arr[mid-1] + self.arr[mid]) / 2
    
    def search_insert_index(self, num):
        left, right = 0, len(self.arr)-1
        while left <= right:
            mid = left + (right-left) // 2
            if self.arr[mid] == num:
                return mid
            if self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()