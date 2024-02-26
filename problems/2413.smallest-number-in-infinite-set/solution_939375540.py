# 2413 - Smallest Number in Infinite Set
# Date: 2023-04-25
# Runtime: 136 ms, Memory: 14.6 MB
# Submission Id: 939375540


import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = list(range(1, 1001))
        self.data = set(range(1, 1001))

    def popSmallest(self) -> int:
        val = heapq.heappop(self.min_heap)
        self.data.discard(val)
        return val

    def addBack(self, num: int) -> None:
        if num in self.data:
            return
        heapq.heappush(self.min_heap, num)
        self.data.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)