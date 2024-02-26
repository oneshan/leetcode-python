# 2818 - Maximum Strictly Increasing Cells in a Matrix
# Date: 2023-10-03
# Runtime: 1691 ms, Memory: 73.6 MB
# Submission Id: 1065902281


from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])
        
        cache = defaultdict(list)
        for r in range(len_r):
            for c in range(len_c):
                cache[mat[r][c]].append((r, c))
                
        dp_r = [0] * len_r
        dp_c = [0] * len_c
        
        dp = [[0] * len_c for _ in range(len_r)]
        for val in sorted(cache, reverse=True):
            for r, c in cache[val]:
                dp[r][c] = 1 + max(dp_r[r], dp_c[c])
            for r, c in cache[val]:
                dp_r[r] = max(dp_r[r], dp[r][c])
                dp_c[c] = max(dp_c[c], dp[r][c])
        return max(max(dp_r), max(dp_c))