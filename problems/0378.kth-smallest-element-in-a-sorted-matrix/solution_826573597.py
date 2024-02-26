# 0378 - Kth Smallest Element in a Sorted Matrix
# Date: 2022-10-20
# Runtime: 205 ms, Memory: 18.7 MB
# Submission Id: 826573597


import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        min_heap = []
        for r in range(min(k, len_r)):
            min_heap.append((matrix[r][0], r, 0))
        heapq.heapify(min_heap)
        
        while k:
            num, r, c = heapq.heappop(min_heap)
            k -= 1
            if c < len_c-1:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
        return num