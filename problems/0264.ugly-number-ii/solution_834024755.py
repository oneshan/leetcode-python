# 0264 - Ugly Number II
# Date: 2022-10-31
# Runtime: 494 ms, Memory: 14.2 MB
# Submission Id: 834024755


import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        heap = [1]
        for _ in range(n):
            while heap[0] in seen:
                heapq.heappop(heap)
            num = heapq.heappop(heap)
            seen.add(num)
            heapq.heappush(heap, num*2)
            heapq.heappush(heap, num*3)
            heapq.heappush(heap, num*5)
        
        return num