# 0993 - Tallest Billboard
# Date: 2023-06-24
# Runtime: 1336 ms, Memory: 250.9 MB
# Submission Id: 978472530


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        
        @cache
        def dfs(diff, j):
            if j >= n:
                return 0 if diff == 0 else float('-inf')
            
            return max(dfs(diff-rods[j], j+1),
                       dfs(diff+rods[j], j+1) + rods[j],
                       dfs(diff, j+1))
        
        return dfs(0, 0)