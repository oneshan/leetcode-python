# 0658 - Find K Closest Elements
# Date: 2022-10-10
# Runtime: 1031 ms, Memory: 15.9 MB
# Submission Id: 818763591


import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [] # max heap (k-smallest)
        for num in arr:
            dist = abs(num-x)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, num))
            elif -heap[0][0] > dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, num))
                
        return sorted([h[1] for h in heap])