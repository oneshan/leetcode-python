# 1127 - Last Stone Weight
# Date: 2022-10-09
# Runtime: 64 ms, Memory: 13.9 MB
# Submission Id: 818208297


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        # Build MaxHeap - O(NlogN)
        weights = []
        for stone in stones:
            heapq.heappush(weights, -stone)
        
        while weights:
            s1 = heapq.heappop(weights)
            if not weights:
                return -s1
            s2 = heapq.heappop(weights)
            if s1 != s2:
                heapq.heappush(weights, s1-s2)
        return 0