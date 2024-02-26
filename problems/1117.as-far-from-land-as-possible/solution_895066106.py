# 1117 - As Far from Land as Possible
# Date: 2023-02-10
# Runtime: 504 ms, Memory: 14.6 MB
# Submission Id: 895066106


from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if len(queue) in (n*n, 0):
            return -1
        
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_r, new_c = r+dx, c+dy
                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = 1
                        queue.append((new_r, new_c))
            ans += 1
        return ans - 1