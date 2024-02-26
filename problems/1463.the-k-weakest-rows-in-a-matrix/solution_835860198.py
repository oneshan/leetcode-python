# 1463 - The K Weakest Rows in a Matrix
# Date: 2022-11-03
# Runtime: 265 ms, Memory: 14.3 MB
# Submission Id: 835860198


import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []
        for idx, row in enumerate(mat):
            heapq.heappush(max_heap, (-sum(row), -idx))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [-heapq.heappop(max_heap)[1] for _ in range(k)][::-1]