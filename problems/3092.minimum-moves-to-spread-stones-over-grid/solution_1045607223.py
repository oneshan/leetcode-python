# 3092 - Minimum Moves to Spread Stones Over Grid
# Date: 2023-09-10
# Runtime: 762 ms, Memory: 16.3 MB
# Submission Id: 1045607223


from itertools import permutations


class Solution:
    
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        pos, neg = [], []
        for r in range(3):
            for c in range(3):
                if grid[r][c] == 0:
                    neg.append((r, c))
                if grid[r][c] > 1:
                    for _ in range(grid[r][c] - 1):
                        pos.append((r, c))
                        
        if not pos and not neg:
            return 0
        
        ans = float('inf')
        for p in permutations(neg):
            dist = sum(abs(n1[0]-n2[0]) + abs(n1[1]-n2[1]) for n1, n2 in zip(p, pos))
            ans = min(ans, dist)
            
        return ans