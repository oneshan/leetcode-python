# 0215 - Kth Largest Element in an Array
# Date: 2023-08-14
# Runtime: 456 ms, Memory: 29.3 MB
# Submission Id: 1020804641


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_heap = []
        for num in nums:
            heapq.heappush(k_heap, num)
            if len(k_heap) > k:
                heapq.heappop(k_heap)
        return k_heap[0]