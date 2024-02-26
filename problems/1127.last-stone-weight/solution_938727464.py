# 1127 - Last Stone Weight
# Date: 2023-04-24
# Runtime: 31 ms, Memory: 13.8 MB
# Submission Id: 938727464


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            p1 = heapq.heappop(stones)
            p2 = heapq.heappop(stones)
            if p1 != p2:
                heapq.heappush(stones, p1-p2)
        return -stones[0] if stones else 0