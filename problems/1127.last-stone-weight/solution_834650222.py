# 1127 - Last Stone Weight
# Date: 2022-11-01
# Runtime: 57 ms, Memory: 13.9 MB
# Submission Id: 834650222


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)
            if s1 > s2:
                heapq.heappush(max_heap, -(s1-s2))
            
        return -max_heap[0] if max_heap else 0