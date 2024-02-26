# 1036 - Rotting Oranges
# Date: 2023-09-30
# Runtime: 53 ms, Memory: 16.3 MB
# Submission Id: 1062955861


from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        fresh_oranges = 0
        queue = deque([])  # rotten_oranges
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    
        if not fresh_oranges:
            return 0
        
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
            if fresh_oranges == 0:
                return step + 1
            step += 1
        return -1