# 0215 - Kth Largest Element in an Array
# Date: 2022-10-20
# Runtime: 821 ms, Memory: 27.1 MB
# Submission Id: 826581224


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]