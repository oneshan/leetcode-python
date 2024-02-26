# 1117 - As Far from Land as Possible
# Date: 2022-11-23
# Runtime: 549 ms, Memory: 14.5 MB
# Submission Id: 848572526


from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        lands = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    lands.append((r, c))

        if len(lands) in (n*n, 0):
            return -1
        
        ans = -1
        while lands:
            ans += 1
            for _ in range(len(lands)):
                r, c = lands.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_r, new_c = r+dx, c+dy
                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = 1
                        lands.append((new_r, new_c))
        return ans