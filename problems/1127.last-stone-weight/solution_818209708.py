# 1127 - Last Stone Weight
# Date: 2022-10-09
# Runtime: 63 ms, Memory: 13.9 MB
# Submission Id: 818209708


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        # Build MaxHeap - O(N)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        # O(N logN)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            heapq.heappush(stones, s1-s2)
        return -stones[0]