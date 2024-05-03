# 0265 - Paint House II
# Date: 2024-05-02
# Runtime: 84 ms, Memory: 16.6 MB
# Submission Id: 1247256353


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        len_r, len_c = len(costs), len(costs[0])
        
        for i in range(1, len_r):
            min1 = min2 = float('inf')
            for j in range(len_c):
                if costs[i-1][j] < min1:
                    min1, min2 = costs[i-1][j], min1
                elif costs[i-1][j] < min2:
                    min2 = costs[i-1][j]
            
            for j in range(len_c):
                costs[i][j] += min1 if costs[i-1][j] != min1 else min2
                
        return min(costs[-1])