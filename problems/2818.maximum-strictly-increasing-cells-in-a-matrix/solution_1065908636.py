# 2818 - Maximum Strictly Increasing Cells in a Matrix
# Date: 2023-10-03
# Runtime: 2356 ms, Memory: 52.3 MB
# Submission Id: 1065908636


from collections import defaultdict
import heapq

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])
        
        min_heap = []
        for r in range(len_r):
            for c in range(len_c):
                heapq.heappush(min_heap, (mat[r][c], r, c))
                
        dp = [[0] * len_c for _ in range(len_r)]
        dp_r = [0] * len_r
        dp_c = [0] * len_c
        
        while min_heap:
            val = min_heap[0][0]
            to_update = set()
            while min_heap and min_heap[0][0] == val:
                val, r, c = heapq.heappop(min_heap)
                to_update.add((r, c))
            
            for r, c in to_update:
                dp[r][c] = 1 + max(dp_r[r], dp_c[c])
                
            for r, c in to_update:
                dp_r[r] = max(dp[r][c], dp_r[r])
                dp_c[c] = max(dp[r][c], dp_c[c])
        
        return max(max(dp_r), max(dp_c))