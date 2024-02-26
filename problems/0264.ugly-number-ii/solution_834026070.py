# 0264 - Ugly Number II
# Date: 2022-10-31
# Runtime: 497 ms, Memory: 14.2 MB
# Submission Id: 834026070


import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {1}
        heap = [1]
        for _ in range(n):
            num = heapq.heappop(heap)
            for i in (2,3,5):
                next_ugly = num * i
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heapq.heappush(heap, next_ugly)        
        return num