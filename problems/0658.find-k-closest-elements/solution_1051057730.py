# 0658 - Find K Closest Elements
# Date: 2023-09-16
# Runtime: 323 ms, Memory: 18.7 MB
# Submission Id: 1051057730


import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        # Build K-size MaxHeap: O(N logK)
        for num in arr:
            dist = abs(num-x)
            heapq.heappush(heap, (-dist, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Sort: O(KlogK)
        return sorted(-num[1] for num in heap)