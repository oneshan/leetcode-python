# 1127 - Last Stone Weight
# Date: 2022-07-24
# Runtime: 38 ms, Memory: 13.9 MB
# Submission Id: 755217840


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            heapq.heappush(h, -abs(x-y))
        return -h[0]