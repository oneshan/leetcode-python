# 0658 - Find K Closest Elements
# Date: 2022-10-10
# Runtime: 1115 ms, Memory: 16.5 MB
# Submission Id: 818772000


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
        return sorted([-h[1] for h in heap])