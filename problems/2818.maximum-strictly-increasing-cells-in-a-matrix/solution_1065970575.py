# 2818 - Maximum Strictly Increasing Cells in a Matrix
# Date: 2023-10-03
# Runtime: 1896 ms, Memory: 86.2 MB
# Submission Id: 1065970575


from collections import defaultdict
import heapq

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])
        
        cache = defaultdict(set)
        for r in range(len_r):
            for c in range(len_c):
                cache[mat[r][c]].add((r, c))
                
        dp = [[0] * len_c for _ in range(len_r)]
        dp_r = [0] * len_r
        dp_c = [0] * len_c
        
        for val in sorted(cache):
            
            for r, c in cache[val]:
                dp[r][c] = 1 + max(dp_r[r], dp_c[c])
                
            for r, c in cache[val]:
                dp_r[r] = max(dp[r][c], dp_r[r])
                dp_c[c] = max(dp[r][c], dp_c[c])
        
        return max(max(dp_r), max(dp_c))