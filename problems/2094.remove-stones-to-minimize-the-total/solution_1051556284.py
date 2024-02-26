# 2094 - Remove Stones to Minimize the Total
# Date: 2023-09-17
# Runtime: 1367 ms, Memory: 31.1 MB
# Submission Id: 1051556284


import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)  # max_heap
        for _ in range(k):
            curr = heapq.heappop(heap)
            heapq.heappush(heap, curr//2)
        return -sum(heap)
    
# math.floor(-3/2) = math.floor(-1.5) = -3 // 2 = -2