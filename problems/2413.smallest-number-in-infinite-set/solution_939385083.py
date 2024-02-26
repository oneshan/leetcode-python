# 2413 - Smallest Number in Infinite Set
# Date: 2023-04-25
# Runtime: 124 ms, Memory: 14.5 MB
# Submission Id: 939385083


import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.added = set()
        self.min_heap = []
        self.curr = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            num = heapq.heappop(self.min_heap)
            self.added.remove(num)
        else:
            num = self.curr
            self.curr += 1
        return num

    def addBack(self, num: int) -> None:
        if self.curr <= num or num in self.added:
            return
        heapq.heappush(self.min_heap, num)
        self.added.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)