# 0789 - Kth Largest Element in a Stream
# Date: 2022-10-09
# Runtime: 193 ms, Memory: 18.5 MB
# Submission Id: 818685900


import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        # O(logk)
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)