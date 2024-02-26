# 0215 - Kth Largest Element in an Array
# Date: 2022-11-01
# Runtime: 609 ms, Memory: 27.1 MB
# Submission Id: 834642283


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]