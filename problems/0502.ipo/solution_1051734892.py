# 0502 - IPO
# Date: 2023-09-17
# Runtime: 793 ms, Memory: 41.2 MB
# Submission Id: 1051734892


import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted((c, p) for c, p in zip(capital, profits))
        n = len(projects)
        
        max_heap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)
        return w