# 2413 - Smallest Number in Infinite Set
# Date: 2024-06-16
# Runtime: 92 ms, Memory: 17.1 MB
# Submission Id: 1290156998


class SmallestInfiniteSet:

    def __init__(self):
        self.marker = 1
        self.infinite_set = []
        self.back_set = set()

    def popSmallest(self) -> int:
        if self.infinite_set:
            num = heapq.heappop(self.infinite_set)
            self.back_set.discard(num)
            return num

        self.marker += 1
        return self.marker - 1

    def addBack(self, num: int) -> None:
        if num >= self.marker or num in self.back_set:
            return
        self.back_set.add(num)
        heapq.heappush(self.infinite_set, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)