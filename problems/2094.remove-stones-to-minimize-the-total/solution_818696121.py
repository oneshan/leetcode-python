# 2094 - Remove Stones to Minimize the Total
# Date: 2022-10-09
# Runtime: 4284 ms, Memory: 28.5 MB
# Submission Id: 818696121


import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)  # max_heap
        for _ in range(k):
            curr = heapq.heappop(heap)
            heapq.heappush(heap, curr//2)
        return -sum(heap)