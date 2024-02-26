# 1127 - Last Stone Weight
# Date: 2023-09-16
# Runtime: 37 ms, Memory: 16.1 MB
# Submission Id: 1050899886


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
            
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            if s1 != s2:
                heapq.heappush(max_heap, s1 - s2)
            
        return -max_heap[0] if max_heap else 0