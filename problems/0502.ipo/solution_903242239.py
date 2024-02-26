# 0502 - IPO
# Date: 2023-02-23
# Runtime: 1118 ms, Memory: 38.8 MB
# Submission Id: 903242239


import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        heap = []
        
        i, n = 0, len(projects)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, (-projects[i][1]))
                i += 1
            if not heap:
                return w
            w -= heapq.heappop(heap)

        return w