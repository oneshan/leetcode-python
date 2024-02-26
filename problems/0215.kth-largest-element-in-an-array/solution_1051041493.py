# 0215 - Kth Largest Element in an Array
# Date: 2023-09-16
# Runtime: 588 ms, Memory: 29.3 MB
# Submission Id: 1051041493


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]