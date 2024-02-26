# 3092 - Minimum Moves to Spread Stones Over Grid
# Date: 2023-09-10
# Runtime: 976 ms, Memory: 16.5 MB
# Submission Id: 1045616707


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
        n = len(neg)
        
        def recur(mask, j, curr_dist):
            nonlocal ans
            if j == n:
                ans = min(ans, curr_dist)
                return

            for i in range(n):
                if mask & (1 << i):
                    continue
                dist = abs(pos[j][0] - neg[i][0]) + abs(pos[j][1] - neg[i][1])
                recur(mask | (1 << i), j+1, curr_dist + dist)
        
        recur(0, 0, 0)
        return ans