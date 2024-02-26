# 0971 - Shortest Bridge
# Date: 2022-11-25
# Runtime: 384 ms, Memory: 17 MB
# Submission Id: 849551440


from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        def dfs(r, c):
            grid[r][c] = 2
            queue.append((r, c))        
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                next_r, next_c = r+dx, c+dy
                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 1:
                    dfs(next_r, next_c)
        
        is_first_found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    is_first_found = True
                    break
            if is_first_found:
                break
                    
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    next_r, next_c = r+dx, c+dy
                    if 0 <= next_r < n and 0 <= next_c < n:
                        if grid[next_r][next_c] == 0:
                            grid[next_r][next_c] = 2
                            queue.append((next_r, next_c))
                        if grid[next_r][next_c] == 1:
                            return distance
            distance += 1
        return 0