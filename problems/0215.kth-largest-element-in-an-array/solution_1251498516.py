# 0215 - Kth Largest Element in an Array
# Date: 2024-05-07
# Runtime: 473 ms, Memory: 29.8 MB
# Submission Id: 1251498516


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]