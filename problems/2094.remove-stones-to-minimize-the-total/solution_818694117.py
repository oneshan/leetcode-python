# 2094 - Remove Stones to Minimize the Total
# Date: 2022-10-09
# Runtime: 2078 ms, Memory: 28.4 MB
# Submission Id: 818694117


import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)  # max_heap
        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr-remove))
        return -sum(heap)